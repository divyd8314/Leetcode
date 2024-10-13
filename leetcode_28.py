class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack: #will return -1 if occurence of needle not in haystack
            return -1
        
        mylist = [] #will add the index of when first letter of needle occurs in haystack
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                mylist.append(i)

        new_list = [] #checks if the length of the first occurence and length of needle is the same or not, if not the same, we know that the first occurence will not spell out needle and will be eliminated 
        for i in mylist:
            if i+len(needle) <= len(haystack):
                new_list.append(i)

        number = 0 #Whatever indexes are possible answers, code will loop through it to check if the word is the same as needle or not, if it is, it will return i (the index of first occurence)
        for i in new_list:
            number = i
            new_str = ""
            for letter in range(i, i + len(needle)):
                new_str+=haystack[letter]
            if new_str == needle:
                return number 
         
              