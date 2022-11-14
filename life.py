from blessed import terminal
from random import randint, choice

status = ["0","1"]

def create_generation(width, height):
    generation = []
    for x in range(height):
        generation.append([])
        for y in range(width):
            if x == 0 or x == height-1 or y == 0 or y == width-1:
                generation[x].append("0")
            else:
                generation[x].append(choice(status))
    return generation
def generation_to_string(generation):
    gen_aux = []
    for elem in generation:
        elem_string = create_string(elem)
        gen_aux.append(elem_string)
    return gen_aux

def create_string(array):
    string = ""
    for i in array:
        string+=i
    return string

term = terminal.Terminal()
print(term.home + term.clear)
#Primera generacion (array)
gen = create_generation(10,5)
gen_string = generation_to_string(gen)

for elem in gen_string:
    print(elem)



        

    