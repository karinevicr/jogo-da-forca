# Levantamento de Requisitos - Jogo de Forca Online

## 1. Requisitos Funcionais

&nbsp;&nbsp;&nbsp;&nbsp;Os requisitos funcionais definem as funcionalidades do sistema, estabelecendo as ações e comportamentos esperados para garantir que o sistema atenda às necessidades dos usuários.

### **RF01**: O sistema deve permitir que os jogadores joguem partidas de forca online, podendo ser multiplayer.
- **Critério de Aceitação**: O sistema deve permitir que no mínimo dois jogadores possam participar da mesma partida em tempo real.
- **Teste**: Criar uma partida e convidar um segundo jogador para a mesma. Verificar se ambos os jogadores conseguem participar da partida simultaneamente.
  - **Pré-condição**: A partida deve estar criada e os dois jogadores devem estar conectados ao sistema.
  - **Procedimento do teste**: Iniciar a partida com dois jogadores e realizar jogadas simultâneas.
  - **Resultado esperado**: Ambos os jogadores podem realizar suas jogadas e o jogo avança conforme as regras.
  - **Pós-condição**: O jogo permite a interação entre múltiplos jogadores.

### **RF02**: O sistema deve permitir a criação de novas partidas com diferentes níveis de dificuldade.
- **Critério de Aceitação**: O sistema deve oferecer pelo menos três níveis de dificuldade: fácil, médio e difícil.
- **Teste**: Criar partidas em diferentes níveis de dificuldade e verificar se o jogo ajusta a complexidade das palavras de acordo com o nível selecionado.
  - **Pré-condição**: O sistema deve ter palavras de diferentes níveis de dificuldade cadastradas.
  - **Procedimento do teste**: Criar uma partida em cada nível de dificuldade e verificar a dificuldade das palavras sorteadas.
  - **Resultado esperado**: As palavras sorteadas devem corresponder ao nível de dificuldade selecionado.
  - **Pós-condição**: O sistema deve permitir a seleção e criação de partidas com diferentes níveis de dificuldade.

### **RF03**: O sistema deve permitir que o jogador escolha entre jogar contra a máquina ou contra outro jogador online.
- **Critério de Aceitação**: O sistema deve oferecer uma opção para escolher entre "jogar contra a máquina" ou "jogar contra outro jogador".
- **Teste**: Selecionar a opção de jogar contra a máquina e verificar se o jogo é iniciado contra um bot. Selecionar a opção de jogar contra outro jogador e verificar se a partida é criada com outro jogador real.
  - **Pré-condição**: O sistema deve estar configurado para oferecer as duas opções de modo de jogo.
  - **Procedimento do teste**: Escolher cada opção e verificar o tipo de adversário.
  - **Resultado esperado**: O sistema deve iniciar o jogo contra a máquina ou contra outro jogador conforme a opção selecionada.
  - **Pós-condição**: O sistema deve permitir escolher entre adversários humanos ou a máquina.

## 2. Requisitos Não Funcionais

