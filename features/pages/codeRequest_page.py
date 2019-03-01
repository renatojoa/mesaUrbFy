from features.pages.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class CodeRequestPage(BasePage):
    lblNumberResquest = MobileBy.ACCESSIBILITY_ID, 'Preencha o campo abaixo'
    txtNumberInput = MobileBy.ACCESSIBILITY_ID, 'DDD + número de telefone'
    btnSendCode = MobileBy.ACCESSIBILITY_ID, 'Enviar código de acesso'
    btnVoltar = MobileBy.ACCESSIBILITY_ID, 'Voltar'

    #   Valida Page de Codigo request
    def valida_page(self):
        self.wait(self.lblNumberResquest, 30)
        print(self.lblNumberResquest.text)
        assert self.lblNumberResquest.text == "Preencha o campo abaixo com o número do seu celular para se cadastrar no aplicativo."

    #   Insere dados referente ao numero do celular do usuario
    def fill_Number(self, value):
        self.type_in(self, self.button_cadastro, value)

    #   Enviar Resquest a solicitação de numero
    def clicar_btnSendCode(self):
        self.click(self.btnSendCode)

    #   Volta para a tela de Login
    def clicar_btnVoltar(self):
        self.click(self.btnVoltar)