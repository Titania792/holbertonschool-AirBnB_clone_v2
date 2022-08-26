#!/usr/bin/python3
""" Fabric script """
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['54.89.74.48', '54.227.178.59']


def do_deploy(archive_path):
    """distributes an archive to our web servers"""
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
