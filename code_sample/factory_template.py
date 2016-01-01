class Player:
	name = ''
	job = ''
	health = 0
	attack = 0
	speed = 0
	# Setters
	def set_name(self, n):
		self.name = n
	def set_health(self, h):
		self.health = h
	# Getters
	def get_name(self):
		return self.name
	def get_job(self):
		return self.job
	def get_health(self):
		return self.health
	def get_attack(self):
		return self.attack
	def get_speed(self):
		return self.speed

class Warrior(Player):
	job = 'Warrior'
	health = 10
	attack = 6
	speed = 4

class Rogue(Player):
	job = 'Rogue'
	health = 8
	attack = 8
	speed = 10

class Magician(Player):
	job = 'Magician'
	health = 6
	attack = 10
	speed = 8

class OnePunch(Player):
	job = 'One Punch Man'
	health = 999999
	attack = 999999
	speed = 999999

player_objects = {'warrior':Warrior, 'rogue':Rogue, 'magician':Magician, 'onepunch':OnePunch}
enemy_objects = {'warrior':Warrior, 'rogue':Rogue, 'magician':Magician}

class PlayerFactory():
	def create_player(self, type):
		return player_objects[type]()

if __name__ == "__main__":

	p_factory = PlayerFactory()

	for p in player_objects.keys():
		print(p_factory.create_player(p).get_job())
		print(p_factory.create_player(p).get_health())