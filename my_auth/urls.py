from django.urls import path
from . import views

#create your urls path

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.log_in, name='login'),
    path('logout/',views.log_out, name='logout'),
]