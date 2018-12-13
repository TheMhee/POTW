import pandas as pd
import pygal as pg
def main():
    """ position Chart 
    make data with pandas library
    make chart with pygal
    """
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    seasons = [dt[i]["Season short"] for i in dt]
    seasons = sorted(list(set(seasons)))
    position = [dt[i]["Position"] for i in dt]
    position_list = ['C', 'F', 'FC', 'G', 'GF', 'PF', 'PG', 'SF', 'SG']
    position_full = ["Center", "Forward", "Forward-center", "Guard", "Guard-forward", "Point forward(PG)", "Point guard", "Small forward", "Point forward(SG)"]
    position_count = {}
    for i in range(len(position_list)):
        position_count[position_full[i]] = position.count(position_list[i])
    chartmaker(position_count, "every season")

    for season in seasons:
        position_count2 = {}
        position2 = [dt[i]["Position"] for i in dt if dt[i]["Season short"] == season]
        position_list2 = sorted(list(set(position2)))
        for i in range(len(position_list)):
            position_count2[position_full[i]] = position2.count(position_list[i])
        chartmaker(position_count2, season)

def chartmaker(position_count, season):
    """chartmaker function"""
    line_chart = pg.HorizontalBar(legend_at_bottom=True, legend_at_bottom_columns=4)
    line_chart.title = "POTW position count in %s" %season
    for key, value in position_count.items():
        line_chart.add(str(key), value)
    line_chart.render_to_file('pic/position/POTW position count in %s.svg' %season)

main()