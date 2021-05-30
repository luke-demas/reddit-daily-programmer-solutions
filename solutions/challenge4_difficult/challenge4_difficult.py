# r/dailyprogrammer
# challenge 4, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

# solution by Luke Demas

nums = []
nums.append(input("What is the first number?\n"))
nums.append(input("What is the second number?\n"))
nums.append(input("What is the third number?\n"))
nums.append(input("What is the fourth number?\n"))

for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if nums.index(num1) == nums.index(num2) or nums.index(num1) == nums.index(num3) or nums.index(num2) == nums.index(num3):
                pass
            else:
                if (int(num1) + int(num2)) == int(num3):
                    print(num1 + " + " + num2 + " = " + num3)
                if (int(num1) - int(num2)) == int(num3):
                    print(num1 + " - " + num2 + " = " + num3)
                if (int(num1) * int(num2)) == int(num3):
                    print(num1 + " * " + num2 + " = " + num3)
                if (int(num1) / int(num2)) == int(num3):
                    print(num1 + " / " + num2 + " = " + num3)