#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack. """
from fabric.api import local, run, env, put
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['54.89.74.48', '54.227.178.59']


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


def do_deploy(archive_path):
    """ distributes an archive to our web servers """
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        fn = archive_path.split("/")[1]
        fn_ext = fn.split(".")[0]
        fpath = "/data/web_static/releases/" + fn_ext + "/"
        run("mkdir -p " + fpath)
        run("tar -xzf /tmp/" + fn + " -C " + fpath)
        run("mv " + fpath + "web_static/*" + " " + fpath)
        run("rm /tmp/{}".format(fn))
        run("rm -rf " + fpath + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + fpath + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """ creates and distributes an archive to the web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
