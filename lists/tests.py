from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # resolve function Django uses internally to resolve URLs and find function/view should map
        found = resolve('/')
        self.assertEqual(found.func, home_page)
