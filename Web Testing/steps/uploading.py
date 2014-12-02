# This Python file uses the following encoding: utf-8
from behave import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = None
username = 'cs1699'
password = 'arctic'
link = None

def cleanUpGlobals():
	global browser
	browser.quit()
	browser = None
	global link
	link = None


class uploadingTest(unittest.TestCase):

	@given(u'the user is already signed in')
	def step_impl(context):
		global browser
		browser = webdriver.Firefox()
		browser.get('http://alpha.wallhaven.cc/')
		try:
			assert 'wallhaven' in browser.title
			assert "Login" in browser.page_source
			signin = browser.find_element_by_id('username')
			signin.send_keys(username)
			keyWord = browser.find_element_by_id('password')
			keyWord.send_keys(password)
			keyWord.send_keys(Keys.RETURN)
			assert username in browser.page_source
			assert "Login" not in browser.page_source
		except Exception, e:
			cleanUpGlobals()
			assert False

	@given(u'the user isn\'t signed in')
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

	@given(u'user is at the homepage "{text}"')
	def step_impl(context, text):
		global browser
		try:
			browser.get(text)
			assert "Awesome Wallpapers" in browser.title
		except Exception, e:
			cleanUpGlobals()
			assert False

	@when(u'the user tries to click the upload button')
	def step_impl(context):
		try:
			button = browser.find_element_by_class_name("upload")
			webdriver.ActionChains(browser).move_to_element(button).click(button).perform()
		except Exception, e:
			cleanUpGlobals()	
			assert False

	@then(u'the user should be forwarded to the login page.')
	def step_impl(context):
		try:
			assert "Login" in browser.title
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False

	@then(u'the user should be forwarded to the upload page.')
	def step_impl(context):
		try:
			assert "Upload" in browser.title
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False

