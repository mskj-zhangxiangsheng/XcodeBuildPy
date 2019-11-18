# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.9pre on Thu Aug 15 16:10:33 2019
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

import os
import thread

from GConfig import gConfig
from pyzlt import MergeFramework

class mergeLibDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: mergeLibDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        
        sizer_1 = wx.FlexGridSizer(3, 1, 10, 2)
        
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 10, 3)
        sizer_1.Add(grid_sizer_1, 10, wx.EXPAND, 0)
        
        static_text_1 = wx.StaticText(self, wx.ID_ANY, u"lib库路径")
        grid_sizer_1.Add(static_text_1, 0, 0, 0)
        
        self.inputLibPathTextView = wx.TextCtrl(self, wx.ID_ANY, "")
        self.inputLibPathTextView.SetMinSize((600, 22))
        grid_sizer_1.Add(self.inputLibPathTextView, 0, 0, 0)
        
        self.libPathButton = wx.Button(self, wx.ID_ANY, u"选择路径")
        grid_sizer_1.Add(self.libPathButton, 0, 0, 0)
        
        static_text_2 = wx.StaticText(self, wx.ID_ANY, u"输出路径")
        grid_sizer_1.Add(static_text_2, 0, 0, 0)
        
        self.outputLibPathTextView = wx.TextCtrl(self, wx.ID_ANY, "")
        self.outputLibPathTextView.SetMinSize((600, 22))
        grid_sizer_1.Add(self.outputLibPathTextView, 0, 0, 0)
        
        self.outputLibPathButton = wx.Button(self, wx.ID_ANY, u"选择路径")
        grid_sizer_1.Add(self.outputLibPathButton, 0, 0, 0)
        
        sizer_2 = wx.GridSizer(1, 1, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        
        self.mergeButton = wx.Button(self, wx.ID_ANY, u"合并")
        sizer_2.Add(self.mergeButton, 0, wx.ALIGN_CENTER, 0)
        
        grid_sizer_3 = wx.FlexGridSizer(1, 1, 0, 0)
        sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        
        self.printTextView = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
        self.printTextView.SetMinSize((750, 300))
        grid_sizer_3.Add(self.printTextView, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onClickLibPathButton, self.libPathButton)
        self.Bind(wx.EVT_BUTTON, self.onClickOutputLibPathButton, self.outputLibPathButton)
        self.Bind(wx.EVT_BUTTON, self.onClickMergeButton, self.mergeButton)
        # end wxGlade

        self.inputLibPathTextView.SetValue(gConfig.mergeLibInputPath)
        self.outputLibPathTextView.SetValue(gConfig.mergeLibOutputPath)

    def onClickLibPathButton(self, event):  # wxGlade: mergeLibDialog.<event_handler>
        picker = wx.DirDialog(self)
        picker.SetPath(gConfig.mergeLibInputPath)
        if picker.ShowModal() != wx.ID_CANCEL :
            path = picker.GetPath().encode('utf-8')
            gConfig.mergeLibInputPath = path
            self.inputLibPathTextView.SetValue(path)
        event.Skip()

    def onClickOutputLibPathButton(self, event):  # wxGlade: mergeLibDialog.<event_handler>
        picker = wx.DirDialog(self)
        picker.SetPath(gConfig.mergeLibOutputPath)
        if picker.ShowModal() != wx.ID_CANCEL :
            path = picker.GetPath().encode('utf-8')
            gConfig.mergeLibOutputPath = path
            self.outputLibPathTextView.SetValue(path)
        event.Skip()

    def onClickMergeButton(self, event):  # wxGlade: mergeLibDialog.<event_handler>
        self.printTextView.Value = ""
        if self.outputLibPathTextView.Value.lower().startswith(self.inputLibPathTextView.Value.lower()):
            self.infoPrint("输出路径不能等于lib库路径，或是其子目录")
            return
        
        def start():
            task = MergeFramework()
            task.infoPrint = self.infoPrint
            task.errorPrint = self.errorPrint
            task.continueOrCancelAsk = self.continueOrCancelAsk

            task.new_framework_dir = os.path.join(self.outputLibPathTextView.Value.encode('utf-8'),"merge_dst")
            task.src_framework_dir = self.inputLibPathTextView.Value.encode('utf-8')
            task.new_framework_name = 'zxszl'

            self.infoPrint("***************开始***************")
            task.func_merge_frameworks_libs()
            self.infoPrint("***************结束***************")

        thread.start_new_thread(start, () )
        event.Skip()

    def infoPrint(self,info):
        wx.CallAfter(self.__infoPrint,info)
        
    def __infoPrint(self,info):
        self.printTextView.AppendText(info + "\n")

    def errorPrint(self,error):
        wx.CallAfter(self.__errorPrint,error)

    def __errorPrint(self,error):
        self.printTextView.AppendText(error + "\n")

    def continueOrCancelAsk(self,tip,continueStr,cancelStr):
        self.infoPrint(tip)
        self.infoPrint("stop")
        return cancelStr


# end of class mergeLibDialog
