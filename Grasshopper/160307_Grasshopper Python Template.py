"""
Realtime Simulator

written by Yan "Ryan" Zhang <ryanz@mit.edu>
for MIT Media Lab, Changing Place Group, CityScope Project
March.7th.2016
"""


import rhinoscriptsyntax as rs
import scriptcontext as sc
import clr
clr.AddReference("Grasshopper")
import Grasshopper as gh


# call main()
if triger and sc.sticky["blnInitiated"] == True:
    main()


# main function
def main():
    currentHeights = sc.sticky["currentHeights"]
    lastHeights = sc.sticky["lastHeights"]
    diffs = []
    for i in range(0, len(currentHeights)):
        hc = currentHeights[i]
        hl = lastHeights[i]
        if not hc == hl:
            diffs.append(i)
    
    if len(diffs) > 0:
        
        xSteps = sc.sticky["xSteps"]
        ySteps = sc.sticky["ySteps"]
        for diff in diffs:
            print "differet module found! at number: ", diff
            print "x step = ", xSteps[diff]
            print "y step = ", ySteps[diff]
            print "lastHeights = ", lastHeights[diff]
            print "currentHeights = ", currentHeights[diff]
        
        # do the first diff first, TODO: loop each diff later
        diff = diffs[0]
        xs = range(int(xSteps[diff])-2,int(xSteps[diff])+2+1)
        ys = range(int(ySteps[diff])-2,int(ySteps[diff])+2+1)
        
        # bufferMatrix: 5 by 5 matrix (list of list), element is a list of
        # [x, y, valid(in bound), n(order in data list), height] 
        # if not valid, height = 0.030934
        
        # initiate bufferMatrix
        bufferMatrix = [[[],[],[],[],[]],
                        [[],[],[],[],[]],
                        [[],[],[],[],[]],
                        [[],[],[],[],[]],
                        [[],[],[],[],[]]]
        #for i in range(5): tempRow.append([0,0,0,0,0]) #doesn't work!
        
        # fill bufferMatrix
        for j in range(5):
            for i in range(5):
                #print "i: ", i, "; j: ", j
                x = xs[i]
                y = ys[j]
                #print "x: ", x, "; y: ", y
                if x >= 0 and x <= 15 and y >= 0 and y <= 15:
                    v = 1 #valid/in bound = 1, not valid = 0
                    n = xy2n(x,y)
                    h = lastHeights[n]
                else: 
                    v = 0 #not valid
                    n = -1 #not valid
                    h = 0.030934
                bufferMatrix[j][i] = [x,y,v,n,h]
        print bufferMatrix
        sc.sticky["bufferMatrix"] = bufferMatrix


# project functions
# given x step and y step return height id
def xy2n(x,y):
    n = y + (15 - x) * 15
    return n


# library functions
# gh data tree and py list
def ghDataTreeToPythonList(dataTree):
    
    """ Converts a GH datatree to a nested Python list """
    
    # Create an empty Python list
    pyList = []
    
    # Add the branches of the Gh datatree to this list
    for i in range(DataTree.BranchCount):
        branch = list(DataTree.Branch(i))
        pyList.append(branch)
        
    return pyList

def pythonListTGhDataTree(pythonList):
    
    """ Converts a  nested Python list to a GH datatree """
    
    # Create GH datatree
    dataTree = gh.DataTree[int]()
    
    # Add pythonlist sub lists to dataTree
    for i,l in enumerate(pythonList):
        for v in l:
            dataTree.Add(v,gh.Kernel.Data.GH_Path(i))
            
    return dataTree

def dataTreePythonListExample():
    # Convert the GH DataTree to nested list and check its content
    pyList = ghDataTreeToPythonList(DataTree)
    print type(pyList)
    print len(pyList)
    print pyList[0]
    print pyList
    
    # Do something with pyList 
    pyList = [[j + 2 for j in sublist] for sublist in pyList]
    print pyList
    
    # Convert pyList to Gh Datatree and return it to GH
    a = pythonListTGhDataTree(pyList)
