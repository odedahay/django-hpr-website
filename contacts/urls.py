from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('thank-you', views.send_success, name='send_success'),
]