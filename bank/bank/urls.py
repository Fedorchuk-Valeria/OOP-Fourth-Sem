from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_page.urls')),
    path('home/', include('main_page.urls')),
    path('office/', include('office.urls'))
]
