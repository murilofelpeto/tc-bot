from page_objects import PageObject, PageElement, MultiPageElement

class NightClubPage(PageObject):
	whoreHouseTab = PageElement(xpath="//a[@href='#/nightlife/whorehouses']")
	whorehouses = MultiPageElement(xpath="//table[@class='table table-condensed']")
	whores = PageElement(xpath="//table[@class='table table-condensed table-top-spacing']")
	exit = PageElement(xpath="//button[@class='btn btn-inverse btn-large pull-right']")