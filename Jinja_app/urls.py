from django.urls import path
from Jinja_app import views

urlpatterns=[
   path('',views.home,name='my_home'),
   path('aboutus/',views.about,name='my_about'),
   path('contactus/',views.contact,name='my_contact'),
   path('gallery/',views.gallery,name='my_gallery')

]