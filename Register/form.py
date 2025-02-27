from django import forms

class BasicRegisterForm(forms.Form):
    template_name = "register_form_snippet.html"

    name =  forms.CharField(max_length=155,widget=forms.TextInput(attrs={'placeholder' : 'Name','class' : "input-name"}))
    phone = forms.RegexField(
        regex = "^\+?[0-9]+$",
        max_length=15,
        error_messages={'invalid' : 'Enter a valid phone number'},
        widget=forms.TextInput(attrs={'placeholder' : 'Phone Number','class' : "input-ph"})
    )
    email = forms.EmailField(
        max_length=155,
        error_messages={'invalid' : 'Enter a valid email address'},
        widget=forms.EmailInput(
            attrs={'placeholder' : 'Email',"class" : "input-email"}
        )
    )
    college_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder' : 'College Name','class' : "input-college"})
    )
    college_id = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={'placeholder' : 'College Id','class' : "input-course"})
    )
    course = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={'placeholder' : 'Course (Optional)','class' : "input-course"}),
        required=False
    )

class FragFestDetailsForm(forms.Form):
    template_name = "fragfest_details_snippet.html"
    team_name = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={'placeholder': 'Team Name'})
    )
    
    real_name_1 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Name'
        }))
    user_name_1 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Username in BGMI'
        }))
    real_name_2 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Name'
        }))
    user_name_2 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Username in BGMI'
        }))
    real_name_3 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Name'
        }))
    user_name_3 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Username in BGMI'
        }))
    real_name_4 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Name'
        }))
    user_name_4 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Username in BGMI'
        }))
    

class ExpoEventDetailsForm(forms.Form):
    template_name = "expo_details_snippet.html"
    team_name = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={'placeholder': 'Team Name'})
    )
    number_of_members = forms.IntegerField(
    
        widget=forms.NumberInput(attrs={'placeholder': 'Number of Members'}),
        min_value=1,max_value=3
    )
    project_detail = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'About Project'}),
        label="Project Details"
    )
    project_detail_file = forms.FileField(
        widget=forms.FileInput(attrs={'placeholder': 'Upload Project in details (in PDF Format)'}),
        label="Upload Project File"
    )


class CyberShowDetailsForm(forms.Form):
    template_name = "cybershow_details_snippet.html"
    team_name = forms.CharField(max_length=155,
    widget=forms.TextInput(attrs={'placeholder' : 'Team Name',}))
    number_of_members = forms.IntegerField(min_value=1,max_value=8,widget=forms.NumberInput(attrs={'placeholder' : 'Number of Members',}))
    skit_detail_file = forms.FileField(widget=forms.FileInput(attrs={'placeholder' : 'Upload Skit (in PDF Format)',}))
    name1 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 1 Name',
        }))
    name2 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 2 Name',
        }))
    name3 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 3 Name',
        }))
    name4 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 4 Name',
        }))
    name5 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 5 Name',
        }))
    name6 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 6 Name',
        }))
    name7 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 7 Name',
        }))
    name8 = forms.CharField(
        max_length=155,
        widget=forms.TextInput(attrs={
            'placeholder' : 'Participant 8 Name',
        }))


     
    


