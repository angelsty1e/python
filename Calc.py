def table(nb, depart, arrive):
    while depart != arrive:
        print depart, "fois", arrive, "est egale a", depart * arrive
        depart = depart + 1


restart = "Voulez continuez?oui/non"
rep = 0
while rep < 100:
    print "\n CalculPi!"
    print "\n Faites ton choix !"
    print "\n 1.Multiplication \n 2.Addition \n 3.Soustraction \n 4.Division"

    choix = input()
    ph = "Choisissez les deux nombres"

    if choix == 1:
        print ph
        a = input()
        b = input()
        print a, "fois", b, "est egale a", a * b
        rep = rep + 1

    elif choix == 2:
        print ph
        nb1 = input()
        nb2 = input()
        print nb1, "plus", nb2, "est egale a ", nb1 + nb2
        rep = rep + 1

    elif choix == 3:
        print ph
        nb1 = input()
        nb2 = input()

        print nb1, "moins", nb2, "est egale a", nb1 - nb2
        rep = rep + 1

    elif choix == 4:
        print ph
        nb1 = input()
        nb2 = input()
        print nb1, "divise par", nb2, "est egale a", nb1 / nb2
        rep = rep + 1

raw_input('Appuyez sur entree pour quitter le programme...')