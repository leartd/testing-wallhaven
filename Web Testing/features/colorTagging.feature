Feature: Text Tagging wallpapers
	As a user of wallhave.cc
	I want to be able to tag any wallpaper
	So that I can help the community find them more quickly.

	@BaseCase
	Scenario: Not logged in tagging
		Given the user is not logged in
		And user at image "wallhaven.cc/asfadsfsdf"
		When the user attempts to select the color for the wallpaper
		Then the user should be shown an add color tag field.
	
	@BaseCase
	Scenario: Logged in tagging
		Given the user is logged in
		And user at image "wallhaven.cc/asfadsfsdf"
		When the user attempts to select the color for the wallpaper
		Then the user should be shown an add color tag field.