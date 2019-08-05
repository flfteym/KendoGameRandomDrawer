#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from CommonUtils.excel_reader import excel

def divideGroup(group, big_vs_info):

    '''
    将给定的一组参赛人数进行分组.
    :param group: 参赛人数, 格式为列表
    :param big_vs_info: 用于存放对阵信息的列表
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
                vs_info = [1, 1]
                vs_info1 = [1, 'N/A']
                big_vs_info.append(vs_info)
                big_vs_info.append(vs_info1)
            if len(x) == 2:
                vs_info = [1, 1]
                big_vs_info.append(vs_info)

    if nums == 2:
        vs_info = [1, 1]
        big_vs_info.append(vs_info)

    if nums == 3:
        vs_info = [1, 1]
        vs_info1 = [1, 'N/A']
        big_vs_info.append(vs_info)
        big_vs_info.append(vs_info1)

    return big_vs_info

def genVsInfo(gamers_list, seeded_players=None):

    '''
    生成对战信息.
    :param gamers_list: 参赛选手列表
    :param seeded_players: 种子选手列表, 大于等于2并且小于等于4
    :return:
    '''

    # 获取参赛人数, 并分成两组
    gamer_nums = len(gamers_list)
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

    if seeded_players is None:
        for i in gamer_group1_vslist:
            if isinstance(i[1], str):
                player1 = random.choice(gamers_list)
                gamers_list.remove(player1)
                i[0] = player1
                gamer_group1_vs_info.append(i)
            else:
                player1 = random.choice(gamers_list)
                gamers_list.remove(player1)
                player2 = random.choice(gamers_list)
                gamers_list.remove(player2)
                i[0] = player1
                i[1] = player2
                gamer_group1_vs_info.append(i)

        for k in gamer_group2_vslist:
            if isinstance(k[1], str):
                player1 = random.choice(gamers_list)
                gamers_list.remove(player1)
                k[0] = player1
                gamer_group2_vs_info.append(k)
            else:
                player1 = random.choice(gamers_list)
                gamers_list.remove(player1)
                player2 = random.choice(gamers_list)
                gamers_list.remove(player2)
                k[0] = player1
                k[1] = player2
                gamer_group2_vs_info.append(k)

    # if 2 >= seeded_players <= 4:
    #     pass

    return gamer_group1_vslist, gamer_group2_vslist

if __name__ == "__main__":
    gamers_list = excel("C:/Users/pc/Desktop/gamelist.xlsx")
    result = genVsInfo(gamers_list)
    # result = divideGroup(gamers_list, [])
    for i in result:
        print(i)