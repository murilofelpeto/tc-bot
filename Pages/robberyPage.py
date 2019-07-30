from page_objects import PageObject, PageElement, MultiPageElement

class RobberyPage(PageObject):
	robberySelect = PageElement(xpath="//select[@id='singlerobbery-select-robbery']")
	robberyButton = PageElement(xpath="//button[@id='singlerobbery-rob']")