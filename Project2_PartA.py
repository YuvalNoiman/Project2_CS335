# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using exhaustive search approach
import ast

def create_combinations(size, items):
   #creates all combinations
   combinations = []
   for i in range(2 ** size):
      combo = []
      for j in range(size):
          if((i>>j) & 1) == 1:
              combo.append(items[j])
      combinations.append(combo)
   return combinations

def verify_combinations(M, items, canidate):
   #verifies the canidate
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
   #gets total value of the canidate
   if (canidate == None):
      return 0
   total = 0
   for x in range(len(canidate)):
      total = total + canidate[x][0]
   return total
   
def stock_maximization(M, items, size):
   #computes best stock value which fits parameter
   best = None
   combinations = create_combinations(size, items)
   for canidate in range(len(combinations)):
      if verify_combinations(M, combinations, canidate):
         if ((best == None) or (total_value(combinations[canidate]) > total_value(combinations[best]))):
            best = canidate
   if (best == None):
       return 0
   return total_value(combinations[best])
   
def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputA.txt","w")
   while True:
      try:
         size_of_array  = int(file1.readline())
         stocks_and_values = ast.literal_eval(file1.readline())
         amount = int(file1.readline())
         file1.readline()
         file2.write(str(stock_maximization(amount, stocks_and_values, size_of_array))+"\n\n")
      except:
         break
   file1.close()
   file2.close()

if __name__ == "__main__":
   main()
