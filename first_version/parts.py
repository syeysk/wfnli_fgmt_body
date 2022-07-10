import Sketcher

doc = FreeCAD.newDocument() 
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")

sketch = Sketcher.Sketch('middle')
sketch.addGeometry([[1,2], [10, 1]])