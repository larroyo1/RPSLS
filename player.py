#reset self.current_gesture after each turn...
class Player:
   def __init__(self):
      self.name = None
      self.score = 0
      self.gestures = ["Rock","Paper","Scissors","Lizard","Spock"]
      self.current_gesture = None
      self.characters = ['Sheldon','Leonard','Penny','Amy Farrah Fowler','Bernadette','Wolowitz']
        
   def choose_gesture(self):
      user_input = self.choose_something(self.gestures, "gesture")
      if user_input <= len(self.gestures) - 1:
         self.current_gesture = self.gestures[int(user_input)]
      else:
         print("That is not a valid repsonse.")
         self.choose_gesture()

   
   def choose_something(self, list, category):
      for item in list:
         print(f'{list.index(item)}: {item}')

      while True:
         try:
            user_input = int(input(f'Enter a number to choose your {category} :'))
            break
         except ValueError:
            print("That is not a valid repsonse.")
            continue
      return user_input

   def choose_character(self):
      user_input = self.choose_something(self.characters, "character")
      if user_input <= len(self.characters) - 1:
         self.name = self.characters[int(user_input)]
      else:
         print("That is not a valid repsonse.")
         self.choose_character()
