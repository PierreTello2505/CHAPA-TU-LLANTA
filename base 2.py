import os
os.system("cls")

#TIPOS DE BUSQUEDA
print("opciones")
print("1. VEHÍCULO")
print("2. MEDIDAD DE LLANTAS")

while True:
    n=int(input("¿Cómo le gustaría hacer la busqueda?"))
    #busqueda por vehiculos
    if n==1:
        #AÑO DE LOS VEHÍCULOS
        while True:
            a=int(input("Ingrese año del vehículo"))

            #1.AÑO DEL VEHÍCULO
            if a==2018:
                #MARCAS DE VEHÍCULOS
                print("1. AICHI SAN")
                print("2. ALFA ROMEO")
                print("3. ASTON MARTIN")
                print("4. AUDI")
                print("5. BAIC")
                print("6. BAJAJ")
                while True:   
                    m=int(input("Ingrese la marca de su vehículo"))
                    # 1 primera marca del vehiculo
                    if m==1:
                        #MODELOS
                        print("Modelo de su vehículo")
                        print("1. HIACE")
                        while True:
                            n=int(input("Elija el modelo de su vehículo"))
                            # 1.1 primer modelo
                            if n==1:
                                #VERSIONES
                                print("VERSIÓN/OPCIÓN")
                                print("1. HIACE 1.3 JUPTIER")
                                print("2. HIACE 2.8 TDI VAN")

                                while True:
                                    m=int(input("Elija la versión/opción de su vehículo"))
                                    # 1.1.1primera version
                                    if m==1:
                                        #DETALLES
                                        print("no hay llantas para tu especificacion")
                                     
                                    # 1.1.2segunda version
                                    elif m==2:
                                        #DETALLES
                                        print("CARACTERISTICAS DE LA LLANTA DE SU VEHÍCULO")
                                        print("medida de la llanta: 195/70R 15C")
                                        print("Indice de la velocidad: R")
                                        print("Indice de carga: 104")
                                        print("Rango de carga: D")
                                        print("Costado: BSW")
                                        print("Carga máxima: 900 lbs")
                                        print("Presión máx de inflado: 65 PSI")
                                        print("Profundidad de banda de rodamiento: 10.500 mm")
                                    #cuando vuelve a preguntar
                                    else:
                                        print("Elija una de estas VERSIÓN/OPCIÓN")
                                        print("1. HIACE 1.3 JUPTIER")
                                        print("2. HIACE 2.8 TDI VAN")
                                    

                # 2 marca del 2018
                    if m==2:
                        #MODELOS DEL VEHICULOS
                        print("Elije un modelo")
                        print("1. GIULIETTA")
                        print("2. mito")
                        while True:
                            n=int(input("Elija el modelo de su vehículo"))
                            # 2.1 primer modelo
                            if n==1:
                                #VERSIONES
                                print("elija una de estas versiones")
                                print("1. GIULIETTA 1.4 16V TB MULTIAIR DISTINCTIVE")
                                print("2. GIULIETTA 1.8 16V TB GDI PROGRESSION")
                                while True:
                                    m=int(input("Elija la versión/opción de su vehículo"))
                                    # 2.1.1 primera version
                                    if m==1:
                                     #DETALLES
                                        print("Medida de la llanta: 225/45R17")
                                        print("Indice de velocidad: W")
                                        print("Indice de craga: 90")
                                        print("LINK DE PAGINAS")
                                        print("https://www.goodyear.com.pe/tire-results?y=2018&m=ALFA+ROMEO&mo=GIULIETTA&v=1.4+16V+TB+MULTIAIR+DISTINCTIVE&addr=Av.+Javier+Prado+Este%2C+Lima%2C+Per%C3%BA&lat=-12.0824361&lng=-76.98570610000002")
                                  
                                    # 2.1.2 segunda version
                                    elif m==2:
                                        #DETALLES
                                        print("CRACTERÍSTICAS DE LA LLANTA")
                                        print("Medida de la llanta: 225/45R17")
                                        print("Indice de velocidad: W")
                                        print("Indice de craga: 93")
                                        print("LINK DE PAGINAS")
                                        print("https://www.goodyear.com.pe/tire-results?y=2018&m=ALFA+ROMEO&mo=GIULIETTA&v=1.8+16V+TB+GDI+PROGRESSION&addr=Av.+Javier+Prado+Este%2C+Lima%2C+Per%C3%BA&lat=-12.0824361&lng=-76.98570610000002")  
                            # 2.2 segundo modelo
                            if n==2:
                                #VERSIONES
                                print("Elija una de estas versiones")
                                print("1. MITO 1.4 16V T-JET")
                                while True:
                                    m=int(input("Elija una version"))
                                    #2.2.1 primera version
                                    if m==1:
                                        #DETALLES
                                        print("CARACTERISTICAS DE LA LLANTA")
                                        print("medida de la llanta: 215/45R17")
                                        print("Indice de velocidad: W")
                                        print("Indice de carga: 91")
                    # 3 marca del 2018                    
                    if m==3:
                        #MODELOS
                        print("Elija su modelo")
                        print("1. DB11")
                        print("2. RAPIDE")
                        print("3. VANQUISH")
                        while True:
                            n=int(input("Elija una de estos modelos"))
                            # 3.1 primer modelo
                            if n==1:
                                #VERSIONES
                                print("Elija la version")
                                print("1. DB11 5.2 V12 TURBO COUPE AUTO")
                                while True:
                                    m=int(input("Elija la versionde su vehículo"))
                                    #3.1.1 primera version
                                    if m==1:
                                        #DETALLES
                                        print("CARACTERISTICAS DE SU LLANTA")
                                        print("Medidad de la llanta delantera: 255/40R20")
                                        print("Medidad de llanta rear: 295/35R20")
                            # 3.2 segundo modelo           
                            if n==2:
                                #VERSIONES
                                print("VERSIONES")
                                print("1. RAPIDE 6.0 V12 S AUTO")
                                while True:
                                    m=int(input("Elija una de las versiones"))
                                    #3.2.1 primera version
                                    if m==1:
                                        #DETALLES
                                        print("CARACTERISTICAS DE SU LLANTA")
                                        print("Medidas de las llantas delanteras: 245/40R20")
                                        print("Medidas de las llantas rear: 298/35R20")
                            # 3.3 tercer modelo
                            if n==3:
                                #VERSIONES
                                print("VERSIONES")
                                print("1. VANQUISH 6.0 V12 AUTO")
                                while True:
                                    m=int(input("Elija la version de su auto"))
                                    #3.3.1 primera version
                                    if m==1:
                                        #DETALLES
                                        print("CARACTERISTICAS DE SU LLANTA")
                                        print("Medidad de las llantas delanteras: 255/35R20")
                                        print("Indice de velocidad-llanta delantero: Y")
                                        print("Indice de carga-llanta delantero: 97 ")
                                        print("Medidad de las llantas rear: 305/30R20")
                                        print("Indice de velocidad-llantas rear: Y")
                                        print("Indice d ecarga-llantas rear: 99")
                                        


                              
                                        







