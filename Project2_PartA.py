# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using exhaustive search approach
import ast

def create_combinations(size, items):
   combinations = []
   values = []
   for x in items:
      values.append(x)
   for i in range(2 ** len(values)):
      combo = []
      for j in range(size):
          if((i>>j) & 1) == 1:
              combo.append(values[j])
      combinations.append(combo)
   return combinations

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
   if (best == None):
       return 0
   return total_value(items[best])
   
def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputA.txt","w")
   while True:
      try:
         size_of_array  = int(file1.readline())
         stocks_and_values = ast.literal_eval(file1.readline())
         amount = int(file1.readline())
         file1.readline()
         combinations = create_combinations(size_of_array, stocks_and_values)
         print(stock_maximization(amount, combinations))
         file2.write(str(stock_maximization(amount, combinations))+"\n\n")
      except:
         break
   file1.close()
   file2.close()

if __name__ == "__main__":
   main()
