def print_return_infor(total):
    list_price = [500, 200, 100, 50, 20, 10, 1]
    count = 0

    for i in list_price:
        count_500 = int(total/i)
        total -= i * count_500
        if count_500 != 0:
            print(i, "$: ", count_500) 

def calc_total_price(a, b):
    return a * b

def calc_return(a, b):
    return b - a
    
def main():

    PRICE_1KG = 21 # $
    weight_apple = float(input("weight: "))
    money_given = float(input("mojney: "))

    sum_money = calc_total_price(weight_apple, PRICE_1KG)
    money_retun = calc_return(sum_money, money_given)

    print(sum_money, "\n", money_retun)
    print_return_infor(money_retun)

main()