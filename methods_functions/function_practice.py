# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
  for i in range(len(nums)):
    if i < len(nums) - 1:
      if nums[i] == 3 and nums[i+1] == 3:
        return True
  return False

print(has_33([1, 3, 3])) # → True
print(has_33([1, 3, 1, 3]))# → False
print(has_33([3, 1, 3]))# → False



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
  return ''.join([letter*3 for letter in text])

print(paper_doll('Hello'))