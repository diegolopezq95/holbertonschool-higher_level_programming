#!/usr/bin/python3
""" This module finds a peak in a list of unsorted integers
"""


def find_peak_lo_hi(arr, lo, hi, n):
    i = lo + (hi - lo)/2
    i = int(i)
    if ((i == 0 or arr[i - 1] <= arr[i]) and
       (i == n - 1 or arr[i + 1] <= arr[i])):
        return arr[i]
    elif (i > 0 and arr[i - 1] > arr[i]):
        return find_peak_lo_hi(arr, lo, (i - 1), n)
    else:
        return find_peak_lo_hi(arr, (i + 1), hi, n)


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    return find_peak_lo_hi(list_of_integers, 0, n - 1, n)
