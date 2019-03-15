from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebCondominioPage(BasePage):
    lblTitle = (By.ID, 'page-header-title')
    btnStartCreateBuild = (By.ID, 'create-building')
    txtSearch = (By.ID, 'search')

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == 'Câmeras'

    def clicar_logoff(self):
        self.click(self.btnLogout)

    def clicar_inicioCriarCondominio(self):
        self.click(self.btnStartCreateBuild)

    def realiza_search(self, nCondominio):
        self.type_in(self.txtSearch, nCondominio)
        self.click(self.btnSearch)
        time.sleep(30)

