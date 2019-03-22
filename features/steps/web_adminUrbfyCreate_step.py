from behave import *
from features.pages.web_adminUrbfyCrate_page import WebAdminUrbfyCreatePage

use_step_matcher("re")

@given("Eu me preparo para acesso a página de criar adminstrador urbfy")
def step_impl(context):
    context.web_adminUrbfyCrate_page = WebAdminUrbfyCreatePage(context.driver)

@step("Eu estou na página de criar adminstrador urbfy")
def step_impl(context):
    context.web_adminUrbfyCrate_page.validarPage()

@step("Eu preencho o campo nome do adminstrador: (?P<nAdministrador>.+)")
def step_impl(context, nAdministrador):
    context.web_adminUrbfyCrate_page.inserir_nomeAdmin(nAdministrador)

@step("Eu preencho o campo de email do administrador: (?P<eAdminstrador>.+)")
def step_impl(context, eAdminstrador):
    context.web_adminUrbfyCrate_page.inserir_emailAdmin(eAdminstrador)

@step("Eu clico no botão de criar administrador urbfy")
def step_impl(context):
    context.web_adminUrbfyCrate_page.clicar_criarAdminUrbfy()