import json
import re

# Simple class that I use to translate documents easily. Probably doesn't need to be an object, but its more fun this way.
class Translator:


    # The constructor, just initializes variables, loads the file's text into a string (maybe not the best idea, I'll fix it if needed, but no file should exceed
    #   the size of memory in most modern computers), and loads the translations JSON file which I use to store all the different translations

    # Note: since the translations are stored as a JSON, they are loaded into Python as a dictionary, and while that is useful in this circumstance, it is only useful
    #   assuming that every word has a one to one translation.
    def __init__(self, filename, output):
        self.filename = filename
        self.output = output

        with open(self.filename, "r") as file:
            self.filedata = file.read()

        with open('translations.json') as f:
            self.translations = json.load(f)
    

    # Just prints out the contents of the input file. It isn't actually part of the CLI, its just a useful debugging tool
    def display(self):
        print(self.filedata)


    # Translates the contents of the original file in place using Python's regex system. DOES NOT MODIFY THE ACTUAL FILE, OR PRODUCE OUTPUT. This just runs a simple for loop
    #   through every possible translatable value, and replaces them with their translations. There might be a faster way to do it, but I feel like in this case mental 
    #   efficieny is more important than time efficiency.
    def translate(self):
        for key in self.translations:
            regex = re.compile(re.escape(key), re.IGNORECASE)
            self.filedata = regex.sub(self.translations[key], self.filedata)


    # Shows all of the implemented translations. Again, it isn't par of the CLI but it is a useful debugging tool.
    def display_translations(self):
        for key in self.translations:
            print(key, self.translations[key])


    # Takes the freshly translated file content and writes it out to a file. It takes in an output location, but only uses it if its not set to None. I use None to indicate
    #   that the user hasn't set their output location (using -o) and so it will just overwrite the initial file with the translation.
    def write_to_file(self):
        with open(self.output, "w") as file:
            file.write(self.filedata)
