import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
print(mtcars)

'''''
#1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.
plt.figure(figsize = (20, 5))
plt.bar(mtcars['mpg'], mtcars['cyl'], color='green', width = 0.2)
plt.xlabel("Potrosnja - MPG")
plt.ylabel("Broj cilindara")
plt.title("1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara")
plt.show()
'''''

'''''
#2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.
plt.figure(figsize = (10, 5))
plt.boxplot(mtcars)
plt.show()
'''''

#3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću
# potrošnju od automobila s automatskim mjenjačem?
plt.figure(figsize = (20, 5))
plt.scatter(mtcars['mpg'], mtcars['am'], c='blue')
plt.xlabel("Potrosnja - MPG")
plt.ylabel("Mjenač: 0 - automatic, 1 - manual")
plt.title("3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem?")
plt.show()

#4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem.
plt.figure(figsize = (20, 5))
plt.scatter(mtcars[['hp', 'qsec']], mtcars['am'], c='red')
plt.xlabel("Snaga i ubrzanje")
plt.ylabel("Mjenač: 0 - automatic, 1 - manual")
plt.title("4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem.")
plt.show()
