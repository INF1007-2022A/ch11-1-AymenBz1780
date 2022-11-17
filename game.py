"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.
	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, nom, niveau, niveau_min):
		self.__nom = nom
		self.niveau = niveau
		self.niveau_min = niveau_min

	@property
	def nom(self):
		return self.__nom


arm = Weapon('Aymen', 10, 10)
print(arm.nom, arm.niveau, arm.niveau_min)
	# UNARMED_POWER = 20


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, nom, max_hp, attack, defense, level):
		self.__nom = nom
		self.__max_hp = max_hp
		self.__attack = attack
		self.__defense = defense
		self.__level = level
		self.__weapon = None
		self.__hp = max_hp

	@property
	def nom(self):
		return self.__nom

	@property
	def hp(self):
		return self.__hp
	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, val):
		self.__weapon = val

	@hp.setter
	def hp(self, val):
		if val < 0:
			self.__hp = 0
		elif val > self.__max_hp:
			self.__hp = self.__max_hp
		else:
			self.__hp = val

	def __isub__(self, value):
		self.__hp -= value
	def compute_damage(self, d):
		crit = random.random() <= 1/16
		modifier = (crit + 1)*random.uniform(0.85, 1)
		dmg = ((2*self.__level/5 + 2) * self.__weapon.niveau * self.__attack / self.__defense + 2) * modifier/50
		return dmg, crit

x = Character('Aymen', 1000, 20, 20, 10)
x.weapon = Weapon('x', 10, 10)
y = Character('Aymen', 1000, 20, 20, 10)
y.weapon = Weapon('x', 10, 10)

dmg, crit = x.compute_damage(y)
print(dmg, crit)
def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	dmg, crit = c1.compute_damage(c2)
	print(f"{c2.nom} used {c2.weapon} \n \t {c1.nom} took {int(dmg)} dmg")
	return dmg, crit


c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)

deal_damage(c1, c2)

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	tour = 0

	while (c2.hp != 0):
		deal_damage(c1, c2)
		c1, c2 = c2, c1
		#c2.hp = c2.hp - dmg
		c2.hp -= dmg
		tour += 1

	print(f"{c2.nom} is sleeping with the fishes.")
	print(f" The battle ended in {tour} turns. ")

c1 = Character("Äpik", 200, 150, 70, 70)
c2 = Character("Gämmor", 250, 100, 120, 60)

c1.weapon = Weapon("BFG", 100, 69)
c2.weapon = Weapon("Deku Stick", 120, 1)
run_battle(c1, c2)

#local lundi A-416