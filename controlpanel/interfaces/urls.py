from django.urls import include, path

urlpatterns = [
    path("", include("controlpanel.interfaces.web.urls")),
]
