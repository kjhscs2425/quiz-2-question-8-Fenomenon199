"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""
# print: ("c","t","b")
# words = ("cat", "boat", "bat", "pat", "nat", "nap", "tap", "cap","tan", "top", "bot", "pot", "not", "coat", 

c_t_b = 'ctb'
for letter1 in c_t_b:
    a_o= 'ao' 
    for letter2 in a_o: 
        # print(letter1)
        # print (letter2 )
        print (letter1+letter2)

# a_string ='a string' 
# for letter in a_string:
#     print : ("t") 

# a_string ='a string' 
# for letter in a_string:
#     print:  ("b" )
  