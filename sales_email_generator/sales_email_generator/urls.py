from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("sea.urls")),
    path('admin/', admin.site.urls),
]
