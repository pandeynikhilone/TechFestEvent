from django.urls import path
from .views import ContactUsView
url_patterns = [
   path('contactus/', ContactUsView.as_view(), name='contactus'),
     
]