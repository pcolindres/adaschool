#Define una variable de cada tipo de primitivo
numero = 3
flotante = 5.8
estudiante = True
cadena = "str"
#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatena = cadena + " "+ str(numero) + " "+ str(flotante) +" "+ str(estudiante)
print (concatena)
#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
#El limite de un entero es: Ninguno, python no tiene limites es decir puede almacenar todos los enteros, mientras que en el caso de los flotantes: La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308 
#aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20
resultado = 0
for i in range (2,n+1,2):
    resultado += i
print (resultado)
