def product_other_num(numbers):
    results = [0] * len(numbers)
    cache = [1, numbers[0]]
    for num in numbers[1:-1]:
        previous_product = cache[-1]
        cache.append(previous_product*num)
    print(f'cache: {cache}')

    single_cache = numbers[-1]
    results[-1] = cache[-1]
    single_cache_index = len(numbers)-2
    for i in list(range(len(numbers)-2,-1,-1)): # reversed list
        print('---------------')
        print(f'i: {i}, results: {results}')
        print(f'single_cache: {single_cache}, single_cache_index: {single_cache_index}')

        current_cache_num = cache[i]
        print(f'current_cache_num: {current_cache_num}')

        new_product = current_cache_num * single_cache
        print(f'new_product: {new_product}')

        results[i] = new_product
        print(f'results: {results}')

        single_cache *= numbers[single_cache_index]
        print(f'\nupdating single cache. single_cache: {single_cache}')
        print(f'numbers[single_cache_index]: {numbers[single_cache_index]}')
        single_cache_index -= 1

    return results


a = [1,7,3,4] # [84,12,28,21]
b = [3,2,6,5,9] # [540,810,270,324,180]
print(product_other_num(a))
