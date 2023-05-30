from django.test import TestCase, Client, RequestFactory
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
        self.memory = Memory.objects.create(title='Test Memory',
                                            description='This is a test memory.',
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


        # memories = Memory.objects.filter(user=self.user)
        # self.assertEqual(memories.count(), 1)
        # memory = memories.first()
        # self.assertEqual(memory.latitude, 10.123)
        # self.assertEqual(memory.longitude, 20.456)
        # self.assertEqual(memory.title, 'Test Memory')
        # self.assertEqual(memory.description, 'This is a test memory.')
        # self.assertEqual(str(memory), 'Test Memory')

    # def test_memory_detail_anonymous(self):
    #     # Access the memory detail view without logging in
    #     response = self.client.get(
    #         reverse('memory_detail', args=[self.memory.id]))
    #
    #     # Verify that the user is not authenticated
    #     self.assertFalse(response.wsgi_request.user.is_authenticated)
    #
    #     # Verify that the response status code is 200 (OK)
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Verify that the 'vk_data' context variable is empty
    #     self.assertEqual(response.context['vk_data'], {})
    #
    #     # Verify that the 'memory' context variable contains the expected
    #     # memory object
    #     self.assertEqual(response.context['memory'], self.memory)