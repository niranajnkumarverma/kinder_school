from django.urls import path
from .views import AboutView, ContactView, CourseView, EventView, GalleryView, LogoutView, TeacherView,  index, login_view, signup


# app_name = 'home'

urlpatterns = [
    #   path('', IndexView.as_view(), name='index'),
    #   path('signup/', SignUpView.as_view(), name='signup'),
    #   path('login/', UserLogin.as_view(), name='login'),

    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
  
    path('teacherview/', TeacherView.as_view(), name='teacherview'),
    path('contactview/', ContactView.as_view(), name='contactview'),
    path('aboutview/', AboutView.as_view(), name='aboutview'),
    path('courseview/', CourseView.as_view(), name='courseview'),
    path('galleryview/', GalleryView.as_view(), name='galleryview'),
    path('eventview/', EventView.as_view(), name='eventview'),
    path('logout/', LogoutView.as_view(), name='logout'),


]
