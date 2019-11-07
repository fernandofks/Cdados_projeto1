cigarros_dia=int(input("quantos cigarros por dia você fuma"))
anos_fumando=int(input("há quantos anos você fuma"))

dias_de_vida_perdidos=int(365*anos_fumando*cigarros_dia*10/(24*60))

print("Você perdeu {0} dias de vida".format(dias_de_vida_perdidos))