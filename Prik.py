#import numpy as np
#import pandas as pd
import random

class elgraph:
    def __init__(self):
        self.flag = False
        self.destrver = 0
        self.ways = []

def create(graph,n,i):
    cont = elgraph()
    YN = [True, False]
    graph.append(cont)
    for j in range(n):
        graph[i].ways.append(random.choice(YN))
    graph[i].destrver = random.random()

#Генератор графа
def creategraph(graph,n):
    for i in range(n):
        create(graph,n,i)
    for i in range(len(graph)):
        graph[i].ways[i] = False
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i].ways[j] == True and graph[j].ways[i] == False :
                choice = random.random()
                if choice < 0.5 :
                    graph[j].ways[i] = True
                else:
                    graph[i].ways[j] = False

    isolete = True
    iteration = 0
    while iteration < len(graph):
        iteration += 1
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i].ways[j]:
                    isolete = False
            if isolete:
                r = random.randint(0,len(graph))
                while r == i:
                    r = random.randint(0, len(graph))
                graph[i].ways[r] = True
                graph[r].ways[i] = True
                r = 0
            isolete = True
    #Генерация пути
    for i in range(len(graph) - 1):
       if graph[i + 1].ways[i] == False:
           graph[i + 1].ways[i] = True
           graph[i].ways[i + 1] = True

#Перегенерация вероятностей разрушения узлов
def createdestver(graph):
    for i in range(len(graph)):
        graph[i].destrver = random.random()

# Печать графа
def printgraph(graph):
    for i in range(len(graph)):
        print(graph[i].ways, end=" ")
        print(graph[i].destrver, end=" ")
        print(graph[i].flag, end=" ")
        print("")
    print("------------------------------------------------ \n")

#Проверка связности
def walkgraph(graph, con, j = 0):
    graph[j].flag = True
    for i in range(len(graph[j].ways)):
        if graph[j].ways[i] and graph[i].flag == False:
            walkgraph(graph,con ,i)
    for i in range(len(graph[j].ways)):
        if graph[i].flag == False:
            con = False
    if j == len(graph) - 1:
        if con:
            print("Граф связанный")
        else:
            print("Граф не связанный")

#Запись в файл
def writingtoafile(graph, con):
    with open("graph.txt", "a") as file:
        for i in range(len(graph)):
            file.write("[")
            for j in range(len(graph[i].ways)):
                if graph[i].ways[j]:
                    file.write("True")
                else:
                    file.write("False")
                if j < len(graph[i].ways):
                    file.write(", ")
            file.write("]")
            file.write(" ")
            file.write(str(graph[i].destrver))
            file.write("\n")
        if con:
            file.write("Граф связанный")
        else:
            file.write("Граф не связанный")
        file.write("\n--------------------------------\n\n")
        file.close()







#-----------------------------------------------------------------------------------------------------------------------
graph = []
con = True
creategraph(graph, 7)
printgraph(graph)
createdestver(graph)
walkgraph(graph, con)
printgraph(graph)
writingtoafile(graph, con)
