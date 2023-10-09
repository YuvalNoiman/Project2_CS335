# Name: Yuval Noiman
# Date: 10/9/2023
# File Purpose: Calculates stock purchase maximization using dynamic programming
import ast

def main():

   file1 = open("Input.txt", "r")
   file2 = open("OutputB.txt","w")
   while True:
      try:
         size_of_array  = int(file1.readline(()
         stocks_and_values = ast.literal_eval(file1.readline())
         Amount = int(file1.readline())
         file1.readline()
         #file2.write(str()+"\n\n")
      except:
         break

   file1.close()
   file2.close()

if __name__ == "__main__":
    main()
