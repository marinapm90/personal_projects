import pandas as pd


def download_plot(plot):
    return plot.figure.savefig('../output/Plot'+'.png')