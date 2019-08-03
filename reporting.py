import pandas as pd
import matplotlib.pyplot as plt

def download_plot(plot, sufijo):
    #plot.figure.savefig('../output/Plot'+str(sufijo)+'.png')
    plot.figure.savefig('../output/Plot{}.png'.format(str(sufijo)))
    #fig.savefig('../output/Plot{}.png'.format(str(sufijo)))
    #fig.savefig('../output/Plot{}.png', format(sufijo))
    #plot.figure.savefig('../output/Plot{}.png', format(sufijo))
    #plt.savefig('../output/Plot{}.png'.format(str(sufijo)))
    #plt.savefig('../output/Plot{}.png')

