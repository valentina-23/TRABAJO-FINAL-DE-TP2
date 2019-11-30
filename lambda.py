# FUNCIONES ANÓNIMAS
# Las funciones normales son definiodas con la palabra
# clave def, mientras que las anónimas se crean con lambda
# lambda x : x + 1  --> x(argumento): x + 1 (cuerpo de la función)

lista = [1,2,3,4,5]

# se crea una nueva lista usando map para elevar
# cada elemento de lista al cuadrado

lista_m = list(map(lambda x:x**2,lista))
print(lista_m) #imprime 1,4,9,16,25

# Asignación de función lambda a una variable
mayores_a_2 = lambda x:x>2
# Uso de la función filtro con la función lambda
# solo filtará elementos mayores a 2
lista_f1 = list(map(mayores_a_2,lista))
print(lista_f1) # imprime false y true

lista_f2 = list(filter(mayores_a_2,lista))
print(lista_f2) # imprime 3 ,4 ,5

# Variable con función lambda para elevar a la 5

potencia = lambda x:x**5
print(potencia(3))#imprime 243
