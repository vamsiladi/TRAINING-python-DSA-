"""Mary is a kindergarten teacher. She has given a task to the 
children after teaching them a list of words. The task is to 
find the unknown words (other than the words they already 
know) from the given text. Write a python function which 
accepts the text and the known list of words and returns
the set of unknown words found.
Return -1 if there are no unknown words.
Estimated Time: 20 minutes

Sample Input	
Text: "the sun rises in the east"
Vocabulary: ["sun","in","east","doctor","day"]	
Expected Output
{'rises', 'the'}"""

def fun(text,voc):
    l=[]
    count=0
    for i in text:  
        if i in voc:
            count+=1
            l.append(i)
    if count>0:
        return {*l}
    else:
        return -1
       
    



Vocabulary=["sun","in","east","doctor","day"]
text1=[i for i in input().split()]
print(fun(text1,Vocabulary))
