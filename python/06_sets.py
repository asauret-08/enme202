# Sets

""" 
Topics
------
Set Declaration
Adding Elements to a Set
Removing Elements From a Set
Converting Between Lists and Sets
Joining Sets
Set Intersection
Subsets and Supersets
Checking Set Overlap
"""


# A Python set is a collection of unordered and unique elements.
#
# Mathematical set operations are available, including union, intersection, difference, 
# symmetric difference, subset, super set, and disjoint set.

print()
print('Set Declaration:')
print('---------------------------------------')

# creat an empty set:
s_empty = set()
print(f's_empty = {s_empty}')

# Creating a set with initial values using curly brackets:
s_init = {'item1', 'item2', 'item3'}
print(f's_init = {s_init}')

# Sets can be heterogeneous (i.e. hold different value types):
s_het = {'some text', 'c', 5, 3.21}
print(f's_het = {s_het}')

print()
print('Set length:')
print('---------------------------------------')
print(f'len(s_empty) = {len(s_empty)}')
print(f'len(s_init) = {len(s_init)}')
print(f'len(s_het) = {len(s_het)}')

print()
print('Accessing set values using "in":')
print('---------------------------------------')

# Because sets are unordered, indexing into a set is not possible.
# Instead, use the membership operator (in) to query set membership:
print('item1' in s_init)
print('item4' in s_init)
print(5 in s_het)


print()
print('Set Methods:')
print('---------------------------------------')

print("""
add()           Add an element to the set
clear()         Remove all the elements from the set
copy()	        Return a deep copy of the set
difference()	Return a set containing the difference between 
                two or more sets
difference_update()	 Removes the items in this set that are also
                     included in another, specified set
discard()	    Remove the specified item
intersection()	Return a set, that is the intersection of two or more sets
intersection_update()	 Remove the items in this set that are not 
                         present in other, specified set(s)
isdisjoint()	  Return whether two sets have a intersection or not
issubset()	      Return whether another set contains this set or not
issuperset()	  Return whether this set contains another set or not
pop()	          Remove & return an element from the set
remove()	      Remove the specified element
symmetric_difference()	Return a set with the symmetric differences 
                        of two sets
symmetric_difference_update()	Insert the symmetric differences from 
                                this set and another
union()	          Return a set containing the union of sets
update()	      Update the set with another set, or any other iterable
""")


print()
print('Adding Elements to a Set: add() and update()')
print('---------------------------------------')

# Add a single element using add() method:
s_het.add('new')
print(s_het)

# What if we try to add a value that is alread in the set?
s_het.add(5)
print(s_het)

# Add multiple elements using update() method:
s_het.update([1, 1/2, 'foo'])  # <-- update() takes list, tuple, or set as argument
print(s_het)

# Example of joining sets together:
foods = {'avacado', 'almond', 'bread'}
veggies = {'carrot', 'lettuce', 'brocolli'}
foods.update(veggies)
print(foods)


print()
print('Removing Elements From a Set:')
print('---------------------------------------')

# The remove() method removes a single element from a set:
s_init.remove('item1')
print(s_init)

# If the set does not contain the remove() argument as a value, an error
# will the thrown. To avoid this (if appropriate for your code!) use the
# discard() method instead:

s_init.discard('foo')      # "foo" is *not* in the set
print(s_init)
s_init.discard('item2')    # "item2" is in the set
print(s_init)

# All elements in a set can be cleared to yield an empty set via clear():
s_init.clear()
print(s_init)

# The set variable itself can be deleted from memory using the del command:
del s_init
print('s_init' in globals())


print()
print('Converting Between Lists and Sets:')
print('---------------------------------------')

# The set() function converts a list to a set. Because set elements are 
# unique, but list elements are not, duplicate values in a list will be 
# dropped when forming the set:
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(fruits)
set_of_fruits = set(fruits)
print(set_of_fruits)

# The list() function will convert a set into a list. By converting
# a list to a set then back into a list, duplicate items
# from the original list are removed
unique_fruits  = list(set(fruits))


print()
print('Joining Sets:')
print('---------------------------------------')

# union() is similar to update(), but it returns a new set instead of
# directly modifying an existing set as seen above.
#
# A.union(B) is mathematically equivalent to A ∪ B
#
fruits = {'avacado', 'grape', 'orange'}
veggies = {'carrot', 'lettuce', 'brocolli'}
foods = fruits.union(veggies)
print(foods)
print(fruits)


print()
print('Set Intersection:')
print('---------------------------------------')

# A.intersection(B) is mathematically equivalent to A ∩ B
#
# Use intersection() to play a card game. The dealer is holding a set of 8
# unique cards. The player guesses 2 of the cards, and wins when 
# at least 2 of the guesses are held by the dealer. Use intersection() to
# find the number of guessed cards in the dealer's hand:
dealer_hand = {2,3,5,6,7,9,11,13}
player_guess = {6,7,8}
print(f'number of correct guesses = {len(dealer_hand.intersection(player_guess))}')

# Another example, showing that set() can convert a string to a
# set of characters:
s1 = set('python')
s2 = set('pneumonoultramicroscopicsilicovulcanoconiosis')
print(s1.intersection(s2))


print()
print('Subsets and Supersets:')
print('---------------------------------------')

# Simple example:
s1 = {1, 2, 3, 4}
s2 = {2, 3}
print(s1.issubset(s2))      # False
print(s2.issubset(s1))      # True
print(s1.issuperset(s2))    # True
print(s2.issuperset(s1))    # False 


print()
print('Symmetric Difference:')
print('---------------------------------------')

# The "symmetric difference" between sets A and B is the set of all items from both A and B,
# except items that are present in both sets.
#
# A.symmetric_difference(B) is mathematically equivalent to (A\B) ∪ (B\A)
# (where \ is "set subtraction", i.e. A\B means all values in A not including those in B)

s1 = {1, 2, 3, 4}
s2 = {2, 3, 5, 6}
result = s1.symmetric_difference(s2)
print(result)



print()
print('Checking Set Overlap:')
print('---------------------------------------')

print(f'{s1} and {s2} have no overlaping elements: {s1.isdisjoint(s2)}')



"""
PROBLEMS

Easy
1. Create a set consisting of all integers from 1 to 5, inclusive.
2. Add "string" to the set.
3. Check if 5 is in the set.
4. Remove the value 2 from the set.

Medium + Hard
Given the sets set1 = {'foo', 1, 2, 3} and set2 = {2, 3, 4, 'foo'}, do the following:
5. Create a new set given by the union of the sets.
6. Create a new set given by the intersection of the sets.
7. Create a new set given by the difference between the sets.
8. Create a new set given by the symmetric difference of the sets.
9. Remove duplicate values of the list a = [1, 2, 2, 3, 4, 4, 5] in a single line of code.
10. Check if set1 = {1, 2} is a subset of set2 = {1, 2, 3}.
11. Check if set1 = {1, 2, 3} is a superset of set2 = {1, 2}.
"""







