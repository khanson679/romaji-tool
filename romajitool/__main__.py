# import sys
import click

from .common import convert, FORMATS


@click.command()
@click.option('--from', '-f', 'in_fmt', default="hiragana",
              type=click.Choice([k for k in FORMATS], case_sensitive=False))
@click.option('--to', '-t', 'out_fmt', required=True,
              type=click.Choice([k for k in FORMATS], case_sensitive=False))
@click.argument('text')
def cli(in_fmt, out_fmt, text):
    print(convert(text, in_fmt, out_fmt))


if __name__ == '__main__':
    cli()
