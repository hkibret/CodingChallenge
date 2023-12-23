def minHeightBst(array):
    return contructMinHeightBst(array, 0 , len(array) -1)
    
def constructMinHeightBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2 
    bst = BST(array[midIdx])
    bst.left= constructMinHeightBst(array,startIdx, midIx - 1 )
    bst.right = constructMinHeightBst(array,midIdx + 1, endIdx)
    return bst1
class BST:
    def _init_(self, value):
        self.value = value
        self.left = None 
        self.right = None
