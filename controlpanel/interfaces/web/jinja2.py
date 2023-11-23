from django.templatetags.static import static
from django.urls import reverse

from jinja2 import ChoiceLoader, Environment, PackageLoader, PrefixLoader


def environment(**kwargs):
    default_filesystem_loader = kwargs["loader"]
    kwargs.update(
        {
            "loader": ChoiceLoader(
                [
                    default_filesystem_loader,
                    PrefixLoader({"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}),
                ]
            ),
        }
    )
    env = Environment(**kwargs)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env
