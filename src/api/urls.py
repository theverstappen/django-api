from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('blog.urls'))
]