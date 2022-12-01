##################################
#   CSV merger for arXiv results
#   Annika Stein, 2022
##################################

import json
import os
import re
import sys

import numpy as np
import pickle

import datetime

import csv

year = str(datetime.datetime.today().isocalendar()[0])
week = str(datetime.datetime.today().isocalendar()[1])
print('='*50)
print('Running script for year', year, 'and week', week)

category = 'hep-ex'
print('For category', category)


output_path = f'data/full.csv'
if not os.path.isfile(output_path):
    print('-'*50)
    print('Initialize new full csv.')
    print()
    initialize = True
    
    date = ['Date']
    u_freq = ['u_freq']
    u_all = ['u_all']
    d_freq = ['d_freq']
    d_all = ['d_all']
    c_freq = ['c_freq']
    c_all = ['c_all']
    s_freq = ['s_freq']
    s_all = ['s_all']
    t_freq = ['t_freq']
    t_all = ['t_all']
    b_freq = ['b_freq']
    b_all = ['b_all']
    np.savetxt(output_path, [p for p in zip(date,
                                            u_freq, u_all,
                                            d_freq, d_all,
                                            c_freq, c_all,
                                            s_freq, s_all,
                                            t_freq, t_all,
                                            b_freq, b_all)], delimiter=',', fmt='%s')
    print('Created placeholder csv file.') 
    

print('-'*50)
print('Begin reading and merging into existing csv.')
print()
date = 'Y' + year + 'W' + week
with open(f'data/Y{year}W{week}.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if row[0] == 'u':
            u_freq, u_all = row[1], row[2]
        elif row[0] == 'd':
            d_freq, d_all = row[1], row[2]
        elif row[0] == 'c':
            c_freq, c_all = row[1], row[2]
        elif row[0] == 's':
            s_freq, s_all = row[1], row[2]
        elif row[0] == 't':
            t_freq, t_all = row[1], row[2]
        elif row[0] == 'b':
            b_freq, b_all = row[1], row[2]

skip = False
with open(output_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == date:
            print(f'Entry for {date} already exists in merged file, skipping writing.')
            skip = True
if not skip:
    with open(output_path, mode='a') as csv_file:
            merged_writer = csv.writer(csv_file, delimiter=',')

            merged_writer.writerow([date,
                                    u_freq, u_all,
                                    d_freq, d_all,
                                    c_freq, c_all,
                                    s_freq, s_all,
                                    t_freq, t_all,
                                    b_freq, b_all])
            print('Wrote results into csv file. Exiting.')  
    
print()
print('='*50)
  
    
    