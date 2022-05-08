import urllib.request as libreq

import requests
import tempfile
import shutil
import tarfile
import json
import os
import re
import sys

"""
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()
    print(r)
"""

category = 'hep-ex'

quarks = ['u','d','c','s','t','b']

quark_names = [['up','Up'],
               ['down','Down'],
               ['charm','Charm'],
               ['strange','Strange'],
               ['top','Top','truth','Truth'],
               ['bottom','Bottom','beauty','Beauty']]

# if once per pub, increment
freq_in_pub = [0, 0, 0, 0, 0, 0]
# increment for every appearance
freq_all_appearances = [0, 0, 0, 0, 0, 0]

#quark_freq = dict(zip(the_quarks, freq))
#print(quark_freq)

print('='*50)
print()

# Find out the total number of recent submissions

with libreq.urlopen('https://arxiv.org/list/{}/recent'.format(category)) as file:
    r = file.read()
    #print(r)
    
    lines = r.splitlines(True)
    
    
    
    #print(lines)
    
    for line in lines:
        decoded_line = line.decode('UTF-8')
        
        if 'total of ' in decoded_line and ' entries' in decoded_line:
            total = (decoded_line.split('total of ')[-1]).split(' entries')[0]
            print('Total number of recent entries:', total)
            break

            
print()
print('-'*50)
print('Start reading the recent submissions.')
print('-'*50)

# get all recent submissions and their identifiers
    
recent_list = []
    
with libreq.urlopen('https://arxiv.org/list/{}/pastweek?show='.format(category)+total) as file:
    r = file.read()
    
    lines = r.splitlines(True)
    
    # ToDo
    for line in lines:
        decoded_line = line.decode('UTF-8')
        
        if '/abs/' in decoded_line and 'list-identifier' in decoded_line:
            #print(decoded_line)
            identifier = decoded_line.split('/abs/')[1].split('"')[0]
            recent_list.append(identifier)
            #print(identifier)
            
bad_files = []    

# Use identifiers and search for pattern in associated files, untar first and decode the content
for (i, recent_id) in enumerate(recent_list):
    #if i != 23:
    #    continue
    print(i, end='\t')
    respurl = 'https://arxiv.org/e-print/{}'.format(recent_id)
    print(respurl)
    
    with libreq.urlopen(respurl) as File:
            
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(File, tmp_file)

    # sometimes there are no other files associated with the pdf (no supplementary material and no version of the paper to parse easily)
    if tarfile.is_tarfile(tmp_file.name) == False:
        bad_files.append(i)
        try:
            os.remove(tmp_file.name)
        except OSError:
            pass
        print('\t\tNot a tar file!')
        continue
    
    """
    if os.path.splitext(tmp_file.name)[1] != 'gz':
        continue
    """
    
    #print('good file yay')
    freq_for_this_id = [0, 0, 0, 0, 0, 0]
    
    with tarfile.open(tmp_file.name,"r:gz") as tf:
        #print("Temp tf File:", tf.name)
        #tf.extractall(path)
        for tarinfo in tf:
            """
            print("tarfilename", tarinfo.name, "is", tarinfo.size, "bytes in size and is", end="")
            if tarinfo.isreg():
                print(" a regular file.")
            elif tarinfo.isdir():
                print(" a directory.")
            else:
                print(" something else.")
            """
            if os.path.splitext(tarinfo.name)[1] == ".tex":
                print("\t\ttex file name:",os.path.splitext(tarinfo.name)[0])
                tex_file = tf.extractfile(tarinfo)
                # capturing tex file to read its contents and further processing.
                content = tex_file.read()
                lines = content.splitlines(True)
                
                for line in lines:
                    try:
                        decoded_line = line.decode('UTF-8')
                        #print(decoded_line)
                        for j in range(len(quarks)):
                            for name in quark_names[j]:
                                if name+' quark' in decoded_line:
                                    freq_for_this_id[j] += 1
                    except:
                        pass
            
        for j in range(len(quarks)):
            freq_all_appearances[j] += freq_for_this_id[j]
            if freq_for_this_id[j] >= 1:
                freq_in_pub[j] += 1
                        
                        
                #for k in range(10):
                #    print(lines[k])
    
    try:
        os.remove(tmp_file.name)
    except OSError:
        pass

     
print()
print('-'*50)
print()
print('Quark','\t','Appeared in # individual items','\t','Total appearances')
for j in range(len(quarks)):
    print(quarks[j],':','\t',freq_in_pub[j],'\t',freq_all_appearances[j])
    
              
print()
print('-'*50)
print('Also tried to extract information from {} bad files.'.format(len(bad_files)))    
print()
print('='*50)     
"""
            #print(line.decode('UTF-8'))
            if 'abs' in decoded_line:
                print(decoded_line)

        for line in r:
            decoded = line
            print(decoded)

        for line in file:
            decoded = line.decode('UTF-8')
            print(decoded)

        with open('thatThing.html', 'a') as f:
            f.write(r.decode('UTF-8'))
"""
    
    
    
    
    
"""
    With the help of:
        - https://stackoverflow.com/a/44377437
        - https://stackoverflow.com/a/23131251
        - https://stackoverflow.com/a/59205103

"""
    