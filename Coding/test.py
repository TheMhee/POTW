import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    dt = pd.read_csv('nba.csv').T.to_dict()
    df = pd.read_csv('nba.csv').to_dict()
    keys = []
    for key in df.keys():
        keys.append(key)
    #Age record --
    age_list = [dt[i]["Age"] for i in dt]
    age_list_2017 = [dt[i]["Age"] for i in dt if "2017" in dt[i]["Season"]]
    age_average = np.average(age_list)

    age_of_people = {}
    for i in range(min(age_list), max(age_list)+1):
        age_of_people[i] = age_list.count(i) 

    #make age list and number list for graph
    ages, numbers = [], []
    for age, number in age_of_people.items():
        ages.append(age)
        numbers.append(number)
    #make graph
    plt.title('Ages of players')
    plt.xlabel('Age')
    plt.ylabel('Amount')
    y_pos = [i for i in range(len(ages))]
    # Create bars
    plt.bar(y_pos, numbers, color=("Yellow"))   
    # Create names on the x-axis
    plt.xticks(y_pos, ages)
    for x,y in zip(ages, numbers):
        plt.text(x-19.2, y+1, str(y), size=5, )
    plt.savefig("Age of people.png", dpi=300)
    #plt.show()
    #End of age record--

    #Conference record
    #Check Season whtch conference not "nan"
    for i in dt:
        if str(dt[i]["Conference"]) != "nan":
            season_has_confer = dt[i]["Season"]
            break
    
    conference = []
    for key, value in df["Conference"].items():
        conference.append(value)
    Conference_arranged = {}
    for i in ["East", "West"]:
        Conference_arranged[i] = conference.count(i) 
    print(Conference_arranged)

        
        

main()