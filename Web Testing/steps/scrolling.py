# This Python file uses the following encoding: utf-8
from behave import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = None

def cleanUpGlobals():
	global browser
	browser.quit()
	browser = None

class scrollingTest(unittest.TestCase):

	@given(u'the user is at page "{text}"')
	def step_impl(context, text):
		global browser
		try:
			browser = webdriver.Firefox()
			browser.get(text)
		except Exception, e:
			cleanUpGlobals()
			assert False

	@when(u'he is at the first page')
	def step_impl(context):
		pageNumbers = browser.find_elements_by_class_name("thumb-listing-page-num")
		if len(pageNumbers) == 1:
			assert True
		else:
			cleanUpGlobals()
			assert False

	@then(u'there should be wallpapers there.')
	def step_impl(context):
		thumbsList = browser.find_elements_by_class_name('thumb')
		if len(thumbsList) > 0:
			cleanUpGlobals()
			assert True
		else:
			cleanUpGlobals()
			assert False		

	@when(u'the user scrolls to page number "{text}"')
	def step_impl(context, text):
		i = 1 #starting page
		n = int(text) - 1
		try:
			while i < n:
				browser.execute_script("window.scrollTo(0,document.body.scrollHeight)", "")	
				pageNumbers = browser.find_elements_by_class_name("thumb-listing-page-num")
				for x in pageNumbers:
					if x.text != '':
						if (i+1) == int(x.text):
							i += 1
							# print x.text
		except Exception, e:
			cleanUpGlobals()
			assert False