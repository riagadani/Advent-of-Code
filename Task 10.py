def look_say_look(input):
    current = input[0]
    count = 0
    answ = ""
    for letter in input:
        if (letter == current):
            count += 1
        else:
            answ = answ + str(count)
            answ = answ + current
            current = letter
            count = 1
    answ = answ + str(count)
    answ = answ + current
    return answ

input = "3113322113"
for i in range(0,50):
    input = look_say_look(input)

print(len(input))
