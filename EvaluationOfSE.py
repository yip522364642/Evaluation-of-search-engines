# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:21
# @Author  : yip
# @Email   : 522364642@qq.com
# @File    : EvaluationOfSE.py

import os
import pylab as pl


# 读txt文件
def read_data(path):
    content = []
    file = open(path, 'r', encoding='UTF-8')
    for line in file:
        content.append(line.strip())
    file.close()
    return content


# 写txt文件(追加)
def write_data(path, data):
    fos = open(path, "a", encoding="utf-8")
    fos.write(data + '\n')
    fos.close()


# 计算各个搜索引擎的PR
def evaluation_SE():
    data_dir = './Data/'
    for root, dirs, files in os.walk(data_dir): # 获取路径
        MAP_value = {'Baidu': 0, 'Bing': 0, 'Google': 0}    # 记录各个搜索引擎的MAP值
        len_query = 0   # 记录query个数
        for txt in files:
            path = data_dir + txt
            relevant_website = []   # 该query下相关网址集合
            all_website = {'Baidu': [], 'Bing': [], 'Google': []}   # 各个搜索引擎下的网站
            relevant_count = {'Baidu': 0, 'Bing': 0, 'Google': 0}   # 各个搜索引擎下的相关文档数量
            P_value = {'Baidu': [], 'Bing': [], 'Google': []}  # 各个搜索引擎下的准确率（每遇到一个1计算一次P）
            R_value = {'Baidu': [], 'Bing': [], 'Google': []}  # 各个搜索引擎下的召回率（每遇到一个1计算一次R）
            search_engine = ['Baidu', 'Bing', 'Google']
            data = read_data(path)
            for line in data:
                temp = line.split(' ')
                flag = int(temp[0])  # 相关/不相关标识：1/0
                se = temp[1]    # 搜索引擎：Baidu/Bing/Google
                website = temp[2]   # 具体网址
                if flag == 1:
                    relevant_website.append(website)
            relevant_website = list(set(relevant_website))  # 去除重复元素

            for line in data:
                temp = line.split(' ')
                flag = int(temp[0])  # 相关/不相关标识：1/0
                se = temp[1]    # 搜索引擎：Baidu/Bing/Google
                website = temp[2]   # 具体网址
                all_website[se].append(website)
                #   每遇到一个相关的网站，计算P/R值
                if flag == 1:
                    relevant_count[se] += 1
                    P_value[se].append(relevant_count[se] / len(all_website[se]))
                    R_value[se].append(relevant_count[se] / len(relevant_website))
            print(P_value)
            print(R_value)
            print()

            # 计算MAP值
            for key in MAP_value.keys():
                MAP_value[key] = (MAP_value[key] * len_query + relevant_count[key] / len(all_website[key])) / (len_query + 1)
            len_query += 1

            # 显示图片，x轴为召回率，y轴为精确率
            pl.ion()
            for se in search_engine:
                # pl.title(txt.replace('.txt', '')) # 无法显示中文
                pl.xlabel(u"Recall_Value")
                pl.ylabel(u"Precision_Value")
                pl.plot(R_value[se], P_value[se], label=se)
                pl.legend()
            pl.savefig('./PR_pic/' + txt.replace('.txt', '') + "_PR.png")
            pl.pause(3)  # 显示秒数
            pl.close()
            # pl.show()
        print('MAP_value: ', MAP_value)


if __name__ == "__main__":
    evaluation_SE()
