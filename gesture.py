class Gesture:
    def __init__(self, name) -> None:
        self.name = name
        self.verb = None

    def determine_verb(self, opponents_gesture):
        if self.name == 'Rock' and opponents_gesture in ['Scissors','Lizard']:
           self.verb = 'crushes'
        elif self.name == 'Paper':
            if opponents_gesture == 'Rock':
                self.verb = 'covers'
            elif opponents_gesture == 'Spock':
                self.verb = 'disproves'
        elif self.name == 'Scissors':
            if opponents_gesture == 'Paper':
                self.verb = 'cuts'
            elif opponents_gesture == 'Lizard':
                self.verb = 'decapitates'
        elif self.name == 'Lizard':
            if opponents_gesture == 'Spock':
                self.verb = 'poisons'
            elif opponents_gesture == 'Paper':
                self.verb = 'eats'
        elif self.name == 'Spock':
            if opponents_gesture == 'Rock':
                self.verb = 'vaporizes'
            elif opponents_gesture == 'Scissors':
                self.verb = 'smashes'
        else:
            self.verb = None
