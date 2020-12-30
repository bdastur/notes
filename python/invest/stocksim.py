#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_direction_up():
    up_down = random.randint(0, 2)
    if up_down == 1:
        return False 
    else:
        return True 

def main():
    stock_price_start = stock_price_current = 250
    stock_price_hist = []
    stock_moving_avg = []
    stock_price_hist.append(stock_price_start)
    initial_balance = 10000
    balance_left = initial_balance
    cost_basis = 0
    stocks = 0
    sell_price = 0
    ma_cost_basis = 0
    ma_sell_price = 0
    ma_stocks = 0
    stock_lump = 20

    for i in range(0, 365):
        price_fluctuation = random.randint(1, 7)
        is_up = is_direction_up()
        if is_up:
            stock_price_current += price_fluctuation
        else:
            stock_price_current -= price_fluctuation
        stock_price_hist.append(stock_price_current)

        percent_change = price_fluctuation/stock_price_hist[-1::][0] * 100

        '''
        if is_up:
            print("New Price: %f, percent fluc UP: %f " % (stock_price_current, percent_change))
        else:
            print("New Price: %f, percent fluc Down: %f " % (stock_price_current, percent_change))
        '''

        if percent_change > 1.5 and not is_up:
            if balance_left <= 0:
                print("Cannot buy.. all balance gone")
                continue 

            max_stock_lump = balance_left / stock_price_current

            stocks += max_stock_lump
            cost_basis += stock_price_current * stock_lump
            balance_left -= cost_basis
            print("Balance left: %d, Buy at %f. Stocks accumulated: %d" % \
                    (balance_left, stock_price_current, stocks))

        if percent_change > 1.5 and is_up:
            if stocks > 0:
                stocks -= 10
                sell_price += stock_price_current * stock_lump
                balance_left += sell_price
                print("Balance left: %d, Selling at: %f, Stocks accumulated: %d" % \
                        (balance_left, stock_price_current, stocks))


        if len(stock_price_hist) > 5:
            max_hist = 5
        else:
            max_hist = len(stock_price_hist)

        price_sum = sum(stock_price_hist[-max_hist::])
        avg = price_sum/max_hist
        stock_moving_avg.append(avg)

        cur_moving_avg = stock_moving_avg[-1]
        try:
            last_moving_avg = stock_moving_avg[-2]
        except IndexError:
            continue

        percent_change = (cur_moving_avg - last_moving_avg)/last_moving_avg * 100 
        percent_change = abs(percent_change)

        if percent_change > 1.0 and not is_up:
            ma_stocks += stock_lump
            ma_cost_basis += stock_price_current * stock_lump
            print(" (%f) Buy based on MA (%f), stocks accumulated: %d " \
                %(percent_change, stock_price_current, ma_stocks))

        
        if percent_change > 1.0 and is_up:
            if ma_stocks > 0:
                #ma_stocks -= 10
                #ma_sell_price += stock_price_current * 10
                ma_sell_price += stock_price_current * ma_stocks
                ma_stocks = 0
                print("MA Selling at %f, stocks accumulated: %d" \
                  %(stock_price_current, ma_stocks))

    #print(stock_price_hist)
    #print(stock_moving_avg)
    print("Cost basis: %f, MA Cost basis: %f, Stocks left: %d" % (cost_basis, ma_cost_basis, stocks))
    print("Sell price: %f, MA  sell price: %f, Stocks lef: %d" % (sell_price, ma_sell_price, ma_stocks))


if __name__ == '__main__':
    main()
