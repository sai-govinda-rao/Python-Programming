# Beak, Continue and Pass keyword
"""
we can use these keyword to any loops
for,while,....etc
Break:
    If you want to break the loop/ stop the execution of the loop then use break keyword
    syntax:
        while Condition:
            //block of code
            if break condition:
                True Exit the Loop
Continue:
    if you want to continue the execution of the loop then use Continue keyword
    while Condition:
        //block of code
        if continue condition:
            continuous the loop execution
Pass:
    when we create a loop or Function or class if we don't implement it right now
    maybe we will make changes in future then pass the function or loop with the help
    of pass keyword
    syntax:
        def MyFunction:
            pass
    when we call the function it doesn't write anything
"""
# Example for break, continue and pass keywords
number = 1
while True:  # we create infinite loop
    count = 1
    while count <= 10:
        print(f"{number} x {count} = {number*count}")
        count += 1
    def display_number_function():
        pass  # pass the function by using pass keyword
        # we will modify this in anytime by removing the pass keyword
    user_response = input("Do you want to continue the loop (yes->y/no->n):").lower()
    if user_response == "y":
        number += 1
        continue  # continue the infinite loop by using continue keyword
    else:
        break  # stop the infinite loop by using break keyword
"""
output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
Do you want to continue the loop (yes->y/no->n):y
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
Do you want to continue the loop (yes->y/no->n):y
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Do you want to continue the loop (yes->y/no->n):n
"""

