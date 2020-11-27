# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room, items = []):
    self.name = name
    self.current_room = current_room
    self.items = items

  def __repr__(self):
    return f"{self.items}"
    #str is intended to be human readable
    #repr is explicit for development

  def pickup(self, item):
    self.items.append(item)

  def drop(self, item):
    self.items.remove(item)