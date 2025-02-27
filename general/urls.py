from django.urls import path
from .views import export_participants_to_excel,TermsAndConditionsView,PrivacyPolicyView,RefundPolicyView
url_patterns = [
    path('get_data/',export_participants_to_excel,name='export_participants_to_excel'),
    path('terms_and_conditions/',TermsAndConditionsView.as_view(),name='terms_and_conditions'),
    path('privacy_policy/',PrivacyPolicyView.as_view(),name='privacy_policy'),
    path('refund_policy/',RefundPolicyView.as_view(),name='refund_policy'),
]