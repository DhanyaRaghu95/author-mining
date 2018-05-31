from nltk.corpus import stopwords

#binary NBC
# 1 is for the author's opinion
# 0 for another author's opinion
train = [('''But insiders on both sides admit that India has had to
wait since 2011 for its biggest tax reform not because the bills had
flaws in them or for a lack of consensus, but simply because the
battle is political not numerical.''', 1),('''Ashok Singhal will
be remembered as one of the most divisive figures in Indian politics
without ever being in active politics.''',1),('''To mark Prime
Minister Narendra Modi's one year in power, the NDA government
released the slogan "varsh ek kaam anek" (one year achievements many)
on May 15. The list of initiatives launched by PM Modi, new or
re-packaged, is visibly long.''',1),('''Prime Minister Narendra
Modi has over the last five months shown remarkable ability to work
quickly towards building or demolishing perceptions about him or his
government.''',1),('''Narendra Modi has taken the first big
gamble of his career as prime minister in Maharashtra. The BJP's "our
way or the highway" dumping of the Shiv Sena, which wanted to be the
dominant player in the partnership, can have serious repercussions for
the Modi-Amit Shah duo.''',1),(''' More than half the population
defecates in the open. Millions of girls drop out of school because
they don't have separate toilets. And the filth costs us billions
because of the ill health it causes.''',0),(''' When we began the NDTV Coca-Cola Support My School campaign back
in 2011, the real motivating factor was one very simple realization -
a realization that a large number of girls in our country are actually
dropping out of schools because of one single factor, something as
basic as not having separate toilets for girls.''',0),(''' Phase three of the
 elections in Jammu Kashmir extends to three ensitive districts in the
 valley, and the turnout here will be a very lear indicator of how
 much things could have changed on the ground. ''',0),('''Mehbooba
 Mufti who could be the first Muslim woman to become a Chief Minister
 is caught between a rock and hard place.''',0),(''' With only six seats, Jammu and Kashmir is numerically
insignificant in the 545-member Lok Sabha. For years thus, this state
with a controversial legacy and turbulent past has held little
interest for national parties other than to use its internal and
external dimensions to garner support at the national
level.''',0)]

# P(C) = n1/N or n0/N
def probabilityOfC(c,train):
    none=0
    nzero=0
    total = 0
    probabilityC=0
    #c=0/1
    
    for i in train:
        if(i[1]==1):
            none+=1
        else:
            nzero+=1
    total=none+nzero
    #print(total)
    #print(none)
    #print(nzero)
    if(c==0):
        probabilityC = nzero/total
        #print(probabilityC)
    elif(c==1):
        probabilityC = none/total
        #print(probabilityC)

probabilityOfC(0,train)
#print("...")
probabilityOfC(1,train)

def probDgivenCForZero(c):
    concat=[]
    finalStr=""
    if(c==0):
        for i in train:
            if(i[1]==0):
                concat.append(i[0])
        for j in concat:
            finalStr+=''.join(j)
            finalStr+=''.join(" ")
    #print(finalStr)
    #print(len(concat))
    return finalStr

def probDgivenCForOne(c):
    concat=[]
    finalStr=""
    if(c==1):
        for i in train:
            if(i[1]==1):
                concat.append(i[0])
        for j in concat:
            finalStr+=''.join(j)
            finalStr+=''.join(" ")
    #print(finalStr)
    #print(len(concat))
    return finalStr
outputStrForZero=""
outputStrForOne=""
outputStrForZero = probDgivenCForZero(0)
outputStrForOne = probDgivenCForOne(1)
#print("----------------------")
#probDgivenC(1)

def preprocess(outputStr):
    listTemp=[]
    stopWords= stopwords.words('english')
    listTemp = [i for i in outputStr.split() if i not in stopWords]
    return listTemp

    
listTempZ=[]
listTempO=[]
listTempZ = preprocess(outputStrForZero)
listTempO = preprocess(outputStrForOne)        
    
def modelInputForZero(listTemp):
    wordCount={}
    for i in range(len(listTemp)):
        count=0
        for j in range(len(listTemp)):
            if(listTemp[i]==listTemp[j]):
                count+=1
            #print(i)
            #print(a[i])
        #print(count)
        if(listTemp[i] in wordCount.keys()):
            wordCount[listTemp[i]]+=count
        else:
            wordCount[listTemp[i]]=count
    return wordCount

def modelInputForOne(listTemp):
    wordCount={}
    for i in range(len(listTemp)):
        count=0
        for j in range(len(listTemp)):
            if(listTemp[i]==listTemp[j]):
                count+=1
            #print(i)
            #print(a[i])
        #print(count)
        if(listTemp[i] in wordCount.keys()):
            wordCount[listTemp[i]]+=count
        else:
            wordCount[listTemp[i]]=count
    return wordCount


wordCountZ={}
wordCountO={}
wordCountZ = modelInputForZero(listTempZ)
wordCountO = modelInputForOne(listTempO)

def findProbEachWord(wordCount,length):
    wordProb={}
    for keys in wordCount.keys():
        wordProb[keys]=float(wordCount[keys])/length
    return wordProb

wordProbZ={}
wordProbO={}
wordProbZ = findProbEachWord(wordCountZ,len(listTempZ))
wordProbO = findProbEachWord(wordCountO,len(listTempO))
        
test = [
    ('''With all the understandable (and justified) focus on OROP, the
media appears to have missed another major development in the Ministry
of Defence - a decision to extend Short Service Commissions for 14
years. ''', 1), (''' Should our society be practising the
philosophy of 'an eye for an eye'?''', 1), ('''To mark Prime Minister
Narendra Modi's one year in power, the NDA government released the
slogan "varsh ek kaam anek" (one year achievements many) on May 15.
The list of initiatives launched by PM Modi, new or re-packaged, is
visibly long. ''', 0),(''' Our media sees every debate in the binary
terms made famous by George W. Bush: "are you with us or against
us?"''', 1),('''Prime Minister Narendra Modi has over the last
five months shown remarkable ability to work quickly towards building
or demolishing perceptions about him or his government. ''',
0),('''Narendra Modi has taken the first big gamble of his career as
prime minister in Maharashtra. The BJP's "our way or the highway"
dumping of the Shiv Sena, which wanted to be the dominant player in
the partnership, can have serious repercussions for the Modi-Amit Shah
duo. ''', 0)]

# find the hypotheses function and compare with the actual output "Y"

# do only for the first test input. (test[0][0])
def preprocessTestData(test):
    listTemp=[]
    stopWords= stopwords.words('english')
    ##### changing the strings of test tuple using indices ( has to be done manually)
    listTemp = [i for i in test[3][0].split() if i not in stopWords]
    return listTemp

finalTest=[]
finalTest = preprocessTestData(test)

def findProbOfTestWords(finalTest):
    probabilityZ=1
    probabilityO=1
    for i in finalTest:
        if( i in wordProbZ.keys()):
            probabilityZ*=wordProbZ[i]
        elif( i in wordProbO.keys()):
            probabilityO*=wordProbO[i]
        elif( i not in wordProbZ.keys() and i not in wordProbO.keys()):
            probabilityZ*=(1/len(listTempZ))
            probabilityO*=(1/len(listTempO))

    if(probabilityZ > probabilityO):
        print(0)
    else:
        print(1)
            
findProbOfTestWords(finalTest)            
