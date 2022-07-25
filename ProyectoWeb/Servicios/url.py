from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.streamers, name="streamers"),
    path('categoria/<int:categorias_id>/',views.categoria, name="categoria"),
    
]
