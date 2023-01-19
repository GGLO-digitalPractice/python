import clr
import math

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument

elev = []
angle_ = []
axis = []

for i,j,m in zip(IN[0],IN[1],IN[3]):
    elev.append(UnwrapElement(i))
    angle_.append(math.radians(j))
    axis.append(m.ToRevitType())

TransactionManager.Instance.EnsureInTransaction(doc)
c = 0
for e in elev:
    Autodesk.Revit.DB.ElementTransformUtils.RotateElement(doc, e.Id, axis[c], angle_[c])
    c+=1
	
TransactionManager.Instance.TransactionTaskDone()

OUT = elev, angle_