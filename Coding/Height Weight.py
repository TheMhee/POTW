import pandas as pd
import numpy as np
import pygal as pg
def main():
    """ Top HEIGHT WEIGHT Chart """
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    player = [dt[i]["Player"] for i in dt]
    height = [dt[i]["Height"] for i in dt]
    weight = [dt[i]["Weight"] for i in dt]
    height_convert, weight_convert = [], []
    for i in height:
        if len(i) <= 4:
            i = convert_h(i)
        elif i[3:] == "cm":
            i = int(i.replace("cm", ""))
        height_convert.append(i)
    for i in weight:
        if len(str(i)) == 3:
            i = int(i)*0.453
        else:
            i = i.replace("kg", "")
        weight_convert.append(int(i))
    player_list = {}


def convert_h(i):
    """Convert height from foot-inch to cm"""
    temp = i.replace("-", " ").split()
    temp = int(temp[0])*30.48 + int(temp[1])*2.54
    return int(temp)

main()