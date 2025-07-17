""" Dia 01
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
""" Dia 02
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
""" Dia 03
Dia - 03
#criando o nó
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Produto():
    def __init__(self,id,nome,preco,quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def __str__(self):
        return f'Id - {self.id} | Nome - {self.nome} | Preco - {self.preco} | Quantidade - {self.quantidade}'

class ListaDeProdutos():
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0
    
    #retorna o tamanho da Lista
    def __len__(self):
        return self.size
    
    def listar_produtos(self):
        pointer = self.head 
        while(pointer):
            print(pointer.data)
            pointer = pointer.next

    def append(self,produto):
        novo_node = Node(produto)
        if self.head:
            #inserir quando a lista já possui elementos
            novo_node.prev = self.tail
            self.tail.next = novo_node
            self.tail = novo_node     
        else:
            #primeiro elemento
            self.head = novo_node
            self.tail = novo_node
        self.size = self.size +1
    
    def remover_produto(self,id):
        #primeiro head
        if self.head and self.head.data.id == id:
            self.head = self.head.next
            self.size -= 1
            return
        pointer = self.head
        while pointer and pointer.next:
            if pointer.next.data.id == id:
                pointer.next = pointer.next.next
                self.size -= 1
                return print(f'produto de id {id} removido')
            pointer = pointer.next
        raise ValueError(f'{id} não está na lista de produtos')
    
    def atualizar_produto(self,id,quantidade):
        pointer = self.head
        while pointer:
            if pointer.data.id == id:
                nome_produto = pointer.data.nome
                pointer.data.quantidade = quantidade 
                print(f' A quantidade de {nome_produto} foi alterada para {quantidade}')
                return 
            pointer = pointer.next
        raise ValueError (f'Produto com Id {id} não foi encontrado')

produto1 = Produto(1,'sabonete',56.5,3)
produto2 = Produto(2,'Botijão de gás',123,1)
produto3 = Produto(3,'detergente',3,1)
print(produto1)

lista = ListaDeProdutos()
lista.append(produto1)
lista.append(produto2)
lista.append(produto3)
print(f'tamanho da lista: {len(lista)}')
lista.listar_produtos()
lista.remover_produto(2)
lista.listar_produtos()
lista.atualizar_produto(1,10)
lista.listar_produtos()

"""

""" Dia 04
class Pedido():
    def __init__(self,id_pedido,nome,mesa,valor):
        self.id_pedido = id_pedido
        self.nome = nome
        self.mesa = mesa
        self.valor = valor
    def __str__(self):
        return f'Id - {self.id_pedido} | Nome - {self.nome} | Mesa - {self.mesa} | Valor - {self.valor}'
    
class FilaDePedidos():
    def __init__(self):
        self.pedidos = []
        
    def adicionar_pedido(self,pedido):
        self.pedidos.append(pedido)

    def remover_pedido(self):
        del self.pedidos[0]
    def listar_pedidos(self):
        for pedido in range(len(self.pedidos)):
            print(f'Pedido nº: {self.pedidos[pedido].id_pedido}| Nome: {self.pedidos[pedido].nome} | Mesa: {self.pedidos[pedido].mesa} | Valor: {self.pedidos[pedido].valor}')

fila = FilaDePedidos()
pedido1 = Pedido(1,'Xis Coração',3,45.6)
pedido2 = Pedido(2,'Xis Carne',4,32.5)
pedido3 = Pedido(3,'Bauru 4 Queijos',2,52.5)
fila.adicionar_pedido(pedido1)
fila.adicionar_pedido(pedido2)
fila.adicionar_pedido(pedido3)
fila.listar_pedidos()
fila.remover_pedido()
print('---------')
fila.listar_pedidos()
fila.remover_pedido()
print('-------')
fila.listar_pedidos()
"""
""" Dia 05
class Livro():
    def __init__(self,nome,paginas):
        self.nome = nome
        self.paginas = paginas
    def __str__(self):
        return f'Nome - {self.nome} | Nº Páginas: {self.paginas}'
    
class PilhaDeLivros():
    def __init__(self):
        self.pilha = []

    def adicionar_livro(self,livro):
        self.pilha.append(livro)
    def remover_livro(self):
        return print(f'{self.pilha.pop()} foi removido')
    def espia_livro(self):
        return print(f'Ultimo livro da lista: {self.pilha[-1]}')
    def lista_livros(self):
        print("-> Lista de livros da coleção <-")
        for livro in self.pilha:
            print(f'{livro}')

livro1 = Livro('Cronica de gelo',324)
livro2 = Livro('outro livro de gelo',523)
livro3 = Livro('aquele do game of thrones',333)
lista = PilhaDeLivros()
lista.adicionar_livro(livro1)
lista.adicionar_livro(livro2)
lista.adicionar_livro(livro3)
lista.lista_livros()
lista.remover_livro()
print(f'-----')
lista.lista_livros()
print(f'testando a espiada')
lista.espia_livro()
"""
""" Dia 06
class ListaJogadores:
    def __init__(self):
        self.jogadores = {}
    
    def __str__(self):
        return f'{self.jogadores}'
    
    def adiciona(self,nome,pontos):
        self.jogadores[nome] = pontos
    def atualizar_jogador(self,nome,pontos):
        self.jogadores[nome] = pontos
    def remover_jogador(self,nome):
        self.jogadores.pop(nome)
    def listar_jogadores(self):
        jogadores_ordenados = sorted(self.jogadores.items(),key=lambda x: int(x[1]),reverse=True)
        maior_pontuacao = 0
        jogador_vencedor = jogadores_ordenados[0][0]
        print("-------Tabela de pontos--------")
        for jogador,pontos in jogadores_ordenados:
            print(f'Jogador: {jogador} -> {pontos} pontos!')
        print(f'O vencedor é o: {jogador_vencedor}')

jogadores = ListaJogadores()
jogadores.adiciona("Erasmo","55")
jogadores.adiciona("Inigo Montoya","89")
jogadores.atualizar_jogador("Erasmo","69")
jogadores.adiciona("Biscoito","10")
jogadores.listar_jogadores()
jogadores.remover_jogador("Erasmo")
"""





