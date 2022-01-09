#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = "прроцесор"
    word2 = 'теекстовыйфайл'
    word3 = 'програма и аллгоритм'
    word4 = 'процесор и паммять'

    word1 = word1.replace('р', '', 1)
    word1 = word1[:6] + 'с' + word1[6:]
    word2 = word2.replace('е', '', 1)
    word2 = word2[:9] + ' ' + word2[9:]
    word3 = word3.replace('л', '', 1)
    word3 = word3[:6] + 'м' + word3[6:]
    word4 = word4.replace('м', '', 1)
    word4 = word4[:5] + 'с' + word4[5:]
    print (f"Исправленные фразы: \n- {word1};\n- {word2};"
           f"\n- {word3};\n- {word4}.")
