import json
import re

# Simple class that I use to translate documents easily. Probably doesn't need to be an object, but its more fun this way.
class Translator:

    # The constructor, loads the file's text into a string and loads the translations JSON file which I use to store all the different translations Since the
    #   translations are stored as a JSON, they are loaded into Python as a dictionary, and while that is useful in this circumstance, it is only useful assuming
    #   that every word has a one to one translation. Also, the storage method is not exactly memory efficient, but it only needs to store text, and modern
    #   computers should have more than enough memory.
    def __init__(self):
        with open('translations.json') as f:
            self.translations = json.load(f)

    # Translates the contents of the original file using Python's regex system, and returns translated content.
    def translate(self, filedata):
        for key in self.translations:
            regex = re.compile(re.escape(key), re.IGNORECASE)
            filedata = regex.sub(self.translations[key], filedata)
        return filedata


    # Shows all of the implemented translations. It isn't part of the CLI but it is a useful debugging tool.
    def display_translations(self):
        for key in self.translations:
            print(key, self.translations[key])

