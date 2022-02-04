# -*- coding: utf-8 -*-
"""
@authors: bennini amine , ali abboud
"""
# les packages
import findspark
findspark.init("C:/spark")

from pyspark import SparkContext

import numpy as np
import random
import time
import math 
import pandas as pd
  
# session sparkContext
sc = SparkContext(master="local",appName="Spark Demo")

# une function qui permet de simuler un point p avec deux coordonnees x et y pour déterminer si le  point simulé est dans le cercle ou pas
def is_point_inside_unit_circle(p):
    # simuler deux point  x et y
    x, y = random.random(), random.random()   
    return 1 if x*x + y*y < 1 else 0 #  pour verifier si ces deux point sont dans la cercle
#cette fonction nous permet d'estimer la valeur de pi en utilisant les rdds de spark
def pi_estimator_spark(n):
    tot_in=0
    count = sc.parallelize(range(0, n))
    test=count.map(is_point_inside_unit_circle).collect()
    #compte le nombre de point qui se trouve dans le cercle
    for i in range(n):
        if test[i]==1:
           tot_in += 1 
    
    # calcul de pi
    pi=(4*tot_in)/n
    return pi
#cette fonction nous permet d'estimer la valeur de pi en utilisant numpy

def pi_estimator_numpy(n):
    tot_in=0
    tot_out=0
#compte le nombre de point qui se trouve dans le cercle
    for i in range(n):
        test=is_point_inside_unit_circle(n)
        if test==1:
            tot_in+=1

    # calcul de pi

    pi=(4*tot_in)/n
    #print("valeur de pi =",pi)
    return pi


# maintenant on définit une fonction qui  permet d'afficher les estimations de pi en utilisant les deux fonctions (numpy et les rdds de spark)
def affichage_tab(n):
    #  en utilisant les rdds spark
    start_time_spark = time.time()
    pi_spark =pi_estimator_spark(n)
    interval_spark = time.time() - start_time_spark  
    # en utilisant numpy
    start_time_numpy = time.time()
    pi_numpy=pi_estimator_numpy(n)
    interval_numpy = time.time() - start_time_numpy 
    aff={"N = "+str(n):["estimation pi","Ecart % Math.pi","Total time in seconds"],"spark":[pi_spark,pi_spark-math.pi,interval_spark],"numpy":[pi_numpy,pi_numpy-math.pi,interval_numpy]}
    aff=pd.DataFrame(aff)
    print("\n")
    print(aff)
    
# cas pour n=100000
n=100000
random.seed(135)
affichage_tab(n)

# cas pour n=1000000
n=1000000
random.seed(135)
affichage_tab(n)

sc.stop()

