class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        new_set=set()
        unique_list=[]
        count=[0]*10**5
        new_list=arr
        arr=[]
        for x in new_list:
            count[x]=count[x]+1
        for x in new_list:
            if count[x]>1:
                new_set.add(x)
                
       
        arr=list(new_set)
        if len(arr)==0:
            arr=[-1]
        arr.sort()
        return arr
        
            
            
