from django.urls import path
from adminapp import views
urlpatterns=[
    path('index_admin/',views.index_admin,name="index"),
    path('contact/',views.about,name="contact")
]
