from math import tan, radians
from mojo.events import EditingTool, installTool
from defcon import Point

class ConstrainAngleEditingTool(EditingTool):
    
    def getToolbarTip(self):
        return "Constrain Angle"    
    
    def modifyDeltaForAngle(self, delta, angle):
        '''Constrain delta to a given angle.'''
        _tan1 = tan(radians(angle + 90))
        _tan2 = tan(radians(angle))
        if abs(_tan1) < abs(_tan2):
            delta.x = -_tan1 * delta.y
        else:
            delta.y = _tan2 * delta.x
                    
    def modifyDraggingPoint(self, point, delta):
        '''Constrain on-curve points to italic angle.'''

        # get italic angle from font!
        f = CurrentFont()
        self.angle = f.info.italicAngle - 90

        # calculate delta for current mouse down point
        if self.mouseDownPoints:
            fx, fy = self.mouseDownPoints[-1]
        else:
            fx, fy = point

        delta.x = point.x - fx
        delta.y = point.y - fy
        
        # constrain delta to angle
        if self.shiftDown:
            self.modifyDeltaForAngle(delta, self.angle)
            
        return point, delta
    
    def _mouseDragged(self, point, delta):
        '''Constrain off-curve points to italic angle.'''

        # apply default _mouseDragged behavior first
        shiftdown = self.shiftDown
        self.shiftDown = False
        super()._mouseDragged(point, delta)
        self.shiftDown = shiftdown

        # handle single off-curve point selection
        if self.shiftDown and self.selection.containsSingleOffCurve():

            # get selected off-curve point
            offcurve = self.selection.selectedPoints[0]

            # get related on-curve point
            info = self.selection.selectionDataForPoint(offcurve)
            anchor = info["anchor"]
            
            # calculate delta for off-curve point
            offcurveDelta = Point((offcurve.x - anchor.x, offcurve.y - anchor.y))

            # constrain delta to angle
            self.modifyDeltaForAngle(offcurveDelta, self.angle)

            # update position of off-curve point
            offcurve.x = anchor.x + offcurveDelta.x
            offcurve.y = anchor.y + offcurveDelta.y

installTool(ConstrainAngleEditingTool())