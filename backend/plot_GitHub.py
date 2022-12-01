################################
#   Plotter for arXiv results
#   Annika Stein, 2022
################################

import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import mplhep as hep
plt.style.use(hep.style.CMS)

year = str(datetime.datetime.today().isocalendar()[0])
week = str(datetime.datetime.today().isocalendar()[1])
print('='*50)
print('Running script for year', year, 'and week', week)

category = 'hep-ex'
print('For category', category)


input_path = f'data/full.csv'


print('-'*50)
print('Begin reading csv.')
print()

with open(input_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    labels = []
    u_freq  = []
    u_all = []
    d_freq  = []
    d_all = []
    c_freq  = []
    c_all = []
    s_freq  = []
    s_all = []
    t_freq  = []
    t_all = []
    b_freq  = []
    b_all = []
    for row in csv_reader:
        if row[0] == 'Date':
            continue
        labels.append(row[0])
        u_freq.append(int(row[1]))
        u_all.append(int(row[2]))
        d_freq.append(int(row[3]))
        d_all.append(int(row[4]))
        c_freq.append(int(row[5]))
        c_all.append(int(row[6]))
        s_freq.append(int(row[7]))
        s_all.append(int(row[8]))
        t_freq.append(int(row[9]))
        t_all.append(int(row[10]))
        b_freq.append(int(row[11]))
        b_all.append(int(row[12]))
n_weeks = len(labels)
x_ax = np.arange(n_weeks)

freqs = np.array([u_freq,
                 d_freq,
                 c_freq,
                 s_freq,
                 t_freq,
                 b_freq])
all_a = np.array([u_all,
                  d_all,
                  c_all,
                  s_all,
                  t_all,
                  b_all])
        
fig,ax1 = plt.subplots(figsize=[14,9])
ax2 = ax1.twinx()

colors = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown']
names = ['up','down','charm','strange','top','bottom']
legtitle = 'Quark'
legloc = 'upper left'
handles = []
for i in range(6):
    y1 = freqs[i]
    y2 = all_a[i]
    legend_text = names[i]
    print(x_ax, y1)
    print(x_ax, y2)
    ax1.plot(x_ax, y1, '-bo', color=colors[i], linewidth=3.0, label=legend_text+' (in papers)')
    ax2.plot(x_ax, y2, '--bo', color=colors[i], linewidth=3.0, label=legend_text+' (all mentions)')
    

    handles.append(mpatches.Patch(color=colors[i], label=names[i]))

handles.append(Line2D([0], [0], color='k', linewidth=3, linestyle='-', label='in papers'))
handles.append(Line2D([0], [0], color='k', linewidth=3, linestyle='--', label='all mentions'))

leg = ax1.legend(handles=handles, title=legtitle, loc=legloc, bbox_to_anchor=(1.1, 1.0), fontsize=16, title_fontsize=20, labelspacing=0.7, frameon=True, framealpha=1, facecolor='white')
if 'right' in legloc:
    aligned = 'right'
else:
    aligned = 'left'
leg._legend_box.align = aligned
leg.get_frame().set_linewidth(0.0)
ax1.set_ylabel('Appearances (in papers)')
ax2.set_ylabel('Appearances (all mentions)')
ax1.set_xlabel('Year & Week')
ax1.set_xticks(x_ax)
ax1.set_xticklabels(labels)
fig.savefig('../frontend/'+legtitle + '.png', bbox_inches='tight', dpi=900, transparent=True)

print()
print('='*50)
  
    
    