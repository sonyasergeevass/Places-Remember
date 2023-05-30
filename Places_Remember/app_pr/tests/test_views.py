from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from app_pr.models import Memory


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.social_account = SocialAccount.objects.create(
            user=self.user,
            provider='vk',
            extra_data={}
        )

    def test_login_page_vk(self):
        response = self.client.get(reverse('login_vk'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_page_vk.html')

    def test_home_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login_vk'))

    def test_add_mem(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_mem'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_mem.html')

        post_data = {
            'latitude': '10.123',
            'longitude': '20.456',
            'title': 'Test Memory',
            'description': 'This is a test memory.'
        }
        response = self.client.post(reverse('add_mem'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))

        memories = Memory.objects.filter(user=self.user)
        self.assertEqual(memories.count(), 1)
        memory = memories.first()
        self.assertEqual(memory.latitude, 10.123)
        self.assertEqual(memory.longitude, 20.456)
        self.assertEqual(memory.title, 'Test Memory')
        self.assertEqual(memory.description, 'This is a test memory.')
