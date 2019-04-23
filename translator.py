import json
import re

class Translator:

    def __init__(self, file):
        self.file = file
        with open('translation.json') as f:
            self.translations = json.load(f)
    
    def display(self):
        for line in self.file:
            print(line, end='')
        print("\n")

    def translate(self):
        for key in self.translations:
            regex = re.compile(re.escape(key), re.IGNORECASE)
            for line in self.file:
                line = regex.sub(self.translations[key], line)
                print(line, end="")
            self.file.seek(0)
        print("\n\n")

    def display_translations(self):
        for key in self.translations:
            print(key, self.translations[key])
