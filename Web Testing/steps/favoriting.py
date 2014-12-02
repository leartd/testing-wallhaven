# This Python file uses the following encoding: utf-8
from behave import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from downloading import browser

browser = None
username = 'cs1699'
password = 'arctic'

def cleanUpGlobals():
	global browser
	browser.quit()
	browser = None
	
class favoritingTest(unittest.TestCase):

	@given(u'the user is signed-in')
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
			cleanUpGlobals()
			assert False

	@given(u'user is at image "{text}"')
	def step_impl(context, text):
		global browser
		try:
			browser.get(text)
		except Exception, e:
			cleanUpGlobals()
			assert False

	@given(u'the image hasn\'t been favorited')
	def step_impl(context):
		global browser
		try:
			assert "Add to Favorites" in browser.page_source
		except Exception, e:
			cleanUpGlobals()
			assert False	

	@when(u'the user attempts favorite an image')
	def step_impl(context):
		global browser
		try:
			button = browser.find_element_by_id("fav-add-button")
			webdriver.ActionChains(browser).move_to_element(button).click(button).perform()
		except Exception, e:
			cleanUpGlobals()
			assert False	

	@then(u'the user should be shown it has been favorited')
	def step_impl(context):
		global browser
		try:
			assert "In Favorites" in browser.page_source
			button = browser.find_element_by_class_name("rm-button")
			webdriver.ActionChains(browser).move_to_element(button).click(button).perform()
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False		

	@given(u'the image has been favorited')
	def step_impl(context):
		global browser
		try:
			assert "In Favorites" in browser.page_source
		except Exception, e:
			cleanUpGlobals()
			assert False		

	@when(u'the user attempts to unfavorite the image')
	def step_impl(context):
		global browser
		try:
			button = browser.find_element_by_class_name("rm-button")
			webdriver.ActionChains(browser).move_to_element(button).click(button).perform()
		except Exception, e:
			cleanUpGlobals()
			assert False	

	@then(u'the user should be shown it has been unfavorited')
	def step_impl(context):
		global browser
		try:
			assert "Add to Favorites" in browser.page_source
			button = browser.find_element_by_id("fav-add-button")
			webdriver.ActionChains(browser).move_to_element(button).click(button).perform()
			cleanUpGlobals()
		except Exception, e:
			cleanUpGlobals()
			assert False
