Feature: Uploading wallpapers
	As a developer of wallhaven.cc
	I want to stop non users from uploading pictures
	So that I can keep my site safe from random uploads.

	@BaseCase @upload
	Scenario: Not signed in tagging
		Given the user isn't signed in
		And user is at the homepage "http://alpha.wallhaven.cc"		
		When the user tries to click the upload button
		Then the user should be forwarded to the login page.
	
	@BaseCase @upload
	Scenario: signed in tagging
		Given the user is already signed in
		And user is at the homepage "http://alpha.wallhaven.cc"
		When the user tries to click the upload button
		Then the user should be forwarded to the upload page.