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
    for i in range(len(player)):
        player_list[player[i]] = [height_convert[i], weight_convert[i]]
    top_h = sorted(player_list.items(), key=lambda x: x[1][0], reverse = True)
    top_w = sorted(player_list.items(), key=lambda x: x[1][1], reverse = True)
    chartmaker(top_h, 30, "Height")
    chartmaker(top_h, 5, "Height")
    chartmaker(top_w, 30, "Weight")
    chartmaker(top_w, 5, "Weight")
    
    
def chartmaker(top, num, title):
    """Chart making function"""
    check = 0 if title == "Height" else 1
    check1 = "cm" if title == "Height" else "kg"
    line_chart = pg.Bar(legend_at_bottom=True, legend_at_bottom_columns=6)
    line_chart.title = "Top %d the most %s players (%s)" %(num, title, check1)
    for key, value in top[:num]:
        line_chart.add(str(key), value[check])
    line_chart.render_to_file('pic/Top %d the most %s players.svg' %(num, title))


def convert_h(i):
    """Convert height from foot-inch to cm"""
    temp = i.replace("-", " ").split()
    temp = int(temp[0])*30.48 + int(temp[1])*2.54
    return int(temp)

main()