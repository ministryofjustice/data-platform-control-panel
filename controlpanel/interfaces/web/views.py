from controlpanel.core.models import User
from controlpanel.interfaces.web.auth.mixins import OIDCLoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class IndexView(OIDCLoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request):
        users = User.objects.all()
        context = {
            "user": request.user,
            "users": users,
        }
        return render(request, "home.html", context=context)
