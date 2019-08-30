# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S, T):
    # write your code in Python 3.6
    if not S or not T or N==0:
        return [0,0]
        
    numberOfShipsHit = 0
    numberOfShipsSunk = 0
    
    hitCells = set(T.split(" "))
    
    for elem in S.split(","):
        cell1,cell2 = elem.split(" ")
        
        cell1Row = int(cell1[:-1])
        cell1Column = cell1[-1]
        
        cell2Row = int(cell2[:-1])
        cell2Column = cell2[-1]
        
        numberOfCellsCovered = (cell2Row-cell1Row+1)*(ord(cell2Column)-ord(cell1Column)+1)
        hits = 0
        
        shipHitCell = []

        for hitCell in hitCells:
            hitCellRow = int(hitCell[:-1])
            hitCellColumn = hitCell[-1]
            
            if cell1Row<=hitCellRow<=cell2Row and cell1Column<=hitCellColumn<=cell2Column:
                hits+=1
                shipHitCell.append(hitCell)

        for cell in shipHitCell:
            hitCells.remove(cell)

        if hits == numberOfCellsCovered:
            numberOfShipsSunk+=1
        elif hits>0:
            numberOfShipsHit+=1
            
    return [numberOfShipsSunk, numberOfShipsHit]

# print solution(4,"1A 2A,12A 12A", "12A")
print solution(12,"1A 2B,12A 12A", "1A 1B 2A")