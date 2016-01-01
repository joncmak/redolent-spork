###
# Maybe make p_factory a global
# Battles are 1 v 1 
# Bugs include instances of the same class that are supposed to be
# seperate are the same
###

from factory_template import *

class BattleInstance:
	def __init__(self, p):
		self.player = p
		self.enemy_stack = []
		for e in enemy_objects.keys():
			self.enemy_stack.append(p_factory.create_player(e))
	def resolve_battle(self):
		for e in self.enemy_stack:
			self.describe_battle(e)
			start, last = self.determine_initiative(e)
			print('%s has initiative over %s' % (start.get_job(), last.get_job()))
			while start.get_health() > 0 and last.get_health() > 0:
				self.resolve_attack(start,last)
				start, last = last, start
			print('%s is dead\n' % start.get_job())

	def describe_battle(self, e):
		print('%s versus %s' % (self.player.get_job(), e.get_job()))
	def determine_initiative(self,e):
		if self.player.get_speed() > e.get_speed():
			return self.player, e
		return e, self.player
	def resolve_attack(self,a,d):
		print('%s attacks %s for %d damage' % (a.get_job(), d.get_job(), a.get_attack()))
		res = d.get_health() - a.get_attack()
		d.set_health(res)
		print('%s has %d health remaining' % (d.get_job(), d.get_health()))

if __name__ == "__main__":
	print('Factory pattern example')
	p_factory = PlayerFactory()

	print('Initialization test')
	for p in player_objects.keys():
		print(p_factory.create_player(p).get_job())
		print('Health is ', p_factory.create_player(p).get_health())
		print('Attack is ', p_factory.create_player(p).get_attack())

	print('Battle test')	
	player = p_factory.create_player('rogue')
	test_battle = BattleInstance(player)
	test_battle.resolve_battle()
