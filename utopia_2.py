# input_str="aks ask akash ayzweg ska"
# s=input_str.split()
#
# pattern = 'aks'
# count = 0
#
# for i in s:
#     print()
#     k=0
#     for j in range(len(i)):
#         if k < len(pattern):
#             if pattern[k] == i[j]: # check if letter in pattern is equal to letter in word
#                 k += 1             # if MATCH, then go to next letter in the pattern
#     # print("K:",k)
#     if k == len(pattern):
#             count += 1
# print("Matched words are :",count)
#

""" Using RegEx """
import re
# This is the string containing white space,tab,multiple white spaces and newline char
words = "ask    aks     ankush \n abhishek ska  abhisheks".split() #split will remove all spaces, tabs and newline
print(words)
#pattern = 'aks'   ##this is the pattern we want to search

##below is the regular expression pattern containg the desired characters surrounded by zero or more word chracters
pattern = r'.*a.*k.*s.*'
count = 0
print("The words matching our pattern are: ")
for word in words:
    match = re.search(pattern,word)
    if match:
        count += 1
        print(count,') ',match.group())
print("No. of such words: ",count)
