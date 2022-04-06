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

      while True:
         try:
            user_input = int(input('Choose a gesture by number :'))
         except ValueError:
            print("That is not a valid repsonse.")
            continue
         else:
            if user_input <= len(self.gestures) - 1:
               self.current_gesture = self.gestures[int(user_input)]
            else:
               print("That is not a valid repsonse.")
               self.choose_gesture()
            break
