from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("controlpanel.interfaces.urls")),
    path("admin/", admin.site.urls),
]
