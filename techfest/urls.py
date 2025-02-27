"""
URL configuration for techfest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from register.urls import url_patterns as register_urls
from general.urls import url_patterns as general_urls
from aboutus.urls import url_patterns as aboutus_urls
from contactus.urls import url_patterns as contactus_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(register_urls)),
    path('',include(general_urls)),
    path('',include(aboutus_urls)),
    path('',include(contactus_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
