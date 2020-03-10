from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def test_can_display_a_heroes_list_and_more_information_per_hero(self):
		# Widget has heard about a new wiki app for the game called The Will of the Wisps. 
		# She goes to check out its homepage
		browser.get('http://localhost:8000')

		# She notices the page title and header mention 
		# 'The Will of the Wisps Wiki'
		self.assertIn('The Will of the Wisps Wiki', self.browser.title)
		
		# She sees a list containing three heroes with their corresponding 
		# names, health points, and damage 
		self.assertIn('Cloud',self.browser.body)
		self.assertIn('Jester',self.browser.body)
		self.assertIn('Sunflowey',self.browser.body)
		self.assertIn('Health Points',self.browser.body)
		self.assertIn('Damage',self.browser.body)
		
		# When she selects one of the heroes, she is sent to another page
		# containing more information about the hero (additional stats, lore, image).
		self.assertIn('Base Attack Damage',self.browser.body)
		self.assertIn('Skills',self.browser.body)
		self.assertIn('Lore',self.browser.body
		
		# She spots the page title and header mentions the name of the hero she selected.
		self.assertIn("Detail - Jester", self.browser.title)
		self.assertIn("Detail - Jester", self.browser.head)
		
		# While she is in a specific hero's page, she sees a button labeled "Back to Heroes List".
		# She clicks this and she is redirected back to the wiki's homepage.	
		self.assertIn(button, self.browser.body)
		self.assertIn("Back to Heroes List",self.browser.body.button)

		self.fail('Finish the test!')