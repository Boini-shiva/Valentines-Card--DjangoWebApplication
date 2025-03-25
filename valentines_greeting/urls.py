from django.urls import path
from . import views

#create your urls path

urlpatterns = [
    path('',views.home, name='home'),
    path('create_card/',views.create_card, name='create_card'),
    path('card_details/',views.card_details, name='card_details'),
    path('card_update/<int:id>/',views.card_update, name='card_update'),
    path('card_delete/<int:id>/',views.card_delete, name='card_delete'),
]