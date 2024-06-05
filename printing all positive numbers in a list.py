def print_all_positives(list):
  for i in list[:]:
    if i<0:
      list.remove(i)
  return list
list1=[1,2,3,-1,-2]
list2=[4,5,-4,-5]
print(print_all_positives(list1))
print(print_all_positives(list2))
  
