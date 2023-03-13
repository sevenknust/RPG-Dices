# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado4:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 4

class SimuladorDeDado6:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        
class SimuladorDeDado8:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 8         
        
class SimuladorDeDado10:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 10         
        
class SimuladorDeDado12:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 12         
        
class SimuladorDeDado20:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 20
              
class Play:    
    def Iniciar(self):
        # Layout
        self.layout = [
            [sg.Text('tem dado em casa?')],
            [sg.Button('d4'),sg.Button('d6'),sg.Button('d8'),sg.Button('d10'),sg.Button('d12'),sg.Button('d20')]
        ]     
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'd4':
                self.GerarValorDoDado(SimuladorDeDado4())
            if self.eventos == 'd6':
                self.GerarValorDoDado(SimuladorDeDado6())
            if self.eventos == 'd8':
                self.GerarValorDoDado(SimuladorDeDado8())            
            if self.eventos == 'd10':
                self.GerarValorDoDado(SimuladorDeDado10())            
            if self.eventos == 'd12':
                self.GerarValorDoDado(SimuladorDeDado12())            
            if self.eventos == 'd20':
                self.GerarValorDoDado(SimuladorDeDado20())
            
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agrecemos a sua participação!')
        except:
            print('Ocorreu um erro ao receber sua resposta')
    
    def GerarValorDoDado(self, dado):
        print(random.randint(dado.valor_minimo, dado.valor_maximo))

play = Play()
play.Iniciar()