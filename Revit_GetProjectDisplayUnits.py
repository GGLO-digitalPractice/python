# Load the Python Standard and DesignScript Libraries
import clr
#imports the Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
#imports revit services and the document manager
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

#gets the current document
doc = DocumentManager.Instance.CurrentDBDocument

# Update this variable to match the length unit type that this script was developed with:
scriptUnitTypeId = UnitTypeId.Feet

# Get the length display units of the current Revit document
projectUnits = Document.GetUnits(doc).GetFormatOptions(SpecTypeId.Length).GetUnitTypeId()
conversionFactor = UnitUtils.Convert(1.0, scriptUnitTypeId, projectUnits)

# Assign your output to the OUT variable.
OUT = conversionFactor