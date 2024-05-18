solution = int("AR", 36)

print(solution)
print("state == " + str(solution % 31) + " mod 31")
print("state == " + str(solution % 23) + " mod 23")
print("state == " + str(solution % 47) + " mod 47")