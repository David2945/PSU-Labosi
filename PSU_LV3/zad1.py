import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)
#1. Kojih 5 automobila ima najveću potrošnju
print(mtcars.sort_values('mpg')[0:5])
#2. Koja 3 automobila s 8 cilindara imaju najmanju potrosnju
print(mtcars.sort_values('mpg', ascending = False)[(mtcars.cyl == 8)][0:3])
#3.Kolika je srednja potrošnja automobila sa 6 cilindara
print(mtcars[(mtcars.cyl == 6)]['mpg'].mean())
#4.Kolika je srednja potrošnja automobila s 4 cilindara mase 2000-2200
print(mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & ( mtcars.wt <= 2.2)]['mpg'].mean())
#5.Koliko je automobila s ručnim, a koliko s automatskim mjenjačem
print(mtcars[(mtcars.am == 1)].count().car)
print(mtcars[(mtcars.am == 0)].count().car)
#6.Koliko je automobila s automatskim mjenjačem i snagom preko 100 hp
print(mtcars[(mtcars.am == 1) & (mtcars.hp > 100)].count().car)
#7.Kolika je masa svakog automobila u kg
print(mtcars.wt * 0.45 * 1000)