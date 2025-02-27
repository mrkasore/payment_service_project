import os
import stripe
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Item, Order
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def buy_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        session = set_session_stripe(item_id, item.price)
        return JsonResponse({'session_id': session.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def buy_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        session = set_session_stripe(order_id, order.total_cost)
        return JsonResponse({'session_id': session.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def set_session_stripe(item_id, price):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': f"order - {item_id}",
                },
                'unit_amount': int(price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f"{os.getenv("YOUR_DOMAIN")}/success/",
        cancel_url=f"{os.getenv("YOUR_DOMAIN")}/cancel/",
    )

    return session

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'stripe_app/item_detail.html', {
        'item': item,
        'stripe_public_key': os.getenv("STRIPE_PUBLIC_KEY"),
    })

def item_all(request):
    items = Item.objects.all()
    return render(request, 'stripe_app/create_order.html', {
        'items': items,
        'stripe_public_key': os.getenv("STRIPE_PUBLIC_KEY"),
    })

def create_order(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')
        items = Item.objects.filter(id__in=item_ids)

        order = Order.objects.create()
        order.items.set(items)
        order.calculate_total_cost()

        return render(request, 'stripe_app/items_buy.html', {
            'order': order,
            'stripe_public_key': os.getenv("STRIPE_PUBLIC_KEY"),
        })

def succes_page(request):
    return render(request, 'stripe_app/success.html')

def cancel_page(request):
    return render(request, 'stripe_app/cancel.html')

