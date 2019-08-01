from page_objects import PageObject, PageElement 

class LeftMenuPage(PageObject):
	robberyMenu = PageElement(xpath="//div[@id='menu-robbery']")
	clubMenu = PageElement(xpath="//div[@id='menu-nightlife']")