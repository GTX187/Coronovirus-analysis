import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

DATA_PATH = "/home/kanishk/Documents/corona_virus/data_sets/"

confirmed_df = pd.read_csv(DATA_PATH + "time_series_covid_19_confirmed.csv")
deaths_df = pd.read_csv(DATA_PATH + "time_series_covid_19_deaths.csv")
recovered_df = pd.read_csv(DATA_PATH + "time_series_covid_19_recovered.csv")
covid_df = pd.read_csv(DATA_PATH + "covid_19_data.csv")

print("What would you like to know?")
print("1. World wide statistics")
print("2. Top 10 countries with respect to infected cases")
print("3. Top 10 countries with respect to deaths")
print("4. Top 10 countries with respect to recoveries")
print("5. Indian Statistics")
choice=input("Choose an option : ")

def func(pct, allvalues):
    return "{:.1f}".format(pct)

if choice == '1':
    confirmed_cases = np.sum(covid_df["Confirmed"])
    death_cases = np.sum(covid_df["Deaths"])
    recovered_cases = np.sum(covid_df["Recovered"])
    labels = ['Confirmed', 'Deaths', 'Recovered']
    fig = plt.figure(figsize =(10, 7))
    plt.pie([confirmed_cases, death_cases, recovered_cases], labels=labels, autopct=lambda pct: func(pct, labels))
    plt.show()
    
elif choice == '2':
    top_10_confirmed = confirmed_df.sort_values(['5/29/21']).tail(10)
    print(top_10_confirmed)
    
    x_values = top_10_confirmed.columns[4:]
    y_values = []
    legends = top_10_confirmed['Country/Region'].values
    for row in top_10_confirmed.iterrows():
        y_values.append(row[1][x_values].values)
        
    fig = plt.figure(figsize =(20, 7))

    for values in y_values:
        plt.plot(x_values, values)
    plt.yticks(rotation=90)
    plt.xticks(rotation=90)
    plt.legend(legends)
    plt.show()
    
elif choice == '3':
    top_10_deaths = deaths_df.sort_values(['5/29/21']).tail(10)
    print(top_10_deaths)
    
    x_values = top_10_deaths.columns[4:]
    y_values = []
    legends = top_10_deaths['Country/Region'].values
    for row in top_10_deaths.iterrows():
        y_values.append(row[1][x_values].values)
        
    fig = plt.figure(figsize =(20, 7))

    for values in y_values:
        plt.plot(x_values, values)
    plt.yticks(rotation=90)
    plt.xticks(rotation=90)
    plt.legend(legends)
    plt.show()
    
elif choice == '4':
    top_10_recovered = recovered_df.sort_values(['5/29/21']).tail(10)
    print(top_10_recovered)
    
    x_values = top_10_recovered.columns[4:]
    y_values = []
    legends = top_10_recovered['Country/Region'].values
    for row in top_10_recovered.iterrows():
        y_values.append(row[1][x_values].values)
        
    fig = plt.figure(figsize =(20, 7))

    for values in y_values:
        plt.plot(x_values, values)
    plt.yticks(rotation=90)
    plt.xticks(rotation=90)
    plt.legend(legends)
    plt.show()
    
elif choice == '5':
    india_y_values=[]
    india_y_values.append(confirmed_df[confirmed_df['Country/Region'] == 'India'].values[0][4:])
    india_y_values.append(deaths_df[deaths_df['Country/Region'] == 'India'].values[0][4:])
    india_y_values.append(recovered_df[recovered_df['Country/Region'] == 'India'].values[0][4:])

    fig = plt.figure(figsize =(20, 7))

    for values in india_y_values:
        plt.plot(x_values, values)
    plt.yticks(rotation=90)
    plt.xticks(rotation=90)
    plt.legend(['Confirmed','Deaths','Recovered'])
    plt.show()
    
else:
    print("This choice doesn't exist!")