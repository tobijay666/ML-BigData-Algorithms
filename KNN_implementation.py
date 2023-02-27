# HI GUYS (¬‿¬)

import matplotlib.pyplot as plt
import numpy as np
import math 

# enter the K value
k = 3

# enter the x & y values as a list
xval = [8,9,6,8.5,5]
yval = [7,6,4.5,5,4]


# enter the new variable here
new_data = np.array([6.5,7.5])

# declaring list to store the Euclidean distances
Euclidean_Dis = []

# calculating euclidean distances 
for dot in range(len(xval)):
    Euclidean_Dis.append( math.sqrt(((float(new_data[0]) - float(xval[dot]))**2) + ((float(new_data[1]) - float(yval[dot]))**2)))
    # ಠ_ರೃ if you change the above code plz send... too lazy to do anything about it... haha...

# # for debugging
# print (Euclidean_Dis) 

# getting the distances in to a ordered dictionary
new_dataic = dict(enumerate(Euclidean_Dis, start=1))
# print(new_dataic)

# sorting the distances according to their values
sortedDic = sorted(new_dataic.items(), key=lambda x:x[1])
# print(sortedDic)

# getting K amount of euclidean distances
for xx in range(k):
    print(sortedDic[xx])

# if you want you can extend this to a fully automated format by adding another list where the titles/classes
# are contained. {too lazy and boring to do it my self (－‸ ლ) } . if u do it, then by using the keys of the dictionary
# u can get the classes which belongs to the respective k values.
# then you can simply get the max of that list.
# ( ๑‾̀◡‾́)σ"   ᕙ(⇀‸↼‶)ᕗ


# plotting the x and y values given above. 
# add titles and whatnot, if you feel like it... ( ˇ෴ˇ )
plt.plot(xval,yval,'o')
plt.show()

# UR WELCOME!!!
