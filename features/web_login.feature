  Feature: Teste no site admin do urbfy
#
#
#    Scenario Outline: Efetuar Login com sucesso
#      Given Eu me preparo para acesso a página de login web pela primeira vez
#      Then Eu estou na página de login web
#      Then  Eu preencho o campo email com valor <email>
#      Then Eu preeencho o campo senha com valor <senha>
#      Then Eu clico em entrar
#      Given Eu me preparo para acesso a página home
#      Then Eu estou na página home
#
#      Examples: login
#        | email               | senha      |
#        | jao@email.com       | abacate    |
#
#    Scenario Outline: Efetuar Logoff com sucesso
#      Given Eu me preparo para acesso a página de login web pela primeira vez
#      Then Eu estou na página de login web
#      Then  Eu realizo login com email <email> e senha <senha>
#      Given Eu me preparo para acesso a página home
#      Then Eu estou na página home
#      Then Eu clico em sair
#      Given Eu me preparo para acesso a página de login web
#      Then Eu estou na página de login web
#      Examples: login
#        | email               | senha      |
#        | jao@email.com       | abacate    |

    Scenario Outline: Criar Camera com sucesso
      Given Eu me preparo para acesso a página de login web pela primeira vez
      Then Eu estou na página de login web
      Then  Eu realizo login com email <email> e senha <senha>
      Given Eu me preparo para acesso a página home
      Then Eu estou na página home
      Then Eu clico em cameras
      Given Eu me preparo para acesso a página de camera
      Then Eu estou na página de camera
      Then Eu inicio a criação de camera
      Given Eu me preparo para acesso a página de criar camera
      Then Eu estou na página de criar camera
      Then Eu crio uma camera com o nome do condominio <nCondominio>, nome da camera <nCamera>, endereco da camera <nCameraAddress>, login da camera <nCameraLogin>, e senha da camera <nCameraPassword>

      Examples: login
        | email               | senha      | nCondominio    | nCamera     | nCameraAddress                                                                     | nCameraLogin      | nCameraPassword   |
        | jao@email.com       | abacate    | Piedade        | Financeiro        | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=8&subtype=1    | urbfy             | urbfy             |
        | jao@email.com       | abacate    | Piedade        | Acesso lateral    | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=9&subtype=1    | urbfy             | urbfy             |
        | jao@email.com       | abacate    | Piedade        | Acesso Galpão     | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=13&subtype=1   | urbfy             | urbfy             |
        | jao@email.com       | abacate    | Piedade        | Fundos Galpão     | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=12&subtype=1   | urbfy             | urbfy             |