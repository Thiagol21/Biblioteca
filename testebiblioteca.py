from datetime import date, timedelta

class Livro:
    def __init__(self, id_livro, titulo, autor, ano_publicacao, disponivel):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        
    def status(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f"ID: {self.id_livro}, Titulo: {self.titulo}, Autor: {self.autor}, Ano de publicação: {self.ano_publicacao}, Status: {self.status}"        



    
class Usuario:
    def __init__(self, id_usuario, nome, email):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.livros_emprestados = []
    
    def __str__(self):
        return f"ID: {self.id_usuario}, Nome: {self.nome}, Email: {self.email}, "
    
    
    
    
class Emprestimo:
    maximo_livros = 4
    limite_devolução = 15
        
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = date.today()
        self.tempo_devolução = self.data_emprestimo + timedelta(days=self.limite_devolução)
        
        
    def __str__(self):
        return (f"Livro: {self.livro.titulo}, Usuario: {self.usuario}, "
                f"Emprestado em : {self.data_emprestimo}, Devolver até: {self.tempo_devolução}")
  
  
    
class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = []
    
    def adicionar_livro (self, livro):
        if livro.id_livro in self.livro:
            print("Este livro já exite")
        else:
            self.livros[livro.id_livro] = livro
            print("Livro adicionado com sucesso!!!")
            
    def remover_livro(self, id_livro):
        livro = self.livro.get(id_livro)
        if livro:
            if livro.disponivel:
                del self.livro[id_livro]
                print(f"Livro ID: {id_livro} removido com sucesso!!")
            else:
                print("Livro se encontra emprestado")
        else:
            print(f"Livro {id_livro} não encontrado")
        
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro disponível na biblioteca")
            
        else:
            print("Livros na biblioteca: ")
            for livros in self.livros:
                print(livros)
    
    def adicionar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"{usuario.id_usuario} já existe no sistema")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print("Usuario adicionado com sucesso!!!")
            
    def listar_usuarios(self, usuario):
        if not self.usuario:
            print("Nenhum usuario cadastrado")
        else:
            for usuario in self.usuarios:
                print(usuario)
    
    def emprestar_livro(self, id_livro, id_usuario):
        livro = self.livros.get(id_livro)
        usuario = self.usuarios.get(id_usuario)
        
        if not livro:
            print(f"Livro {id_livro} não encontrado.")
            return
        if not usuario:
            print(f"Usuário {id_usuario} não encontrado.")
            return
        if not livro.disponivel:
            print(f"Livro '{livro.titulo}' não está disponível")
            return
        if len(usuario.livros_emprestados) >= Emprestimo.maximo_livros:
            print (f"Usuário {usuario.nome} atingiu o limite de empréstimos")
            return
        emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(emprestimo)
        usuario.livros_emprestados.append(emprestimo)
        livro.disponivel = False
        print(f"Livro {livro.titulo} foi emprestado para {usuario.nome}. Devolução até {emprestimo.tempo_devolução}.")
        
        def devolver_livro(self, id_livro, id_usuario):
            usuario = self.usuarios.get(id_usuario)
            livro = self.livros.get(id_livro)
            if not usuario:
                print(f"Usuario {id_usuario} não encontrado")
                return
            emprestado = None
            for emprestimo in usuario.livros_emprestados:
                if emprestimo.livro.id_livro == id_livro:
                    emprestado = emprestimo
            if emprestado:
                usuario.livros_emprestados.remove(emprestado)
                self.emprestimos.remove(emprestado)
                emprestado.livro_disponivel = True
                print(f"Livro {emprestado.livro.titulo} devolvido por {usuario.nome}")
                
        def listar_emprestimos(self):
            if not self.emprestimos:
                print("Nenhum empréstimo encontrado")
            else:
                for emprestimo in self.emprestimo:
                    print(emprestimo)