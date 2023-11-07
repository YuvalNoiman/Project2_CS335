# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using exhaustive search approach
import ast

def create_combinations(size, items):
   combinations = []
   i = 1
   while (i <= size):  
      combinations.append(items)
      i = i + 1
   #for x in range(1, (size * size)):
    #  combinations.append(
   return combinations

def create_combinations(size, items, combinations):
   if (size == 0): #size = 0
       return
   if (items not in combinations):
      for x in range(0, size):
      #combinations.append(items[x:size])
     #print(items[0:x])
     #print(items[x+1:size-1])
         create_combinations(size-1, items[0:x]+items[x+1:size], combinations)
      combinations.append(items)
   #create_combinations(size-1, items[0:size-2], combinations)
   """if ((size%2) == 0):
      y = int(size/2)
      print(y)
      list = items[0:y]+items[y+1:size]
      return create_combinations(size-1, list, combinations)
   if ((size%2) == 1):
      y = int(size/2)+1
      print(y)
      list = items[0:y]+items[y+1:size]
      return create_combinations(size-1, list, combinations)"""
   #return create_combinations(size-1, items[1:size], combinations)
   
def powerset(seq): #returns wrong number
   if len(seq) == 1:
      yield seq
      #yield []
   else:
      for item in powerset(seq[1:]):
         yield [seq[0]]+item
         yield item

def verify_combinations(M, items, canidate):
   value = items[canidate]
   if (len(value) > len(items)):
      return False
   amount = 0
   for x in range(len(value)):
      amount = amount + value[x][1]
   if (amount <= M):
      return True
   return False

def total_value(canidate):
   if (canidate == None):
      return 0
   total = 0
   for x in range(len(canidate)):
      total = total + canidate[x][0]
   return total
   
def stock_maximization(M, items):
   best = None
   for canidate in range(len(items)):
      if verify_combinations(M, items, canidate):
         if ((best == None) or (total_value(items[canidate]) > total_value(items[best]))):
            best = canidate
   return total_value(items[best])
   
def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputA.txt","w")
   while True:
      try:
         #print(file1.readline())
         size_of_array  = int(file1.readline())
         stocks_and_values = ast.literal_eval(file1.readline())
         amount = int(file1.readline())
         file1.readline()
         combo = []
         create_combinations(size_of_array, stocks_and_values, combo)
         print(combo)
         #combinations = [x for x in powerset(stocks_and_values)]
         #print(combinations)
         #print(stock_maximization(amount,combinations))
         print(stock_maximization(amount, combo))
         #file2.write(str(stock_maximization(amount,combinations))+"\n\n")
         file2.write(str(stock_maximization(amount,combo))+"\n\n")
      except:
         break

   file1.close()
   file2.close()

if __name__ == "__main__":
    #combo = []
    #create_combinations(7, [1, 2, 3, 4, 5, 6, 7], combo)
    #print(combo)
    #print(len(combo))
    #res = []
    #for i in combo:
      #  if i not in res:
    #        res.append(i)
   # print(len(res))
    main()
