from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('authentication.urls')),
    path('api/fa/', include('fixed_assets.urls'))
]
