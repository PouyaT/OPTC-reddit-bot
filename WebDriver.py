from selenium import webdriver

def browse(url):
	
	#sets the options for the browser
	browser_options = webdriver.FirefoxOptions()
	browser_options.set_headless(headless=True)

	#intializes them for the driver
	browser = webdriver.Firefox(firefox_options=browser_options)

	#takes in the url
	browser.get(url)
	
	#searches for the wanted id
	element = browser.find_element_by_id("mainTable_info")
	
	#takes in what it in that id
	numberOfEntries = element.text
	
	browser.quit()
	
	return numberOfEntries
	