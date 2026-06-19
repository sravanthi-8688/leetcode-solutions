class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words=0
        for i in sentences:
            max_words=max(max_words,i.count(" ")+1)
        return max_words
        