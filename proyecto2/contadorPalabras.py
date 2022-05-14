



'''Preguntamos al usuario en que está pensando. 
   Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia
    e imprimimos en la salida el resultado.'''


from tokenize import String


import csv
import string

pensamiento = input("Hola que esta pensado")
f  = open("declaracion.txt","w")
f.write(pensamiento)


translator = str.maketrans('', '', string.punctuation)

#creo una lista vacia 
word_count = {}

# abrir un documento declaracion para contar las palabras 
text = open('declaracion.txt').read()

#Usa la funcion split() para separar el texto en palabras
words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word
