 #inventario
inventario = { 

        "pro1":  (101, "Leche de almendras", 7),
        "pro2": (102, "Cafe amargo y fuerte", 2),
        "pro3":  (103, "mantequilla azul", 5),
        "pro4":  (104, "pan rojo integral", 8),
        "pro5":  (105, "salchichas de edicion limitada del show de Mr.pork", 10),
        "pro6":  (106, "pipis", 1),
        "pro7":  (107, "salsa no especificada", 4)
    }


def revisar_inventario(productos):

    print("="*50)
    print("\nEntrada de administracion de inventario\n")
    print("="*50)

   

    F1 = True



    while F1:
            D1 = int(input("[1]>>reviasar un producto\n[2]>>ver todo en inventario\n[3]>>verificar productos por reavastecer\n[4]>>salir\n"))

            if D1 == 1:
                print("-"*50)
                D2 = input("\nIntroduzca ID o nombre del producto: ").lower()
                if D2 == "101" or D2 == "Leche de almendras":
                    print("-"*50)
                    print(f"ID:{inventario['pro1'][0]}\tProducto:{inventario['pro1'][1]}\tCantidad:{inventario['pro1'][2]}")
                    print("Descripcion del administrador:")
                    print("Nota:Cambiar el lugar de la leche para que el vagabundo de\n" \
                    "la ventilacion no se las robe... otra vez")

                elif D2 == "102" or D2 == "Cafe amargo y fuerte":
                    print("-"*50)
                    print(f"ID:{inventario['pro2'][0]}\tProducto:{inventario['pro2'][1]}\tCantidad:{inventario['pro2'][2]}")
                    print("Descripcion del administrador:")
                    print("un cafe muy amargo pero lo suficientemente fuerte como para que\n" \
                    "un viejo de 3 piruetas y saltar por la ventana, si aun seguimos tratando de lidiar con esa demanda")

                elif D2 == "103" or D2 == "mantequilla azul":
                    print("-"*50)
                    print(f"ID:{inventario['pro3'][0]}\tProducto:{inventario['pro3'][1]}\tCantidad:{inventario['pro3'][2]}")
                    print("Descripcion del administrador:")
                    print("una mantequilla de color azul hecha de leche azul con el que hace el queso azul.")

                elif D2 == "104" or D2 == "pan rojo integral":
                    print("-"*50)
                    print(f"ID:{inventario['pro4'][0]}\tProducto:{inventario['pro4'][1]}\tCantidad:{inventario['pro4'][2]}")
                    print("Descripcion del administrador:")
                    print("Nota: poner un cartel que aclare que el pan no esta malo por ser de otro color, eso es racista")

                elif D2 == "105" or D2 == "salchichas de edicion limitada del show de Mr.pork":
                    print("-"*50)
                    print(f"ID:{inventario['pro5'][0]}\tProducto:{inventario['pro5'][1]}\tCantidad:{inventario['pro5'][2]}")
                    print("Descripcion del administrador:")
                    print("Nota: POR FAVOR jefe no compren mas esas salchichas POR FAVOR!!!")

                elif D2 == "106" or D2 == "pipis":
                    print("-"*50)
                    print(f"ID:{inventario['pro6'][0]}\tProducto:{inventario['pro6'][1]}\tCantidad:{inventario['pro6'][2]}")
                    print("Descripcion del administrador:")
                    print("esta cosa ni siquiera deberia estar en el inventario")

                elif D2 == "107" or D2 == "salsa no especificada":
                    print("-"*50)
                    print(f"ID:{inventario['pro7'][0]}\tProducto:{inventario['pro7'][1]}\tCantidad:{inventario['pro7'][2]}")
                    print("Descripcion del administrador:")
                    print("una salsa... no se de que pero es salsa")
        
                else:
                    print("Producto inexistente")
                print("-"*50)

#----------------------------------------------------------------------------------------------
            elif D1 == 2:
                print("\n" + "="*30)
                print("INVENTARIO COMPLETO")
                print("="*30)

                for id_p, nombre, cant in inventario.values():
                    print(f"ID: {id_p}\t Cant: {cant}\t Producto: {nombre}")
                print("-" * 50)

            elif D1 == 3:
                print("\n" + "-"*50)
                print("PRODUCTOS POR REABASTECER")
                
                hay_faltantes = False
                for id_p, nombre, cant in inventario.values():
                    if cant < 10:
                        print("-"*50)
                        print(f"ALERTA: {nombre} (Solo quedan {cant} unidades)")
                        hay_faltantes = True
        
                if not hay_faltantes:
                    print("Todo tiene stock suficiente.")
                print("-" * 50)

            elif D1 == 4:
                print("Saliendo del sistema...")
                F1 = False

revisar_inventario(inventario)