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


class downloadingTest(unittest.TestCase):

	@when(u'the user tries to get the link to file')
	def step_impl(context):
		global link
		try:
			imgLink = browser.find_element_by_id('wallpaper')
			link = imgLink.get_attribute('src')
		except Exception, e:
			cleanUpGlobals()
			assert False

	@then(u'the link should exist and the image therefore be downloadable.')
	def step_impl(context):
		try:
			browser.get(link)
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False

	@given(u'the user is signed in')
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
		except Exception, e:
			# cleanUpGlobals()
			assert False

	@given(u'user is at link "{text}"')
	def step_impl(context, text):
		global browser
		try:
			browser.get(text)
		except Exception, e:
			cleanUpGlobals()
			assert False

	@given(u'the user is not signed in')
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