class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_list=list(order)
        print(order_list)
        ans=True
        for i in range(len(words)-1):
            for ptr in range(min(len(words[i]),len(words[i+1]))):
                if order_list.index(words[i][ptr])>order_list.index(words[i+1][ptr]):
                    return False
                elif order_list.index(words[i][ptr])==order_list.index(words[i+1][ptr]):
                    if ptr==min(len(words[i+1])-1,len(words[i])-1):
                        if len(words[i])>len(words[i+1]):
                            return False
                elif order_list.index(words[i][ptr])<order_list.index(words[i+1][ptr]):
                 
                    ans=True
                    break;
        return ans    