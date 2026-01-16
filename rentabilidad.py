def calcular_margen(costo, precio):
    if precio <= 0: return 0
    return ((precio - costo) / precio) * 100

def sistema_interactivo():
    inventario = []
    
    print("=== SISTEMA DE ANÁLISIS DE RENTABILIDAD ===")
    print("Escribe 'salir' en el nombre del producto para terminar.\n")

    while True:
        nombre = input("Nombre del producto: ")
        if nombre.lower() == 'salir':
            break
            
        try:
            costo = float(input(f"Costo de producción de '{nombre}': "))
            precio = float(input(f"Precio de venta de '{nombre}': "))
        except ValueError:
            print("❌ Error: Por favor ingresa números válidos para costo y precio.\n")
            continue

        margen = calcular_margen(costo, precio)
        

        if margen >= 40:
            estado = "✅ ALTA RENTABILIDAD"
        elif margen >= 20:
            estado = "⚠️ RENTABILIDAD MEDIA (Ajuste sugerido)"
        else:
            estado = "🚨 BAJA RENTABILIDAD (Revisión urgente)"

       
        inventario.append({"nombre": nombre, "margen": margen})

        
        print(f"\n> RESULTADO PARA: {nombre.upper()}")
        print(f"> Margen calculado: {margen:.2f}%")
        print(f"> Estado técnico: {estado}")
        print("-" * 40 + "\n")


    if inventario:
        print("\n=== RESUMEN ESTRATÉGICO FINAL ===")
        mas_rentable = max(inventario, key=lambda x: x['margen'])
        print(f"🏆 Producto líder: {mas_rentable['nombre']} ({mas_rentable['margen']:.2f}%)")

sistema_interactivo()