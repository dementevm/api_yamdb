from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import api_users.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_users.urls)),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
    path('auth/', include('django.contrib.auth.urls')),

]
