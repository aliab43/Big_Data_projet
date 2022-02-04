
Réalisé par:
BENNINI AMINE ET ABBOUD ALI
# ESTIMATION DE PI
-------------------------------------
## EXÉCUTION DU CODE
- open terminal
- pip install pyspark
- git clone https://github.com/aliab43/Big_Data_projet
- python src/script.py

-----------------------------------------
### Estimation de pi si n=100000
------------------------------------------------------------
n=100000                spark                   numpy
------------------------------------------------------------
temps d'exuction      1.941759                    0.090170
------------------------------------------------------------
valeur de pi          3.139840                     3.144960
------------------------------------------------------------
écart %Math.pi        -0.001753                      0.003367
------------------------------------------------------------

### Estimation de pi si n=1000000
------------------------------------------------------------
n=1000000                spark                   numpy
------------------------------------------------------------
temps d'exuction      1.289558                  0.491911
------------------------------------------------------------
valeur de pi         3.140136                     3.143464
------------------------------------------------------------
écart%Math.pi        -0.001457                      0.001871
------------------------------------------------------------

On constate que plus que n est assez grand plus que l'écart%Math.pi est petit.

