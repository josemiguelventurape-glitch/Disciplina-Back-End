from Aula.acervo import acervo


for i in acervo:
    print(f"{i.titulo}: {i.npag}")

for i in acervo:
    if i.titulo == "Python Fluente":
        print(f"O Autor do Livro é: {i.autor}")
        break


acervo[1].sit=False #como o atributo self.sit tem "_" na frente "_self.sit", ele está protegido!
acervo[1].emprestar()
acervo[1].emprestar()