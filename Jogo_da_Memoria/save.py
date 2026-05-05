#Mecanismo de placar do jogo

pontos = []

conteudo = open('savepoint', 'r')

c = conteudo.readline()
cont = c.split(' ')

#['Pontos', '=', '1']

pontos = int(cont[0]) + 1
conteudo.close()


arq = open('savepoint', 'w')

arq.write(f'Pontos = {pontos}')

arq.close()



print(c)

