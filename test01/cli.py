import click
from __future__ import print_function

def hello():
    ''' return a hello world! '''
    return("hello, Mehdi!")

def say_hello():
    ''' print hello world message '''
    print(hello())


@click.command()
def cli():
    click.echo("Hello, World!")

if __name__ == '__main__':
    cli()
