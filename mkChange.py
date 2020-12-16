import numpy as np
import sys

coins = [1,5,10,25]
calls = 0
reads = 0

  
''' Making Change based on the either or recursion
    slide 6 06-coinsPA lecture
'''
def mkChangeDC(n, c):
   global calls
   # increment global calls with 1
   calls += 1
   if(c == 0):
      return 1


   if(c > 0):
      if(coins[c] > n):
         return mkChangeDC(n,c-1)
      else:
         return mkChangeDC(n - coins[c],c) + mkChangeDC(n,c-1)

''' Dynamic Programming version of mkChangeDC'''     
def mkChangeDP(cap):
   global reads
   # increment global redas with 1 if you do 1 read, and with 2 if you do 2
   lenh = len(coins) - 1
   book = [[1]*cap] + [[0]*cap]*lenh

   for i in range(1,len(coins)):
      for j in range(cap):
         if coins[i] > j:
            book[i][j] = book[i-1][j]
            reads += 1
         else:
            book[i][j] = book[i-1][j] + book[i][j-coins[i]]
            reads += 2
   return book[len(coins) - 1][cap - 1]

if __name__ == "__main__":
   '''mkChangeDP(5 + 1)'''
   c = len(coins)-1
   print()
   print("Making change with coins:", coins)

   # performance data: [[n, complexity], ... ]
   dataDC  = []
   dataDP  = []
   
   for n in range(200,2050,200):
      print()
      print("Amount:",n)
      
      calls = 0
      ways = mkChangeDC(n,c)
      print("DC", ways, calls, "calls")
      dataDC.append([n,calls])
                        
      reads = 0
      ways = mkChangeDP(n+1)
      print("DP", ways, reads, "reads")
      dataDP.append([n,reads])
      
      
   print("dataDC:", dataDC)
   np.savetxt('dataDC', dataDC, delimiter=',', fmt='%d')

   
   print("dataDP:", dataDP)
   np.savetxt('dataDP', dataDP, delimiter=',', fmt='%d')
   
