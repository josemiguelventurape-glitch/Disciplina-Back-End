class Livro:
    def __init__(self, titulo, autor, npag, sit = True):
        self.titulo = titulo
        self.autor = autor
        self.npag = npag
        self._sit = sit

    def descricao(self):
        return f"O Livro {self.titulo}, do autor {self.autor} tem {self.npag} páginas"

    def emprestar(self):
        if self._sit == True:
            self._sit = False
            print(f"O Livro {self.titulo} foi emprestado a você!")
        else:
            print(f"O Livro {self.titulo} já foi emprestado!")

    def devolver(self):
        self._sit = True
        print(f"O Livro {self.titulo} está disponível novamente!")