# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using dynamic programming
import ast

"""def stock_maximization(M, items, size):
   #values = []
   #weights = []
   array = [[0 for x in range(M + 1)] for x in range(size + 1)]
   #print(array)
   for i in range(0, size + 1):
      for w in range(0, M + 1):
         if (i == 0 or w == 0):
            array[i][w] = 0
         #elif (weights[i-1] <= w): # max(1 case, 0 case)
         elif (items[i-1][0] <= w): # max(1 case, 0 case)
            #array[i][w] = max(values[i-1]+ array[i-1][w-weights[i-1]], array[i-1][w])
            #print(array)
            array[i][w] = max(items[i-1][1]+ array[i-1][w-items[i-1][0]], array[i-1][w])
         else: # 0 case
            array[i][w] = array[i-1][w]
   print(array)
   return array[size][M]"""

def stock_maximization(M, items, size):
   #values = []
   #weights = []
   array = [[0 for x in range(M + 1)] for x in range(size + 1)]
   #print(array)
   for i in range(0, size + 1):
      for w in range(0, M + 1):
         if (i == 0 or w == 0):
            array[i][w] = 0
         #elif (weights[i-1] <= w): # max(1 case, 0 case)
         elif (items[i-1][1] <= w): # max(1 case, 0 case)
            #array[i][w] = max(values[i-1]+ array[i-1][w-weights[i-1]], array[i-1][w])
            #print(array)
            array[i][w] = max(items[i-1][0]+ array[i-1][w-items[i-1][1]], array[i-1][w])
         else: # 0 case
            array[i][w] = array[i-1][w]
   #print(array)
   return array[size][M]

def max(case1, case0):
   #print(str(case1) + "  case1")
   #print(str(case0) + "  case0")
   if case1 >= case0:
      return case1
   #if (case1 < case0):
    #  print(str(case1) + " case1 + case0: " + str(case0))
   return case0

def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputB.txt","w")
   while True:
      try:
         size_of_array  = int(file1.readline())
         stocks_and_values = ast.literal_eval(file1.readline())
         amount = int(file1.readline())
         file1.readline()
         print(stock_maximization(amount, stocks_and_values, size_of_array))
         file2.write(str(stock_maximization(amount, stocks_and_values, size_of_array))+"\n\n")
      except:
         break
   file1.close()
   file2.close()

if __name__ == "__main__":
    """size_of_array = 4
    Stocks = [[1,2],[4,3],[3,6],[6,7]]
    Amount = 12
    print(stock_maximization(Amount, Stocks, size_of_array))
    size_of_array = 4
    Stocks = [[3,2],[4,3],[5,3],[6,7]]
    Amount = 10
    print(stock_maximization(Amount, Stocks, size_of_array))
    size_of_array = 2
    Stocks = [[10,1],[13,2]]
    Amount = 1
    print(stock_maximization(Amount, Stocks, size_of_array))"""
    main()
