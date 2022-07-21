from django.urls import path
from admin_portal.products.views import  Add_Auther_Ajax, Add_Book_Ajax, AuthorDeleteView, AuthorUpdateView, BookDeleteView, BookUpdateView, PublisherDeleteView, PublisherUpdateView, add_publisher, publisher_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [

    ## .................Product Url  .....................###
   
    path('', Add_Book_Ajax.as_view(), name='add_book_ajax'),
    path('book_update/<int:pk>/',BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<int:pk>/',BookDeleteView.as_view(), name='book_delete'),

    # path('ajax/crud/create/',  CreateproductUser.as_view(), name='crud_ajax_create'),

    ##....................Brand url .................##

 
    path('publisher_list/', publisher_list, name='publisher_list'),
    path('add_publisher/', add_publisher, name='add_publisher'),
    path('publisher_update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher_delete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher_delete'),
    
    #######,,,,,,,,,,,Author part url ,,,,,,,,,,,#################

    path('author_list/', Add_Auther_Ajax.as_view(), name='author_list'),
    path('author_update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
