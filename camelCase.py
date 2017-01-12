
print ("Enter a sentence to convert to Camel Case")
#get input from user
stringSentence = input()
newString = ""
#break sentence into list of words in the sentence
camelList  = stringSentence.split()
print (camelList)
#loop through list to generate camel case
for x in camelList:
#make the fisrt word lower case
    if (x ==camelList[0]):
        p=x.lower()
#add the first word (in lower case) to the camel case string
        newString+=p
        print(p)
#make the first letter of each word uppercase
    else:
#make the word lowercase
        x.lower()
#get the first letter of the word and make it uppercase
        s=x[0].upper()
#add the uppercase letter
        newString+=s
#add the rest of the word by excluding the fisrt letter
        newString+=x[1:]
#print the camel case
print (newString)
