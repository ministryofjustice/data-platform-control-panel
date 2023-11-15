from django.urls import path

from controlpanel.interfaces.web import auth
from controlpanel.interfaces.web.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", auth.OIDCLoginView.as_view(), name="login"),
    path("authenticate/", auth.OIDCAuthenticationView.as_view(), name="authenticate"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("login-fail/", auth.LoginFail.as_view(), name="login-fail"),
]
