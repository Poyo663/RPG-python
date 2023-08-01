class Ienemies:

  def __init__(self):
    self.name = self.name
    self.maxhp = self.maxhp
    self.hp = self.hp
    self.atk = self.atk

  def GetHp(self):
    return self.hp

  def GetAtk(self):
    return self.atk

  def TakeDamage(self, damage):
    self.hp -= damage

  def SetHp(self, heal):
    self.hp += heal


class Enemies:

  class Bear(Ienemies):

    def __init__(self):
      self.name = "Bear"
      self.maxhp = 100
      self.hp = 100
      self.atk = 20

  class Wolf(Ienemies):

    def __init__(self):
      self.name = "Wolf"
      self.maxhp = 50
      self.hp = 50
      self.atk = 40
