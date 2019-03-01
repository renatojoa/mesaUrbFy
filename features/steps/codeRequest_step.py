import time

from behave import *
from features.pages.codeRequest_page import CodeRequestPage

use_step_matcher("re")


@given("Eu estou na página de CodeRequest")
def step_impl(context):
    context.login_page = CodeRequestPage(context.driver)
    context.login_page.valida_page()