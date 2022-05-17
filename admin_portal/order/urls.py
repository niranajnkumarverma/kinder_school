from django.urls import path
from admin_portal.order.views import CartListView, OrderDetailView, OrderListView, OrderUpdateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'
urlpatterns = [


    path('', OrderListView.as_view(), name='order_list'),
    path('order_detail/', OrderDetailView.as_view(), name='order_detail'),
    path('order_update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    # path('order_delete/<int:pk>/', OrderDeleteView.as_view() , name='order_delete'),
    path('cart/', CartListView.as_view(), name='cart_list'),

    # path('product_add/', AddproductView.as_view() , name='product_add'),
    # path('product_update/<int:pk>/', ProductUpdateView.as_view() , name= 'product_update'),
    # path('product_delete/<int:pk>/', ProductDeleteView.as_view() , name= 'product_delete'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
