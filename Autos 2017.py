import os
os.system("cls")

print("opciones")
print("1. VEHÍCULO")
print("2. MEDIDAD DE LLANTAS")

while True:
    n=int(input("¿Cómo le gustaría hacer la busqueda?"))

    if n==1:
        while True:
            a=int(input("Ingrese año del vehículo"))
  #MARCAS...
            if a==2017:
                print("1. DAIHATSU")
                print("2. DODGE")
                print("3. ASTON MARTIN")
                print("4. AUDI")
                print("5. AUTOCRAFT")
                print("6. BAIAC")
                while True:   
                    m=int(input("Ingrese la marca de su vehículo"))
  #MODELOS...
                    if m==1:
                        print("Modelo de su vehículo")
                        print("1. TERIOS")
     #Modelo especifico(por ejemplo si el usuario tiene un Toyota Corolla del 2017
     #el auto viene en 2 versiones...basico y full/ en el basico en auto viene con aros 
     # standar y en la version full vienes con otro tipo de aro que va influir en el tipo de llanta 
                        while True:
                            n=int(input("Elija el modelo de su vehículo"))
                            if n==1:
                                print("VERSIÓN/OPCIÓN")
                                print("1. TERIOS 1.5 LUJO ")
                                print("2. TERIOS 1.5 LUJO 4X4")
      #Modelos de neumatico que calzan...              
                                while True:
                                    m=int(input("Elija la versión/opción de su vehículo"))
                                    if m==1:
                                        print(" NEUMATICO Goodyear Wrangler SUV:")
                                        print("Caracteristicas del neumatico:")
                                        print("medida del neumatico: 215/65R16")
                                        print("Indice de la velocidad: H")
                                        print("Indice de carga: 98")
                                        print("Rango de carga: SL")
                                        print("Costado: VSB")
                                        print("Carga máxima: 750 lbs")
                                        print("Presión máx de inflado: 51 PSI")
                                        print("Profundidad de banda de rodamiento: 9.500 mm")
                        
                                    elif m==2:
                                        print(" NEUMATICO Goodyear Wrangler SUV:")
                                        print("Caracteristicas del neumatico:")
                                        print("medida de la llanta: 215/65R16")
                                        print("Indice de la velocidad: H")
                                        print("Indice de carga: 98")
                                        print("Rango de carga: SL")
                                        print("Costado: BSW")
                                        print("Carga máxima: 850 lbs")
                                        print("Presión máx de inflado: 65 PSI")
                                        print("Profundidad de banda de rodamiento: 10.000 mm")
                                    else:
                                        print("Elija una de estas VERSIÓN/OPCIÓN")
                                        print("1. HIACE 1.3 JUPTIER")
                                        print("2. HIACE 2.8 TDI VAN")
                #segunda marca del 2017 (Dodge) 2 modelos...
                    if m==2:
                        print("1. CHALLENGER")
                        print("2. DURANGO")
                        while True:
                            n=int(input("Elija el modelo de su vehículo"))          
                            if n==1:
                                print("1. CHALLENGER 5.7 V8 RT")
                                print("2. CHALLENGER 6.1 TURBO")
                                while True:
                                    m=int(input("Elija la versión/opción de su vehículo"))
                                    if m==1:
                                        print(" NEUMATICO Michelin PLUS")
                                        print("Medida de la llanta: 255/60R18")
                                        print("Indice de velocidad: T")
                                        print("Indice de carga: 130")
                                        print("LINK DE PAGINAS")
                                        print(" https://www.michelin.com.pe/")
                                    elif m==2:
                                        print(" NEUMATICO Super Good year")
                                        print("CRACTERÍSTICAS DEL NEUMATICO:")
                                        print("Medida de la llanta: 255/60R18")
                                        print("Indice de velocidad: T")
                                        print("Indice de craga: 130")
                                        print("LINK DE PAGINAS")
                                        print("https://www.goodyear.com.pe/")  
                                    if m==1 or m==2:
                                        break
                            elif n==2:
                                print("1. DURANDO 3.6 V6 AUTO")
                                print("2. DURANGO 5.7 V8 LX AUTO 4X4")
                                while True:
                                    m=int(input("Elija la versión/opción de su vehículo"))
                                    if m==1:
                                        print(" NEUMATICO Michelin PLUS")
                                        print("Medida de la llanta: 255/60R18")
                                        print("Indice de velocidad: T")
                                        print("Indice de carga: 130")
                                        print("LINK DE PAGINAS")
                                        print(" https://www.michelin.com.pe/")
                                    elif m==2:
                                        print(" NEUMATICO Super Good year")
                                        print("CRACTERÍSTICAS DEL NEUMATICO:")
                                        print("Medida de la llanta: 255/60R18")
                                        print("Indice de velocidad: T")
                                        print("Indice de craga: 130")
                                        print("LINK DE PAGINAS")
                                        print("https://www.goodyear.com.pe/")  
                                    if m==1 or m==2:
                                        break
