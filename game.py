from player import Player
from items import Items
from combat import Battle
from enemies import Enemies 


def main():
  player = Player()
  potion1 = Items.HealingPotion()
  bear1 = Enemies.Bear()

  print("Voce conseguiu uma pocao no bau")
  player.AddItem(potion1)

  Battle(player, bear1)
