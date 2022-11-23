qs = {
    "How many wings does as bee have?" : "4",
    "What was the name of the first Space Shuttle?" : "Columbia",
    "What city hosted the 1932 Summer Olympics" : "Los Angeles",
    "Who wrote Great Expectations?" : "Charles Dickens",
    "What is the tallest mountain in North America?" : "Denali",
    "What metal is liquid at room temperature?" : "Mercury",
    "What planet is closest to the sun?" : "Mercury",
    "What is the capital of England?" : "London",
    "What group sang the origninal version of Africa?" : "Toto",
    "What is Mario's brother's name?" : "Luigi"
    }

score = 0

print("Welcome to Trivia Master!")
name = input("Please enter your name: ")
print("Okay " + name + ", answer the following")

# q is the variable for questions (keys)
# a is the variable for answers (values)
for q, a in qs.items():
    print(q)
    response = input("What is your answer?\t")

    if response.lower() == a.lower():
        score = score + 1
        print("Correct!")
    else:
        print("I'm sorry, game over!")
        break

print("Your score was " + str(score))