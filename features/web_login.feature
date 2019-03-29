  @runLogin
  Feature: Teste na funcionalidade de login
    @runLoginDone
    Scenario Outline: Efetuar Login com sucesso
      Given Eu me preparo para acesso a página de login web pela primeira vez
      Then Eu estou na página de login web
      Then  Eu preencho o campo email com valor <email>
      Then Eu preeencho o campo senha com valor <senha>
      Then Eu clico em entrar
      Given Eu me preparo para acesso a página home
      Then Eu estou na página home

      Examples: login
        | email               | senha      |
        | jao@email.com       | abacate    |

    @runLoginFail
    Scenario Outline: Valida login e usuario fail
      Given Eu me preparo para acesso a página de login web pela primeira vez
      Then Eu estou na página de login web
      Then  Eu preencho o campo email com valor <email>
      Then Eu preeencho o campo senha com valor <senha>
      Then Eu clico em entrar
      Then Valido login fail

      Examples: login
        | email               | senha      |
        | renatojoa@email.com | abacate    |
        | jao@email.com       | oipopo     |