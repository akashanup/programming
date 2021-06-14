class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda boxType: boxType[1], reverse=True)
        boxUnits = 0
        boxes = 0
        for boxType in boxTypes:
            remainingSize = truckSize - boxes
            if remainingSize == 0:
                break
            else:
                boxesAdded = min(boxType[0], remainingSize)
                boxes += boxesAdded
                boxUnits += (boxesAdded * boxType[1])
        return boxUnits
