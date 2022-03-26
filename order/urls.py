from django.urls import path
from order.views import AddToCartView,CartDelete, CartUpdate, CartView, CreateCheckoutSessionView, OrderView, initiate_payment,callback, paymentCancel, paymentSuccess


app_name = 'order'

urlpatterns = [
         path('cartview/',CartView.as_view(), name='cartview'),
         path('addtocart/<int:pk>/',AddToCartView.as_view(), name='addtocart'),
         path('updatecart/<int:pk>/',CartUpdate.as_view(), name='updatecart'),
         path('deletecart/<int:pk>/',CartDelete.as_view(), name='deletecart'),
         path('orderview/',OrderView.as_view(), name='orderview'),



        ################ Stripe ##################
        # path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
        # path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
        path('payment-cancel/', paymentCancel, name='payment-cancel'),
        path('payment-success/', paymentSuccess, name='payment-success'),
        # path('landing-page/', ProductLandingPageView.as_view(), name='landing-page'),
        path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
      
     


        # payment
        path('pay/', initiate_payment, name='pay'),
        path('callback/', callback, name='callback'),

     
]