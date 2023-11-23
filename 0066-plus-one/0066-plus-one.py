class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        new = []
        result = "".join(str(item) for item in digits)

        str_to_int = int(result)
        str_to_int += 1
        for i in str(str_to_int):
            i = new.append(int(i))
        return new
   
            
        
        