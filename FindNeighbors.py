import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

# preparing input from dynamo to revit
rooms = UnwrapElement(IN[0])

# spatial boundary
spatialElementBoundaryOptions = SpatialElementBoundaryOptions();
spatialElementBoundaryOptions.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Finish

# output list
roomNeighbors = []
sharedWalls = []
# iterate through the rooms (Note, this will be faster than Dynamo nodes because it does not use Dynamo's geometry engine)

if isinstance(rooms, list):
	items = ProcessList(Unwrap, rooms)
else:
	items = [Unwrap(rooms)]
    
for i in rooms:
	rooms = []
	relatedWall = []
	boundSegments = i.GetBoundarySegments(spatialElementBoundaryOptions)
	# iterates through the exterior curves of the room for now
	for bs in boundSegments[0]:
		wall = doc.GetElement(bs.ElementId)
		wallThickness = wall.Width
		derivatives  = bs.GetCurve().ComputeDerivatives(0.5,True)
		midPoint = derivatives.Origin
		tangent = derivatives.BasisX.Normalize()
		normal = XYZ(tangent.Y, tangent.X * ( -1), tangent.Z)
		point = midPoint + wallThickness * normal
		# try to find rooms. if no room, continue. Also prevents adding room to itself
		try:
			otherRoom = doc.GetRoomAtPoint(point)
			if not otherRoom.Id.IntegerValue == i.Id.IntegerValue:
				rooms.append(otherRoom)
				relatedWall.append(wall)
		except:
			continue
	# the below is commented out but allows for the lists to be weaved.	
#	roomNeighbors.append(zip(rooms,relatedWall))
	roomNeighbors.append(rooms)
	sharedWalls.append(relatedWall)
# output the neighboring rooms and the shared walls in two lists
OUT = roomNeighbors,sharedWalls