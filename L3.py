#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#1 2 3 4 5
#3
#-> 1

N = int(input('Кол. чисел:'))
list1 = [int(input('Ввести число:')) for i in range(N)]
k = int(input('Заданное число:'))

inc = 0
for i in list1:
    if i == N:
        inc += 1
print(inc)

 
#b=[abs(a[i]-x) for i in range(len(a))]
#print(sum(map(lambda z: int(z == x), a)))'''


#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#1 2 3 4 5
#6

#-> 5

'''N = int(input('Кол. чисел:'))
list1 = [int(input('Ввести число:')) for i in range(N)]
k = int(input('Заданное число:'))
m = abs(k - list1[0])
number = list1[0] 

for i in range(1, len(list1)):
	if m > abs(k - list1[i]):
		m = abs(k - list1[i])
		number = list1[i]

print(number)'''

#Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.
#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#Ввод:
#ноутбук
#Вывод:
#12

'''points_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
points_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

text = input().upper()
count = 0

for i in text:
	if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
		for j in points_en:
			if i in points_en[j]:
				count += j  
else:
       for j in points_ru:
	        if i in points_ru[j]:
                 count += j  
	
print(count)'''

	




'''import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
text = input().upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))'''