""" 
Dia - 01
class ListaDeCompras:
    def __init__(self):
        self.produtos = []
        self.quantidades = []

    def adicionar_item(self,produto,quantidade):
        if quantidade <= 0:
            return print(f"Produto {produto} não pode ter estoque 0 ou negativo")
        self.produtos.append(produto)
        self.quantidades.append(quantidade)
    
    def remover_item(self,item):
        for produto in self.produtos:
            if produto == item:
                i = self.produtos.index(produto)
                self.produtos.pop(i)
                self.quantidades.pop(i)
                break
        else:
            return print(f"{item} não está na lista") 
               
    def listar_item(self):
        for item in range((len(self.produtos))):
            print(f'Nome - {self.produtos[item]} | Quantidade - {self.quantidades[item]}')
             
novaLista = ListaDeCompras() 
novaLista.adicionar_item("abacate",2)
novaLista.adicionar_item("banana",3)
novaLista.adicionar_item("laranja",5)
novaLista.adicionar_item("maçã",4)
novaLista.remover_item("maçã")
novaLista.adicionar_item("tomate",0)

novaLista.listar_item()
"""

"""
Dia - 02
#criando o nó
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#class paciente
class Paciente:
    def __init__(self,nome,identificacao,estado):
        self._nome = nome 
        self._identificacao = identificacao
        self._estado = estado

    def __str__(self):
        return f'Nome - {self._nome} | Idade - {self._identificacao} | Estado - {self._estado}'
   
#lista cadeada onde vão ficar os pacientes
class ListaDePacientes:
    def __init__(self):
        self.head = None
        self._size = 0
    #append percorrendo os nós
    def append(self,paciente):
        if self.head:
            #inserir quando a lista já possui elementos
            pointer = self.head 
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(paciente)
        else:
            #primeiro elemento
            self.head = Node(paciente)
        self._size = self._size +1
    #retorna o tamanho da Lista
    def __len__(self):
        return self._size
    
    def __getitem__(self,index):
        pointer = self.head 
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        raise IndexError("List index out of range")
    
    def index(self,paciente):
        #retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == paciente:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(paciente))
    
    def index_by_name(self,nome):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data._nome == nome:
                return f'indice - {i} '
            pointer = pointer.next
            i = i+1
        raise ValueError(f'{nome} não está na lista de Pacientes')

    def listar_pacientes(self):
        for paciente in self:
            print(paciente)

    def remover_paciente(self,nome):
        #primeiro head
        if self.head and self.head.data._nome == nome:
            self.head = self.head.next
            self._size -= 1
            return
        pointer = self.head
        while pointer and pointer.next:
            if pointer.next.data._nome == nome:
                pointer.next = pointer.next.next
                self._size -= 1
                return
            pointer = pointer.next
        raise ValueError(f'{nome} não está na lista de pacientes')
    
paciente1 = Paciente('Roberto',56,'doente')
paciente2 = Paciente('Erasmo',52,'maisomenos')
paciente3 = Paciente('Supla',52,'Papito')

lista = ListaDePacientes()
lista.append(paciente1)
lista.append(paciente2)
lista.append(paciente3)
print(len(lista))
lista.listar_pacientes()
print(lista.index_by_name('Erasmo'))
lista.remover_paciente('Supla')
lista.listar_pacientes()

"""











    