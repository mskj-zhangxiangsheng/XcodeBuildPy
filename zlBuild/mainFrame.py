# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.9pre on Thu Aug 15 16:10:33 2019
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
from GConfig import gConfig

from mergeLibDialog import mergeLibDialog
from buildLibDialog import buildLibDialog

class mainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        self.frame = self # self.Bind(wx.EVT_CLOSE, self.onWindowClose, self.frame) 崩溃 没有frame属性
        # begin wxGlade: mainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        
        sizer_1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        
        self.buildLibButton = wx.Button(self, wx.ID_ANY, u"构建lib库")
        sizer_1.Add(self.buildLibButton, 0, 0, 0)
        
        self.mergeLib = wx.Button(self, wx.ID_ANY, u"合并lib库")
        sizer_1.Add(self.mergeLib, 0, 0, 0)
        
        self.SetSizer(sizer_1)
        
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onClickBuildLibButton, self.buildLibButton)
        self.Bind(wx.EVT_BUTTON, self.onClickMergeLibButton, self.mergeLib)
        self.Bind(wx.EVT_CLOSE, self.onWindowClose, self)
        # end wxGlade

    def onClickMergeLibButton(self, event):  # wxGlade: mainFrame.<event_handler>
        mergeLibDialog(None, wx.ID_ANY, "").ShowModal()
        event.Skip()

    def onWindowClose(self, event):  # wxGlade: mainFrame.<event_handler>
        gConfig.syncToFile()
        event.Skip()
        wx.Exit()

    def onClickBuildLibButton(self, event):  # wxGlade: mainFrame.<event_handler>
        buildLibDialog(None, wx.ID_ANY, "").ShowModal()
        event.Skip()
# end of class mainFrame
