#EJERCICIO PRUEBA
print('EJERCICIO PRUEBA')
file1=open('resultados1.txt')
file=file1.read()
file=file.split()
file2=[]

for i in file:
	if i not in file2:
		file2.append(i)

print('RESULTADO EJERCICIO PRUEBA')
for i in range (0, len(file2)):
	if len(file2[i])>4:
		print ('(', file2[i],')',file.count(file2[i]),')')

#PALABRAS MAYORES A 4 CARACTERES
print()
print('EJERCICIO CLASE')
filea=open('Starwars.txt')
file=filea.read()
file=file.split()
fileb=[]

for i in file:
	if i not in fileb:
		fileb.append(i)

print('RESULTADO EJERCICIO CLASE')
for i in range (0, len(fileb)):
	if len(fileb[i])>4:
		print ('(', fileb[i],')',file.count(fileb[i]),')')

