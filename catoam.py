import click
import translator

@click.command()
@click.argument("filename")
def translate(filename):
    file = open(filename, "r")
    click.echo("Working: %s" %filename)
    thing = translator.Translator(file)
    thing.translate()
    thing.display_translations()
