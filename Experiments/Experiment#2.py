sentence = str(input("Enter Sentence : "))
searchword = str(input("Enter word you would like to search : "))
words = sentence.split()
count = sp = 0
for i in words:
    count+=len(i)
    if searchword == i:
        if searchword == words[0]:
            print("The word '",searchword,"' is present in the sentence starting at index 0")
            break
        else:
            count-=len(i)
            print("The word '",searchword,"' is present in the sentence starting at index",count+sp+1)
            break
    else:
        sp+=1

else:
    print("The word '",searchword,"' is not present in the sentence")
