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
    category = wrangling.category(my_data, 'main_category')
    types = wrangling.types(my_data, "main_category", "goal_usd", "usd_pledged")
    country = wrangling.country(my_data, "country")
    start = wrangling.star(my_data, "start_month", "id")
    end = wrangling.end(my_data, "end_month", "id")
    success = wrangling.success(my_data, "status", "id")
    return my_data, category, types, country, start, end, success


def analyze(my_data, category, types, country, start, end, success):
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


def report(iter_plots):
    for ind, plotx in enumerate(iter_plots):
        print(ind, plotx)
        reporting.download_plot(plotx, ind)


def main():
    d = read_file('./input/Kickstarter_projects_Feb19.csv')
    my_data, category, types, country, start, end, success = cleaning(d)
    figure = analyze(my_data, category, types, country, start, end, success)
    report(figure)


if __name__ == "__main__":
    main()




