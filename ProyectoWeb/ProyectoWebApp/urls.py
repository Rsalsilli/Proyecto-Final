from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from ProyectoWebApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('acercaDe/', views.acercaDe, name="acercaDe"),
       
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)