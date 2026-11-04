from Aula.livro import Livro

class Ebook(Livro):
    def __init__(self, titulo, autor, npag, mb, sit = True):
        super().__init__(titulo, autor, npag, sit)
        self.mb = mb

    def descricao(self):
        return f"O E-book {self.titulo} do autor {self.autor} tem {self.npag} paginas e pesa {self.mb}mb, Ele está disponível: {self.sit}"