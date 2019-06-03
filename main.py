#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
from tkinter import filedialog
from CommonUtils.excel_reader import excel


def main():

    def selectExcelfile():
        fname = filedialog.askopenfile(title="选择Excel文件",
                                       filetype=[("Excel", "*.xlsx"), ("Excel2003", "*.xls"), ("All Files", "*")])
        text1.insert(0, fname.name)
        return fname.name

    def closeThisWindow():
        root.destroy()

    def doProcess():
        excelpath = selectExcelfile()
        gamerlist = excel(excelpath)

        y = 1
        oldypos = 0
        for gamer in gamerlist:
            cbutton = tkinter.Checkbutton(root, text="%d,%s, %s, %s" % \
                                                     (gamer["编号"], gamer["姓名"], gamer["地区"], gamer["段位"]))
            if oldypos == 0:
                ypos = y * 10 + 60
            if oldypos != 0:
                ypos = oldypos + 20
            oldypos = ypos
            cbutton.pack()
            cbutton.place(x=30, y=ypos)
            y += 1

    root = tkinter.Tk()
    root.title("KendoGameRandomDrawer")
    root.geometry("630x768")

    label1 = tkinter.Label(root, text="请选择文件:")
    text1 = tkinter.Entry(root, bg="white", width=45)
    button1 = tkinter.Button(root, text="选择文件", width=8, command=doProcess)
    button2 = tkinter.Button(root, text="退出", width=8, command=closeThisWindow)

    label1.pack()
    button1.pack()
    button2.pack()

    label1.place(x=30, y=30)
    text1.place(x=98, y=30)
    button1.place(x=420, y=26)
    button2.place(x=500, y=26)

    root.mainloop()

if __name__ == '__main__':
    main()