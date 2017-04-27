# -*- coding:utf-8 -*-

############################################
#by wangbin
############################################

import traceback

import re

class master_check():

    def __init__(self):
        self.check_name = u"这是check的名字。"
        self.description = u"这是一个描述 "
        self.auto_fix = False
        return
    def do_check(self):
        try:
            print "do check....."
            return ""
        except:
            return traceback.format_exc()


    def do_fix(self):
        "auto fix"
        return


    def get_check_name(self):
        return self.check_name

    def get_description(self):
        return self.description


    def get_auto_fix(self):
        return self.auto_fix
