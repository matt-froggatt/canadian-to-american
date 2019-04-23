
class Translator:

    def __init__(self, file):
        self.file = file
    
    def display(self):
        for line in self.file:
            print(line)