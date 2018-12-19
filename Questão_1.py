#CLASSE FILA =====================================

class Fila:
    def  __init__ (self):
        self.fila = []


    def enqueue (self):
      valor = int(input("Digite o valor a ser adcionado na Fila:"))
      self.fila.append(valor)


    def dequeue (self):
        if not (self.isEmpty()):
            self.fila.pop(0)
            
             

    def isEmpty (self):
        return len(self.fila)== 0


    def Length (self):
        return len(self.fila)

#===============================================


#CLASSE PILHA==================================

class Pilha():
#===================Construtor======================

  def __init__(self):
    self.pilha = []

#=======Adciona Um Elemento ao Topo da Pilha========

  def Push(self,elemento):
    self.pilha.append(elemento)


#=======Retira Um Elemento do Topo da Pilha=========
  
  def Pop(self):
    if (len(self.pilha)==0):
      print("Não Há Elementos na Sua Pilha!")
    else:  
      self.pilha.pop()


#==========Verifica se a Pilha está Vazia============
  
  def IsEmpty(self):
    if len(self.pilha) == 0:
      print("Sua Pilha Esta Vazia")
    else:
      print("Sua Pilha Contem Elementos")

#===========Verifica o Topo da Pilha=================
  
  def Peek(self):
    topo = self.pilha[-1]
    print("O Topo da Pilha é o",topo)

  #========Verifica o Tamanho da Pilha===============  
  def Length(self):
    tamanho = (len(self.pilha))
    if tamanho >1:
      print("Sua Pilha Contem %d Elementos"%(tamanho))
    elif tamanho ==1:
      print("Sua Pilha Contem 1 Elemento!")
    else:
      print("Sua Pilha Não Contem Nenhum Elemento!")


fila = Fila()

fila.enqueue()
fila.enqueue()
fila.enqueue()
fila.enqueue()
fila.enqueue()

print("Sua Fila:",fila.fila)

lista_auxiliar = Pilha()

aux_2 = 0

for i in range (len(fila.fila)-1):
  aux_2 = fila.fila[0]
  fila.dequeue()
  lista_auxiliar.Push(aux_2)

print(lista_auxiliar.pilha)
print(fila.fila)

lista_final = []

aux_3 = 0

lista_final.append(fila.fila[0])

for i in range(len(lista_auxiliar.pilha)):
  
  aux_3 = lista_auxiliar.pilha[-1]

  lista_final.append(aux_3)

  lista_auxiliar.Pop()


print("Lista Final:",lista_final)
