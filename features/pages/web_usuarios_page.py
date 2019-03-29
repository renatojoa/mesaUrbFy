from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebUsuariosPage(BasePage):
    lblTitle = (By.ID, 'page-header-title')
    txtSearch = (By.ID, 'search')
    btnSearch = By.ID, 'search-icon'

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == 'Câmeras'

    def realiza_search(self, nUsuario):
        self.type_in(self.txtSearch, nUsuario)
        self.click(self.btnSearch)

    def valida_item(self, nUsuario):
        print(self.return_elements_on_cell(nUsuario))