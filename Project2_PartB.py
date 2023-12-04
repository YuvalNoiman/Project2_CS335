# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using dynamic programming
import ast

def stock_maximization(M, items, size):
   array = [[0 for x in range(M + 1)] for x in range(size + 1)]
   for i in range(0, size + 1):
      for w in range(0, M + 1):
         if (i == 0 or w == 0):
            array[i][w] = 0
         elif (items[i-1][1] <= w): # max(1 case, 0 case)
            array[i][w] = max(items[i-1][0]+ array[i-1][w-items[i-1][1]], array[i-1][w])
         else: # 0 case
            array[i][w] = array[i-1][w]
   return array[size][M]

def max(case1, case0):
   if case1 >= case0:
      return case1
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
    main()
