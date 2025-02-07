def hakimi(conjunto):
    for x in conjunto:
        if x<0:
            return 0
        else:
            

try:
    entrada = input().replace(","," ").replace("  ", " ").split(" ")
    conjunto = [int(x) for x in entrada]
except:
    print("Error en la lectura de datos.")
    #exit()

suma = sum(conjunto)
if suma%2!=0:
    print("El conjunto no cumple con el teorema de la mano derecha.")
else:
    hakimi(conjunto)
    
#print(conjunto)
