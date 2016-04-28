#!/usr/bin/env python
import os
import sys
import logging
from base import AbstractProductAPI


def execute():
    args = sys.argv
    if len(args) == 2:
        try:
            with open(os.path.expanduser('~') + "/.speedycfg", "r") as cfg:
                key1 = cfg.readline().strip().replace(" ", "").split("=")
                key2 = cfg.readline().strip().replace(" ", "").split("=")
                if key1[0] == "ACCESS_KEY":
                    access_key = key1[1]
                    secret_key = key2[1]
                else:
                    access_key = key2[1]
                    secret_key = key1[1]
                api = AbstractProductAPI(access_key, secret_key)
                res = api.get("/api/v1/censor", {"url": sys.argv[1]})
                print res
        except Exception, e:
            logging.exception(e)
            print None
    else:
        print "please input the url of an image"

if __name__ == "__main__":
    execute()
