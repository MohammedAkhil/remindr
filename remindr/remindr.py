#!/usr/bin/env python3
__version__ = "0.1.1"

import os
import click
import parsedatetime
from datetime import datetime
from tinydb import TinyDB, Query
import uuid
import json
from time import sleep
from crontab import CronTab


db = TinyDB('./tasks.json')
Tasks = Query()
cron = CronTab(user=True)


def notify(name):
    apple_cmd = "osascript -e '{0}'"
    base_cmd = 'display notification "{0}" with title "{1}"'.format(
        name, "Reminder")

    # os.system(apple_cmd.format(base_cmd))
    return apple_cmd.format(base_cmd)


def addCron(query, match):
    cmd = notify(query)
    job = cron.new(command=cmd)
    job.setall(match)
    cron.write()
    tab = CronTab()


def getTask(id):
    task = {}
    for dbTask in db:
        if dbTask['id'] == id:
            task = dbTask
    return task


@click.group()
def main():
    """
    Simple CLI for tasks
    """
    pass


@main.command()
@click.option('--list', is_flag=True, help='list all tasks')
def list(list):
    for task in db.all():
        click.echo("{}      {}".format(task['id'], task['time']))


@main.command()
@click.argument('query')
def add(query):
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(query)
    match = datetime(*time_struct[:6])
    db.insert({"id": str(uuid.uuid1()), "name": query, "time": str(match)})
    click.echo(click.style("Task added -", fg="green") +
               "    {}".format(query))
    addCron(query, match)


@main.command()
@click.argument('id')
def remove(id):
    db.remove(Tasks.id == id)
    click.echo("{}".format('remove %s' % id))


@main.command()
@click.argument('id')
def get(id):
    task = getTask(id)
    click.echo("{}".format(task))
