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


def creat_new_version(entity_name,task_name,version_name,project_name,description,uploaded_movie_path=None):
    filters = [ ['name', 'is',project_name]]
    Project = sg.find_one('Project', filters)
    data = { 'project': Project,
             'code': 'main.v008',
             'description': u'这是个测试',
             'sg_status_list': 'rev',
             'entity': asset,
             'sg_task': task}
    if uploaded_movie_path:
        data = {'sg_uploaded_movie': {'local_path': uploaded_movie_path,
    #                               'name': 'Better Movie'}}

#Version = sg.create('Version', data)
#print Version

#Versionid=6751

# data = {'sg_uploaded_movie': {'local_path': 'D:/pletest/shotgun/funcs/main.mov',
#                               'name': 'Better Movie'}}
#result = sg.update("Version",6746,data)


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











