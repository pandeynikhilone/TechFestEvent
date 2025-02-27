from django.urls import path
from .views import AboutUsView
url_patterns = [
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
     
]