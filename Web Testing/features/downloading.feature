Feature: Downloading wallpapers
	As a user of wallhaven.cc
	I want to be able to download any wallpaper
	So that I can use them offline.

	@BaseCase
	Scenario: Not logged in tagging
		Given the user is not logged in
		And user at image "wallhaven.cc/asfadsfsdf"
		When the user attempts to download the picture
		Then the user should have the picture start download
	
	@BaseCase
	Scenario: Logged in tagging
		Given the user is logged in
		And user at image "wallhaven.cc/asfadsfsdf"
		When the user attempts to download the picture
		Then the user should have the picture start download