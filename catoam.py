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

    # Sets output file location based on whether output_location is None
    output_file = output_location if output_location is not None else filename
    click.echo("Translating to %s" % os.path.abspath(output_file))

    # Creates the the translator, gives it the required info (current filename, and output location), and translates the file
    file_translator = translator.Translator(filename, output_location)
    file_translator.translate()

    # Writes the translation to the output file
    file_translator.write_to_file()

    click.echo("Translation complete.")
