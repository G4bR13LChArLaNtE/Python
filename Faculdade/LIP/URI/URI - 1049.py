#URI - 1049 - Animal:

c1 = input()
c2 = input()
c3 = input()

if c1 == "vertebrado":

    if c2 == "ave":
        if c3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")

    elif c2 == "mamifero":
        if c3 == "onivoro":
            print("homem")
        else:
            print("vaca")

elif c1 == "invertebrado":

    if c2 == "inseto":
        if c3 == "hematofago":
            print("pulga")
        else:
            print("largata")

    elif c2 == "anelideo":
        if c3 == "hematofago":
            print("saguessuga")
        else:
            print("minhoca")
