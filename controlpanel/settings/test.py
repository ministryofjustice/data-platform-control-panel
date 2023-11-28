# First-party/Local
from controlpanel.settings.common import *

ENV = "test"

LOG_LEVEL = "WARNING"

LOGGING["loggers"]["django_structlog"]["level"] = LOG_LEVEL  # noqa: F405
LOGGING["loggers"]["controlpanel"]["level"] = LOG_LEVEL  # noqa: F405

AUTHENTICATION_BACKENDS = [
    "rules.permissions.ObjectPermissionBackend",
    "django.contrib.auth.backends.ModelBackend",
]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

OIDC_RP_CLIENT_ID = "testing"
OIDC_RP_CLIENT_SECRET = "testing"
OIDC_RP_SCOPES = "openid email profile offline_access"
OIDC_OP_CONF_URL = "https://testing.oidc.com/.well-known/openid-configuration"


AUTHLIB_OAUTH_CLIENTS = {
    "auth0": {
        "client_id": OIDC_RP_CLIENT_ID,
        "client_secret": OIDC_RP_CLIENT_SECRET,
        "server_metadata_url": OIDC_OP_CONF_URL,
        "client_kwargs": {"scope": OIDC_RP_SCOPES},
    }
}

