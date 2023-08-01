import random


def Battle(player, enemy):
  while True:
    if player.GetHp() <= 0:
      print("Voce perdeu!")
      break
    elif enemy.GetHp() <= 0:
      print("Voce venceu")
      break

    print(f"{enemy.name}: {enemy.GetHp()}/{enemy.maxhp}")
    print()
    print(f"Player: {player.GetHp()}/{player.maxhp}")
    print()
    print("1 - Attack")
    print("2 - Heal")
    print("3 - Run")
    print()

    question = int(input())

    if question == 1:
      Attack(player, enemy)
    elif question == 2:
      Heal(player)
    elif question == 3:
      if Run() == 1:
        print("Player got awat safely")
        break
      else:
        print("Failed to get away")
    else:
      pass


def Attack(player, enemy):
  enemy.TakeDamage(player.GetAtk())
  if enemy.GetHp() <= 0:
    return 0
  player.TakeDamage(enemy.GetAtk())
  return 1


def Heal(player):
  player.SetHp(player.ConsumeItem())


def Run():
  number = random.randint(1, 100)
  if number <= 70:
    return 1
