from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView
from . import form as local_form
from django.views import View
from django.http import JsonResponse
from .form import ExpoEventDetailsForm,CyberShowDetailsForm,FragFestDetailsForm
from .models import Participant,FragFestDetail,CyberShowDetail,ExpoDetail,Bill
from general.models import Event
import json



class RegisterView(FormView):
    form_class = local_form.BasicRegisterForm
    template_name = 'register.html'
    success_url = '/choose_event/'

    def form_valid(self, form):
    
        form_data = form.cleaned_data
        name = form_data.get('name')
        phone = form_data.get('phone')
        email = form_data.get('email')
        college_name = form_data.get('college_name')
        college_id = form_data.get('college_id')
        course = form_data.get('course', None)  

        participant = Participant.objects.create(
            name = name,
            phone = phone,
            email = email,
            college_name = college_name,
            college_id = college_id,
            course = course
        )
        self.request.session['p_id'] = participant.id

        return super().form_valid(form)

    

class EventSelectionView(TemplateView):
    template_name = 'event_selection.html'
    def get_context_data(self, **kwargs):
        events = Event.objects.all()
        return {'events': events}
        
    
class EventDetailsView(View):
    def get(self, request, event, *args, **kwargs):
        # Storing the event with participant
        

        form = None
        if event == 'ExpoRenaissance':
            form = ExpoEventDetailsForm()
        elif event == 'CyberShow':
            form = CyberShowDetailsForm()
        elif event == 'FragFest':
            form = FragFestDetailsForm()
        else: 
            return redirect('/check_out/')
        
        return render(request, 'event_details.html', {'form': form, 'event': event})
    
    def post(self, request, event, *args, **kwargs):
        form = None

        participant_id = self.request.session['p_id']
        current_participant = Participant.objects.get(id=participant_id)
        current_participant.event = event
        current_participant.save()
         
        if event == 'ExpoRenaissance':
            print('Expo Activated .. ')
            form = ExpoEventDetailsForm(request.POST, request.FILES)
            if form.is_valid():

                form_data = form.cleaned_data
                participant_id = self.request.session['p_id']
                participant = Participant.objects.get(id=participant_id)

                expo_detail = ExpoDetail(
                    participant=participant,
                    team_name=form_data['team_name'],
                    number_of_members=form_data['number_of_members'],
                    project_detail=form_data['project_detail'],
                    project_detail_file=form_data['project_detail_file']
                )
                expo_detail.save()
                return redirect('/check_out/')  # Redirect to a success page

        elif event == 'CyberShow':
            print('Cyber Show Activated .. ')
            form = CyberShowDetailsForm(request.POST, request.FILES)
            if form.is_valid():
                # Extract cleaned data
                form_data = form.cleaned_data
                # Save to CyberShowDetail model
                print('here')
                participant_id = self.request.session['p_id']
                participant = Participant.objects.get(id=participant_id)

                cybershow_detail = CyberShowDetail(
                    participant=participant,
                    team_name=form_data['team_name'],
                    number_of_members=form_data['number_of_members'],
                    skit_detail_file=form_data['skit_detail_file'],
                    participant_names=[form_data[f'name{i}'] for i in range(1, 9)]
                )
                cybershow_detail.save()
                print("cyber show end")
                return redirect('/check_out/')  # Redirect to a success page

        elif event == 'FragFest':
            print('Frag Activated .. ')
            form = FragFestDetailsForm(request.POST)
            if form.is_valid():
                # Extract cleaned data
                form_data = form.cleaned_data
                # Save to FragFestDetail model
                participant_id = self.request.session['p_id']
                participant = Participant.objects.get(id=participant_id)

                fragfest_detail = FragFestDetail(
                    participant=participant,
                    team_member_details=[{
                        'real_name': form_data[f'real_name_{i}'],
                        'user_name': form_data[f'user_name_{i}']
                    } for i in range(1, 5)]
                )
                fragfest_detail.save()
                
                return redirect('/check_out/')
        elif event == 'CodeGolf' or event == 'PromptMatrix' or event == 'ArtBurst' or event == 'MemeIfy':   
            print('Other Activated .. ')
            return redirect('/check_out/')
            
        return render(request, 'event_details.html', {'form': form, 'event': event})

    
class CheckOutView(View):
    def get(self,request,*args,**kwargs):
        participant_id = self.request.session['p_id']
        participant = Participant.objects.get(id = participant_id)
        participant_event = Event.objects.get(name = participant.event)

        return render(request,'check_out.html',context={'event' : participant_event})
    
    def post(self,request,*args,**kwargs):
        participant_id = self.request.session['p_id']
        participant = Participant.objects.get(id = participant_id)
        participant_event = Event.objects.get(name = participant.event)

        return render(request,'check_out.html',context={'event' : participant_event})
    


import razorpay
from techfest import settings
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class PaymentForRegistration(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        amount_in_paisa = int(data.get('amount')) * 100
        currency = "INR"

        order = client.order.create({
            "amount": amount_in_paisa,
            "currency": currency,
            "payment_capture": 1
        })
        return JsonResponse({
            "order_id": order['id'],
            "amount": order['amount'],
            "currency": order['currency'],
            "key_id": settings.RAZORPAY_KEY_ID,  # Ensure this is the correct key
            "name": "TechFest",
            "description": "Payment for registration"
        })

class SuccessfulPaymentView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        order_id = data.get('razorpay_payment_id')
        participant_id = self.request.session['p_id']
        participant = Participant.objects.get(id=participant_id)
        bill = Bill.objects.create(participant=participant, razorpay_order_id=order_id)
        return JsonResponse({"status": "success"})
        
        
