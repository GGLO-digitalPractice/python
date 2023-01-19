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
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=16.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

ex = Excel.ApplicationClass()   
ex.Visible = True
ex.DisplayAlerts = False   

fp = filePath
wn = wsNumber
#sv = saveAs
lData = l_data
lLoc = l_location
rData = r_data
rLoc = r_location

x = 1
#wn = []

workbook = ex.Workbooks.Open(fp)
#ws = workbook.Worksheets[1]

i = 0
for w in wn:
    workbook.Worksheets[w].Range(str(lLoc[i])).Value2 = int(lData[i])
    workbook.Worksheets[w].Range(str(rLoc[i])).Value2 = int(rData[i])
    i += 1

if (workbook.save()):
    #print(ws)
    O = 1
    print(wn)
    print(lData)
    print(lLoc)
    print(rData)
    print(rLoc)
    #workbook.close()