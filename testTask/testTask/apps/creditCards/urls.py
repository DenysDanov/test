from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('generate/', views.generateCards, name='generate'),
    path('deactivate/', views.deactivate, name='deactivate'),
    path('activate/', views.activate, name='activate'),
    path('delete/', views.delete, name='delete'),
    path('history/addTransaction/', views.addTransaction, name='addTransaction'),
]