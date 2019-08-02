import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_boxplot(col, df):
    plot = df.boxplot(col)
    return plot


def plot_bar(df):
    plot = df.plot(kind='bar')
    return plot


def plot_scatter(df, col1, col2):
    plot = plt.scatter(df[col1], df[col2], alpha=0.5)
    return plot


def plot_line(df):
    plot = df.plot(kind='line', style='.-')
    plt.legend(loc='best', bbox_to_anchor=(1.0, 0.5))
    return plot


def plot_hist(df, col):
    plot = df[col].hist()
    return plot