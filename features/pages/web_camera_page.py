from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebCameraPage(BasePage):
    lblTitle = (By.ID, 'page-header-title')
    btnStartCreateCamera = (By.ID, 'create-camera')
    txtSearch = (By.ID, 'search')
    btnForgot = (By.ID, 'login-link')
    btnLogin = (By.ID, 'login-button')
    btnSearch = (By.ID, 'search-icon')

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == 'Câmeras'

    def clicar_logoff(self):
        self.click(self.btnLogout)

    def clicar_menuCriarCamera(self):
        self.click(self.btnStartCreateCamera)

    def realiza_search(self, nCamera):
        self.type_in(self.txtSearch, nCamera)
        self.click(self.btnSearch)
        time.sleep(30)

