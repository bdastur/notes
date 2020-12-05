#!/usr/bin/env python


def check_alert(mylist, idx, interval, threshold):
    new_list = []
    sum = 0
    avg = 0

    new_list = mylist[idx:idx+interval]
    if len(new_list) < interval:
        return 0

    for item in new_list:
        sum += item

    avg = float(sum / interval)
    print("avg: ", avg)
    if avg >= threshold:
        return 1

    return 0

def rolling_avg(mylist, threshold, interval):
    new_list = []
    alert_count = 0

    for idx in range(0, len(mylist)):
        alert_count += check_alert(mylist, idx, interval, threshold)

    return alert_count
        

def main():
    mylist = [1, 3, 2, 1, 4, 5, 6, 7, 9]
    alert_count = rolling_avg(mylist, 4, 3)
    print("Alert: ", alert_count)

if __name__ == '__main__':
    main()

