import click
import translator
import os

# Denotes the upcoming method as a command, and it is what gets called when the user runs the command (catoam)
@click.command()
# Sets the option -o or --output-file to take in text to parameter output_location and gives a help message
@click.option("-o", "--output-file", "output_location", default=None, help="Set the output file.")
# Sets an argument for the command, and outputs it to the parameter filename
@click.argument("filename")
# Where the magic happens. Called when the command is run, and uses the parameters from the arguments and options to translate.
def translate(filename, output_location):
    click.echo("Translating %s" % os.path.abspath(filename))

    # Loads file's text as string filedata
    with open(filename, "r") as file:
            filedata = file.read()

    # Creates the the translator, translates the file, and stores the translation as a string
    file_translator = translator.Translator()
    translated_filedata = file_translator.translate(filedata)

    # Sets output file location based on whether output_location is None, and outputs translation
    output_file = output_location if output_location is not None else filename
    click.echo("Translating to %s" % os.path.abspath(output_file))
    with open(output_file, "w") as file:
        file.write(translated_filedata)

    click.echo("Translation complete.")
