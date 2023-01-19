import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

def CheckListBoxFix(items, message=None, title=None):
    checkstates = [item[1] for item in items]
    itemstrs = ["{}".format(item[0]) for item in items]
    newcheckstates = Rhino.UI.Dialogs.ShowCheckListBox(title, message, itemstrs, checkstates)
    if newcheckstates:
        rc = zip(itemstrs, newcheckstates)
        return rc

sc.doc = Rhino.RhinoDoc.ActiveDoc

def SelectLayers():
    #get a list of layers to turn on
    names=rs.LayerNames()
    layerNames=[(LName,False) for LName in names]
    msg="Select layers to turn on in all details"
    CLB= CheckListBoxFix(layerNames,msg)
    if not CLB: return
    LL=[]
    for item in CLB:
        if item[1]: LL.append(item[0])
    if len(LL)==0: return
    cView=rs.CurrentView()

SelectLayers()

sc.doc = ghdoc