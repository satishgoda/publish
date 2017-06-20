#encoding=utf8
import sys
import os
sys.path.append("D:\pletest\shotgun\python-api")

import shotgun_api3


sg = shotgun_api3.Shotgun("https://blackdragonentltd.shotgunstudio.com",
                          script_name="ple",
                          api_key="744df90922cb65474e449f3ebdd10b8caadc8d216236ad3a37aba44094f6fde3")



filters = [
	['project', 'name_is', "__UniPipe_Test"]
]
# res=sg.find("Task",filters,fields)
# print res

fields = []
filters = [ ['name', 'is',"__UniPipe_Test"]]
Project = sg.find_one('Project', filters)

fields = ["code"]
filters = [ ['project', 'is',Project],
            ['code', 'is', 'chabei'] ]
asset = sg.find_one('Asset', filters,fields)

print asset

fields = ["content"]
filters = [ ['project', 'name_is',"lst"],
            ['entity', 'is',{'type':'Asset', 'id': asset['id']}],
            ['step', 'name_is', 'cfx']]
task = sg.find_one('Task', filters,fields)
print task




#print Project



data = { 'project': Project,
         'code': 'main.v008',
         'description': u'这是个测试',
         'sg_status_list': 'rev',
         'entity': asset,
         'sg_task': task}
Version = sg.create('Version', data)
print Version

Versionid=6751

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



filters = [['code','is', 'testtemplate' ]]
template = sg.find_one('TaskTemplate', filters)


data = {'project': Project,
        'code': 'xiaozi',
        'sg_asset_type':"Character",
        'description': 'xiao zi htest',
        'task_template': template }
result = sg.create('Asset', data)

sg.upload("Asset", result['id'], 'D:/pletest/shotgun/funcs/main.mov', field_name="sg_uploaded_movie")
print template
print result











