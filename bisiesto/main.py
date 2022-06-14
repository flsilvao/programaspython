año = int(input("ingresar solo el año: "))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("Es un año bisiesto")
else:
    print("Es un año comun")

