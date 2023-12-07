from django.urls import reverse


def nav_items(request):
    data_products_url = reverse("data-products")
    return {
        "nav_items": [
            {"name": "Home", "url": "/", "active": request.get_full_path() == "/"},
            {
                "name": "Data Products",
                "url": data_products_url,
                "active": request.get_full_path() == data_products_url,
            },
        ]
    }


def header_context(request):
    is_logged_in = request.user.is_authenticated
    return {
        "header_nav_items": [
            {
                "name": request.user.name,
                "url": "",
            },
            {
                "name": "Sign out" if is_logged_in else "Sign in",
                "url": reverse("logout") if is_logged_in else reverse("login"),
            },
        ],
        "header_organisation_url": "https://www.gov.uk/government/organisations/ministry-of-justice",  # noqa
        "header_service_url": "https://github.com/ministryofjustice/data-platform",
    }
