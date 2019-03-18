from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time, os



class WebCondominioCreatePage(BasePage):
    lblTitle = (By.ID, "page-header-title")
    txtBuildName = (By.ID, "building-name")
    selectBuildType = (By.ID, 'building-type')
    txtBuildAddress = (By.ID, 'building-address')
    selectDaysRecord = (By.ID, 'building-retention-period')
    txtImagePath = (By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div[2]')
    btnCreateBuild = (By.ID, 'create-building-button')

    def validarPage(self):
        time.sleep(6)
        #assert self.find(self.lblTitle).text == "Criar Condominio"

    def inserir_nomeCondominio(self, nome):
        self.type_in(self.txtBuildName, nome)

    def seleciona_tipoCondominio(self, tipo):
        self.select_in_combo_by_xpath(self.selectBuildType, tipo)

    def inserir_condominioAddress(self, address):
        self.type_in(self.txtBuildAddress, address)

    def seleciona_diasGravacao(self, dias):
        self.select_in_combo_by_xpath(self.selectDaysRecord, dias)

    def inserir_caminhoImagem(self, caminho):
        time.sleep(20)

    def clicar_criarCondominio(self):
        self.click(self.btnCreateBuild)
        time.sleep(10)