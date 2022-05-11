# binary search with recursion

def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'

  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
#base case
#checks if mid value is equal to target and returns index
  if mid_val == target:
    return mid_idx

#checks if mid value is greater than target
# splices list 0-mid (noninclusive), recursively calls binary search
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)

#checks if mid value is less than target
# splices list mid+1 to -1 index, recursively calls binary search on right half
  if mid_val < target:
    right_half = sorted_list[mid_idx + 1:]
    result = binary_search(right_half, target)

    #error occurs if you try to add 'value not found' to mid index', so I checked for it

    if result == 'value not found':
      return result
    else:
      return result + mid_idx + 1
  
# for testing
sorted_values = [13, 14, 15, 16, 17]
print(binary_search(sorted_values, 13))