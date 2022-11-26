print("N. Nusselt ")
h=input("Entrez la coefficient de transfert thermique : ")
D=input("Entrez la longueur caractéristique (m): ")
Lambd=input("Entrez la conductivité thermique du fluide: ")
try:
    h=float(h)
    D=float(D)
    Lambd=float(Lambd)
    Nu=(h*D)/Lambd
    print("Le nombre Nusselt", Nu)
except:
    print("erreur")