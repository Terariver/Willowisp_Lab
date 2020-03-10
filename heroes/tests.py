from django.test import TestCase


class HomePageTest(TestCase):


	def test_home_page_returns_correct(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'heroes.html')


class CloudPageTest(TestCase):


	def test_cloud_hero_page_returns_correct(self):
		response = self.client.get('/hero/cloud')
		self.assertTemplateUsed(response, 'detail_cloud.html')