from behave import *
from features.pages.web_condominioCrate_page import WebCondominioCreatePage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de criar condominio")
def step_impl(context):
    context.webcondominioCreate_page = WebCondominioCreatePage(context.driver)

@step("Eu estou na página de criar condominio")
def step_impl(context):
    context.webcondominioCreate_page.validarPage()

@step("Eu preencho o campo nome do novo condominio com valor (?P<nCondominio>.+)")
def step_impl(context, nCondominio):
    context.webcondominioCreate_page.inserir_nomeCondominio(nCondominio)

@step("Eu seleciono o tipo de condominio com valor (?P<tCondominio>.+)")
def step_impl(context, tCondominio):
    context.webcondominioCreate_page.seleciona_tipoCondominio(tCondominio)

@step("Eu preencho o campo de endereco do novo condominio (?P<nCondominioAddress>.+)")
def step_impl(context, nCondominioAddress):
    context.webcondominioCreate_page.inserir_condominioAddress(nCondominioAddress)

@step("Eu seleciono o tipo de dias de gravação com valor (?P<tDiasGravacao>.+)")
def step_impl(context, tDiasGravacao):
    context.webcondominioCreate_page.seleciona_diasGravacao(tDiasGravacao)

@step("Eu preeencho o caminho da imagem do condominio com o valor (?P<nImagemCaminho>.+)")
def step_impl(context, nImagemCaminho):
    context.webcondominioCreate_page.inserir_caminhoImagem(nImagemCaminho)

@step("Eu clico no botão de criar condominio")
def step_impl(context):
    context.webcondominioCreate_page.clicar_criarCondominio()

# @step("Eu crio uma condominio com o nome do condominio (?P<nCondominio>.+), nome da condominio (?P<nCondominio>.+), endereco da condominio (?P<nCondominioAddress>.+), login da condominio (?P<nCondominioLogin>.+), e senha da condominio (?P<nCondominioPassword>.+)")
# def step_impl(context, nCondominio, nCondominio, nCondominioAddress, nCondominioLogin, nCondominioPassword):
#     context.webcondominioCreate_page.inserir_nomeCondominio(nCondominio)
#     context.webcondominioCreate_page.inserir_nomeCondominio(nCondominio)
#     context.webcondominioCreate_page.inserir_condominioAddress(nCondominioAddress)
#     context.webcondominioCreate_page.inserir_condominioUser(nCondominioLogin)
#     context.webcondominioCreate_page.inserir_condominioPassword(nCondominioPassword)
#     context.webcondominioCreate_page.clicar_criarCondominio()
