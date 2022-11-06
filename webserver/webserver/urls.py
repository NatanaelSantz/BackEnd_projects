from django.contrib import admin
from django.urls import path
from user.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", index, name="index",)
]
