#wangbin
import os
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import pprint
import hashlib 
from upUtil import Get

def get_geo_info(geo_group_name):
    asset_type=cmds.getAttr(geo_group_name+".AssetCatagory")
    asset_name=cmds.getAttr(geo_group_name+".AssetName")
    return asset_type,asset_name
def get_all_info():
    all_info={}
    trans = [x for x in cmds.ls(type="transform",dag=True) if x not in ['persp','top','front','side']]
    for tran in trans:
        each_infp={}
        if cmds.listRelatives(tran,children=True):
            for tranchild in cmds.listRelatives(tran,children=True,f=True):
                if cmds.attributeQuery('UniPipeGeometryGrp', n=tranchild, exists=1):
                    master=tran
                    word_xform=cmds.xform(tranchild,ws=True,q=True,m=True)
                    asset_type,asset_name=get_geo_info(tranchild)
                    group_name=cmds.listRelatives(cmds.listRelatives(tranchild,p=True),p=True)
                    each_infp["word_xform"]=word_xform
                    each_infp["asset_type"]=asset_type
                    each_infp["asset_name"]=asset_name
                    each_infp["group_name"]=group_name
                    all_info[master]=each_infp
    return all_info
def get_asset_info(asset_name,asset_type,step,Variant="default"):
    asset_info={}
    asset_type=Get.Get().CataName(asset_type,long=1)
    s_name=Get.Get().CataName(asset_type,long=0)
    ServerPath=Get.Get().Get_ServerPath()
    ActiveProject=Get.Get().Get_ActiveProject()
    asset_folder=os.path.join(ServerPath,ActiveProject,"_Assets",asset_type,asset_name,step,Variant,"Main")
    if os.path.exists(asset_folder):
        asset_abc_path=os.path.join(asset_folder,s_name+"_"+asset_name+"_abc.abc")
        asset_ad_path=os.path.join(asset_folder,s_name+"_"+asset_name+"_AD.ma")
        if os.path.exists(asset_abc_path):asset_info["asset_abc_path"]=asset_abc_path
        if os.path.exists(asset_ad_path):asset_info["asset_ad_path"]=asset_ad_path
    return asset_info
def cret_ar_Reference():
    all_info=get_all_info()
    for key in all_info:
        asset_name=all_info[key]["asset_name"]
        asset_type=all_info[key]["asset_type"]
        group_name=all_info[key]["group_name"]
        step="Model"
        ar_xform=all_info[key]["word_xform"]
        asset_info=get_asset_info(asset_name,asset_type,step)
        ad_path=asset_info.get("asset_ad_path","")
        if ad_path:
            ad_asset_name=os.path.splitext(os.path.basename(ad_path))[0]
            new_ad_name=cmds.assembly(name=ad_asset_name+"_AR", type='assemblyReference')
            cmds.parent(new_ad_name,group_name)
            cmds.setAttr(new_ad_name+".definition",ad_path,type="string")
            #cmds.setAttr(ad_asset_name+"_AR"+".repNamespace","sdsd",type="string")
            mel.eval('AEassemblyChangeAttrNamespace "%s.repNamespace""%s";'%(new_ad_name,new_ad_name))
            cmds.xform(new_ad_name,ws=True,m=ar_xform)
cret_ar_Reference()
