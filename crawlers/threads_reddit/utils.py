""" module to utils function """

from datetime import datetime, timedelta


def printTable(myDict, colList=None, keys_list=None):
    """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
    if not colList:
        colList = list(myDict[0].keys() if myDict else [])
    if not keys_list:
        keys_list = list(myDict[0].keys() if myDict else [])

    myList = [colList]  # 1st row = header
    for item in myDict:
        myList.append([str(item[col] or "") for col in keys_list])

    colSize = [max(map(len, col)) for col in zip(*myList)]
    formatStr = " | ".join(["{{:<{}}}".format(i) for i in colSize])
    myList.insert(1, ["-" * i for i in colSize])  # Seperating line
    for item in myList:
        print(formatStr.format(*item))


def print_result_threads(threads_data):
    """ print report data in shell """

    head_list = [
        "Pontuação",
        "Subreddit",
        "Título da thread",
        "Link para os comentários da thread",
        "Link da thread",
    ]

    keys_list = ["score", "subreddit", "title", "link_comment", "link_thread"]

    printTable(threads_data, head_list, keys_list)
