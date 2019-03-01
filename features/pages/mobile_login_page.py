from features.pages.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
from features.pages.codeRequest_page import CodeRequestPage
import time


class MobileLoginPage(BasePage):
    lblWelcome = MobileBy.ACCESSIBILITY_ID, 'Seja bem-vindo!'
    btnEnterLogin = MobileBy.ACCESSIBILITY_ID, 'Entrar no urbfy'
    btnEnterSLogin = MobileBy.ACCESSIBILITY_ID, 'Entrar sem cadastro'
    btnPolitic = MobileBy.ACCESSIBILITY_ID, 'Política de privacidade'

    #   Valida Page de login
    def valida_page(self):
        time.sleep(40)
        self.wait(self.lblWelcome, 60)
        print(self.lblWelcome.text)
        assert self.lblWelcome.text == "Seja bem-vindo!"

    #   Realizar inicio de acesso com login
    def clicar_btnEnterLogin(self):
        self.click(self.button_cadastro)
        return CodeRequestPage

    #   Realizar acesso sem login
    def clicar_btnEnterSLogin(self):
        self.click(self.btnEnterSLogin)

    #   Encaminhado para tela de Politica e privacidade
    def clicar_btnPolitic(self):
        self.click(self.btnPolitic)
