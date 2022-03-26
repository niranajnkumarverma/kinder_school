from django.urls import path
from admin_portal.products.views import AddproductView,  ProductDeleteView, ProductUpdateView, productListView
from admin_portal.products.views import BrandListView, AddBrandView,BrandUpdateView,BrandDeleteView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
   
    ## .................Product Url  .....................###
  
    path('', productListView.as_view() , name='product_list'),
    path('product_add/', AddproductView.as_view() , name='product_add'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view() , name= 'product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view() , name= 'product_delete'),

    # path('ajax/crud/create/',  CreateproductUser.as_view(), name='crud_ajax_create'),

    ##....................Brand url .................##

    path('brand/', BrandListView.as_view() , name='brand_list'),
    path('brand_add/', AddBrandView.as_view() , name='brand_add'),
    path('brand_update/<int:pk>/', BrandUpdateView.as_view() , name= 'brand_update'),
    path('brand_delete/<int:pk>/', BrandDeleteView.as_view() , name= 'brand_delete'),
  



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
