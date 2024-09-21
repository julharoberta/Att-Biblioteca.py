class Livro:
    def __init__(self, titulo, autor, isbn, preco, quantidade_em_estoque):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def adicionar_ao_estoque(self, quantidade):
        self.quantidade_em_estoque += quantidade
        print(f"{quantidade} unidades adicionadas. Novo estoque: {self.quantidade_em_estoque}")

    def remover_do_estoque(self, quantidade):
        if quantidade <= self.quantidade_em_estoque:
            self.quantidade_em_estoque -= quantidade
            print(f"{quantidade} unidades removidas. Estoque restante: {self.quantidade_em_estoque}")
        else:
            print("Estoque insuficiente para remover a quantidade solicitada.")

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Preço: R${self.preco:.2f}, Estoque: {self.quantidade_em_estoque} unidades")


class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.historico_compras = []

    def registrar_compra(self, livro, quantidade):
        if quantidade <= livro.quantidade_em_estoque:
            livro.remover_do_estoque(quantidade)
            self.historico_compras.append((livro, quantidade))
            print(f"Compra registrada: {quantidade} unidades de '{livro.titulo}' por R${livro.preco:.2f} cada.")
        else:
            print(f"Estoque insuficiente para '{livro.titulo}'.")

    def visualizar_historico(self):
        print(f"\nHistórico de Compras de {self.nome}:")
        for livro, quantidade in self.historico_compras:
            print(f"{quantidade} unidades de '{livro.titulo}' (ISBN: {livro.isbn})")


class Livraria:
    def __init__(self):
        self.estoque = []
        self.clientes = []

    def adicionar_livro(self, titulo, autor, isbn, preco, quantidade_em_estoque):
        livro = Livro(titulo, autor, isbn, preco, quantidade_em_estoque)
        self.estoque.append(livro)
        print(f"Livro '{titulo}' adicionado ao estoque.")

    def listar_livros(self):
        if not self.estoque:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.estoque:
            livro.exibir_informacoes()

    def buscar_livro(self, termo):
        for livro in self.estoque:
            if livro.titulo.lower() == termo.lower() or livro.isbn == termo:
                livro.exibir_informacoes()
                return
        print("Livro não encontrado.")

    def atualizar_estoque(self, isbn, quantidade, adicionar=True):
        for livro in self.estoque:
            if livro.isbn == isbn:
                if adicionar:
                    livro.adicionar_ao_estoque(quantidade)
                else:
                    livro.remover_do_estoque(quantidade)
                return
        print("Livro não encontrado.")

    def remover_livro(self, isbn):
        for livro in self.estoque:
            if livro.isbn == isbn:
                self.estoque.remove(livro)
                print(f"Livro '{livro.titulo}' removido do estoque.")
                return
        print("Livro não encontrado.")

    def registrar_cliente(self, nome, email):
        cliente = Cliente(nome, email)
        self.clientes.append(cliente)
        print(f"Cliente '{nome}' registrado.")

    def realizar_compra(self, email, isbn, quantidade):
        for cliente in self.clientes:
            if cliente.email == email:
                for livro in self.estoque:
                    if livro.isbn == isbn:
                        cliente.registrar_compra(livro, quantidade)
                        return
        print("Cliente ou livro não encontrado.")


# Exemplo de uso
if __name__ == "__main__":
    livraria = Livraria()

    # Adicionando livros
    livraria.adicionar_livro("Python para Iniciantes", "João Silva", "978-3-16-148410-0", 59.90, 10)
    livraria.adicionar_livro("Aprendendo MySQL", "Maria Souza", "978-1-23-456789-7", 79.90, 5)

    # Listando livros
    print("\nLista de Livros:")
    livraria.listar_livros()

    # Registrando clientes
    livraria.registrar_cliente("Carlos Mendes", "carlos@example.com")
    livraria.registrar_cliente("Ana Oliveira", "ana@example.com")

    # Realizando compras
    print("\nRealizando compras:")
    livraria.realizar_compra("carlos@example.com", "978-3-16-148410-0", 2)
    livraria.realizar_compra("ana@example.com", "978-1-23-456789-7", 1)

    # Visualizando histórico de compras
    for cliente in livraria.clientes:
        cliente.visualizar_historico()

    # Listando livros novamente
    print("\nLista de Livros Atualizada:")
    livraria.listar_livros()
