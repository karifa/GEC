from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page
from .models import Departement

class HomePageTestCase(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('gec/home.html')
        self.assertEqual(response.content.decode(), expected_html)

class DepartementTestCase(TestCase):

    def test_can_save_a_departement(self):
        departement1 = Departement.objects.create(name='Math',
                                                  description='offer math')
        departement2 = Departement.objects.create(name='Computer Science',
                                                  description='help hummans')
        self.assertEqual(Departement.objects.count(), 2)
        self.assertEqual(departement1.name, 'Math')
