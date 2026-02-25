import random
class Quiz:
    def __init__(self,question,options):
        self.question = question
        self.options = options
        random.shuffle(self.options)
    def __str__(self):
        return self.question + \
        f'1){self.options[0]}' + \
        f'2){self.options[1]}' + \
        f'3){self.options[2]}' + \
        f'4){self.options[3]}'





