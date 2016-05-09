#!/usr/bin/env python
import argparse
import copy
import importlib
import logging
import os
import sys

from products.base import AbstractProductAPI


def execute():
    if len(sys.argv) < 2:
        print "command error"
        return
    sys.argv[0] = sys.argv[0].split('/')[-1]
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
            if sys.argv[0].split('/')[-1] == "censor":
                api = AbstractProductAPI(access_key, secret_key)
                print api.get("/api/v1/censor", {"url": sys.argv[1]})
                return
            parser = argparse.ArgumentParser()
            ret = ['-module', sys.argv[0], '-method', sys.argv[1]]
            args = ret + sys.argv[2:]
            for arg in args:
                if arg.startswith("-"):
                    parser.add_argument(arg)
            params = parser.parse_args(args).__dict__
            filenames = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/products')
            for filename in filenames:
                if params['module'] in filename and not filename.endswith('c'):
                    module = importlib.import_module('speedycmd.products.' + filename[:-3])
                    class_name = ''
                    parts = filename[:-3].split('_')
                    for part in parts:
                        class_name += part.capitalize()
                    class_name += "API"
                    api = getattr(module, class_name)(access_key, secret_key)
                    kwargs = copy.deepcopy(params)
                    del kwargs['module']
                    del kwargs['method']
                    print getattr(api, params['method'])(**kwargs)
                    return
    except Exception, e:
        logging.exception(e)
        print None


if __name__ == "__main__":
    execute()
