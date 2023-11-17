from controlpanel.interfaces.web import auth, data_products
from controlpanel.interfaces.web.views import IndexView
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", auth.OIDCLoginView.as_view(), name="login"),
    path("authenticate/", auth.OIDCAuthenticationView.as_view(), name="authenticate"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    path("login-fail/", auth.LoginFail.as_view(), name="login-fail"),
    path("data-products/", data_products.DataProductsView.as_view(), name="data-products"),
]
