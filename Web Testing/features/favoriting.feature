Feature: Text Tagging wallpapers
	As a user of wallhave.cc
	I want to be able to favorite any wallpaper
	So that I can go back to them later

	@BaseCase @fave
	Scenario: Signed in favoriting
		Given the user is signed-in
		And user is at image "http://alpha.wallhaven.cc/wallpaper/114060"
		And the image hasn't been favorited
		When the user attempts favorite an image
		Then the user should be shown it has been favorited
	
	@BaseCase @fave
	Scenario: Signed in unfavoriting
		Given the user is signed-in
		And user is at image "http://alpha.wallhaven.cc/wallpaper/114138"
		And the image has been favorited
		When the user attempts to unfavorite the image
		Then the user should be shown it has been unfavorited