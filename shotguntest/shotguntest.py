#encoding=utf8
import sys
import os
sys.path.append("D:\pletest\shotgun\python-api")

import shotgun_api3


sg = shotgun_api3.Shotgun("https://liontest.shotgunstudio.com",
                          script_name="wbtest",
                          api_key="b98e4bde3bbc1828e65e6ccb81758992657a5210eeee80d3c4960d28fb7effc7")



filters = [
	['project', 'name_is', "lst"]
]
fields = ["code"]
#res=sg.find("Task",filters,fields)
#print res

# fields = []
# filters = [ ['name', 'is',"lst"]]
# Project = sg.find_one('Project', filters)
# fields = ["code"]
# filters = [ ['project', 'is',Project],
#             ['code', 'is', 'xiaohei'] ]
# asset = sg.find_one('Asset', filters,fields)

#print asset

# fields = ["content"]
# filters = [ ['project', 'name_is',"lst"],
#             ['entity', 'is',{'type':'Asset', 'id': asset['id']}],
#             ['step', 'name_is', 'cfx']]
#task = sg.find_one('Task', filters,fields)
#print task




#print Project


def creat_Asst_new_version(asset_name,task_name,version_name,ple_step,project_name,description,uploaded_movie_path=None,local_path=None,status="ip"):
    filters = [ ['name', 'is',project_name]]
    Project = sg.find_one('Project', filters)
    filters = [ ['project', 'is',Project],
                 ['code', 'is', asset_name] ]
    asset = sg.find_one('Asset', filters)
    task=sg.find("Task",[ ['project', 'is',Project],["content","is",task_name],["step",'name_is',ple_step],['entity','is',asset]])
    data = { 'project': Project,
             'code': version_name,
             'description': description,
             'sg_status_list': status,
             'entity': asset,
             'sg_task': task[0]}
    Version = sg.create('Version', data)
    data = {'sg_localpath':{'local_path': local_path}}
    result = sg.upload("Version",Version['id'],uploaded_movie_path,field_name="sg_uploaded_movie")
    result = sg.update("Version",Version['id'],data)

### Asst_new_version
# asset_name="xiaohei"
# task_name="default"
# version_name="main.v011"
# project_name="LST"
# description="ceshi yige "
# ple_step="cfx"
# uploaded_movie_path="D:\\pletest\\shotgun\\projects\\lst\\assets\\Character\\xiaobai\\model\\pub\\v001\\main.mov"
# local_path="D:\\pletest\\shotgun\\projects\\lst\\assets\\Character\\xiaobai\\model\\pub\\v001\\"
# status="ip"
# creat_Asst_new_version(asset_name,task_name,version_name,ple_step,project_name,description,uploaded_movie_path,local_path,status)
###



def set_task_status(project_name,asset_name,task_name,ple_step,task_ststus,version_ststus):
    filters = [['name', 'is', project_name]]
    Project = sg.find_one('Project', filters)
    filters = [['project', 'is', Project],
               ['code', 'is', asset_name]]
    asset = sg.find_one('Asset', filters)

    task=sg.find("Task",[ ['project', 'is',Project],["content","is",task_name],["step",'name_is',ple_step],['entity','is',asset]])
    Last_version=get_laset_version(task)
    task_data = {'sg_status_list':task_ststus}
    version_data = {'sg_status_list':version_ststus}
    result = sg.update("Version",Last_version['id'],version_data)
    result = sg.update("Task",task[0]['id'],task_data)


def get_laset_version(task):
    Version=sg.find("Version",[["sg_task","is",task]],["created_at"])
    all_time=[x["created_at"] for x in  Version]
    all_time.sort()
    for x in Version:
        if x["created_at"]==all_time[-1]:
            return x

### work set_task_status
# asset_name="xiaohei"
# project_name="LST"
# task_name="default"
# ple_step="cfx"
# task_ststus="final"
# version_ststus="down"
# set_task_status(project_name,asset_name,task_name,ple_step,task_ststus,version_ststus)
###







#print Last_version

# sg_task=
# created_at
#def
#Version = sg.create('Version', data)
#print Version

#Versionid=6751


#result = sg.update("Version",6768,data)


# upload .mov
#sg.upload("Version", Version['id'], 'D:/pletest/shotgun/funcs/main.mov', field_name="sg_uploaded_movie")


# add sg_path_to_movie
# data = {
#     'sg_path_to_movie': 'D:/pletest/shotgun/funcs/main.mov'
#     }
# sg.update("Version", Versionid,data)


# update sg_status_list
# data = {
#     'description': '这是一个测试',
#     'sg_status_list': 'apr'
#     }
# sg.update("Version", Versionid,data)



# filters = [['code','is', 'testtemplate' ]]
# template = sg.find_one('TaskTemplate', filters)
#
#
# data = {'project': Project,
#         'code': 'xiaozi',
#         'sg_asset_type':"Character",
#         'description': 'xiao zi htest',
#         'task_template': template }
# result = sg.create('Asset', data)
#
# sg.upload("Asset", result['id'], 'D:/pletest/shotgun/funcs/main.mov', field_name="sg_uploaded_movie")
# print template
# print result











