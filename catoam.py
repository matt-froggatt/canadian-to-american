import click
import translator

@click.command()
@click.argument("filename")
def translate(filename):
    file = open(filename, "r")
    click.echo("Working: %s" %filename)
    for word in file:
        click.echo(translator.translate(word))
