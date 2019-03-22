from behave import *
from features.pages.web_login_page import WebLoginPage

use_step_matcher("re")


@given("Eu me preparo para acesso a página de login web")
def step_impl(context):
    context.weblogin_page = WebLoginPage(context.driver)
    context.weblogin_page.validarPage()

@given("Eu me preparo para acesso a página de login web pela primeira vez")
def step_impl(context):
    context.weblogin_page = WebLoginPage(context.driver)
    context.weblogin_page.navegar_pagina(context.config.userdata['url'])
    context.weblogin_page.validarPage()

@step("Eu estou na página de login web")
def step_impl(context):
    context.weblogin_page.validarPage()

@step("Eu preencho o campo email com valor (?P<email>.+)")
def step_impl(context, email):
    context.weblogin_page.inserir_email(email)

@step("Eu preeencho o campo senha com valor (?P<senha>.+)")
def step_impl(context, senha):
    context.weblogin_page.inserir_password(senha)

@step("Eu clico em esqueci minha senha")
def step_impl(context, email):
    context.weblogin_page.clicar_forgot()

@step("Eu clico em entrar")
def step_impl(context):
    context.weblogin_page.clicar_entrar()

@step("Eu realizo login com email (?P<email>.+) e senha (?P<senha>.+)")
def step_impl(context, email, senha):
    context.weblogin_page.inserir_email(email)
    context.weblogin_page.inserir_password(senha)
    context.weblogin_page.clicar_entrar()

@step("Valido login fail")
def step_impl(context):
    context.weblogin_page.valida_loginError2()