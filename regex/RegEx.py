# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Import the regular expression module

# <codecell>

import re

# <markdowncell>

# Open your file of interest

# <codecell>

struct=open("./regex/structureoutput.txt").readlines()

# <markdowncell>

# I like to take a look to make sure I opened the right thing

# <codecell>

struct[:10]

# <markdowncell>

# decide what you are searching for in this set of strings (this is where regexpal can be quite handy!)

# <codecell>

sestr="\f\d\d"

# <codecell>

print(sestr)

# <markdowncell>

# Using raw fotmatted string in python is often useful for regular expression searches.

# <codecell>

sestr=r"\f\d\d"

# <codecell>

print(sestr)

# <markdowncell>

# Important! when doing a regular expression search in python: search term first: THEN place you are looking.
# This is a really common mistake, that is hard to notice.

# <codecell>

fi[10]

# <codecell>

item=re.search(r".+(\n)",fi[10])
item.group(0)

# <codecell>

item.group(1)

# <codecell>

struct[21]

# <codecell>

match=re.search(r"\d\d\d:\s .+",struct[21])
print(match)

# <codecell>

match.group(0)

# <codecell>

match.group(1)

# <codecell>

match2=re.search(r"(\d\d\d):\s+(\d+\.\d+)\s+(\d+\.\d+).+",struct[21])

# <codecell>

match2

# <codecell>

match2.group(0)

# <codecell>

print(match2.group(1))
print(match2.group(2))
print(match2.group(3))

# <codecell>

for lin in struct:
    if re.search(r"(\d\d\d):\s+(\d+\.\d+)\s+(\d+\.\d+).+",lin):
        

# <codecell>

def show_groups(pattern, text):
  m = re.search(pattern, text)
  if m is None:
    print 'NO MATCH'
    return
  for i in range(1, 1 + len(m.groups())):
    print '%2d: %s' % (i, m.groups(i))


show_groups(r"(\d\d\d):\s+(\d+\.\d+)\s+(\d+\.\d+).+", lin)
 

# <codecell>


