Feature: Downloading wallpapers
	As a user of wallhaven.cc
	I want to be able to download any wallpaper
	So that I can use them offline.

	@BaseCase @download
	Scenario: Not signed in tagging
		Given the user is not signed in
		And user is at link "http://alpha.wallhaven.cc/wallpaper/114060"
		When the user tries to get the link to file
		Then the link should exist and the image therefore be downloadable.
	
	@BaseCase @download
	Scenario: signed in tagging
		Given the user is signed in
		And user is at link "http://alpha.wallhaven.cc/wallpaper/114060"
		When the user tries to get the link to file
		Then the link should exist and the image therefore be downloadable.