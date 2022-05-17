from django.urls import path
from admin_portal.products.views import  Add_Auther_Ajax,  Add_product_Ajax, AuthorDeleteView, AuthorUpdateView,ProductDeleteView, ProductUpdateView, PublisherDeleteView, add_publisher, publisher_list, update_publisher

from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [

    ## .................Product Url  .....................###
   
    path('', Add_product_Ajax.as_view(), name='add_product_ajax'),
    # path('', productListView.as_view(), name='product_list'),
    # path('product_add/', AddproductView.as_view(), name='product_add'),
    path('product_update/<int:pk>/',ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/',ProductDeleteView.as_view(), name='product_delete'),

    # path('ajax/crud/create/',  CreateproductUser.as_view(), name='crud_ajax_create'),

    ##....................Brand url .................##

    # path('add_publisher_ajax/', Add_Publisher_Ajax.as_view(), name='add_publisher_ajax'),
    path('publisher_list/', publisher_list, name='publisher_list'),
    path('add_publisher/', add_publisher, name='add_publisher'),
    path('publisher_update/<int:pk>/',update_publisher, name='publisher_update'),
    # path('brand/', BrandListView.as_view(), name='brand_list'),
    # path('brand_add/', AddBrandView.as_view(), name='brand_add'),
    # path('publisher_update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher_delete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher_delete'),
    
    #######,,,,,,,,,,,Author part url ,,,,,,,,,,,#################

    path('add_author_ajax/', Add_Auther_Ajax.as_view(), name='add_author_ajax'),
    # path('brand/', BrandListView.as_view(), name='brand_list'),
    # path('brand_add/', AddBrandView.as_view(), name='brand_add'),
    path('author_update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
