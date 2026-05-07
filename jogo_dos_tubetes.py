from random import shuffle as mix
import click

blue =    '💙'
yellow =  '💛'
green =   '💚'
vazio =   '  '

tub1 = [vazio, vazio, vazio, vazio]
tub2 = [blue, blue, yellow, green]
tub3 = [yellow, yellow, blue, green]
tub4 = [green, green, blue, yellow]

mix(tub2)
mix(tub3)
mix(tub4)

def tela():
    click.clear()
    print(f'''

    |{tub1[0]}|  |{tub2[0]}|  |{tub3[0]}|  |{tub4[0]}| 
    |{tub1[1]}|  |{tub2[1]}|  |{tub3[1]}|  |{tub4[1]}|
    |{tub1[2]}|  |{tub2[2]}|  |{tub3[2]}|  |{tub4[2]}|
    |{tub1[3]}|  |{tub2[3]}|  |{tub3[3]}|  |{tub4[3]}|
    \\_/   \\_/   \\_/   \\_/ ''')


def passar(origem, destino):
    
    def trocar( idO  ,  idD  ):
        origem[idO], destino[idD] = destino[idD], origem[idO]
            
    if '        ' == ''.join(origem):
        print(f"Não tem nada neste tubete!")
        tela()
        return 
        
    elif '  ' not in destino:
        print(f"Não cabe!")
        tela()
        return 
        
    else:
        for numdest, it in enumerate(destino):   
            if it == '  ' and numdest <= 2 and destino[numdest+1] == '  ':
                continue
            else:
                for numori, i in enumerate(origem):                    
                    if i == '  ':
                        continue
                    elif numdest <= 2 and destino[numdest+1] != i:
                        print(f"{destino[numdest+1]} e {origem[numori]} são diferentes. Precisam ser iguais!")
                        tela()
                        return 
                    else:
                        trocar(numori, numdest)
                        tela()
                        return 

if __name__ == '__main__':
    while True:
        tela()
        quest1 = quest2 = ''
        while not quest1.isdigit() and not quest2.isdigit():
            print('informe apenas números.')
            quest1 = input('informe o número da origem: ')
            if quest1.isdigit() and int(quest1) > 4:
                print('deve ser entre 1 e 4')
                break
            quest2 = input('informe o número do destino: ')
            if quest2.isdigit() and int(quest1) > 4:
                print('deve ser entre 1 e 4')
                break
                    
        passar(quest1, quest2)
        
        
