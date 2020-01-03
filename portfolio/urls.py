from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('projet/<int:id>-<slug:slug>', views.more, name='more'),
    path('fichier/', views.fichier, name='fichier')
]