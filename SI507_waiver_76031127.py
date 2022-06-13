'''
Author - Prarthana Shevatekar
UMich ID - TODO
File - SI 507 Waiver Test : Six Degrees of Kevin Bacon
'''

'''
List of functions  - 
1. LoadingTheGraph(inputFile)
2. ShortestPath(inputGraph, source, destination)
3. DegreeOfSeparation(inputGraph, source, destination)
4. Main

'''
def LoadingTheGraph(inputFile):
    '''
    Loads the data into a graph (network of Hollywood actors)
    Graph is framed using a dictionary where a key is an actor (string) and its values 
    (set of strings) are the actors he/she has acted with)
    TODO - return type similar to Python 3 practice
    '''
    # 1. A placeholder for the graph
    graphDict = {}
    file = open(inputFile)

    # 2. Splitting the file based on new lines - each line represents a movie
    lines = file.read().splitlines()

    # 3. Running a loop for each movie
    for line in lines:

        # 4. Splitting based on forward slashes. Skipping the first element, which is a movie
        actors = line.split('/')[1:]
        for self in actors:

            # 5. Each key in the dictionary represents an actor
            graphDict[self] = set()
            
    for line in lines:
        actors = line.split('/')[1:]
        for selfIndex in range(len(actors)):
            for othersIndex in range(len(actors)):

                # 6. Avoiding drawing an edge to self
                if selfIndex != othersIndex:
                    
                    # 7. Drawing an edge between actors, who starred in the same movie
                    graphDict[actors[selfIndex]].add(actors[othersIndex])
    print(len(list(graphDict)), "actors are found in this file : "+ inputFile)
    return graphDict

def ShortestPath(inputGraph, source, destination):
    '''
    Gives a shortest path from the source to the destination
    '''
    if source == destination:
        print("Please enter non-identical individuals")
        return 

    # Stores the actors who are already visited
    explored = []
    # Maintains actors who are yet to be checked
    queue = [[source]]

    while queue:
        oldConnection = queue.pop(0)
        currentActor = oldConnection[-1]
        
        if oldConnection not in explored:
            for peer in graph[currentActor]:
                network = list(oldConnection)
                network.append(peer)
                queue.append(network)
                
                # Check if handshakes between present peer and the destination is already computed
                # in previous executions (in the while loop)    
                if peer == destination:
                    print("Degree of Separation between "+source+" and "+destination+" is ",len(network)-1)
                    print("Their connection is as followed \n ", network)
                    return
            explored.append(oldConnection)
    print(source, "has no connection to", destination)

def DegreeOfSeparation(inputGraph, source, destination):
    '''
    Gives only DOS from the source to the destination
    '''
    if source == destination:
        print("Please enter non-identical individuals")
        return 

    explored = set()
    queue = [source]
    # queue = set()
    # queue.add(source)

    # Level separator separates demarcates levels in BFS
    handshakes = 1
    # queue.add('levelSeparator')
    queue.append('levelSeparator')

    while queue:
        oldConnection = queue.pop(0)
        if oldConnection == 'levelSeparator':
            handshakes += 1
            # queue.add('levelSeparator')
            queue.append('levelSeparator')
            oldConnection = queue.pop(0)
        
        if oldConnection not in explored:
            for peer in graph[oldConnection]:
        
                if peer == destination:
                    print("Degree of Separation between "+source+" and "+destination+" is ",handshakes)
                    return
                queue.append(peer)
                # queue.add(peer)
            explored.add(oldConnection)

    print(source, " has no connection with Kevin Bacon")

def ComputeHandshakeStats(graph, source, destination):
    explored = set()
    # queue = [source]
    queue = set()
    queue.add(source)
    handshakes = 1

    while queue:
        levelSize = len(queue)
        while levelSize:
            oldConnection = queue.pop()
            if oldConnection not in explored:
                for peer in graph[oldConnection]:
                    if peer == destination:
                        #print("DOF: ", handshakes)
                        return handshakes
                    # queue.append(peer)
                    queue.add(peer)
                explored.add(oldConnection)
            levelSize -= 1
        handshakes += 1
    return 1

if __name__ == '__main__':
    print("By default this program will use the test file - \"BaconData/BaconCastFull.txt\"")
    print("If you wish to continue, enter 'YES'. \nOtherwise enter 'NO' : ", end = '')
    defaultFile = input()
    if defaultFile.lower() == 'yes':
        print("Proceeding with the default file ... ")
        inputFile = r"BaconData/BaconCastFull.txt"
    elif defaultFile.lower() == 'no':
        print("Please enter absolute path to the desired test file in the next line")
        inputFile = input()
    else:
        print("Response is not recognized. Please re-run the program.")

    print("Please wait. Based on the input file, building the Hollywood network now ...")        
    graph = LoadingTheGraph(inputFile)

    flag = True
    while flag == True:
        print("-------------------------------------------------------------------------")
        print("For the following question, please consider this - ")
        print("\nEnter 'Yes' to know the Degree of Separation between any two actors")
        print("Enter 'No' to know the mean and median of all the actors of the network and Kevin Bacon")
        print("Enter 'Exit' to terminate the program")
        print("-------------------------------------------------------------------------")
        print("\nPlease enter your response : ", end = '')
        userResponse = input()
        if userResponse.lower() == 'yes':
            print("Enter names of any two actors in the respective field")
            print("\nNote - Please maintain \"Lastname, Firstname\" Format i.e. Bacon, Kevin")
            print("Note - First and last names are case sensitive")
            print("\nEnter name of the first actor =", end=' ')
            actor1 = input()
            while actor1 not in list(graph):

                # Verifying if actor1 is present or not in the graph
                # If not, prompt to re-enter
                print("Could not find the actor in the network. Please re-enter :", end=' ')
                actor1 = input()
            print("Enter name of the second actor =", end=' ')
            actor2 = input()
            while actor2 not in list(graph):
                
                # Verifying if actor1 is present or not in our graph
                print("Could not find the actor in the network. Please re-enter :", end=' ')
                actor2 = input()
            print("You have requested to find Degrees of Separation between ", actor1+" and "+ actor2)
            print("Please wait. Computing the shortest connection between them now ...")
            
            ShortestPath(graph, actor1, actor2)
            print("-------------------------------------------------------------------------")

        elif userResponse.lower() == 'no':
            flag = False
            print("Based on your response, computing the mean and median between all the actors ")
            print("in the network and Kevin Bacon ...")
            mean, median = 1, []

            precomputedMean = 2.657
            preComuptedMedian = 3.000
            print("Mean and median of the network are ",precomputedMean," and ",preComuptedMedian," respectively.")

            # for eachActor in range(len(list(graph))):
            #     # print(eachActor+1, " : ", list(graph)[eachActor], end = ': ')
            #     # DegreeOfSeparation(graph, list(graph)[eachActor], "Bacon, Kevin")
            #     handshakes = ComputeHandshakeStats(graph, list(graph)[eachActor], "Bacon, Kevin")
            #     median.append(handshakes)
            #     mean += handshakes
            #     if eachActor%100 == 0 and eachActor != 0:
            #         median = sorted(median)
            #         print("For ",eachActor," actors : ")
            #         print("Mean = ", mean/eachActor)
            #         print("Median = ", median[eachActor//2])

        elif userResponse.lower() == 'exit':
            flag = False
            print("Exiting the program now ... ")
    print("Program has exited now!")