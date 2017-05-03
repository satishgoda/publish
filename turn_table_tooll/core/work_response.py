#!/usr/bin/python
#-*- coding=utf-8 -*-
# Author: wangbin
import os
import maya.cmds as cmds
import sys
#sys.path.append("..")
from turn_table_tooll.ui.head import *
#from ui.head import *
from turn_table_tooll.env.Config import Config


def get_template_info():
    template_floder_path=Config.TEMPLATEPATH
    template_step = Config.TEMPLATESTEP
    template_name = Config.TEMPLATENAME

    template_morning_path=Config.TEMPLATEPATHMORNING
    template_noon_path=Config.TEMPLATEPATHNOON
    template_night_path=Config.TEMPLATEPATHMNIGHT
    template_nightfall_path=Config.TEMPLATEPATHMNIGHTFALL
    # template_file_path=os.path.join(template_floder_path,template_step,template_name,"turn_table_template.ma")
    # color_card_file_path = os.path.join(template_floder_path, template_step, template_name, "color_card.exr")
    # morning_hdr_file_path = os.path.join(template_floder_path, template_step, template_name, "morning.hdr")
    # night_hdr_file_path = os.path.join(template_floder_path, template_step, template_name, "night.hdr")
    # nightfall_hdr_file_path = os.path.join(template_floder_path, template_step, template_name, "nightfall.hdr")
    # noon_hdr_file_path = os.path.join(template_floder_path, template_step, template_name, "noon.hdr")
    # return template_file_path,\
    #        color_card_file_path,\
    #        morning_hdr_file_path,\
    #        night_hdr_file_path,\
    #        nightfall_hdr_file_path,\
    #        noon_hdr_file_path
    return template_morning_path,template_noon_path,template_night_path,template_nightfall_path

def import_turntable_template(time_mod=""):
    template_morning_path,\
    template_noon_path,\
    template_night_path,\
    template_nightfall_path\
        =get_template_info()
    if time_mod:
        #template_color_file, template_time_file=get_template_node_info(template_file_path)
        #set_file_path_tonode(template_color_file, color_card_file_path)
        if "morning" == time_mod:
            #set_file_path_tonode(template_time_file, morning_hdr_file_path)
            import_templatefile(template_morning_path)
        if "night" == time_mod:
            import_templatefile(template_night_path)
            #set_file_path_tonode(template_time_file, night_hdr_file_path)
        if "nightfall" == time_mod:
            #print template_nightfall_path
            import_templatefile(template_nightfall_path)
            #set_file_path_tonode(template_time_file, nightfall_hdr_file_path)
        if "noon" == time_mod:
            import_templatefile(template_noon_path)
            #set_file_path_tonode(template_time_file, noon_hdr_file_path)
def import_templatefile(template_file_path):
    print "zhixing le e yi ge ",template_file_path
    cmds.file(template_file_path, i=True)
def set_file_path_tonode(nodename="",file_path=""):
    cmds.setAttr(nodename+".fileTextureName", file_path, type="string")

def get_template_file_node():
    template_color_file = ""
    template_time_file = ""
    allfile = cmds.ls(typ="file")
    allfileitem = "template_color_file"
    if allfile:
        for allfileitem in allfile:
            if "template_color_file" in allfileitem and cmds.attributeQuery('istemplate', n=allfileitem, exists=1):
                template_color_file = allfileitem
            if "template_time_file" in allfileitem and cmds.attributeQuery('istemplate', n=allfileitem, exists=1):
                template_time_file = allfileitem
        return template_color_file, template_time_file


def get_template_node_info(template_file_path):
    check_template = False
    all_transform = cmds.ls(typ="transform")
    for i in all_transform:
        if cmds.attributeQuery('istemplate', n=i, exists=1):
            check_template = True
    if not check_template:
        cmds.file(template_file_path, i=True)
    template_color_file, template_time_file = get_template_file_node()
    return template_color_file, template_time_file