&nbsp;&nbsp;&nbsp;&nbsp;Os requisitos não funcionais descrevem as características de qualidade e desempenho do sistema, assegurando que ele atenda a critérios como tempo de resposta, usabilidade, segurança e conformidade com regulamentações. A ISO/IEC 25010 fornece uma base para a avaliação da qualidade do software, estabelecendo oito características essenciais: funcionalidade, desempenho, usabilidade, confiabilidade, segurança, compatibilidade, manutenibilidade e portabilidade, as quais devem ser atendidas para garantir que o sistema seja eficiente, seguro e adequado às necessidades do usuário, para mais informação acesse esse [link](https://blog.onedaytesting.com.br/iso-iec-25010/).


### **RNF01**: O sistema deve carregar a página inicial em menos de 2 segundos.
- **ISO/IEC 25010 - Desempenho**: O sistema deve fornecer um tempo de resposta eficiente, garantindo que o carregamento da página esteja dentro de parâmetros aceitáveis.
- **Critério de Aceitação**: A página inicial deve ser carregada em até 2 segundos.
- **Teste**: Medir o tempo de carregamento da página inicial utilizando ferramentas como o cronômetro.
  - **Pré-condição**: O servidor deve estar operacional e a página inicial deve estar completamente implementada.
  - **Procedimento do teste**: Acessar a página inicial e cronometrar o tempo de carregamento.
  - **Resultado esperado**: A página deve ser carregada em menos de 2 segundos.
  - **Pós-condição**: O tempo de carregamento da página está dentro dos limites especificados.

### **RNF02**: O sistema deve ser responsivo e funcionar bem em dispositivos móveis.
- **ISO/IEC 25010 - Usabilidade**: O sistema deve ser facilmente utilizável em diferentes plataformas, com uma interface que se adapte a dispositivos móveis.
- **Critério de Aceitação**: O layout da página inicial e das partidas deve ser adequado a diferentes tamanhos de tela.
- **Teste**: Acessar o jogo em dispositivos móveis com diferentes tamanhos de tela (smartphones e tablets) e verificar se o layout se adapta corretamente.
  - **Pré-condição**: O sistema deve ser acessível através de um dispositivo móvel.
  - **Procedimento do teste**: Acessar a página e jogar uma partida em dispositivos móveis de diferentes tamanhos.
  - **Resultado esperado**: O sistema deve se ajustar adequadamente a diferentes tamanhos de tela, sem perder funcionalidade ou legibilidade.
  - **Pós-condição**: O sistema é responsivo e acessível em dispositivos móveis.

### **RNF03**: O sistema deve garantir que os dados sejam armazenados e tratados de acordo com a Lei Geral de Proteção de Dados (LGPD).
- **ISO/IEC 25010 - Segurança**: O sistema deve proteger os dados contra acessos não autorizados, garantindo sua integridade e confidencialidade.
- **Critério de Aceitação**: O sistema deve implementar medidas de proteção de dados, como criptografia e anonimização quando aplicável.
- **Teste**: Verificar se os dados pessoais dos jogadores estão sendo criptografados ao serem armazenados e acessados, além de verificar se há uma política de consentimento explícito para coleta de dados.
  - **Pré-condição**: O sistema deve estar implementado com um banco de dados configurado para armazenar dados pessoais.
  - **Procedimento do teste**: Realizar testes de acesso e armazenamento dos dados, verificando se estão criptografados e se o consentimento foi obtido antes de coletar qualquer dado.
  - **Resultado esperado**: Os dados devem ser criptografados e acessíveis apenas por usuários autorizados, com o consentimento do jogador para a coleta.
  - **Pós-condição**: O sistema está em conformidade com a LGPD.

### **RNF04**: O sistema deve oferecer uma experiência de aprendizado gradual, permitindo que o jogador aprenda as regras e jogabilidade conforme for jogando.

- **ISO/IEC 25010 - Usabilidade**: O sistema deve ser fácil de aprender e utilizar, oferecendo um aprendizado progressivo e contínuo ao jogador.
- **Critério de Aceitação**: O sistema deve fornecer dicas e orientações durante o jogo, principalmente para novos jogadores, explicando as regras de forma simples e intuitiva.
- **Teste**: Testar o jogo com um jogador novo e verificar se o sistema oferece dicas contextuais que o ajudem a entender as regras durante a partida. O sistema deve permitir que o jogador saiba, sem a necessidade de sair do jogo, como jogar e o que fazer em cada etapa do jogo.
  - **Pré-condição**: O sistema deve estar configurado para detectar quando o jogador está jogando pela primeira vez.
  - **Procedimento do teste**: Iniciar uma partida com um jogador iniciante e verificar se o sistema oferece:
    1. Dicas sobre como jogar, por exemplo, explicando o objetivo do jogo, como escolher letras, e como o progresso do jogo é mostrado.
    2. Orientações durante a partida, como sugestões quando o jogador estiver em dúvida.
    3. Feedback imediato sobre o que foi correto ou incorreto.
  - **Resultado esperado**: O jogador deve receber dicas e orientações ao longo do jogo, de forma que ele entenda o que está acontecendo e aprenda as regras sem sair do jogo.
  - **Pós-condição**: O jogador, mesmo sendo iniciante, consegue jogar e entender as regras conforme vai avançando na partida.