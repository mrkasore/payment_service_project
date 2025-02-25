from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('success/', views.succes_page, name='success_page'),
    path('cancel/', views.cancel_page, name='cancel_page'),
]
