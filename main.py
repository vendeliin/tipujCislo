import random


def game():
    win = False
    ranNum = random.randint(0, 100)
    count = 0

    while not win:

        try:
            num = int(input("Zadej cislo od 1 do 100: "))

            # force error
            if num < 1 or num > 100:
                li = []
                for x in range(1):
                    print(li[x + 1])

            count += 1

            if num == ranNum:
                print(f"Vyhra ({count} pokusy)")
                break
            elif num < ranNum:
                print("Vygenerovane cislo je vetsi: ")
            else:
                print("Vygenerovane cislo je mensi: ")

        except:
            print("Nebylo zadano cislo, nebo nebylo v rozsahu.")


response = input("Chcete si zahrát? ")

while response == "ano":
    game()
    response = input("Chcete si zahrát? ")
