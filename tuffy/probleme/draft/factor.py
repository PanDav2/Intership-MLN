# -*-coding: utf-8 -*-

## Automated script to parse and create the evidence file
import random
import numpy
inp = "./entree.txt"
out = "./sortie.txt"

#Version 0.1 using an array to keep track of our calculus
typeOfContent = ["Class","Entity","Relationship"]

def createResourceType():
    #We create an array that will remember the resourceType created in case of redundance and will allow us to match ressource types to 
    res = []
    with open(out,"w") as file:
        with open(inp,"r") as data:
            for line in data:
                #Creation of the resourceType feature
                #We consider that all phrases have all the possible types
                for X in typeOfContent:
                    #We create random ressources type using a uniform distribution
                    temp = line[:-1]+"["+X+"]"
                    if temp not in res :
                        res.append(temp)
                        file.write("resourceType(dbo:"+temp+","+X+")\n")
                        #   +","+str(random.random())+")\n") NO NEED TO ADD THE EVALUATION YET

#We create a dictionary that will store every single operation we do

res = {}
with open(out,"w") as file:
    with open(inp,"r") as data:
        for line in data:
            #Creation of the resourceType feature
            #We consider that all phrases have all the possible types
            for X in typeOfContent:
                #We create random ressources type using a uniform distribution
                temp = line[:-1]
                #res.append(temp)
                res[temp]= X[:1]
                file.write("resourceType(dbo:"+temp+"["+res[temp]+"],"+X+")\n")
                    
                    
                    #   +","+str(random.random())+")\n") NO NEED TO ADD THE EVALUATION YET

