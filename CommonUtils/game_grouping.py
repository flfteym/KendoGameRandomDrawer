#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from CommonUtils.excel_reader import excel

def divideGroup(group, big_vs_info):

    '''
    将给定的一组参赛人数进行分组.
    :param group: 参赛人数, 格式为列表
    :return: 分组序列
    '''
    nums = len(group)
    sub_group1 = nums // 2
    sub_group2 = nums - sub_group1
    layer = [sub_group1, sub_group2]

    if nums > 2 and nums % 2 == 0:
        for i in layer:
            x = [x for x in range(1, i + 1) ]
            if len(x) > 2:
                divideGroup(x, big_vs_info)
            if len(x) == 2:
                vs_info = [1, 1]
                big_vs_info.append(vs_info)

    if nums > 3 and nums % 2 == 1:
        for i in layer:
            x = [x for x in range(1, i + 1)]
            if len(x) > 3:
                divideGroup(x, big_vs_info)
            if len(x) == 3:
                vs_info = [[1, 1], 1]
                big_vs_info.append(vs_info)
            if len(x) == 2:
                vs_info = [1, 1]
                big_vs_info.append(vs_info)

    if nums == 2:
        vs_info = [1, 1]
        big_vs_info.append(vs_info)

    if nums == 3:
        vs_info = [[1, 1], 1]
        big_vs_info.append(vs_info)

    return big_vs_info

def genVsInfo(games_list):

    '''
    生成对战信息.
    :param games_list: 参赛选手列表
    :return:
    '''

    # 获取参赛人数, 并分成两组
    gamer_nums = len(games_list)
    gamer_group1_nums = gamer_nums // 2
    gamer_group2_nums = gamer_nums - gamer_group1_nums

    # 将两组参赛选手生成列表
    gamer_group1 = [x for x in range(1, gamer_group1_nums + 1)]
    gamer_group2 = [x for x in range(1, gamer_group2_nums + 1)]

    big_vs_info1 = []
    big_vs_info2 = []

    # 获取两组参赛选手对阵信息
    gamer_group1_vslist = divideGroup(gamer_group1, big_vs_info1)
    gamer_group2_vslist = divideGroup(gamer_group2, big_vs_info2)
    gamer_group1_vs_info = []
    gamer_group2_vs_info = []

    for i in gamer_group1_vslist:
        if isinstance(i[0], list):
            x = random.choice(gamers_list)
            gamers_list.remove(x)
            y = random.choice(gamers_list)
            gamers_list.remove(y)
            z = random.choice(gamers_list)
            gamers_list.remove(z)
            i[0][0] = x["姓名"]
            i[0][1] = y["姓名"]
            i[1] = z["姓名"]
            gamer_group1_vs_info.append(i)
        else:
            x = random.choice(gamers_list)
            gamers_list.remove(x)
            y = random.choice(gamers_list)
            gamers_list.remove(y)
            i[0] = x["姓名"]
            i[1] = y["姓名"]
            gamer_group1_vs_info.append(i)

    for k in gamer_group2_vslist:
        if isinstance(k[0], list):
            x = random.choice(gamers_list)
            gamers_list.remove(x)
            y = random.choice(gamers_list)
            gamers_list.remove(y)
            z = random.choice(gamers_list)
            gamers_list.remove(z)
            k[0][0] = x["姓名"]
            k[0][1] = y["姓名"]
            k[1] = z["姓名"]
            gamer_group2_vs_info.append(k)
        else:
            x = random.choice(gamers_list)
            gamers_list.remove(x)
            y = random.choice(gamers_list)
            gamers_list.remove(y)
            k[0] = x["姓名"]
            k[1] = y["姓名"]
            gamer_group2_vs_info.append(k)

    return gamer_group1_vslist, gamer_group2_vslist

if __name__ == "__main__":
    # gamers = [x for x in range(1, 32 + 1)]
    # big_vs_info = divideGroup(gamers)
    # vs_info = []
    # for i in big_vs_info:
    #     if isinstance(i[0], list):
    #         x = random.choice(gamers)
    #         gamers.remove(x)
    #         y = random.choice(gamers)
    #         gamers.remove(y)
    #         z = random.choice(gamers)
    #         gamers.remove(z)
    #         i[0][0] = x
    #         i[0][1] = y
    #         i[1] = z
    #         vs_info.append(i)
    #     else:
    #         x = random.choice(gamers)
    #         gamers.remove(x)
    #         y = random.choice(gamers)
    #         gamers.remove(y)
    #         i[0] = x
    #         i[1] = y
    #         vs_info.append(i)
    #
    # print(vs_info)

    gamers_list = excel("C:/Users/pc/Desktop/gamelist.xlsx")
    result = genVsInfo(gamers_list)
    for i in result:
        print(i)