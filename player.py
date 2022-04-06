#reset self.current_gesture after each turn...
class Player:
   def __init__(self, name):
      self.name = name
      self.score = 0
      self.gestures = ["Rock","Paper","Scissors","Lizard","Spock"]
      self.current_gesture = None
        
   def choose_gesture(self):
      for gesture in self.gestures:
         print(f'{self.gestures.index(gesture)}: {gesture}')

      user_input = input('Choose a gesture by number :')
      #;need to check if the user enters a letter...
      for gesture in self.gestures:
         index = self.gestures.index(gesture)
         if int(user_input) == index:
            self.current_gesture = self.gestures[int(user_input)]
            print(f"You chose {self.gestures[int(user_input)]}")
            break
      if self.current_gesture == None:
         print("That is not a valid repsonse.")
         self.choose_gesture()
       