import pandas as pd
import pygal as pg
def main():
    """Top player chart
    make data with pandas library
    make chart with pygal
    """
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    player = [dt[i]["Player"] for i in dt]
    player_list = sorted(list(set(player)))
    player_count = {}
    for i in player_list:
        player_count[i] = player.count(i)
    player_count = sorted(player_count.items(), key=lambda x: x[1], reverse = True)
    line_chart = pg.Bar(legend_at_bottom=True, legend_at_bottom_columns=6)
    line_chart.title = "Top 30 Players got the most POTW"
    for key , value in player_count[:30]:
        line_chart.add(key, value)
    line_chart.render_to_file('pic/Top 30Players got the most POTW.svg')
    line_chart = pg.Bar()
    line_chart.title = "Top 5 Players got the most POTW"
    for key , value in player_count[:5]:
        line_chart.add(key, value)
    line_chart.render_to_file('pic/Top 5 Players got the most POTW.svg')
        
main()