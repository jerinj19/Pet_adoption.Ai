from django.urls import path
from userside import views
urlpatterns=[
    path('userindex/',views.userdashboard,name="userindex"),
    path('userregister/',views.user_register_page,name="user_register"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('userlogin/',views.user_login_page,name="userlogin"),
    path('login_user/',views.loginUser,name="login")
]