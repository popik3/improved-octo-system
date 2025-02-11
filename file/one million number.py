filename = 'pi_digits.txt.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(f"{pi_string[:11]}")
print(len(pi_string))