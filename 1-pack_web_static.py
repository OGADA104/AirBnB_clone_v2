#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if generated successfully, None otherwise.
    """
    try:
        # Create the versions directory if it doesn't exist
        c.run("mkdir -p versions")

        # Create the name of the .tgz file with current timestamp
        date_format = "%Y%m%d%H%M%S"
        current_time = datetime.now().strftime(date_format)
        archive_name = "web_static_{}.tgz".format(current_time)

        # Compress the web_static folder into the .tgz file
        c.run("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if generated successfully
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("An error occurred:", e)
        return None
