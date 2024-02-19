#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric import task
import time

@task
def do_pack(c):
    """Generate a .tgz archive from the web_static folder."""
    try:
        c.run("mkdir -p versions")
        current_time = time.strftime("%Y%m%d%H%M%S")
        c.run("tar -cvzf versions/web_static_{}.tgz web_static/".format(current_time))
        return "versions/web_static_{}.tgz".format(current_time)
    except Exception as e:
        print("An error occurred:", e)
        return None
