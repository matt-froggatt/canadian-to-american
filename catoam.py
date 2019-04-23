import click
import translator
import os

@click.command()
@click.option("-o", "--output-file", "output_file", default=None, help="Set the output file.")
@click.argument("filename")
def translate(filename, output_file):
    click.echo("Working: %s" % os.path.abspath(filename))
    file_translator = translator.Translator(filename)
    file_translator.translate()
    file_translator.write_to_file(output_file)
    print("Translation complete.")
