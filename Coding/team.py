import pandas as pd
import numpy as np
import pygal as pg
def main():
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    seasons = [dt[i]["Season short"] for i in dt]
    seasons = sorted(list(set(seasons)))
    team = [dt[i]["Team"] for i in dt]
    team_list = sorted(list(set(team)))
    team_count = {}
    for i in team_list:
        team_count[i] = team.count(i)
    chartmaker(team_count, "every season")
    
    
def chartmaker(team_count, season):
    line_chart = pg.HorizontalBar(legend_at_bottom=True, legend_at_bottom_columns=4)
    line_chart.title = "POTW teams count in %s" %season
    for key, value in team_count.items():
        line_chart.add(str(key), value)
    line_chart.render_to_file('pic/team/POTW teams count in %s.svg' %season)
main()
    