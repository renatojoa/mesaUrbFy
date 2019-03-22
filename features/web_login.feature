  Feature: Teste no site admin do urbfy

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
  #  Scenario Outline: Efetuar Logoff com sucesso
  #    Given Eu me preparo para acesso a página de login web pela primeira vez
  #    Then Eu estou na página de login web
  #    Then  Eu realizo login com email <email> e senha <senha>
  #    Given Eu me preparo para acesso a página home
  #    Then Eu estou na página home
  #    Then Eu clico em sair
  #    Given Eu me preparo para acesso a página de login web
  #    Then Eu estou na página de login web
  #    Examples: login
  #      | email               | senha      |
  #      | jao@email.com       | abacate    |

# @runDebug
#    Scenario Outline: Criar Camera com sucesso
#      Given Eu me preparo para acesso a página de login web pela primeira vez
#      Then Eu estou na página de login web
#      Then  Eu realizo login com email <email> e senha <senha>
#      Given Eu me preparo para acesso a página home
#      Then Eu estou na página home
#      Then Eu clico em cameras
#      Given Eu me preparo para acesso a página de camera
#      Then Eu estou na página de camera
#      Then Eu inicio a criação de camera
#      Given Eu me preparo para acesso a página de criar camera
#      Then Eu estou na página de criar camera
#      Then Eu crio uma camera com o nome do condominio <nCondominio>, nome da camera <nCamera>, endereco da camera <nCameraAddress>, login da camera <nCameraLogin>, e senha da camera <nCameraPassword>
#      Then Eu inicio uma busca pela camera cadastrada: <nCamera>
#      Then Eu valido a inclusão da camera cadastrada: <nCamera>
#      Examples: login
#        | email               | senha      | nCondominio    | nCamera       | nCameraAddress                                                                     | nCameraLogin      | nCameraPassword   |
#        | renatojoa@gmail.com | oipopo     | Piedade        | Teste 1       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=13&subtype=1   | urbfy             | urbfy             |
#        | renatojoa@gmail.com | oipopo     | Piedade        | Teste 2       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=12&subtype=1   | urbfy             | urbfy             |
#        | renatojoa@gmail.com | oipopo     | Piedade        | Teste 3       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=11&subtype=1   | urbfy             | urbfy             |
#        | renatojoa@gmail.com | oipopo     | Piedade        | Teste 4       | rtsp://cameras.nuvemverifybrasil.com.br:554/cam/realmonitor?channel=10&subtype=1   | urbfy             | urbfy             |

  @runDebug
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
       #| jao@email.com      | oipopo     |
    # @runDebug
    # Scenario Outline: Criar Condominio com sucesso
    #   Given Eu me preparo para acesso a página de login web pela primeira vez
    #   Then Eu estou na página de login web
    #   Then  Eu realizo login com email <email> e senha <senha>
    #   Given Eu me preparo para acesso a página home
    #   Then Eu estou na página home
    #   Then Eu clico em condominios
    #   Given Eu me preparo para acesso a página de condominio
    #   Then Eu estou na página de condominio
    #   Then Eu inicio a criacao de Condominio
    #   Given Eu me preparo para acesso a página de criar condominio
    #   Then Eu estou na página de criar condominio
    #   Then Eu preencho o campo nome do novo condominio com valor <nCondominio>
    #   Then Eu seleciono o tipo de condominio com valor <tCondominio>
    #   Then Eu preencho o campo de endereco do novo condominio <nCondominioAddress>
    #   Then Eu seleciono o tipo de dias de gravação com valor <tDiasGravacao>
    #   Then Eu preeencho o caminho da imagem do condominio com o valor <nImagemCaminho>
    #   Then Eu clico no botão de criar condominio

    #   Examples: login
    #     | email               | senha      | nCondominio             | nCamera           | tCondominio              | nCondominioAddress  | tDiasGravacao   | nImagemCaminho                      |
    #     | renatojoa@gmail.com | oipopo     | Edf. Piedade Life       | Acesso Galpão     | Condomínio Residencial   | Rua Amabai, 246     | 7 dias          | C:\Users\Renato\Desktop\build.jpg   |