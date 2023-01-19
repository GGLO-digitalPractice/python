import clr
clr.AddReference('System.Core')
#clr.AddReference('RhinoInside.Revit')
#clr.AddReference('RevitAPI') 
#clr.AddReference('RevitAPIUI')

from System import Enum

import rhinoscriptsyntax as rs
import Rhino
#import RhinoInside
import Grasshopper
from Grasshopper.Kernel import GH_RuntimeMessageLevel as RML

import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
#clr.AddReferenceByName('System.Runtime.InteropServices')
#System.Threading.Thread.CurrentThread.CurrentCulture = System.Globalization.CultureInfo("en-US")
from System.Runtime.InteropServices import Marshal

def ExitExcel (filePath, xlApp, wb, ws):
    #clean up before exiting excel, if any COM Object remains
    #unreleased then excel crashes on open following time
    def CleanUp(_list):
        if isinstance(_list, list):
            for i in _list:
                Marshal.ReleaseComObject(i)
        else:
            Marshal.ReleaseComObject(_list)
        return None
    
    wb.SaveAs(str(filePath))
    xlApp.ActiveWorkbook.Close(False)
    xlApp.ScreenUpdating = True
    Cleanup([ws,wb,xlApp])
    return None

ex = Excel.ApplicationClass()   
ex.Visible = True
ex.DisplayAlerts = False   

fp = filePath
nd = int(numDup)
nn = newName
numdupList = range(nd)
wn = []
levelCols = []
lCol = []

workbook = ex.Workbooks.Open(fp)
ws = workbook.Worksheets[1]

for i in numdupList:
    ws.Copy(ws)
    workbook.Worksheets[i+1].Name = str(nn[i])
    wn.append(workbook.Worksheets[i+1].Name)
    lCol = workbook.Worksheets[i+1].Range("Levels").Cells
    for l in lCol:
        levelCols.append(l.Value2)
    workbook.Worksheets[i+1].Range("C4").Value2 = nn[i]

if (workbook.save()):
    #print(wn)
    print(levelCols)
    O = 1 , levelCols
    workbook.Close()
    ex.Quit()
    workbook = None
    ex = None