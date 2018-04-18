def list_of_ints(array_of_3_inputs):
    highest = array_of_3_inputs[0]
    lowest = array_of_3_inputs[0]

    highest_product_of_2 = array_of_3_inputs[0]
    lowest_product_of_2 = array_of_3_inputs[0]
    highest_product_of_3 = array_of_3_inputs[0]

    print(f'array_of_3_inputs: {array_of_3_inputs}')
    for number in array_of_3_inputs:
        if number > highest:
            highest_product_of_2 = highest * number
            highest = number
        if number < lowest:
            lowest_product_of_2 = lowest * number
            lowest = number

    print(f'highest: {highest}, lowest: {lowest}')
    print(f'highest_product_of_2: {highest_product_of_2}, lowest_product_of_2: {lowest_product_of_2}')



a = [-5,8,-10,4,-2,0] # (-5)(-10)(8), 400
b = [1,2,3] # 6
c = [-1,-3,-4,-20] # -1,-3,-4 => -12
d = [3,-7,0,1,-2] # -7,-2,3 => 42
e = [-7,0,1,-3,-7] # -7,1,-3 => 21
f = [3,-7,0,1] # 0,1,3 => 0
g = [1,10,-5,1,-100]

print(list_of_ints(g))
