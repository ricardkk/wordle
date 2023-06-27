import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words

def menu():
    print("Bem vindo ao wordle.py!")
    print("Digite uma palavra com 5 letras e aperte enter.\n")

def pick_palavra():
    with open('db.txt') as f:
        palavras = f.read().splitlines()
        return random.choice(palavras)

menu()

jogar_novamente = ""
while jogar_novamente != "quit":
    palavra = pick_palavra()
    for tentativa in range(1,6+1):
        tent = input().lower()
        
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(tent), 5)):
            if tent[i] == palavra[i]:
                print(colored(tent[i], 'green'), end=" ")
            elif tent[i] in palavra:
                print(colored(tent[i], 'yellow'), end=" ")
            else:
                print(colored(tent[i], 'red'), end=" ")
        print()

        if tent == palavra:
            print(colored(f"Parabéns! você adivinhou a palavra em {tentativa} tentativas.", 'blue'))
            break
        elif tentativa == 6:
            print(colored(f"Que pena! você não conseguiu adivinhar a palavra '{palavra}' :(", 'blue'))
    jogar_novamente = input("Jogar novamente? digite 'quit' para sair.")
    

