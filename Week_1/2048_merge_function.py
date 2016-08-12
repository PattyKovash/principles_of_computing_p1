"""
Merge function for 2048 game.
Run code in www.codeskulptor.org
July 2016 - PK
"""       
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    merged = list(line)
    zeros = []
    
    # separate 0's & non-zero
    while 0 in merged:
        merged.pop(merged.index(0))
        zeros.append(0)
        
    # iterate non-zero list      
    for indx in range(len(merged)):
        # check to see if reached end of list
        if (indx + 1) != len(list(merged)):
            # if the current element == the next element,
            # multiply current element by 2, remove neighboring
            # element
            if merged[indx] == merged[indx + 1]:
                added = merged[indx] * 2
                merged[indx] = added
                merged.pop(indx + 1)
                merged.append(0)
    merged.extend(zeros)
    return merged
        
          
#def test_merged():
#    """
#    Function to test merge.
#    """
#    print "Computed [2,0,2,4]: ", merge([2,0,2,4]), "Expecte: [4,4,0,0]"
#    print "Computed [0,0,2,2]: ", merge([0,0,2,2]), "Expecte: [4,0,0,0]"
#    print "Computed [2,2,0,0]: ", merge([2,2,0,0]), "Expecte: [4,0,0,0]"
#    print "Computed [2,2,2,2,2]: ", merge([2,2,2,2,2]), "Expecte: [4,4,2,0,0]"
#    print "Computed [8,16,16,8]: ", merge([8,16,16,8]), "Expecte: [8,32,8,0]"
#    
#test_merged()
