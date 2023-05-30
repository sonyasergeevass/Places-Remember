from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

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
        self.memory = Memory.objects.create(title='Test Memory',
                                            description='This is a test '
                                                        'memory.',
                                            latitude='10.123',
                                            longitude='20.456',
                                            user=self.user
                                            )
        self.url = reverse('memory_detail', args=[self.memory.id])

    def test_login_page_vk(self):
        response = self.client.get(reverse('login_vk'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_page_vk.html')

    def test_home_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

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
        # self.assertEqual(memories.count(), 1)
        memory = memories.first()
        self.assertEqual(memory.latitude, 10.123)
        self.assertEqual(memory.longitude, 20.456)
        self.assertEqual(memory.title, 'Test Memory')
        self.assertEqual(memory.description, 'This is a test memory.')
        self.assertEqual(str(memory), 'Test Memory')

    def test_memory_detail_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memory_detail.html')
        self.assertContains(response, self.memory.title)
        self.assertContains(response, self.memory.description)

    def test_custom_login_required(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
