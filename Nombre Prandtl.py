print("Transfert de chaleur ")
Cp=input("Entrez la conductivit√© thermique: ")
Vc=input("Entrez la viscosit√© dynamique: ")
Lambd=input("Entrez la conductivit√© thermique: ")
try:
    Cp=float(Cp)
    Vc=float(Vc)
    Lambd=float(Lambd)
    Pr=(Cp*Vc)/Lambd
    print("Le nombre Prandtl", Pr)
except:
    print("erreur")