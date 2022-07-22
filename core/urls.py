from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('authentication.urls')),
    path('api/v1/fa/', include('fixed_assets.urls'))
]
