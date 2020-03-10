from django.test import TestCase


class HomePageTest(TestCase):


	def test_home_page_returns_correct(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'heroes.html')

