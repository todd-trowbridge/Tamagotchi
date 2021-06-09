from pet import Pet

pet_name = input("Name your pet: ")

pet = Pet(pet_name)

while True:
  print(pet.get_status())
  print("""
1. Feed Pet
2. Play with Pet
3. Do Nothing""")
  choice = int(input(': '))
  if choice == 1:
    # feed the pet
    pet.eat_food()
  elif choice == 2:
    # play with pet
    pet.get_love()
  
  # each time the loop runs, reduce the pet stats
  pet.be_alive()