# This Python file uses the following encoding: utf-8
from behave import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = None
username = None

def cleanUpGlobals():
	global browser
	browser.quit()
	browser = None
	global username
	username = None

class logInTest(unittest.TestCase):

	@given(u'the user is not logged in')
	def step_impl(context):
		global browser
		browser = webdriver.Firefox()
		browser.get('http://alpha.wallhaven.cc/')		
		try:
			assert 'wallhaven' in browser.title
			assert "Login" in browser.page_source
		except Exception, e:
			cleanUpGlobals()
			assert False

	@when(u'the user enters the username "{text}"')
	def step_impl(context, text):
		try:
			global username
			username = text
			login = browser.find_element_by_id('username')
			login.send_keys(text)
		except Exception, e:
			cleanUpGlobals()
			assert False

	@when(u'password "{text}"')
	def step_impl(context, text):
		global browser
		try:
			login = browser.find_element_by_id('password')
			login.send_keys(text)
			login.send_keys(Keys.RETURN)
			# browser.find_element_by_type("submit").click()
		except Exception, e:
			e

	@then(u'the user should be notified he is logged in')
	def step_impl(context):
		try:
			assert 'Login' not in browser.page_source
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False

	@then(u'the user should be notified he is not logged in')
	def step_impl(context):
		try:
			assert 'Login' in browser.page_source
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False