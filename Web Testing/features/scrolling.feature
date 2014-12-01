Feature: Scrolling Wallpapers
	As a user of wallhave.cc
	I want to be able to see as many wallpapers as I want
	So that I choose a wallpaper better.

	@BaseCase
	Scenario: Not logged in tagging
		Given the user is at page "wallhaven.cc/lastUpdates"
		When he is at the first page
		Then there should be wallpapers there.
	
	@BaseCase
	Scenario: Not logged in tagging
		Given the user is at page "wallhaven.cc/lastUpdates"
		When the user scrolls to page number 10
		Then there should be wallpapers there.

	@BaseCase
	Scenario: Not logged in tagging
		Given the user is at page "wallhaven.cc/lastUpdates"
		When the user scrolls to page number 100
		Then there should be wallpapers there.

	@BaseCase
	Scenario: Not logged in tagging
		Given the user is at page "wallhaven.cc/lastUpdates"
		When the user scrolls to the last page
		Then there should be wallpapers there.