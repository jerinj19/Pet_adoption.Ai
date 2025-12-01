
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from . import settings
import adminapp.urls
import admin_pannel.urls
import userside.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminapp/',include(adminapp.urls)),
    path('admin_pannel/',include(admin_pannel.urls)),
    path('userside/',include(userside.urls))

]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
