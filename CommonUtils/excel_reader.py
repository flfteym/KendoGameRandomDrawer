#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

def excel(fname):
    data = xlrd.open_workbook(fname)
    table_one = data.sheet_by_index(0)
    gamers_numbers = table_one.nrows - 1
    gamers_properties = [table_one.cell_value(0, 0), table_one.cell_value(0, 1), table_one.cell_value(0, 2)]
    gamers_list = []
    for gamer_num in range(1, gamers_numbers + 1):
        gamer_dict = {}
        gamer_dict[gamers_properties[0]] = table_one.cell_value(gamer_num, 0)
        gamer_dict[gamers_properties[1]] = table_one.cell_value(gamer_num, 1)
        gamer_dict[gamers_properties[2]] = table_one.cell_value(gamer_num, 2)
        gamers_list.append(gamer_dict)
    return gamers_list

if __name__ == '__main__':
    gamers = excel("C:/Users/pc/Desktop/gamelist.xlsx")
    print(gamers)