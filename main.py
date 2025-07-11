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
    