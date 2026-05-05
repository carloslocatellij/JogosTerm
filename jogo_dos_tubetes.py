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
        return None
        
    elif '  ' not in destino:
        print(f"Não cabe!")
        tela()
        return None
        
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
                        return None
                    else:
                        trocar(numori, numdest)
                        tela()
                        return None