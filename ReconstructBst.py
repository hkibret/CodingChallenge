# This is an input class. Do not edit.
class BST: 
    def _init_(self, rootIdx):
        self.value= value
        self.left = left
        self.right = right
class TreeInfo: 
    def _init_(self, rootIdx):
        self.rootIdx = rootIdx
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), perOrderTraversalValues, treeInfo)
    
def reconstructBstFromRange(lowerBound,uppperBound, preOrderTraversalValues, currentSubtreeinfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= uppperBound:
        return None 
    currentSubtreeInfo.rootIdx +=1 
    leftSubtree = reconstrcutBstFromRange(
        lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo
    )
    rightSubtree = reconstructBstFromRange(
        rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo
    )
    return BST(rootValue, leftSubtree, rightSubtree)
