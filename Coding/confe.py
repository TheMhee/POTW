import pandas as pd
import numpy as np
import pygal as pg
def main():
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    seasons = [dt[i]["Seasons in league"] for i in dt]
    seasons = sorted(list(set(seasons)))
    #data for after 2001 season chart
    conference = []
    for key, value in df["Conference"].items():
        conference.append(value)
    conference_count = [conference.count(i) for i in ["East", "West"]]
    #make chart
    pie_chart = pg.Pie()
    pie_chart.title = "Conference difference after 2001 season"
    pie_chart.add("East", conference_count[0])
    pie_chart.add("West", conference_count[1])
    pie_chart.render_to_file('pic/conf/Conference difference after 2001 season.svg')

    #data for each year chart
    conference_west, conference_east = [], []
    for season in seasons:
        conference = [dt[i]["Conference"] for i in dt if dt[i]["Seasons in league"] == season]
        if str(conference[0]) != "nan":
            conference_west.append((conference.count("West")/(conference.count("West")+conference.count("East")))*100)
            conference_east.append((conference.count("East")/(conference.count("East")+conference.count("West")))*100)
    #make each year chart
    line_chart = pg.StackedBar()
    line_chart.title = "Conference difference each years (2001-2002 to 2017-2018) in %"
    line_chart.x_labels = seasons[seasons.index("2001-2002"):]
    line_chart.add("West", conference_west)
    line_chart.add("East", conference_east)
    line_chart.render_to_file("pic/conf/Conference difference each years.svg")

main()
