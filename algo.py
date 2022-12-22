from collections import defaultdict
import pandas as pd
import math
import numpy as np
import heapq
def graph_gen():
    #Reading the data fro csv files which conatin about source, destination,weights
    df=pd.read_csv('co2_data.csv')
    #Converting the weight to approximate the vaues
    df['length']=df['length'].apply(np.ceil).astype(int)
    df['Co2Emitted']=df['Co2Emitted'].apply(np.ceil).astype(int)

    # Converting the csv file into list for creating a graph object
    data=df.values.tolist()
    #Simply returning the newly returned grah object
    return data
    

def Dij_generator(l):
    """

    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    
    adj=defaultdict(list)
    for i in range(len(l)):
                
                node=l[i][0]
                adjnode=l[i][1]
                weight=l[i][2]
                co2=l[i][3]
                adj[node].append([adjnode,weight,co2])
                # print(adj)
                
        # Enter your code here
    return adj
    
    
def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    distance=[float('inf') for i in range(934)]
    co2_emission=[float('inf') for i in range(934)]
    parent=[i for i in range(935)]
    parent[1]=1
    
    distance[source]=0
    co2_emission[source]=0
    pq=[(source,0,0)]
    heapq.heapify(pq)
    while(len(pq)>0):
        curr=heapq.heappop(pq)
        node=curr[0]
        dis=curr[1]
        co2_emitted=curr[2]

        for i in graph_object[node]:
            adjnode=i[0]
            # print(adjnode)
            weight=i[1]
            co2=i[2]
            if(dis+weight<distance[adjnode] and co2_emitted+co2<co2_emission[adjnode]):
                distance[adjnode]=dis+weight
                co2_emission[adjnode]=co2_emitted+co2
                parent[adjnode]=node
                heapq.heappush(pq,(adjnode,distance[adjnode],co2_emission[adjnode]))
   


    node=destination

    arr=[]
    while parent[node]!=node:
            arr.append(node)
            node=parent[node]
    
    arr.append(source)
    arr[::-1]
    shortest_path_distance = distance[destination]
    least_ammount_co2=co2_emission[destination]
    try:
        # Enter your code here
        return shortest_path_distance,least_ammount_co2,arr
    except:
        return shortest_path_distance,least_ammount_co2,ans
data=graph_gen()
ans=Dij_generator(data)
# print(ans)
print("\nShortest Path with Minimum CO2 Emission and Shortest Path \n")
source=785
destination=296
ans2,ans3,path=Q1_dijkstra(source, destination,ans)
print("Source Graph Node :",source)
print("Destination Graph Node :",destination)
print("Minimum Cost Path Node :",ans2/1000,"KM")
print("Minimum CO2 Emission Path  :",ans3,"gm")
print("Minimum Cost Route is  :\n",path,"\n")






