# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
  for i in range(len(nums)):
    if i < len(nums) - 1:
      if nums[i] == 3 and nums[i+1] == 3:
        return True
  return False

# print(has_33([1, 3, 3])) # → True
# print(has_33([1, 3, 1, 3]))# → False
# print(has_33([3, 1, 3]))# → False



# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
  return ''.join([letter*3 for letter in text])

print(paper_doll('Hello'))



# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a, b, c): 
  cards = [a, b, c]
  total = sum(cards)

  if total > 21:
    if 11 in cards:
      total -= 10
    if total > 21: 
      return 'Bust'
    else:
      return total
  else:
    return total


# print(blackjack(5,6,7))
# print(blackjack(9,9,9))
# print(blackjack(9,9,11))


def spy_game(nums):
  target = [0, 0, 7]
  idx = 0 
  for num in nums:
    if idx > 2: break
    if (num == target[idx]): idx += 1
  if idx >= 3: return True
  else: return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))