from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include("myapp.api.base.urls")),
    path('api/v2/', include("myapp.api.versioned.v2.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
