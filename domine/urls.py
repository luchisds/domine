"""domine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^escuela/$', views.school, name='escuela'),
    url(r'^capacitaciones/ppg/$', views.ppg, name='ppg'),
    url(r'^capacitaciones/pactivo/$', views.pactivo, name='pactivo'),
    url(r'^capacitaciones/kstretch/$', views.kstretch, name='kstretch'),
    url(r'^capacitaciones/profesionales/$', views.profesionales, name='profesionales'),
    url(r'^eventos/$', views.events, name='eventos'),
    url(r'^galeria/$', views.gallery, name='galeria'),
    url(r'^contacto/$', views.ContactFormView.as_view(), name='contacto'),
    url(r'^centro-entrenamiento/$', views.centroEntrenamiento, name='centro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)