from django.urls import path
from admin_pannel import views
urlpatterns=[
    path('adminpannel/',views.admin_index,name="adminindex"),
    path('admin_loginpage/',views.adminlogin_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="adminlogin"),
    path('admin_logout/',views.adminlogout,name="adminlogout"),
    path('adminadd/',views.admin_add,name="adminadd"),
    path('saveadd/',views.saveadd,name="saveadd"),
    path('viewadd/',views.viewadd,name="viewadd"),
    path('edit/<int:A_id>/',views.editadd,name="edit"),
    path('update/<int:u_id>/',views.updateadd,name="update_add"),
    path('delete/<int:del_id>/',views.deleteadd,name="delete_add")
]
