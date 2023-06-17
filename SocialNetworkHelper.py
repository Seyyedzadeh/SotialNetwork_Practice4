def GetDegreeDistribiution(degrees):
    '''
    Parameters:
     degrees : List of (node,degree)
     این پارامتر لیستی از گره ها را به همراه درجه آنها شامل میشود
     return : نتیجه یک دیکشنری است که کلید آن درجه و مقدار هر کلید تکرار آن درجه می باشد
    '''
    distributionDectionary=dict() 
    for node , deg in degrees:   
     if deg in distributionDectionary.keys():
         distributionDectionary[deg]+=1
     else:
         distributionDectionary[deg]=1
    return distributionDectionary


def GetShortestPathDistribution(pathList):
    '''
    Parameters:
     pathList : List of (source-node,List of (target-node,path-length) )
     این پارامتر لیستی است که عنصر اول آن گره مبدا و عنصر دوم آن لیستی است از زوج مرتبهایی که بخش اول آن گره مقصد و بخش دوم آن طول مسیر است 
     return : نتیجه یک دیکشنری است که کلید آن طول مسیر و مقدار هر کلید تکرار آن طول مسیر می باشد
    '''
    distributionDectionary=dict() 
    for source_node, node_pathList in pathList:
     for target_node, Path_length in node_pathList.items():
        if Path_length in distributionDectionary.keys():
            distributionDectionary[Path_length] += 1
        else:
            distributionDectionary[Path_length] = 1
    return distributionDectionary


def GetWCC_SizeDistribution(conectedComponents):
    wccSizeList=[]
    for cc in conectedComponents:
        wccSizeList.append(len(cc))
    distributionDectionary = dict()
    for size in wccSizeList:
            if size in distributionDectionary.keys():
                distributionDectionary[size] += 1
            else:
                distributionDectionary[size] = 1
    return distributionDectionary


def GetClusteringCoefficientDistribution(clusteringCoefficients):
    distribution = dict()
    for cc in clusteringCoefficients.values():
        distribution[cc] = distribution.get(cc, 0) + 1
    return distribution

def GetCoreNumberDistribution(coreNumberList):
    distribution = dict()
    for cn in coreNumberList.values():
        if(cn in distribution.keys()):
            distribution[cn]+=1
        else:
            distribution[cn]=1
    return distribution

import random
def generateRandomNetwork(b, height, k, alpha):
    network = {}
    nodes = [0]
    for level in range(1, height + 1):
        new_nodes = []
        for parent in nodes:
            for child in range(b):
                node = (parent * b) + child + 1
                new_nodes.append(node)
                network[node] = []
                prob = pow(b, -alpha * (height - level))
                for neighbor in random.sample(nodes, min(k, len(nodes))):
                    network[node].append((neighbor, prob))
        nodes = new_nodes
    return network