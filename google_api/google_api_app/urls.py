from django.urls import path,include
from .views import sheets,calender,index
urlpatterns = [
    path('',index,name="index"),
    path('sheets',sheets,name="sheets"),
    path('calender',calender,name="cal")
    
]