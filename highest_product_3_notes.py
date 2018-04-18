def list_of_ints(array_of_3_inputs):
    highest_product = 1

    neg_nums = []
    pos_nums = []

    first_min_neg = 0
    second_min_neg = 0
    first_max_pos = 0
    second_max_pos = 0

    print(f'array_of_3_inputs: {array_of_3_inputs}')
    for number in array_of_3_inputs:
        if number < 0:
            neg_nums.append(number)
            if number < first_min_neg:
                second_min_neg = first_min_neg
                first_min_neg = number
            elif number < second_min_neg:
                second_min_neg = number
        else:
            pos_nums.append(number)
            if number > first_max_pos:
                second_max_pos = first_max_pos
                first_max_pos = number
            elif number > second_max_pos:
                second_max_pos = number
    print(f'\nneg_nums: {neg_nums}, first_min_neg: {first_min_neg}, second_min_neg: {second_min_neg}')
    print(f'pos_nums: {pos_nums}, first_max_pos: {first_max_pos}, second_max_pos: {second_max_pos}\n')

    min_neg_product = first_min_neg * second_min_neg
    max_pos_product = first_max_pos * second_max_pos

    if max_pos_product > min_neg_product:
        array_of_3_inputs.remove(first_max_pos)
        array_of_3_inputs.remove(second_max_pos)
        highest_product_2 = max_pos_product
    elif min_neg_product > max_pos_product:
        array_of_3_inputs.remove(first_min_neg)
        array_of_3_inputs.remove(second_min_neg)
        highest_product_2 = min_neg_product
    print(f'min_neg_product: {min_neg_product}, max_pos_product: {max_pos_product}')
    print(f'highest_product_2: {highest_product_2}')
    print(f'array_of_3_inputs: {array_of_3_inputs}')

    highest_product_3 = float('-inf')
    for number in array_of_3_inputs:
        if number * highest_product_2 > highest_product_3:
            highest_product_3 = number * highest_product_2

    print(f'highest_product_3: {highest_product_3}')
    return highest_product_3

a = [-5,8,-10,4,-2,0] # (-5)(-10)(8), 400
b = [1,2,3] # 6
c = [-1,-3,-4,-20] # -1,-3,-4 => -12
d = [3,-7,0,1,-2] # -7,-2,3 => 42
e = [-7,0,1,-3,-7] # -7,1,-3 => 21

# doesn't work yet
f = [3,-7,0,1] # 0,1,3 => 0

print(list_of_ints(c))
