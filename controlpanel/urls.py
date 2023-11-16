from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("controlpanel.interfaces.web.urls")),
    path("admin/", admin.site.urls),
    path("", include("controlpanel.interfaces.urls")),
]
