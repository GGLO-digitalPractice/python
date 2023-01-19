import clr

clr.AddReference('RevitServices')
import RevitServices

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import DisplayUnitType, UnitUtils, FilteredElementCollector, ViewFamilyType, BuiltInParameter, XYZ, Transform, BoundingBoxXYZ, ViewSection

from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc =  DocumentManager.Instance.CurrentDBDocument

def units(mmToFeets):
	dut = DisplayUnitType.DUT_MILLIMETERS
	return UnitUtils.ConvertToInternalUnits(mmToFeets, dut)

# wall selection
walls = UnwrapElement(IN[0])

# Check if an input data is a list
if not isinstance(IN[0], list):
    walls = [walls]

# user section type name
sectionTypeName = IN[1]

# filtering user section type name (id)
viewFamilyTypes = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()

for vf in viewFamilyTypes:
	if vf.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString() == sectionTypeName:
		viewFamilyTypeId = vf.Id

newSections = []
for wall in walls:
    def builtInParam(wallParam):
        return units(float(wall.get_Parameter(wallParam).AsValueString()))

    # Determine section box
    lc = wall.Location
    line = lc.Curve

    if line == Line:
        return line
    elif:
        e = ("Unable to retrieve wall location line.")
        return Result.Failed

    p = line.GetEndPoint(0)
    q = line.GetEndPoint(1)
    v = q - p

    bb = wall.get_BoundingBox(None)
    minZ = bb.Min.Z
    maxZ = bb.Max.Z

    w = v.GetLength()
    h = maxZ - minZ
    d = wall.WallType.Width
    wallBaseOffset = builtInParam(BuiltInParameter.WALL_BASE_OFFSET)
    wallUnconnectedHeight = builtInParam(BuiltInParameter.WALL_USER_HEIGHT_PARAM)
    offset = 0.1 * w

    # XYZ(min/max section line length, min/max height of the section box, min/max far clip)
    min = XYZ(-0.5*w - offset, wallBaseOffset - offset, - offset - 0.5*d)
    max = XYZ(0.5*w + offset, wallBaseOffset + wallUnconnectedHeight + offset, offset + 0.5*d)

    # factor for direction of section view
    if p.X > q.X or (p.X == q.X and p.Y < q.Y): fc = 1
    else: fc = -1

    midpoint = p + 0.5*v
    walldir = fc*v.Normalize()
    up = XYZ.BasisZ
    viewdir = walldir.CrossProduct(up)

    t = Transform.Identity
    t.Origin = midpoint
    t.BasisX = walldir
    t.BasisY = up
    t.BasisZ = viewdir

    sectionBox = BoundingBoxXYZ()
    sectionBox.Transform = t
    sectionBox.Min = min # scope box bottom
    sectionBox.Max = max # scope box top

    # Create wall section view
    TransactionManager.Instance.EnsureInTransaction(doc)

    newSection = ViewSection.CreateSection(doc, viewFamilyTypeId, sectionBox)
    newSections.append(newSection)

    TransactionManager.Instance.TransactionTaskDone()

OUT = newSections