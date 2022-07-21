from datetime import date, datetime
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django import views
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from student.models import Student
from order.models import Cart, Order, OrderItem, Transaction
from product.models import Publisher,Book
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import random
#################  Stripe #####################

import json
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View


#################### Paytm ####################################################
from order.paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from .import paytm


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        # profile = Profile.objects.get(user=self.request.user)
        book = Book.objects.get(pk=self.kwargs['pk'])
        cart = Cart.objects.filter(book=book, user=user).first()
        quantity = 1
        if cart:
            messages.warning(request, 'already exists in the cart')
        else:
            cart = Cart(book=book, quantity=quantity,price=book.book_price, total=book.book_price, user=user)
            cart.save()
            messages.success(request, 'Product has been added to your cart!')
        return redirect('product:shopview')


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'user/cart.html'
    success_url = reverse_lazy('product:shopview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user)[::-1]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        total_cart_amount = 0
        for c in cart:
            total_cart_amount += int(c.total)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>.", type(
                total_cart_amount), (total_cart_amount / 100) * 18)
            tax = (total_cart_amount / 100) * 18
            final_amount = total_cart_amount + tax
            context['cart_data'] = {'cart': cart, 'tax': tax, 'final_amount': final_amount,'total_cart_amount': total_cart_amount, 'total_cart': len(cart)}
        return context




class CartUpdate(LoginRequiredMixin, TemplateView):
    def post(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        cart.quantity = int(request.POST['qty'])
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",
              type(cart.quantity), cart.quantity)
        cart.total = cart.quantity * cart.book.book_price
        cart.save()
        messages.success(request, 'Your Quanity has been Updated!')
        return redirect('order:cartview')


class CartDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        cart = Cart.objects.get(pk=self.kwargs['pk'])
        if cart:
            cart.delete()
            messages.success(request, 'Card has been delete!')
        return redirect('order:cartview')

## >>>>>>>>>>>>>>>>>>>>>>>>>>>>Order part >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##


class OrderView(LoginRequiredMixin, CreateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        neworder = Order()
        profile = Student.objects.filter(user=self.request.user).first()
        neworder = Order.objects.create(user=self.request.user, profile=profile)
        cart = Cart.objects.filter(user=self.request.user)
        for car in cart:
            item = OrderItem.objects.create(
                order=neworder,
                book=car.book,
                price=car.price,
                quantity=car.quantity,
                total=car.total)
            car.delete()
            messages.success(request, 'Your order has been placed Succesfully!')
        total_cart_amount = 0

        for c in cart:
            total_cart_amount = total_cart_amount + \
                (c.book.book_price) * int(c.quantity)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>.", type(
            total_cart_amount), (total_cart_amount / 100) * 18)
        tax = (total_cart_amount / 100) * 18
        neworder.total_price = total_cart_amount+tax
        # print(">>>>>>>>>>>>>>>>>>price total>", neworder.total_price)
        trackno = 'verma'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'verma'+str(random.randint(1111111, 9999999))
        neworder.tracking_no = trackno
        neworder.save()
        return redirect('product:shopview')


##.....................PAYTM PAYMENT INTEGRATIONS ....................................###
##......................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,######

## payment views

def initiate_payment(request):
    try:
        amount = float(request.POST['amount'])
        print('final_amount', request.POST['amount'], type(
            request.POST['amount']))
    except Exception as e:
        print(e)
        return render(request, 'user/cart.html')
    transaction = Transaction.objects.create(amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY
    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', transaction.made_by),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/order/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    print('params ', params)
    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)
    transaction.checksum = checksum
    transaction.save()
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'user/redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(
            paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            msg = 'Your payment made successfully done.'
        else:
            msg = 'Your payment failed. Please try again later.'
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'user/callback.html', context=received_data)
        #return render(request, 'mycart.html', context=received_data)
        # return redirect('/')
        return render(request, 'user/callback.html', context=received_data)


###...............................STRIPE INTEGRATIONS ........................................##
######################## Stripe View ##########################################################


stripe.api_key = settings.STRIPE_SECRET_KEY
class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        host = self.request.get_host()
        user = request.user
        neworder = Order()
        profile = Student.objects.filter(user=self.request.user).first()
        neworder = Order.objects.create(
            user=self.request.user, profile=profile)
        cart = Cart.objects.filter(user=self.request.user)
        total_cart_amount = 0.00
        for c in cart:
            total_cart_amount = total_cart_amount + \
                (c.book.book_price) * int(c.quantity)
        tax = (total_cart_amount / 100) * 18
        neworder.total_price = total_cart_amount+tax
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': int(neworder.total_price * 100),
                        'product_data': {
                            'name': 'School Library Book online payment',
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity':1,
                },
            ],
            mode='payment',
            success_url="http://{}{}".format(host,
                                             reverse('order:payment-success')),
            cancel_url="http://{}{}".format(host,
                                            reverse('order:payment-cancel')),
        )
        for car in cart:
            item = OrderItem.objects.create(
                order=neworder,
                book=car.book,
                price=car.price,
                quantity=car.quantity,
                total=car.total)
            car.delete()
        trackno = 'verma'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'verma'+str(random.randint(1111111, 9999999))
        neworder.tracking_no = trackno
        neworder.save()
        # messages.success(request, 'Your order has been placed Succesfully!')
        return redirect(checkout_session.url, code=303)


def paymentSuccess(request):
    context = {
        'payment_status': 'success'
    }
    return render(request, 'user/success.html', context)


def paymentCancel(request):
    context = {
        'payment_status': 'Cancel'
    }
    return render(request, 'user/cancel.html', context)

# class ProductLandingPageView(TemplateView):
#     template_name = "user/landing.html"

#     def get_context_data(self, **kwargs):
#         # product = Product.objects.get(name="Test Product")
#         # card = Cart.objects.filter(product=product)
#         context = super(ProductLandingPageView, self).get_context_data(**kwargs)
#         context.update({
#             # "product": product,
#             # "card": card,

#             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
#         })
#         return context


# class SuccessView(TemplateView):
#     template_name = "user/success.html"


# class CancelView(TemplateView):
#     template_name = "user/cancel.html"


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        if session.payment_status == "paid":
            line_item = session.list_line_items(session.id, limit=1).data[0]
            order_id = line_item['description']
            fulfill_order(order_id)

        customer_email = session["customer_details"]["email"]
        book_id = session["metadata"]["book_id"]

        book = Book.objects.get(id=book_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {book.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        book_id = intent["metadata"]["product_id"]

        book = Book.objects.get(id=book_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {book.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

    return HttpResponse(status=200)


def fulfill_order(order_id):
    order = Order.objects.get(id=order_id)
    order.ordered = True
    order.orderDate = datetime.datetime.now()
    order.save()

    for item in order.items.all():
        book_var = BookVarification.objects.get(id=item.book.id)
        book_var.stock = item.quantity
        book_var.save()

    pass


# class StripeIntentView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             req_json = json.loads(request.body)
#             customer = stripe.Customer.create(email=req_json['email'])
#             product_id = self.kwargs["pk"]
#             product = Product.objects.get(id=product_id)
#             intent = stripe.PaymentIntent.create(
#                 amount=product.price,
#                 currency='usd',
#                 customer=customer['id'],
#                 metadata={
#                     "product_id": product.id
#                 }
#             )
#             return JsonResponse({
#                 'clientSecret': intent['client_secret']
#             })
#         except Exception as e:
#             return JsonResponse({ 'error': str(e) })
