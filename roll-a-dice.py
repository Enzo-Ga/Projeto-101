import random

response = "y"


def roll(response):
    while response == "y":
        no = random.randint(1, 6)
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif no == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        elif no == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif no == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        elif no == 6:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
        response = input("Pressione y para jogar novamente e n para sair: ")


roll(response)
