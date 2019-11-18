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
                        print("MODELOS")
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
                        print("MODELOS")
                        print("1. GIULIETTA")
                        print("2. mito")
                        while True:
                            n=int(input("Elija el modelo de su vehículo"))
                            # 2.1 primer modelo
                            if n==1:
                                #VERSIONES
                                print("VERSIONES")
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
                                print("VERSIONES")
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
                        print("MODELOS")
                        print("1. DB11")
                        print("2. RAPIDE")
                        print("3. VANQUISH")
                        while True:
                            n=int(input("Elija una de estos modelos"))
                            # 3.1 primer modelo
                            if n==1:
                                #VERSIONES
                                print("VERSIONES")
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

    if n==2:
        while True:
            x=int(input("Ingrese el ancho"))
            y=int(input("Ingrese perfil"))
            z=int(input("Ingrese el diametro"))

            if x==255 and y==4 and z==19:
                print("Neumático: Goodyear Eagle F1 Asymmetric 2 ROF")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Control preciso y potente Aproveche al máximo su coche con un neumático fabricado para maximizar el rendimiento de alta potencia. Un compuesto de sílice especial ofrece un agarre fiable en carreteras secas y mojadas con una carcasa rígida que aumenta la precisión de la dirección incluso a alta velocidad.")
            elif x==225 and y==45 and z==17:
                print("Neumático: Goodyear Eagle F1 Asymmetric 3")
                print(x,"/",y,"R",z)
                s=["Precio 140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Neumático para camiones ligeros que puede convertirse en su socio más fiable proporcionándole 10.000 km adicionales, ahorrándole combustible y ofreciéndole distancias de frenado más cortas sobre carreteras mojadas.")
                print("Reseña: Comportamiento cómodo, tranquilo y predecible. Quizás no para todos los paseos deportivos debido al perfil ligeramente más alto, sino para las carreras normales, el mejor.")
            elif x==205 and y==55 and z==16:
                print("Neumático: Goodyear Assurance")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("2,600 millas/4,000 kilómetros en base a una mejora de ahorro de combustible del 4%.")
            elif x==225 and y==50 and z==17:
                print("Neumatico: Goodyear EfficientGrip Performance ROF")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Distancia de frenado reducida Siéntase más seguro al volante en cada viaje con la tecnología ActiveBraking. Esta característica aumenta la superficie de contacto entre el neumático y la carretera, para reducir drásticamente las distancias de frenado, hasta un 8% más cortas en carreteras mojadas y hasta un 3 por ciento en carreteras secas.")
            elif x==175 and y==70 and z==13:
                print("Neumatico: Direction Touring")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Surcos transversales y longitudinales más anchos, lo que brinda mejor adherencia en piso mojado.")
            elif x==235 and y==45 and z==19:
                print("Neumatico: Goodyear EfficientGrip ROF")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Para que un pinchazo nunca vuelva a detener su viaje: gracias a la revolucionaria tecnología RunOnFlat, podrá conducir una distancia de hasta 80 km después de un pinchazo o reventón.")
            elif x==225 and y==40 and z==18:
                print("Neumatico: Goodyear Eagle F1 Asymmetric")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Reducción de la distancia de frenado en carreteras mojadas y secas. Deténgase con total confianza cuando sea cuestión de milésimas de segundo gracias a la tecnología ActiveBraking, que aumenta el contacto del neumático con la calzada cuando frena.")
            elif x==185 and y==60 and z==14:
                print("Neumatico: Kelly Edge Sport")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Bajo índice de desgaste de la banda de rodamiento: Ventaja de hasta 6 por ciento si se compara a su antecesor, entregando un alto kilometraje.")
            elif x==225 and y==55 and z==17:
                print("Neumatico: Goodyear Excellence ROF")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Las plantas automotrices más reconocidas del mercado equipan sus vehículos con Neumaticos que tienen tecnología RunOnFlat®. Esta tecnología permite que la llanta ruede sin presión del aire hasta 80 km/h.")
            elif x==205 and y==60 and z==16:
                print("Neumatico: Goodyear EfficientGrip Performance")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("El mejor frenado sobre terreno mojado con una resistencia mínima La tecnología WearControl de Goodyear está diseñada para encontrar el equilibrio ideal entre un agarre firme sobre carreteras mojadas y una baja resistencia a la rodadura, para reducir el consumo de combustible y garantizar una conducción más estable.")
            elif x==175 and y==65 and z==14:
                print("Neumatico: Kelly Edge Touring")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Kelly Edge Touring es una llanta desarrollada para autos de baja a media potencia. Su desempeño en pistas mojadas es de hasta un 20 por ciento superior, en comparación con su predecesor.")
            elif x==205 and y==55 and z==16:
                print("Neumatico: Goodyear EfficientGrip")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","ideal para ciudad", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Con estructura liviana y compuesto avanzado de banda, EfficientGrip necesita menos energía para rodar. Disfruta viajes más silenciosos gracias al diseño de los bloques que reduce los niveles de ruido.")

        #Siguiente

            elif x==255 and y==60 and z==17:
                print("Neumatico: Goodyear EfficientGrip Performance SUV")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Desarrollado con la tecnología Fuel Saving, que proporciona ahorro de combustible. Ofrece un desempeño hasta 30 % mejor en maniobrabilidad y 15 por ciento superior en tracción y frenado en piso mojado.")
            elif x==255 and y==70 and z==18:
                print("Neumatico: Goodyear Wrangler All-Terrain Adventure")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("El neumático versátil todoterreno con la rigidez de Kevlar® para circular fuera de carretera en cualquier momento. Capa reforzada de Kevlar®. Resiste los pinchazos y los cortes para una conducción segura fuera de la carretera.")
            elif x==285 and y==75 and z==16:
                print("Neumatico: Goodyear Wrangler MT/R Kevlar")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Insuperable agarre en caminos Off-Road y lluvia. Compuesto de sílica en la banda de rodamiento que proporciona mayor tracción. Extraordinaria tracción en lodo, grava y caminos rocosos. Costado especial de la llanta con un agresivo dibujo que brinda tracción lateral.")
            elif x==225 and y==65 and z==16:
                print("Neumatico: Goodyear G32 CARGO")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Rodar tranquilo, confortable y silencioso. Excelente kilometraje y tracción. Fuerte resistencia a las condiciones rigurosas de los servicios comerciales.")
            elif x==235 and y==65 and z==17:
                print("Neumatico: Goodyear Wrangler SUV")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mejor adherencia en piso mojado. Kilometraje y ahorro de combustible.")
            elif x==245 and y==75 and z==16:
                print("Neumatico: Goodyear Wrangler Armortrac")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mejor desempeño en piso mojado. Kilometraje y resistencia en condiciones de carretera y todo terreno.")
            elif x==255 and y==70 and z==18:
                print("Neumatico: Goodyear Wrangler Adventure")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Láminas en tacos y hombros que proporcionan mayor capacidad de enfriamiento y superior alcance en kilometroje. Surcos longitudinales y transversales para mejor desalojo de agua y limpieza de barro y piedras, permitiendo un mejor desempeño en todo tipo de terreno.")
            elif x==265 and y==65 and z==17:
                print("Neumatico: Goodyear Wrangler Duratrac")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mayor tracción: gracias a la tecnología TractiveGroove™, que consiste en pequeños dientes de sierra en la base de los surcos para mejorar la tracción en lodo profundo. Rodar silencioso: Bloques centrales altamente angulados que aumentan la tracción y la estabilidad lateral y reducen el ruido externo.")
            elif x==215 and y==70 and z==14:
                print("Neumatico: Goodyear G32 PLUS")
                print(x,"/",y,"R",z)
                s=["Precio 70$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mejor rendimiento en curvas y frenado. Resistencia a impactos y temperatura elevadas.")
            elif x==235 and y==60 and z==18:
                print("Neumatico: Goodyear Wrangler HP All Weather")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Las acanaladuras de la banda de rodadura aseguran la rápida dispersión del agua, lo que ayuda a mantener un control óptimo sobre mojado.")
            elif x==205 and y==40 and z==16:
                print("Neumatico: Goodyear Wrangler AT/S")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Camioneta", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Su diseño profundo en la parte exterior de los hombros y amplios bloques laterales ofrecen una adecuada protección para el costado. Diseño de la banda de rodamiento optimizado para brindar un rodar suave y proveer un desgaste parejo.")

        #Siguiente

            elif x==205 and y==55 and z==16:
                print("Neumatico: Goodyear Assurance")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Assurance", "pagina de compra: https://www.goodyear.com.pe/llantas "]
                print(s)
                print("Grandes surcos laterales en la banda de rodamiento que ayudan a evacuar el agua para un excelente agarre en mojado. 16% mayor vida de la banda de rodamiento debido a un diseño optimizado de la llanta.")

        #Siguiente

            elif x==255 and y==44 and z==19:
                print("Neumatico: Goodyear Eagle F1 Asymmetric 2 ROF") 
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Eagle", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Menor consumo de combustible La mayor eficiencia del consumo de combustible le ayuda a reducir gastos y a minimizar las emisiones CO2, lo que es bueno para su bolsillo y para el medio ambiente.")
            elif x==225 and y==45 and z==17:
                print("Neumatico: Goodyear Eagle F1 Asymmetric 3")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Eagle", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("La tecnología ActiveBraking proporciona mayor contacto de la llanta con el suelo en el frenado. Estructura reforzada que garantiza mayor precisión en la dirección y durabilidad.")
            elif x==255 and y==40 and z==19:
                print("Neumatico: Goodyear Eagle F1 Asymmetric 2")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Eagle", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("La tecnología ActiveBraking proporciona mayor contacto de la llanta con el suelo en el frenado.")
            elif x==225 and y==40 and z==18:
                print("Neumatico: Goodyear Eagle F1 Asymmetric")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Eagle", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Conducción de alto rendimiento. Obtenga un mayor rendimiento de su coche de alta potencia. El compuesto de sílice de la superficie mejora el agarre para una maniobrabilidad fiable sobre calzadas secas y mojadas.")
            elif x==245 and y==45 and z==19:
                print("Neumatico: Goodyear Excellence ROF")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Eagle", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Creada con compuesto especial de polimero, Excellence brinda una excepcional adherencia y agarre en curvas, con menor distancia de frenado.")

        #Siguiente

            elif x==255 and y==70 and z==18:
                print("Neumatico: Goodyear Wrangler All-Terrain Adventure")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("37 por ciento superior en tracción en piso mojado. Agilidad en terrenos difíciles (barro, arena y piedra).")
            elif x==265 and y==85 and z==16:
                print("Neumatico: Goodyear Wrangler MT/R Kevlar")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Insuperable agarre en caminos Off-Road y lluvia. Compuesto de sílica en la banda de rodamiento que proporciona mayor tracción. Extraordinaria tracción en lodo, grava y caminos rocosos. Costado especial de la llanta con un agresivo dibujo que brinda tracción lateral.")
            elif x==215 and y==70 and z==16:
                print("Neumatico: Goodyear Wrangler SUV")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mejor adherencia en piso mojado. Kilometraje y ahorro de combustible.")
            elif x==245 and y==70 and z==16:
                print("Neumatico: Goodyear Wrangler Armortrac")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Mejor desempeño en piso mojado. Kilometraje y resistencia en condiciones de carretera y todo terreno.")
            elif x==235 and y==70 and z==16:
                print("Neumatico: Goodyear Wrangler Adventure")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Construcción reforzada en el costado con Durawal TechnologyTM  que proporciona  mayor resistencia a cortes y perforaciones. Láminas en tacos y hombros que proporcionan mayor capacidad de enfriamiento y superior alcance en kilometroje.")
            elif x==275 and y==55 and z==18:
                print("Neumatico: Goodyear Wrangler Duratrac")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Rodar silencioso: Bloques centrales altamente angulados que aumentan la tracción y la estabilidad lateral y reducen el ruido externo.")
            elif x==275 and y==70 and z==16:
                print("Neumatico: Goodyear Wrangler HP All Weather")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Rodar suave y confortable. Mayor poder de tracción en pisos secos o mojados.")
            elif x==205 and y==80 and z==16:
                print("Neumatico: Goodyear Wrangler AT/S")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Wrangler", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Excelente tracción en todo tipo de terreno gracias a sus canales autolimpiantes que permiten una mejor evacuación del agua y barro. Su diseño profundo en la parte exterior de los hombros y amplios bloques laterales ofrecen una adecuada protección para el costado.")

        #Siguiente

            elif x==255 and y==60 and z==17:
                print("Neumatico: Goodyear EfficientGrip Performance SUV")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Efficient", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Desarrollado con la tecnología Fuel Saving, que proporciona ahorro de combustible. Ofrece un desempeño hasta 30 % mejor en maniobrabilidad y 15 porciento superior en tracción y frenado en piso mojado.")
            elif x==205 and y==60 and z==16:
                print("Neumatico: Goodyear EfficientGrip Performance")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Efficient", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Compuesto de banda de rodamiento desarrollado para optimizar la adherencia en pisos secos y mojados.")
            elif x==205 and y==65 and z==16:
                print("Neumatico: Goodyear EfficientGrip")
                print(x,"/",y,"R",z)
                s=["Precio 70$-140$","Clase/Tipo: Efficient", "pagina de compra: https://www.goodyear.com.pe/llantas"]
                print(s)
                print("Con estructura liviana y compuesto avanzado de banda, EfficientGrip necesita menos energía para rodar. Disfruta viajes más silenciosos gracias al diseño de los bloques que reduce los niveles de ruido. Economiza combustible con EfficientGrip, con la tecnología FuelSaving.")

            else:
                print("Lo sentimos, no existen ejemplares de las medidas deseadas.")

            if x<=500 and y<=500 and z<=500:
                break
        