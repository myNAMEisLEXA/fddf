from book_1 import d as d1
from book_2 import d as d2
from book_3 import i as d3
from book_4 import d as d4
from book_5 import d as d5
from book_6 import d as d6
from book_7 import d as d7
from book_8 import d as d8
from book_9 import d as d9
from book_10 import d as d10
from book_11 import d as d11
from book_12 import d as d12
from book_13 import d as d13

import random
import time


d = {}
d.update(d1)
d.update(d2)
d.update(d3)
d.update(d4)
d.update(d5)
d.update(d6)
d.update(d7)
d.update(d8)
d.update(d9)
d.update(d10)
d.update(d11)
d.update(d12)
d.update(d13)
start_table = {
	2: (8, 22, 8),
    3: (10, 20, 6),
 	4: (12, 16, 5),
    5: (9, 18, 8),
    6: (11, 20, 6),
    7: (9, 20, 7),
    8: (10, 16, 7),
    9: (8, 24, 7),
    10: (9, 22, 6),
    11: (10, 18, 7),
    12: (11, 20, 5)
}


class player:
	lov = 0
	sil = 0
	obon = 0
	max_lov = 0
	max_sil = 0
	max_obon = 0
	inventory = {}


	def add_sila(self,number):
		self.sil = min(self.sil+int(number),self.max_sil)

	def add_lov(self,number):
		self.lov = min(self.lov+int(number),self.max_lov)

	def add_oban(self,number):
		self.obon = min(self.obon+int(number),self.max_obon)



	#принимает кортеж (name,effect)
	def add_to_inv(self,item):
		if (len(self.inventory)>=7):
			return ("Инвентарь переполнен")
		else:
			self.inventory[item[0]] = item[1]
			return (item[0] + " успешно добавлен")

	def __init__(self):
		print("Приступаем к созданию персонажа...")
		self.lov, self.sil, self.obon = start_table[random.randrange(2, 12)]
		print("ВАШИ ХАРАКТЕРИСТИКИ: ЛОВКОСТЬ - %d,СИЛА - %d, ХАРИЗМА - %d " % (self.lov, self.sil, self.obon))
		self.max_lov, self.max_sil, self.max_obon = self.lov, self.sil, self.obon

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

dices = {
		1:'\u2680',
		2:'\u2681',
		3:'\u2682',
		4:'\u2683',
		5:'\u2684',
		6:'\u2685'
}


def roll_dice():
	num = random.randrange(1,6)
	return(str(dices[num]) + " Выпадает " + str(num))



class game:
	playa = player()
	curr_room = 1
	notes = []

	inputs = {
		'!stats': ("ЛОВКОСТЬ - %s,СИЛА - %s, ХАРИЗМА - %s "),
		'!level': ("ТЕКУЩИЙ УРОВЕНЬ - %s"),
		'!rules': (d[0]['text']),
		'!roll' : '',
		'!add_inv' : '',
		'!inv' : 'ТЕКУЩИЙ ИНВЕНТАРЬ: ',
		'!add_note': '',
		'!notes':'',
		'!use_item':'',
		'!change_sila': '' , 
		'!change_lov': '' ,
		'!change_oban': '' ,
		'!help':''
	}

	def add_note(self,_input):
		self.notes.append(time.ctime()[11:]+" "+_input)
		return ("Запись добавлена")


	def get_ready(self,_input):
		if (_input=='!stats'):
			return (self.inputs[_input] % (self.playa.lov, self.playa.sil, self.playa.obon))
		elif (_input=='!level'):
			return (self.inputs[_input] % (self.curr_room))
		elif (_input == '!rules'):
			return self.inputs[_input]
		elif (_input == '!roll'):
			return str(roll_dice())
		elif (_input == '!add_inv'):
			name = input("Введите название:")
			effect = input("Введите эффект:")
			while (not (is_number(effect))):
				if ("СИЛА" in effect):
					if (is_number((effect.split())[0])):
						is_number((effect.split())[0])
						break
				effect = input("Введите эффект:")
			return self.playa.add_to_inv((name,effect))
		elif (_input == '!inv'):
			answ = self.inputs[_input]
			for item in self.playa.inventory :
				answ = answ + item
			return(answ)
		elif (_input == '!add_note'):
			note = input("Запись для добавления:")
			return(self.add_note(note))
		elif (_input == '!notes'):
			answ = ""
			for note in self.notes:
				answ = answ +  note + " \n"
			return answ
		elif (_input == '!use_item'):
			item_name = input("Введите название предмета: ")
			self.use_item(self.get_item(item_name))
		elif (_input == '!change_sila'):
			number = input("Введите значение")
			while (not(is_number(number))):
				number = input("Введите значение")
			self.playa.add_sila(number)
			print("Cила изменена на %s" % number) 
		elif (_input == '!change_lov'):
			number = input("Введите значение")
			while (not(is_number(number))):
				number = input("Введите значение")
			self.playa.add_lov(number)
			print("Ловкость изменена на %s" % number)
		elif (_input == '!change_oban'):
			number = input("Введите значение")
			while (not(is_number(number))):
				number = input("Введите значение")
			self.playa.add_oban(number)
			print("Обаяние изменено на %s" % number)  
		elif (_input == '!help'):
			answ = ''
			for com in self.inputs:
				print (com)


	def remove_item

	def get_item(self,item_name):
		if (item_name in self.playa.inventory):
			return ((item_name,self.playa.inventory[item_name]))


	def use_item(self,item):
		if (item==None):
			print("У вас нет такого предмета!")
		else:
			print(item)
			if ("СИЛА" in item[1]):
				self.playa.add_sila(int(item[1].split()[0]))
				del(self.playa.inventory[item[0]])
				print("Предмет успешно использован")
			else:	
				self.change_level(self.curr_room+int(item[1]))
				del(self.playa.inventory[item[0]])
				print("Предмет успешно использован")



	def change_level(self,where_to):
		self.curr_room = where_to
		if (where_to in d):
			print(d[self.curr_room]['text'])
		else:
			self.curr_room = str(self.curr_room)
			print(d[str(self.curr_room)]['text'])	

	def __init__ (self):
		print(d[1]['text'])
		while (d[self.curr_room]['goto']!=[1] and self.playa.sil>0) :
			_input = input("Ваши действия:")
			if (is_number(_input)):
				if (int(_input) in d[self.curr_room]['goto']):
					self.change_level(int(_input))
			else :
				if (_input in self.inputs):
					print(self.get_ready(_input))
		print("Вы умерли! Не повезло")
game()		
