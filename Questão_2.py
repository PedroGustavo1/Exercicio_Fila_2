import random
import time

class Fila:
    def  __init__ (self):
        self.fila = []


    def enqueue (self):
      valor = (input("digite o seu nome para aguardar na fila de impressão: "))
      self.fila.append(valor)


    def dequeue (self):
        if not (self.isEmpty()):
            self.fila.pop(0)
            
             

    def isEmpty (self):
        return len(self.fila)== 0


    def Length (self):
        return len(self.fila)

    
    def Imprimir(self):
      quant = int(input("Quantos arquivos você deseja imprimir? : "))
      for i in range(1,quant+1):    
        print("Seu %d° Arquivo está sendo Impresso.."%(i))
        tempo = random.randint(1,10)
        time.sleep(tempo)
        print("Sua %d° Impressão Foi Finalizada!"%(i))
        print("Tempo: %d Segundos"%(tempo))
        self.fila.pop(0)
      print("Fila de Espera Atual:",self.fila)
     


f = Fila()

f.enqueue()
f.enqueue()
f.enqueue()
f.enqueue()

print(f.fila)

f.Imprimir()









import random
import time

class Fila:
    def  __init__ (self):
        self.fila = []


    def enqueue (self):
      valor = (input("digite o seu nome para aguardar na fila de impressão: "))
      self.fila.append(valor)


    def dequeue (self):
        if not (self.isEmpty()):
            self.fila.pop(0)
            
             

    def isEmpty (self):
        return len(self.fila)== 0


    def Length (self):
        return len(self.fila)

    
    def Imprimir(self):
      quant = int(input("Quantos arquivos você deseja imprimir? : "))
      for i in range(1,quant+1):    
        print("Seu %d° Arquivo está sendo Impresso.."%(i))
        tempo = random.randint(1,10)
        time.sleep(tempo)
        print("Sua %d° Impressão Foi Finalizada!"%(i))
        print("Tempo: %d Segundos"%(tempo))
        self.fila.pop(0)
      print("Fila de Espera Atual:",self.fila)
     


f = Fila()

f.enqueue()
f.enqueue()
f.enqueue()
f.enqueue()

print(f.fila)

f.Imprimir()









