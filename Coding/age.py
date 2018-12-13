import pandas as pd
import pygal as pg
def main():
    """Age chart
    make data with pandas library
    make chart with pygal
    s"""
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    seasons = [dt[i]["Season short"] for i in dt]
    seasons = sorted(list(set(seasons)))
    keys = []
    #make datas for bar
    for key in df.keys():
        keys.append(key)
    age_list = [dt[i]["Age"] for i in dt]
    age_of_people = {}
    for i in range(min(age_list), max(age_list)+1):
        age_of_people[i] = age_list.count(i)

    #make chart
    line_chart = pg.HorizontalBar()
    line_chart.title = "Age of player in every season"
    for key, value in age_of_people.items():
        line_chart.add(str(key), value)
    line_chart.render_to_file('pic/age/Age of player in every season.svg')

    #each season pie
    for season in seasons:
        age_list_each = [dt[i]["Age"] for i in dt if season == dt[i]["Season short"]]
        age_of = {}
        for i in range(min(age_list_each), max(age_list_each)+1):
            if age_list_each.count(i) != 0 : age_of[i] = age_list_each.count(i)
        pie_chart = pg.Pie()
        pie_chart.title = "Player\'s age difference in %s season" %season
        for key, value in age_of.items():
            pie_chart.add(str(key), value)
        pie_chart.render_to_file("pic/age/Player\'s age difference in %s season.svg" %season)
        
main()
