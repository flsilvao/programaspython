import os
def borrarpantalla():
     os.system("clear")


i = 0
totalacumulado = 0
igvacumulado = 0
factura = []
numproductos = int(input("Ingresar el numero de productos: "))
while i < numproductos:
    codigo = input("Ingresar el codigo del producto: ")
    nomproducto = input("Ingresar el nombre del producto: ")
    cantidad = int(input("Ingresar la cantidad del producto: "))
    precio = float(input("Ingresar el precio del producto: "))
    total = round(cantidad * precio, 2)
    igv = round(total * 0.18, 2)
    totalacumulado = totalacumulado + total
    igvacumulado = igvacumulado + igv
    registro = "P-" + codigo + "  " + nomproducto + " " * (20 - len(nomproducto)) + str(cantidad) + " " * (10 - len(str(cantidad))) + str(precio) + " " * (10 - len(str(precio))) + str(igv)+" " * 3 + str(total)
    factura.append(registro)
    i += 1
x = 0
# while x <= 10:
#     print(" ")
#     x += 1
borrarpantalla()
print("CODIGO","NOMBRE DEL PRODUCTO", "CANTIDAD", "PRECIO", "   IGV", "   TOTAL")
for x in factura:
    print(x)
print("*"*50)
print("Total: ", totalacumulado)
print("IGV:   ", round(igvacumulado, 2))
