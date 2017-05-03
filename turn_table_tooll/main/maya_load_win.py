import sys
r"D:\work\ple" in sys.path or sys.path.append(r"D:\work\ple")
from turn_table_tooll.ui.head import *
import maya.cmds as cmds
import maya.OpenMayaUI as apiUI
import shiboken2
#get maya windownhange pyqt lib
def getMayaWindow():
      ptr = apiUI.MQtUtil.mainWindow()
      return shiboken2.wrapInstance(long(ptr),QWidget)
class importmayapUI(object):
      @staticmethod
      def mayaplayWindow(MayaWindow=getMayaWindow()):
          for wnd in MayaWindow.children():#find all windown from maya
              if not hasattr(wnd,'isWindow'):continue#if zhe windown is Exist
              if not wnd.isWindow():continue
              if wnd.windowTitle()=='turn_table_tool':#if zhe windwon name is you windownn name
                    wnd.show()#show window
                    wnd.activateWindow()#active windwon
                    return
          importmayapUI.ShowWindow()#if do not have windown and creat it
      @staticmethod
      def ShowWindow():
        import turn_table_tooll.core.response as response
        reload(response)
        print response.Response()
        #from response import Response
        myWindow = response.Response(parent = getMayaWindow())
        myWindow.show()
#importmayapUI.mayaplayWindow()

'''
import sys
sys.path.append(r"D:\work\ple")
import turn_table_tooll.main.maya_load_win as maya_load_win
reload(maya_load_win)
ui = maya_load_win.importmayapUI()
ui.ShowWindow()
'''