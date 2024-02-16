print("Welcome to the Love Calculator!")
first_name = input("What is your name?\n")
second_name = input("What is their name?\n")

# Angela's solution
# lower_case_names = first_name + second_name
# t = lower_case_names.count("t")... etc...

lower_first_name = first_name.lower()
lower_second_name = second_name.lower()

t = lower_first_name.count("t") + lower_second_name.count("t")
r = lower_first_name.count("r") + lower_second_name.count("r")
u = lower_first_name.count("u") + lower_second_name.count("u")
e = lower_first_name.count("e") + lower_second_name.count("e")

l = lower_first_name.count("l") + lower_second_name.count("l")
o = lower_first_name.count("o") + lower_second_name.count("o")
v = lower_first_name.count("v") + lower_second_name.count("v")

word_true = t + r + u + e
word_love = l + o + v + e
total = word_true * 10 + word_love

print(f"T occurs: {t} times\nR occurs: {r} times\nU occurs: {u} times\nE occurs: {e} times\nTotal={word_true}\n\nL occurs: {l} times\nO occurs: {o} times\nV occurs: {v} times\nE occurs: {e} times\nTotal={word_love}\n")

if total <10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")