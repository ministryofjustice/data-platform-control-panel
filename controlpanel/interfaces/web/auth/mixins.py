from django.contrib.auth.mixins import LoginRequiredMixin
from controlpanel.core.auth import OIDCSessionValidator


class OIDCLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is (still) authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if OIDCSessionValidator(request).expired():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
