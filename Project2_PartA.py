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
   return combinations
   
def verify_combinations(M, items, canidate):
   if (len(canidate) > len(items)):
      return False
   amount = 0
   for x in range(len(canidate)):
      amount = amount + canidate[x][1]
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
      if verify_combinations(M, items, items[canidate]):
         if ((best == None) or (total_value(items[canidate]) > total_value(best))):
            best = canidate
   return best
   
def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputA.txt","w")
   while True:
      try:
         size_of_array  = int(file1.readline(()
         stocks_and_values = ast.literal_eval(file1.readline())
         amount = int(file1.readline())
         file1.readline()
         combinations = create_combinations(size_of_array, stocks_and_values)
         file2.write(str(stock_maximization(amount,combinations)+"\n\n")
      except:
         break

   file1.close()
   file2.close()

if __name__ == "__main__":
    main()
