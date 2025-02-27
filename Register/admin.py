from django.contrib import admin
from .models import Participant,CyberShowDetail,FragFestDetail,ExpoDetail,Bill

# Register your models here.
admin.site.register(Participant)
admin.site.register(CyberShowDetail),
admin.site.register(FragFestDetail),
admin.site.register(Bill)
admin.site.register(ExpoDetail)
