import random
import matplotlib.pyplot as plt
 
k = int(input("No of times you want to flip the coin = ")) 
l = int(input("No of times you want to conduct this experiment = "))

def prob_heads(coin_heads,k):
        prob = float(coin_heads)/float(k)
        return prob
 
i = 1
x = []
y = []
 
while i < l+1:
        coin_heads, coin_tails, timesflipped = 0, 0, 0
        while timesflipped < k:
                r = random.randrange( 2 )
                if r == 0:
                        coin_heads += 1
                else:
                        coin_tails += 1
                timesflipped += 1
        print("Out of %d flips, "%k + str(coin_heads) + " were heads and " + str(coin_tails) + " were tails.")
        a=[i,prob_heads(coin_heads,k)]
        for j in range(0,l):
                x.append(a[0])
                y.append(a[1])
        i += 1
      
plt.scatter(x, y)
plt.xlabel('Experiments')
plt.ylabel('Probability of getting head')
plt.title('Coin Simulation Graph')
plt.show()
