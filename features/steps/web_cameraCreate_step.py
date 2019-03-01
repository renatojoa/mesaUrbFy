from behave import *
from features.pages.web_cameraCrate_page import WebCameraCreatePage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de criar camera")
def step_impl(context):
    context.webcameraCreate_page = WebCameraCreatePage(context.driver)

@step("Eu estou na página de criar camera")
def step_impl(context):
    context.webcameraCreate_page.validarPage()

@step("Eu preencho o campo nome do condominio com valor (?P<nCondominio>.+)")
def step_impl(context, nCondominio):
    context.webcameraCreate_page.inserir_nomeCondominio(nCondominio)


@step("Eu preeencho o campo nome da camera com valor (?P<nCamera>.+)")
def step_impl(context, nCamera):
    context.webcameraCreate_page.inserir_nomeCamera(nCamera)

@step("Eu preeencho o campo de endereco do condominio (?P<nCameraAddress>.+)")
def step_impl(context, nCameraAddress):
    context.webcameraCreate_page.inserir_cameraAddress(nCameraAddress)

@step("Eu preeencho o campo usuario de login da camera com valor (?P<nCameraLogin>.+)")
def step_impl(context, nCameraLogin):
    context.webcameraCreate_page.inserir_inserir_cameraUser(nCameraLogin)

@step("Eu preeencho o campo senha de login da camera com valor (?P<nCameraPassword>.+)")
def step_impl(context, nCameraPassword):
    context.webcameraCreate_page.inserir_cameraPassword(nCameraPassword)

@step("Eu clico no botão de criar camera")
def step_impl(context):
    context.webcameraCreate_page.clicar_criarCamera()

@step("Eu crio uma camera com o nome do condominio (?P<nCondominio>.+), nome da camera (?P<nCamera>.+), endereco da camera (?P<nCameraAddress>.+), login da camera (?P<nCameraLogin>.+), e senha da camera (?P<nCameraPassword>.+)")
def step_impl(context, nCondominio, nCamera, nCameraAddress, nCameraLogin, nCameraPassword):
    context.webcameraCreate_page.inserir_nomeCondominio(nCondominio)
    context.webcameraCreate_page.inserir_nomeCamera(nCamera)
    context.webcameraCreate_page.inserir_cameraAddress(nCameraAddress)
    context.webcameraCreate_page.inserir_cameraUser(nCameraLogin)
    context.webcameraCreate_page.inserir_cameraPassword(nCameraPassword)
    context.webcameraCreate_page.clicar_criarCamera()
