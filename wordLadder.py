#@file wordLadder.py
#@author Ben Gruher
#@see "Seattle University, CPSC 3400, January 2019"

def main():

    #returns character differences between two strings
    def wordDiff(word1, word2):
        diff = 0
        if len(word1) == len(word2):
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
        return diff
        
    #returns solution as a list, returns None is no ladder can be found
    def findSolutions(w1, w2):
        sol = [[w1]]
        while(sol[-1][-1] != w2): #while the last element's last element is not w2 (solution has not been reached)
            neighbors = len(dic[sol[0][-1]])
            for i in range(neighbors): #for each neighbor of first element's last element to find next solution
                newWord = dic[sol[0][-1]][i] #add next neighbor to partial solution
                unique = True #tests whether or not the word has already been used in another solution to avoid backtracking
                for x in range(len(sol)):
                    if newWord in sol[x]:
                        unique = False
                if unique == True:
                    newList = sol[0] + [newWord]
                    sol.append(newList) #enqueue new partial solution
            del sol[0] #dequeue
            if len(sol) == 0:
                return None
        return sol[-1]



    #reads in dictionary.txt
    with open("dictionary.txt") as f:
        f1 = f.read().splitlines()

    #assembles python dictionary structure from dictionary.txt
    dic = {}
    print("Please wait 4-5 minutes for words to be added into dictionary...")
    for word in f1:
        if len(word) < 7 and len(word) > 3:
            dic[word] = []
            for entry in dic:
                if wordDiff(word, entry) == 1:
                    dic[entry].append(word)
                    #print("adding " + word + " to " + entry)
                    dic[word].append(entry)
                    #print("adding " + entry + " to " + word)

    #reads in pairs.txt
    g = open("pairs.txt", "r")
    g1 = g.readlines()

    #for each pair, checks lengths and passes to findSolutions function
    for pair in g1:
        w1 = pair.split()[0]
        w2 = pair.split()[1]
        if w1 not in dic:
            print(w1 + " not in dictionary")
        elif w2 not in dic:
            print(w2 + " not in dictionary")
        elif len(w1) == len(w2):
            sol = findSolutions(w1, w2)
            if sol == None:
                print("No ladder found for " + w1 + " and " + w2)
            else:
                print("Ladder for " + w1 + " to " + w2 + ":")
                print(sol)
        else:
            print(w1 + " and " + w2 + " have different lengths")

        
if __name__ == "__main__": main()
