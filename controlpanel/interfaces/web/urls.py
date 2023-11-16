from django.urls import path
from controlpanel.interfaces.web import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
