#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random




def run_trial(upside=5.00, downside=5.00, balance=100.00, iterations=1):
    for i in range(0, iterations):
        trade_result = "positive"
        up_down = random.randint(1, 2)
        if up_down == 1:
            gain_loss = balance * (upside/100.00)
            trade_result =  "positive"
        else:
            gain_loss = balance * (downside/100.00)
            trade_result = "negative"

        if up_down == 1:
            balance += gain_loss
        else:
            balance -= gain_loss

        print("Trade result: [%s], Value: [%f]" % \
                (trade_result, balance))
    return balance

def main():
    upside = 5.00
    downside = 5.00
    balance = 100.00
    iterations = 5
    trials =  10

    total_balance = balance * trials

    balances = []
    for j in range(0, trials):
        balance = run_trial();
        balances.append(balance)

    sum_of_balances = 0;
    sum_of_balances  = sum(balances)
    print("Sum of all trials: ", sum_of_balances)
    print("No trial sum: ", total_balance)

    if sum(balances) > total_balance:
        print("Trial Made Profit: ", sum(balances) - total_balance)
    else:
        print("Trial Lost Money: ", total_balance - sum(balances))



if __name__ == '__main__':
    main()
