Feature: Scrolling Wallpapers
	As a user of wallhave.cc
	I want to be able to see as many wallpapers as I want
	So that I choose a wallpaper better.

	@BaseCase @scroll
	Scenario: First Page no scrolling
		Given the user is at page "http://alpha.wallhaven.cc/search?categories=111&purity=100&sorting=date_added&order=desc"
		When he is at the first page
		Then there should be wallpapers there.
	
	@BaseCase @scroll
	Scenario: Scrolling to Page 10
		Given the user is at page "http://alpha.wallhaven.cc/search?categories=111&purity=100&sorting=date_added&order=desc"
		When the user scrolls to page number "10"
		Then there should be wallpapers there.

	@BaseCase @scroll
	Scenario: Scrolling to page 100
		Given the user is at page "http://alpha.wallhaven.cc/search?categories=111&purity=100&sorting=date_added&order=desc"
		When the user scrolls to page number "100"
		Then there should be wallpapers there.