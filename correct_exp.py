import json, re
import os, sys



dump_list = []
dump_json = {}
uid = 0
name = ""

f1= open("dev_set.txt", mode='r', encoding='utf-8')

for line in f1:
    pairs = line.split(":")
    abbr_word = pairs[0]
    if abbr_word == "n":
        continue
    complete_word = pairs[1].strip()
    complete_word = complete_word.split(" ")
    for i in range(len(complete_word)):
        complete_word[i] = complete_word[i].split("/")[0]
    dump_json[abbr_word] = ''.join(complete_word)


f2 = open("test_set.txt", mode='r', encoding='utf-8')


for line in f2:
    pairs = line.split(":")
    abbr_word = pairs[0]
    if abbr_word == "n":
        continue
    complete_word = pairs[1].strip()
    complete_word = complete_word.split(" ")
    for i in range(len(complete_word)):
        complete_word[i] = complete_word[i].split("/")[0]
    dump_json[abbr_word] = ''.join(complete_word)

f3 = open("train_set.txt", mode='r', encoding='utf-8')

for line in f3:
    pairs = line.split(":")
    abbr_word = pairs[0]
    if abbr_word == "n":
        continue
    complete_word = pairs[1].strip()
    complete_word = complete_word.split(" ")
    for i in range(len(complete_word)):
        complete_word[i] = complete_word[i].split("/")[0]
    dump_json[abbr_word] = ''.join(complete_word)
#     dicts = json.load(f)
#     # 将多个字典从json文件中读出来
#     for i in dicts:
#         print(i["uid"])
#         print(i["name"])
#         print(i["content"])
#         print("========")
#
# print(pre_data)
# for i in range(len(pre_data)-1):
#     # 如果以xls为为结尾，就是新员工信息
#
#             dump_json["uid"] = uid
#             dump_json["name"] = name
#             dump_json["gender"] = ""
#             dump_json["nation"] = ""
#             dump_json["birthday"] = ""
#             dump_json["birthplace"] = ""
#             dump_json["origo"] = ""
#
#             dump_json["t_party"] = ""
#             dump_json["t_job"] = ""
#
#             dump_json["ft_edu_career"] = ""
#             dump_json["ft_edu_school"] = ""
#             dump_json["pt_edu_career"] = ""
#             dump_json["pt_edu_school"] = ""
#
#             dump_json["position"] = ""
#             dump_json["rank"] = ""
#             dump_json["content"] = content
#
#             dump_list.append(dump_json)
#             content = []
#             dump_json = {}
#
#
#
#
# print(dump_list)
#
with open('abbr_pairs.json', mode='w', encoding='utf-8') as f:
    json.dump(dump_json, f, ensure_ascii=False)
#
#
# with open(data_path + '/sample_data180.json', mode='r', encoding='utf-8') as f:
#     dicts = json.load(f)
#     # 将多个字典从json文件中读出来
#     for i in dicts:
#         print(i["uid"])
#         print(i["name"])
#         print(i["content"])
#         print("========")

