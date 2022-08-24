#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack. """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    ftgz = "versions/web_static_" + dt + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + ftgz + " web_static")
    if not os.path.exists(ftgz):
        return None
    else:
        return ftgz
