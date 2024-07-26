# For Else
"""
In this for else loop syntax like below
for i in range():
    ....
    ....
    ....
else:
    ...
    ...
    ...
in this for loop successfully completed then else block execute
otherwise else block doesn't execute
if loop exit by break keyword then else block doesn't execute
"""
# Example for else block execution:
for i in range(5):
    print(i)
else:
    print("Loop successfully completed!")
"""
output:
    0
    1
    2
    3
    4
Loop successfully completed!
here clearly we can observe else block executed
"""
# Example for without execution else block by using break
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop successfully completed!")
"""
output:
    0
    1
    2
    3
 
here clearly we can observe else block didn't execute
"""
