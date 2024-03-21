# Don't Touch Me

> "Don't Touch Me" é um jogo "one hit kill" (onde o jogador morre caso seja tocado por um inimigo) que tem como objetivo coletar o maior número de moedas sem ser tocado pelos obstáculos. A diversão do jogo reside na dificuldade de desviar dos obstáculos enquanto se coleta as moedas espalhadas pela tela. Além disso, cada moeda possui efeitos únicos que podem ajudar ou prejudicar o jogador, sendo eles:
> - Moeda Amarela: Aumenta a velocidade que o jogador se movimenta.
> - Moeda Azul: Diminui o tamanho do jogador
> - Moeda Roxa: Aumenta o tamanho do jogador


## Membros:

- Leonardo Cabral (lfc5)
- Bruno Gabriel (bgprs)
- Bruno Henrique (bhfp)
- Thiago Felipe (tffs)

## Divisão de trabalho:

| Grupo | Contribuição       |
|----------------|--------------------|
| Leonardo Cabral           | Responsavel pela organização geral do main.py e Readme  |
| Bruno Henrique           | Responsavel pela criação e movimentação dos obstáculos    |
| Bruno Gabriel           | Responsavel pelas configurações de jogabilidade do player    |
| Thiago Felipe           | Responsavel pela coleta e contabilidade dos coletáveis    |


## Estruturação do código:
  ###  Pasta do projeto:
  > Pasta geral do projeto, todos os arquivos e pastas utilizados estão localizadas nessa pasta.
  
  ### Assets:
  > Pasta com os arquivos de áudio do jogo. Nela está presente o som ao pegar as moedas e a música de fundo do jogo.

  ### Main.py:
  > Este é o arquivo principal onde o jogo será executado. Nele, ocorre o loop do jogo, durante o qual os eventos possíveis ocorrerão enquanto o jogador estiver jogando. Alem disso, importamos as blibiotecas "Pygame" e "random" para ajudar com algumas funções, e as classes "Player" e "Obst" dos nossos outros arquivos.

  ### jogador.py:
  > Nesse arquivo, temos a Classe do player, onde definimos onde ele irá surgir na tela e toda a sua movimentação dentro do jogo. A biblioteca pygame foi utilizada nesse arquivo para conseguirmos realizar a movimentação do personagem da forma que desejamos.

  ### obstaculos.py:
  > Nesse arquivo, criamos a Classe Obst, que é responsável pela criação dos obstáculos e do seu padrão de movimentação. Para fazer isso utilizamos a blibioteca "random" e a função "randint" para gerar as posições inicias dos obstáculos aleatoriamente. 

  ### Readme.md:
  > Arquivo onde foi feito o relatório do projeto Don't Touch Me.

## Conceitos utilizados que foram apresentados na diciplina:

Diversos conceitos que foram ensinados na diciplina foram usados durante a criação deste jogo. Entre eles estão:
- Condicionais: Utilizamos o "if" em diversas partes do nosso código, como na contagem das moedas, diferenciando entre as cores azul, vermelha ou roxa, na finalização do jogo, na movimentação do jogador, na movimentação dos obstáculos e em diversas outras partes do código.
- Laço de repetição: O jogo é rodado em um laço de repetição em que o "while" é utilizado para fazer o loop.
- Função: As funções são utilizadas em diversas partes como na criação dos obstáculos e sua movimentação, na criação do player e sua movimentação, nos coletáveis e é tambem utilizado no main.
- Programação orientada a objeto: Utilizamos classes em grande parte do nosso projeto. A criação de objetos foi fundamental para uma melhor organização e definição dos atributos. Adotamos a Programação Orientada a Objetos (POO) para modelar os obstáculos, o jogador (Player) e os itens coletáveis.


## Bibliotecas utilizada:
- Pygame: A biblioteca "Pygame" foi a mais utilizada em nosso projeto, sendo responsável por facilitar a realização do jogo e ter varias funções uteis ao nosso alcance. Ela ajudou na utilização de sons, na inserção de textos na tela do jogo, na definição do clock do jogo, na criação dos objetos e na colisão entre eles.
- Random: A biblioteca "Random" foi utilizada para usarmos a função "Randint" em diversar partes do nosso projeto. Essa função foi importante para gerar aleatoriamente os coletaveis na tela e na criação dos obstaculos.


## Desafios encontrados/Lições aprendidas:

- Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
  > Nosso maior erro foi começar com um projeto muito ambicioso sem termos noção do trabalho envolvido, o que nos levou a ter que revisar completamente a ideia do jogo devido a restrições de tempo. Como resultado, acabamos desenvolvendo um jogo muito mais simples do que inicialmente planejado.

- Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
  > Tivemos 2 grandes desafios, o primeiro sendo o aprendizado de Git e Github, e o segundo o aprendizado do Pygame e de Programação Orientada a Objetos (POO). Enfrentamos muitas dificuldades, pois nunca tinhamos usados estas ferramentas antes e não estávamos habituados com suas funcionalidades. Para lidar com isso, tivemos que dedicar tempo para estudarmos essas ferramentas antes de começar o projeto. Em seguida, aprendemos na prática como utilizar suas funcionalidades durante o desenvolvimento do nosso jogo.
 
- Quais as lições aprendidas durante o projeto?
  > As lições aprendidas durante o projeto foram que a organização é fundamental para o andamento, ter um código fácil de ser lido e uma comunicação entre os membros da equipe é importantíssimo para o progresso do projeto como um todo. De nada adianta ter ideias ambiciosas sem um gerenciamento decente do tempo e das tarefas a serem realizadas.

## Imagens do jogo:

![Imagem1](https://github.com/obrunohenrique/don-t-touch-me/assets/162651240/7d1a1628-220a-4e42-8354-2fcc6bf091c4)

![Imagem2](https://github.com/obrunohenrique/don-t-touch-me/assets/162651240/90023ab3-5178-423c-8058-5d120dfcc260)

![Imagem3](https://github.com/obrunohenrique/don-t-touch-me/assets/162651240/1916c98b-1db4-467e-b88e-7844096b16f8)

## Instruções de uso:
### Requisitos para rodar o jogo:
- [Python](https://www.python.org/downloads/)

### Como rodar na minha máquina?
- ```git clone https://github.com/obrunohenrique/don-t-touch-me.git```
- Instalar pygame: ```pip install pygame```
- Rodar Main.py

