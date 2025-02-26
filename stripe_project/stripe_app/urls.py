from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('buy_order/<int:order_id>/', views.buy_order, name='buy_order'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('success/', views.succes_page, name='success_page'),
    path('cancel/', views.cancel_page, name='cancel_page'),
    path('items/', views.item_all, name='items'),
    path('create-order/', views.create_order, name='create_order'),
]
