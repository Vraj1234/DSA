class Solution:
    def countValidWords(self, sentence: str) -> int:
        # sentence = "-   hello"
        words = sentence.split()
        # print(words)
        res = 0

        def check_valid(word):
            n = len(word)
            hyphen_count = 0
            p_marks = 0
            for i in range(len(word)):
                
                if word[i].isnumeric():
                    return False
                if (word[i] == "-"):
                    if hyphen_count>0:
                        return False
                    if i-1<0 or i+1>=n:
                        return False
                    if not word[i-1].isalpha() or not word[i+1].isalpha():
                        return False
                    hyphen_count+=1
                if word[i] in {"!", ".", ","} and i!= n-1:
                    return False
            return True

        for word in words:
            if check_valid(word):
                # print(word)
                res+=1
        
        return res