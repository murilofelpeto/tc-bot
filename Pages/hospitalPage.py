from page_objects import PageObject, PageElement 

class HospitalPage(PageObject):
	desintoxicar = PageElement(xpath="//button[@class='btn btn-small btn-inverse pull-left']")