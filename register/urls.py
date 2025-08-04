from django.urls import path
from .views import RegisterView,EventSelectionView,EventDetailsView,CheckOutView,PaymentForRegistration,SuccessfulPaymentView

url_patterns = [
     path('',RegisterView.as_view(),name="register"),
     path('choose_event/',EventSelectionView.as_view(),name = 'eventselection'),
     path('event_details/<event>',EventDetailsView.as_view(),name='eventdetails'),
     path('check_out/',CheckOutView.as_view(),name='checkout'),
     path('payment_for_registration/',PaymentForRegistration.as_view(),name='payment_for_registration'),
     path('payment_successful/',SuccessfulPaymentView.as_view(),name='successful_payment')
]