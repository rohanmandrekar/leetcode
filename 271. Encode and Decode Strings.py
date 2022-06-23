    def encode(self, strs):
        # write your code here
        ans=[]
        for s in strs:
            ans.append[chr(ord(s)+6)]
        return ans
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        ans=[]
        for s in str:
            ans.append(chr(ord(s)-6))
        return ans