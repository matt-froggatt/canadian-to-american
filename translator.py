import json
import re

class Translator:

    def __init__(self, filename):
        self.filename = filename

        with open(self.filename, "r") as file:
            self.filedata = file.read()

        with open('translations.json') as f:
            self.translations = json.load(f)
    
    def display(self):
        print(self.filedata)

    def translate(self):
        for key in self.translations:
            regex = re.compile(re.escape(key), re.IGNORECASE)
            self.filedata = regex.sub(self.translations[key], self.filedata)

    def display_translations(self):
        for key in self.translations:
            print(key, self.translations[key])

    def write_to_file(self, output_location):
        output_file = output_location if output_location is not None else self.filename
        with open(output_file, "w") as file:
            file.write(self.filedata)
