from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time, os



class WebAdminUrbfyCreatePage(BasePage):
    lblTitle = (By.ID, "page-header-title")
    txtAdminName = (By.ID, "admin-name")
    txtAdminEmail = (By.ID, 'admin-email')
    btnCreateAdminUrbfy = (By.ID, 'create-admin-button')

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == "Criar Condominio"

    def inserir_nomeAdmin(self, nome):
        self.type_in(self.txtAdminName, nome)

    def inserir_emailAdmin(self, email):
        self.type_in(self.txtAdminEmail, email)

    def clicar_criarAdminUrbfy(self):
        self.click(self.btnCreateAdminUrbfy)
        self.wait(10)