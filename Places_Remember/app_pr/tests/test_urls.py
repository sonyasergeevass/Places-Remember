from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from app_pr.views import add_mem, home_page, login_page_vk


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        urls = reverse('login_vk')
        self.assertEquals(resolve(urls).func, login_page_vk)

    def test_home_page_url_resolves(self):
        urls = reverse('home')
        self.assertEquals(resolve(urls).func, home_page)

    def test_add_mem_url_resolves(self):
        urls = reverse('add_mem')
        self.assertEquals(resolve(urls).func, add_mem)
