# author: Spring
import control
import os
import sys
import time

import APIManager.api
from CatalogManager import catalog
from IndexManager import index
from RecordManager import record
from utiles import dbinfo

class miniSQL(cmd.Cmd):
    intro = '''
MiniSQL database server, version 1.0.0-release, (x86_64-apple)
Copyright 2022 @ Spring from ZJU. Course final project for DDBS.
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
    '''
    def do_select(self, args):
        try:
            APIManager.api.select(args.replace(';', ''))
        except Exception as e:
            print(e)

    def do_create(self, args):
        try:
            APIManager.api.create(args.replace(';', ''))
        except Exception as e:
            print(e)

    def do_drop(self, args):
        try:
            APIManager.api.drop(args.replace(';', ''))
        except Exception as e:
            print(e)

    def do_insert(self, args):
        try:
            APIManager.api.insert(args.replace(';', ''))
        except Exception as e:
            print(e)

    def do_delete(self, args):
        try:
            APIManager.api.delete(args.replace(';', ''))
        except Exception as e:
            print(e)

    def do_commit(self, args):
        time_start = time.perf_counter()
        __finalize__()
        time_end = time.perf_counter()
        print('Modifications has been commited to local files,', end='')
        print(" time elapsed : %fs." % (time_end - time_start))

    def do_quit(self, args):
        __finalize__()
        print("bye")
        sys.exit()

    def do_test(self, args):
        index.print_B_plus_tree(dbinfo.table_index[args])

    def do_truncate(self, args):
        try:
            APIManager.api.truncate(args.replace(';', ''))
        except Exception as e:
            print(e)

    def emptyline(self):
        pass

    def default(self, line: str):
        print("Unable to recognize the command %s" % line)
        print("Type `help' to see this list")

    def help_commit(self):
        text = "To reduce file transfer's time, this SQL server is designed to \n"+\
        "'lasy' write changes to local files, which means it will not store changes \n"+\
        "until you type 'quit' to normally exit the server. if this server exit \n"+\
        "unnormally, all changes will be lost. If you want to write changes to \n"+\
        "local files immediately, please use 'commit' command.\n"
        print(text)

    def help_quit(self):
        print('?????????????????????')

    def help_select(self):
        print("********  ??????????????????????????????????????????  ********\n")
        print("SELECT ????????? FROM ????????? WHERE ????????? =(>, <, >=, <=) ??? and(or) ...")

    def help_create(self):
        print("********  ????????????  ********\n")
        print("CREATE INDEX index_name ON table_name (column_name)")
        print()
        print("********   ?????????   ********\n")
        print('''CREATE TABLE ?????????
(
    ?????????1 ????????????(??????int, float, char),
    ?????????2 ????????????,
    ?????????3 ????????????,
    ....
    primary key(),
    unique()
)
        ''')

    def help_drop(self):
        print("********  ????????????  ********\n")
        print("DROP INDEX index_name ON table_name")
        print()
        print("********   ?????????   ********\n")
        print("DROP TABLE table_name")

    def help_insert(self):
        print("********  ????????????  ********\n")
        print("INSERT INTO ????????? VALUES (???1, ???2,....)")

    def help_delete(self):
        print("********  ????????????  ********\n")
        print("DELETE FROM ????????? WHERE ????????? =(>, <, >=, <=) ??? and(or) ...")

def __initialize__():
    pwd = os.getcwd()
    catalog.__initialize__(pwd)
    index.__initialize__()
    record.__initialize__()


def __finalize__():
    pwd = os.getcwd()
    catalog.__finalize__(pwd)
    index.__finalize__()
    record.__finalize__()


if __name__ == '__main__':
    try:
        __initialize__()
        miniSQL.prompt = '>>>'
        miniSQL().cmdloop()
    except Exception as e:
        print(e)


