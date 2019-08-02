import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import acquisition
import wrangling
import analysis
import reporting


def read_file(file):
    my_data = acquisition.load_data(file)
    return my_data


def cleaning(my_data):
    my_data = wrangling.new_column(my_data, "usd_pledged", "goal_usd")
    return my_data

def analyze(my_data):
    plot_boxplot = analysis.plot_boxplot("usd_pledged", my_data)
    plot_bar1 = analysis.plot_bar(category)
    plot_bar2 = analysis.plot_bar(types)
    plot_scatter = analysis.plot_scatter(my_data, "duration", "usd_pledged")
    plot_bar3 = analysis.plot_bar(country)
    plot_line1 = analysis.plot_line(start)
    plot_line2 = analysis.plot_line(end)
    plot_hist = analysis.plot_hist(my_data, 'duration')
    plot_bar4 = analysis.plot_bar(success)
    return plot_boxplot, plot_bar1, plot_bar2, plot_scatter, plot_bar3, plot_line1, plot_line2, plot_hist, plot_bar4

def report(plot):

    plot = reporting.download_plot(plot)
    return plot

def main():
    kickstarter = read_file('./Kickstarter_projects_Feb19.csv')
    kickstarter_clean = cleaning(kickstarter)
    figure = analyze(kickstarter_clean)
    report(figure)


if __name__ == "__main__":
    main()




