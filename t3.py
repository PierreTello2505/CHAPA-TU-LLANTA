print("opciones")
print("1. VEHÍCULO")
print("2. MEDIDAD DE LLANTAS")

while True:
    n=int(input("¿Cómo le gustaría hacer la busqueda?"))

    if n==1:
        while True:
            a=int(input("Ingrese año del vehículo: "))

            if a==2017:
                print("1. Toyota")
                print("2. Nissan")
                print("3. Volskwagen")
                print("4. AUDI")
                print("5. Porsche")
                print("6. BAJAJ")
                while True:   
                    m=int(input("Ingrese la marca de su vehículo: "))
                    if m==1:
                        print("1. Corolla")
                        print("2. Supra")
                        while True:
                            n=int(input("Elija el modelo de su vehículo: "))
                            if n==1:
                                print("VERSIÓN/OPCIÓN")
                                print("1. Tire1")
                                print("2. Tire2")
                            else:
                                print("1. Tire1 ")

                                while True:
                                    m=int(input("Elija la versión/opción del neumatico: "))
                                    if m==1:
                                        print("no hay llantas para tu especificacion")
                                     
                        
                                    elif m==2:
                                        print("CARACTERISTICAS DE LA LLANTA DE SU VEHÍCULO")
                                        print("medida de la llanta: 195/70R 15C")
                                        print("Indice de la velocidad: R")
                                        print("Indice de carga: 109")
                                        print("Rango de carga: D")
                                        print("Costado: BSW")
                                        print("Carga máxima: 1200 lbs")
                                        print("Presión máx de inflado: 70 PSI")
                                        print("Profundidad de banda de rodamiento: 12.500 mm")
                                    else:
                                        print("VERSIÓN/OPCIÓN")
                                        print("1. HIACE 1.3 JUPTIER")
                                        print("2. HIACE 2.8 TDI VAN")
