from page_objects import PageObject, PageElement 

class LoginPage(PageObject):
	username = PageElement(xpath="//input[@placeholder='Username']")
	password = PageElement(xpath="//input[@placeholder='Password']")
	submit = PageElement(xpath="//button[@type='submit']")
	roubo = PageElement(xpath="//div[@id='menu-robbery']")
	mainDiv = PageElement(xpath="//div[@id='app']")