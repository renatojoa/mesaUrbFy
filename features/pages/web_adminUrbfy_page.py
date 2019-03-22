from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebAdminUrbfyPage(BasePage):

    lblTitle = (By.ID, 'page-header-title')
    btnStartCreateAdmin = (By.ID, 'create-admin')
    txtSearch = (By.ID, 'search-icon')

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == 'Câmeras'

    def clicar_logoff(self):
        self.click(self.btnLogout)

    def clicar_inicioCriarAdmin(self):
        self.click(self.btnStartCreateAdmin)

    def realiza_search(self, nAdmin):
        self.type_in(self.txtSearch, nAdmin)
        self.click(self.btnSearch)