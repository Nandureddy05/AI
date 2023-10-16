import copy  
from heapq import heappush, heappop  
  

n = 3  
  
  
rows = [ 1, 0, -1, 0 ]  
cols = [ 0, -1, 0, 1 ]  
  

class priorityQueue:  
      
    
    def _init_(self):  
        self.heap = []  
  
     
    def push(self, key):  
        heappush(self.heap, key)  
  
   
    def pop(self):  
        return heappop(self.heap)  
  
      
    def empty(self):  
        if not self.heap:  
            return True  
        else:  
            return False  
  
  
class nodes:  
      
    def _init_(self, parent, mats, empty_tile_posi,  
                costs, levels):  
                      
       
        self.parent = parent  
  
         
        self.mats = mats  
  
       
        self.empty_tile_posi = empty_tile_posi  
  
       
        self.costs = costs  
  
        
        self.levels = levels  
  
      
    def _lt_(self, nxt):  
        return self.costs < nxt.costs  
  

def calculateCosts(mats, final) -> int:  
      
    count = 0  
    for i in range(n):  
        for j in range(n):  
            if ((mats[i][j]) and  
                (mats[i][j] != final[i][j])):  
                count += 1  
                  
    return count  
  
def newNodes(mats, empty_tile_posi, new_empty_tile_posi,  
            levels, parent, final) -> nodes:  
                  
    
    new_mats = copy.deepcopy(mats)  
  
     
    x1 = empty_tile_posi[0]  
    y1 = empty_tile_posi[1]  
    x2 = new_empty_tile_posi[0]  
    y2 = new_empty_tile_posi[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]  
  
     
    costs = calculateCosts(new_mats, final)
