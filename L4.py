#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.
#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18

#6 12

'''N = input('Ввести кол-во элементов первого множества:').split()
M = input('Ввести кол-во элементов второго множества:').split()
result_set = set ()
for s in input().split():
	result_set = set.add(i)
print(len(result_set))'''
	


#for elem in A:
    #print(elem, end=' ')


#k = int(input('Заданное число:'))
#m = abs(k - list1[0])
#number = list1[0] 

#for i in range(1, len(list1)):
#	if m > abs(k - list1[i]):
		#m = abs(k - list1[i])
		#number = list1[i]

#print(number)'''


#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#4 -> 1 2 3 4
#9


n = int( input( 'колличество кустов = ' ) )
lis = [ int(x) for x in input( '-> ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max( ma, lis[i] + lis[i+1] + lis[i+2] )
print(ma)


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

