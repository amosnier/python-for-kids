# String with new line
print('''How do dinosaurs pay their bills?
With tyrannosaurus checks!''')

# String with single and double quotes
print('''He said, "Aren't can't shouldn't wouldn't."''')
print("He said, \"Aren't can't shouldn't wouldn't.\"")

# Embedded value in string
score = 1000
print("You score is %s points" % score)

# Changing an embedded string
text = '%s is a programming language'
language1 = 'Python'
language2 = 'C++'
print(text % language1)
print(text % language2)

# Print hexadecimal values
print('Hexadecimal is often used instead of decimal in programming')
print('0 in hex: %x' % 0)
print('9 in hex: %x' % 9)
print('10 in hex: %x' % 10)
print('11 in hex: %x' % 11)
print('12 in hex: %x' % 12)
print('13 in hex: %x' % 13)
print('14 in hex: %x' % 14)
print('15 in hex: %x' % 15)
print('16 in hex: %x' % 16)
print('32 in hex: %x' % 32)
print('255 in hex: %x' % 255)
print('256 in hex: %x' % 256)

# Several embedded values
nums = 'What did the number %s say to the number %s? Nice belt!!'
print(nums % (0, 8))

# Adding strings
first_part = "First part of the string, "
second_part = "second part of the string"
print(first_part + second_part)
print(first_part, second_part)

# Multiply strings
print("Ten times 'a':", 10 * 'a')
#print(1000 * 'snirt')
