from math import hypot
def midPoint(p1 ,p2):
    # -------------------------- Calculating the midpoint of the eyes ---------------------------
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def getBlinkingRatio(eyePoints, facialLand):
    # ------------------------- Find the left furthest point of the eye ------------------
    leftPoint = (facialLand.part(eyePoints[0]).x, facialLand.part(eyePoints[0]).y)
    rightPoint = (facialLand.part(eyePoints[3]).x, facialLand.part(eyePoints[3]).y)

    # ------------------------- Find the center point of the eye ------------------
    cenTop = midPoint(facialLand.part(eyePoints[1]), facialLand.part(eyePoints[2]))
    cenBot = midPoint(facialLand.part(eyePoints[5]), facialLand.part(eyePoints[4]))

    # ----------------------- Calculate the horizontal and vertical line --------------------
    horLineLength = hypot((leftPoint[0] - rightPoint[0]), (leftPoint[1] - rightPoint[1]))
    verLineLength = hypot((cenTop[0] - cenBot[0]), (cenTop[1] - cenBot[1]))

    # ---------------------- Calculate the ratio ------------------------------
    blinkingRatio = horLineLength / verLineLength
    return blinkingRatio