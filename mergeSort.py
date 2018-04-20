#!/usr/bin/python -tt

# Merge Sort the given list of N numbers

import sys

def main():
  input = [9, 6, 5, 4, 3, 2, 1, 8]
  output = mergeSort(input)
  print output




# Merge Sort Function
# PSudoCode:
# 1. Dive the array into 2 equal parts
# 2. Solve both parts recursively and get two small sorted arrays
# 3. Merge Both arrays to get the final solution - a sorted full array

step = 1

def mergeSort(input_list):
  #print input_list
  size = len(input_list)
  
  #base case
  if size == 1:
    return input_list
  
  # Recursive call: Divide into two lists and call mergeSort on both of them
  # The output is two sorted small lists
  list1 = mergeSort(input_list[0:size/2])
  list2 = mergeSort(input_list[size/2:])
  
  global step
  print "step " + str(step)
  print list1
  print list2
  step = step + 1
  
  output = []
  
  #Merge step: Merge the two sorted smaller lists
  while len(list1) != 0 and len(list2) != 0:
    if list1[0]>list2[0]:
      output.append(list2[0])
      list2.remove(list2[0])
    else:
      output.append(list1[0])
      list1.remove(list1[0])
    
  if len(list1) == 0:
    output.extend(list2)
  else:
    output.extend(list1)
  
  print output
  print '\n'
  
  return output


   
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()