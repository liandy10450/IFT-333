#Programmer: Andy Li
#Assignment Lab 3
#IFT333
#Spring 2019 B

#functions

#compares two arrays of binary numbers nad returns SMC
def compareArraysJaccard(firstArray, secondArray):
    
    count = 0
    nonZeroCount = 0
    #count nonzero attributes
    for i in firstArray:
        if firstArray[i] != 0:
            nonZeroCount+= 1
    for i in secondArray:
        if secondArray[i] != 0:
            nonZeroCount+= 1        
    #for loop to compare both arrays
    for i in firstArray:
        #check if both are 1
        if firstArray[i]==1 and secondArray[i] == 1:
            count += 1
    return count        

#Reads data file in form <user_ID>, <movie_1>, <movie_2>, <movie_3> then computes
# similarities between each two users in the data set
def comparePairWiseSimilarities(fileName):
    #open and read input file
    inp = open(fileName, "r")
    allfile = inp.read()

    #convert into an array of string, each entry one line
    lines = allfile.split("\n")

    #for each line/user x
    for ll in lines:

         #4. split line ll and extract the user binary information
        entries = ll.split(" , ")
        x = []
        for i in range(1, len(entries)):
            x.append( int(entries[i]) )

        #5. compute the similarity between that user and all other users:
        #   for each line/user y:    
        for jj in lines:
            #6. split line jj and extract the user binary information
            entries = jj.split(" , ")

            y = []
            for i in range(1,len(entries)):
                y.append( int(entries[i]) )
            
            
            #7. compute the JC similarity between x & y & print it
            
            print("Jaccard coefficient between ",x," and ",y," is: ", compareArraysJaccard(x,y))

#calls functions
def main():
    aArray = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bArray = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1] 
    print("Jaccard coefficient = number of 11 matches/number of nonzero attributes: ", compareArraysJaccard(aArray,bArray))   
    comparePairWiseSimilarities("user_movie_binary_dataset_lab3.txt")
main()

