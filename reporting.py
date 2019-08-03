import pandas as pd


def download_plot(plot, sufijo):
    # plot.figure.savefig('../output/Plot'+str(sufijo)+'.png')
    fig = plot.get_figure()
    fig.savefig('../output/Plot{}.png'.format(sufijo))
