Feature: Log in to website
	As a user of wallhaven.cc
	I want to be able to log in
	So that I can have my settings saved

	@BaseCase
	Scenario: Log in with correct input
		Given the user is not logged in
		When the user enters the username "cs1699test" and password "arctic"
		Then the user should be notified he is logged in
	
	@BaseCase
	Scenario: Log in with wrong input
		Given the user is not logged in
		When the user enters the username "cs1699test" and password "polar"
		Then the user should be notified he is not logged in