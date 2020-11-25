# Implement a class to hold room information. This should have name and
# # description attributes.
# * Put the Room class in `room.py` based on what you see in `adv.py`.

#   * The room should have `name` and `description` attributes.

#   * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
#     which point to the room in that respective direction.
class Room:
  def __init__(self, name, description, items = []):
    self.name = name
    self.description = description
    self.items = items
    n_to = None
    s_to = None
    e_to = None
    w_to = None
  def __repr__(self):
    return f'{self.items}'
  def add(self, item):
    self.items.append(item)
  def steal(self, item):
    self.items.remove(item)