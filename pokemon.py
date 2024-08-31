class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry= entry
    self.name= name
    self.types= types
    self.description= description
    self.is_caught= is_caught

  def speak(self):
    print(self.name + " " + self.name + "!")
  
  def display_details(self):
    print("Entry Number: " + str(self.entry))
    print("Name: "+ self.name)
    print("Type: "+ self.types)
    print("Description: " + self.description)
    if self.is_caught:
      print(self.name + "has already been caught! \n")
    else:
      print(self.name+ "is yet to be caught! \n")

pika= Pokemon(25,'Pikachu','Electric','It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charm= Pokemon(2,'Charmander','Fire','The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly.', False)
butter= Pokemon(10, 'Butter-free', 'Bug','It loves the nectar of flowers and can locate flower patches that have even tiny amounts of pollen.', True)

pika.speak()
pika.display_details()

print("-------")

charm.speak()
charm.display_details()

print("-------")

butter.speak()
butter.display_details()

print("-------")