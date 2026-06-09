class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        all=set('abcdefghijklmnopqrstuvwxyz')
        return set(sentence)==all
        