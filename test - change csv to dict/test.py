import pandas as pd
def main():
    dt = pd.read_csv('nba.csv').T.to_dict()
    for i in range(len(dt)):
        print((dt[i]))
        print()
main()