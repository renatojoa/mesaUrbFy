@runCondominio
  Feature: Teste na funcionalidade de condominio
    @runCriarCondominio
    Scenario Outline: Criar Condominio com sucesso
      Given Eu me preparo para acesso a página de login web pela primeira vez
      Then Eu estou na página de login web
      Then  Eu realizo login com email <email> e senha <senha>
      Given Eu me preparo para acesso a página home
      Then Eu estou na página home
      Then Eu clico em condominios
      Given Eu me preparo para acesso a página de condominio
      Then Eu estou na página de condominio
      Then Eu inicio a criacao de Condominio
      Given Eu me preparo para acesso a página de criar condominio
      Then Eu estou na página de criar condominio
      Then Eu preencho o campo nome do novo condominio com valor <nCondominio>
      Then Eu seleciono o tipo de condominio com valor <tCondominio>
      Then Eu preencho o campo de endereco do novo condominio <nCondominioAddress>
      Then Eu seleciono o tipo de dias de gravação com valor <tDiasGravacao>
      Then Eu preeencho o caminho da imagem do condominio com o valor <nImagemCaminho>
      Then Eu clico no botão de criar condominio

      Examples: login
        | email               | senha      | nCondominio             | nCamera           | tCondominio              | nCondominioAddress  | tDiasGravacao   | nImagemCaminho                      |
        | renatojoa@gmail.com | oipopo     | Edf. Piedade Life       | Acesso Galpão     | Condomínio Residencial   | Rua Amabai, 246     | 7 dias          | C:\Users\Renato\Desktop\build.jpg   |