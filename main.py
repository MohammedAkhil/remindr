#!/usr/bin/env python3

import click
import parsedatetime
from datetime import datetime


@click.group()
def main():
    """
    Simple CLI for querying books on Google Books by Oyetoke Toby
    """
    pass


@main.command()
@click.argument('query')
def add(query):
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(query)
    match = datetime(*time_struct[:6])
    click.echo("{}".format(match))


@main.command()
@click.argument('id')
def remove(id):
    click.echo("{}".format('remove %s' % id))


if __name__ == "__main__":
    main()
