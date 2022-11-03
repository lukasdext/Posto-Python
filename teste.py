class projeto:

    n2 = int(input("Quantos KM seu carro faz por litro ? \n"))

    n1 = int(input("Quantidade de combustível por litro restante no veículo ? \n"))

    n3 = n1*n2

    print ("Com combustivel atual o carro faz",n3,"por km")

    lista = ["Posto disponivel em 10km","Posto disponivel em 20km","Posto disponivel em 25km"]

    if n3>= 10 and n3 <20:
        print (lista[0])
    elif n3>=20 and n3 <25 :
        print (lista[0])
        print (lista[1])
    elif n3>=25 :
        print (lista[0])
        print (lista[1])
        print (lista[2])
    else:
        print ("-1")


