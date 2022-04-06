#reset self.current_gesture after each turn...
class Player:
   def __init__(self, name):
      self.name = name
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

   # getting used twice, so i made this function 
   def choose_something(self, list, category):
      for item in list:
         print(f'{list.index(item)}: {item}')

      while True:
         try:
            user_input = int(input(f'{self.name}, enter a number to choose your {category} :'))
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
