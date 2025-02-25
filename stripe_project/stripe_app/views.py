from django.shortcuts import render
import stripe
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Item
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def buy_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, id=item_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{os.getenv("YOUR_DOMAIN")}/success/",
            cancel_url=f"{os.getenv("YOUR_DOMAIN")}/cancel/",
        )
        return JsonResponse({'session_id': session.id})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'stripe_app/item_detail.html', {
        'item': item,
        'stripe_public_key': os.getenv("STRIPE_PUBLIC_KEY"),
    })

def succes_page(request):
    return render(request, 'stripe_app/success.html')

def cancel_page(request):
    return render(request, 'stripe_app/cancel.html')

