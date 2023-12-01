from django.urls import reverse

import pytest

from controlpanel.interfaces.web.views import BaseView


class TestBaseView:
    @pytest.fixture
    def view_obj(self, rf, superuser):
        view = BaseView()
        request = rf.get("/")
        request.user = superuser
        view.request = request
        return view

    def test_get_context_data(self, view_obj):
        context = view_obj.get_context_data()
        assert "nav_items" in context
        assert "header_nav_items" in context
        assert "header_organisation_url" in context
        assert "header_service_url" in context

    def test_get_nav_items(self, view_obj):
        nav_items = view_obj.get_nav_items()
        home = {"name": "Home", "url": "/", "active": True}
        data_products = {"name": "Data Products", "url": reverse("data-products"), "active": False}
        assert home in nav_items
        assert data_products in nav_items
