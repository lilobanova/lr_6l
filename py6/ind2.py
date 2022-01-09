#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    n = s.find(',')
    p = s.find(',', n+1, )
    if n > 0 and p > 0:
        s = s[n+1: p]
    else:
        s = s[n+1:]
    print (s)
