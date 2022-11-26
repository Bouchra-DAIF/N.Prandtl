print("Transfert de chaleur ")
Cp=input("Entrez la conductivité thermique: ")
Vc=input("Entrez la viscosité dynamique: ")
Lambd=input("Entrez la conductivité thermique: ")
try:
    Cp=float(Cp)
    Vc=float(Vc)
    Lambd=float(Lambd)
    Pr=(Cp*Vc)/Lambd
    print("Le nombre Prandtl", Pr)
except:
    print("erreur")