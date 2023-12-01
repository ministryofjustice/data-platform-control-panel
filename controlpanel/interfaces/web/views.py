from typing import Any

from django.urls import reverse
from django.views.generic import TemplateView

from controlpanel.core.models import User
from controlpanel.interfaces.web.auth.mixins import OIDCLoginRequiredMixin


class BaseView(OIDCLoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Adds context used in the nav and header
        """
        context = super().get_context_data(**kwargs)
        context["nav_items"] = self.get_nav_items()
        context.update(self.get_header_context())
        return context

    def get_nav_items(self) -> list[dict]:
        return [
            {"name": "Home", "url": "/", "active": self.request.get_full_path() == "/"},
            {
                "name": "Data Products",
                "url": reverse("data-products"),
                "active": self.request.get_full_path() == reverse("data-products"),
            },
        ]

    def get_header_context(self) -> dict[str, Any]:
        login_logout_url = (
            reverse("logout") if self.request.user.is_authenticated else reverse("login")
        )
        return {
            "header_nav_items": [
                {
                    "name": self.request.user.name,
                    "url": "#tbc",
                    "active": True,
                },
                {
                    "name": "Sign out" if self.request.user.is_authenticated else "Sign in",
                    "url": login_logout_url,
                    "active": self.request.get_full_path() == login_logout_url,
                },
            ],
            "header_organisation_url": "https://www.gov.uk/government/organisations/ministry-of-justice",  # noqa
            "header_service_url": "https://github.com/ministryofjustice/data-platform",
        }


class IndexView(BaseView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "users": User.objects.all(),
            }
        )
        return context
