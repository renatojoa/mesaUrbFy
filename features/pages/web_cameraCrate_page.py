from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time



class WebCameraCreatePage(BasePage):
    lblTitle = (By.ID, "page-header-title")
    txtBuildName = (By.ID, "building-name")
    txtCameraName = (By.ID, "camera-name")
    txtCameraAddress = (By.ID, "camera-host")
    txtCameraUser = (By.ID, "camera-login")
    txtCameraPassword = (By.ID, "camera-password")
    btnCreateCamera = (By.ID, "create-camera-button")

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == "Criar Câmera"

    def inserir_nomeCondominio(self, nome):
        self.type_in(self.txtBuildName, nome)
        self.press_enter(self.txtBuildName)

    def inserir_nomeCamera(self, nome):
        self.type_in(self.txtCameraName, nome)

    def inserir_cameraAddress(self, address):
        self.type_in(self.txtCameraAddress, address)

    def inserir_cameraUser(self, user):
        self.type_in(self.txtCameraUser, user)

    def inserir_cameraPassword(self, password):
        self.type_in(self.txtCameraPassword, password)

    def clicar_criarCamera(self):
        self.driver.switch_to.active_element
        self.click(self.btnCreateCamera)
        time.sleep(10)