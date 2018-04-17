
def get_max_profit_o_2n(stock_prices_yesterday):
    min_element = min(stock_prices_yesterday[:-1])
    min_element_index = stock_prices_yesterday[:-1].index(min_element)
    print(f'min_element_index: {min_element_index}, min_element: {min_element}')

    max_element = max(stock_prices_yesterday[min_element_index+1:])
    print(f'stock_prices_yesterday[min_element_index+1:]: {stock_prices_yesterday[min_element_index+1:]}')
    print(f'max_element: {max_element}')

    return max_element - min_element

def get_max_profit_o_n(stock_prices_yesterday):
    min_element = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - min_element

    for current_price in stock_prices_yesterday:
        profit = current_price - min_element

        print('----------')
        print(f'current_price: {current_price}, min_element: {min_element}')
        print(f'profit: {profit}, max_profit: {max_profit}')

        if profit > max_profit:
            max_profit = profit

        if current_price < min_element:
            min_element = current_price

    return max_profit

a = [10, 7, 5, 8, 11, 9] # 6
b = [-10,-5,-20,-1] # 19
c = [-10,-5,-20,1] # 21
print(get_max_profit_o_n(c))
