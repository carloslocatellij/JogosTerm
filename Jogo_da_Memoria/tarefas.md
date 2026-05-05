### Tarefas a fazer no Jogo da Memoria:

- [x] 1) Fazer todas as verificações necessárias para confirmar que a entrada do jogador é válida.
 - [x] verifcar se o jogador não fez escolha repetida.
 - [x] Se a entrada não tem nem mais nem menos do que 2 caracteres.
 - [x] Se o primeiro caracter é uma letra valida
 - [x] Se o segundo caracter é um digito
 - [x]  2) Permitir que o jogador escolha sair.
- [X] 3) Verificar ao final de cada escolha se o jogador, na jogada presente, venceu o jogo. 
- [ ] identificar o jogador.
- [ ] tornar o jogo rankeável.
- [ ] interface gráfica (click).


## Próxima Etapa
### Nos vamos integrar ao jogo um sistema de pontuação:

 * Cada par formado valem 5 pontos, se não formou par perde 1 ponto (sem ficar negativo)
 * O sistema de pontos tem seus dados salvos em arquivo (savepoint.csv).
 * O sistema de pontos é um modulo a ser importado em nosso jogo.
   - Assim o código do jogo fica isolado do código do "save"
 * A cada vez que é executado, o jogo pede o nome do jogador.
 EU SÓ ACHO QUE: CADA JOGADOR DEVERIA ESTAR ATRELADO A UM CÓDIGO.
 E QUE OS NOMES NÃO PODEM SE REPETIR 
   - Após, vai imprimir o nome e a pontuação do jogador 1º do ranking. 

- 4) 
- [ ] permitir que o jogo tenha dois players vs.