from page_objects import PageObject, PageElement 

class RightMenuPage(PageObject):
	stamina = PageElement(xpath="//div[contains(text(),'Stamina')]")
	vicio = PageElement(xpath="//div[contains(text(), 'Addiction')]")