from Animal import Animal

class Cachorro(Animal):
    def __init__(nome, falar = "Au!"):
        super().__init__(nome, falar)

class Gato(Animal):
    def __init__(nome, falar = "Miau!"):
        super().__init__(nome, falar)


acervo = [
    Cachorro("Snoppy"),
    Cachorro("Scooby"),
    Gato    ("Garfield")
]

