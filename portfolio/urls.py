from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projet/<int:id>-<slug:slug>', views.more, name='more')
]