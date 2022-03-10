import random
class JogoAdivinha:

    def __init__(self):
        # aleatório entre 1 e 20
        self.baixo = 1
        self.alto  = 20

    # gerador do número mágico
    def get_random_number(self):
        return random.randint(self.baixo, self.alto)
    # inicia 
    def start(self):
        random_number = self.get_random_number()

        print(
            f"Adivinhe um número aleatório {self.baixo} entre {self.alto}")

        ## heart of the game
        chances = 0
        while True:
            user_number = int(input("Introduza um número: "))
            if user_number == random_number:
                print(
                    f"-> Parabéns, conseguiu adivinhar na {chances + 1} tentativa{'' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Pista: Este número é menor que o número aleatório")
            else:
                print("-> Pista: Este número é maior que o número aleatório")
            chances += 1

## instantiating and starting the game
JogoAdivinha = JogoAdivinha()
JogoAdivinha.start()
