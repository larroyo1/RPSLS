class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = ["Rock","Paper","Scissors","Lizard","Spock"]
        self.current_gesture = ''
        
     def choose_gesture(self):
        for gesture in self.gestures:
           print(f'{self.gestures.index(gesture)}: {gesture}')

        user_input = int(input('Choose a gesture by number.'))
        self.current_gesture = self.gestures[user_input]
       