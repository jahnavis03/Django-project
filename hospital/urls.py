from django.contrib import admin
from django.urls import path
from hospital.views import ABOUT,HOME,CONTACT,LOGIN,Logout_Admin,View_doctor,view_patient,view_appointment,Add_doc,Add_Patient,Add_appointment

urlpatterns = [
    path('about/', ABOUT, name='about'),
    path('',HOME,name='home'),
    path('contact/', CONTACT, name='contact'),
    path('admin_login/',LOGIN,name='login'),
    path('logout/',Logout_Admin,name='logout_admin'),
    path('view_doctor/',View_doctor, name='view_doctor'),
    path('view_patient/', view_patient, name='view_patient'),
    path('view_appointment/', view_appointment, name='view_appointment'),
    path('add_doctor/', Add_doc,name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_appointment/', Add_appointment, name='add_appointment'),
]