# The purpose of the walrus operator is to consolidate an assignment statement and a boolean expression when both
# assignment and expression would utilize a similar statement.

# Case: len(my_list) I had to type twice
my_list = [1,2,3,4,5]
if len(my_list) > 3:
    print(f'The list is {len(my_list)} element long. Too Long. Make it shorter. ')

# Solution:
print('\n Now, the walrus operator will eliminate calling the len() function twice.')
my_list = [1,2,3,4,5]
if (n := len(my_list)) > 3: # Don’t Forget the Parenthesis. n will return True if dont parenthesize the assignment part
                            # (meaning the boolean part is stored in n)
                            # and if we parenthesize, n will return the assignemnt part, ignoring the boolean part!

    print(f'The list is {n} element long. Too Long. Make it shorter. ')
print('Basically, without the parenthesis, the evaluation of len(my_list) > 3 is assigned.')


