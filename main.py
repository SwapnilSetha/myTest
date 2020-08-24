from question2_solution import countPairsWithDiffK
from question3_solution import get_indices
from question4_solution import iterations


print("------question2_solution Result Start--------\n")
arr = [1, 4, 7, 10]
n = len(arr)
k = 3

print("We will have {} pairs: {}".format(k, countPairsWithDiffK(arr, n, k)))

print("** question2_solution Result End **\n\n")


print("------question3_solution Result Start--------\n")
data = [
    ("username1", "phone_number1", "email1"),
    ("usernameX", "phone_number1", "emailX"),
    ("usernameZ", "phone_numberZ", "email1Z"),
    ("usernameZ34", "phone_numberZ434", "email1Zz"),
    ("usernameY", "phone_numberY", "emailX"),
]
get_indices(data)

print(get_indices(data))
print("** question3_solution Result End **\n\n")


print("------question4_solution Result Start--------\n")
iterations()

print("** question4_solution Result End **\n\n")
