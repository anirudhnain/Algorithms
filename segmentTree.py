
class SegmentNode(object):
    def __init__(self, value, i , j):
        self.value = value
        self.startNode = i
        self.endNode = j

class SegmentTree(object):

    def updateParent(self, tree, parentIndex, updateSum):

        tree[parentIndex].value += updateSum
        
        if parentIndex <= 0:    
            return
        else:
            self.updateParent(tree, parentIndex-1>>1, updateSum)

    def update(self, tree, currentIndex, index, newValue):

        node = tree[currentIndex]
        startNode = node.startNode
        endNode = node.endNode

        if startNode == endNode == index:
            updateVal = newValue-node.value
            node.value = newValue
            return self.updateParent(tree, currentIndex-1>>1, updateVal)

        mid = (startNode+endNode)/2

        if index<=mid:
            return self.update(tree, 2*currentIndex+1, index, newValue)
        else:
            return self.update(tree, 2*currentIndex+2, index, newValue)

    def traverseTree(self, tree, currentIndex, i , j):

        node = tree[currentIndex]
        startNode = node.startNode
        endNode = node.endNode

        if startNode>=i and endNode<=j:
            return node.value

        mid = (startNode+endNode)/2

        # print mid, i, j, startNode, endNode
        #Complete overlap
        if i<=mid and j>mid:
            return self.traverseTree(tree, 2*currentIndex+1, i, j) + self.traverseTree(tree, 2*currentIndex+2, i , j)

        if i<=mid:
            return self.traverseTree(tree, 2*currentIndex+1, i, j)

        if j>mid:
            return self.traverseTree(tree, 2*currentIndex+2, i, j)

    def rangeSum(self, i, j):
        if self.tree:
            return self.traverseTree(self.tree, 0, i, j)
        else:
            return 0
            
    def formTree(self, tree, arr, currentIndex, low, high):
        if low == high:
            tree[currentIndex] = SegmentNode(arr[low], low, high)
            return

        if low<high:
            mid = (high+low)/2
            
            tree[currentIndex] = SegmentNode(sum(arr[low:high+1]), low, high)
            self.formTree(tree, arr, 2*currentIndex+1, low, mid)
            self.formTree(tree, arr, 2*currentIndex+2, mid+1, high)

    def __init__(self, arr):
        self.tree = [SegmentNode(0,0,0) for i in range(4*len(arr))]
        self.formTree(self.tree, arr, 0, 0, len(arr)-1)
        
        for elem in self.tree:
            print elem.value, elem.startNode, elem.endNode
        
        print self.rangeSum(0,0)

        print "Update index 0 to 1"
        self.update(self.tree, 0, 0, 1)
        
        # for elem in self.tree:
        #     print elem.value, elem.startNode, elem.endNode

        # self.update(self.tree, 0, 0, -1)
        
        # print "Update index 0 to -1"

        # for elem in self.tree:
        #     print elem.value, elem.startNode, elem.endNode

        # self.update(self.tree, 0, 2, 7)
        
        # print "Update index 2 to 7"

        # for elem in self.tree:
        #     print elem.value, elem.startNode, elem.endNode

        print self.rangeSum(0,0)
        

s = SegmentTree([-1])