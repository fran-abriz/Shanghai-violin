# $Id: gx.py,v 1.1 2016-10-04 13:37:51-07 fran abriz $
#!/usr/bin/python

import sys, re, string

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import pandas as pd

global contest, jlab
jlab = ["DS", "VW", "ZB", "DC", "DH", "EH", "BK", "EO", "JW", "ZW", "LY"]

# Possible TODO: add axis=0 arg and change the comment
def stdize(y): # standardize columns (i.e. axis=0); returns numpy array
  global contest, jlab

  yp = pd.DataFrame(y, columns=jlab, index=contest)
  zy = yp.apply(scipy.stats.zscore, axis=0).as_matrix()
  return(zy)

# plot_cj() works with standardized columns.
# Background: We noted that different judges (columns) have
# different ranges of scores.  If we look at each contestant's scores, we want
# to know that a high (or low) score that stands out isn't because that judge
# doesn't score high (or low) relative to the other judges.

# Findings: the skewness of the scores each judge assigns varies.  So looking
# at the raw OR the standardized scores alone isn't enough.

def plot_cj(y):
  global contest, jlab

  nc = len(contest)
  nj = len(jlab)
  ncol = 4
  nr = nc/ncol

  zy = stdize(y)

  fig, axes = plt.subplots(nrows=nr, ncols=ncol, sharey=True, sharex=True, figsize=(14,11)) # 24 contestants

  fig.suptitle("Shanghai-Stern Competition: Quarterfinal Scores, Standardized by Judge", size='x-large')
  kt = {'size': 'medium'}
  sx = np.arange(nj)
  for i in range(nr):
      for j in range(ncol):
          k = i*ncol+j
          axes[i,j].scatter(sx, zy[k,:])
          axes[i,j].set_title(contest[k], **kt)

  kxt = {'size': 'x-small'}
  plt.setp([a.set_xticks(np.arange(nj)) for a in fig.axes])
  plt.setp([a.set_xticklabels(jlab, **kxt) for a in fig.axes])
  plt.setp([a.set_ylim(-3.5,3.5) for a in fig.axes])
  plt.setp([a.set_xlim(-.5,10.5) for a in fig.axes])
  plt.show()

# TODO: check that nc = len(contest)
# read in data from a file
# convert the array of scores into a Numpy nd array
# store contestant names in the array "contest"
def scores():
    global contest, njudge, nc
    q = []
    nj = 0; # number of judges
    nc = 0; # number of contestants
    newcont = 0
    contest = []; # format: number-name of contestant
    njudge = 0
    f = open("scores.data", 'r')
    while (1):
      l = f.readline()
      if (len(l) < 1): break;
      if (l[0] == '#' and len(l) > 1 and l[1].isdigit()):
	    nc += 1;
	    contest.append(l[1:-1]) # cuts off the '\n'
	    newcont = 1
	    continue
      elif (l[0] == '#'):
	    if (nj > 0): njudge = nj
	    newcont = 0
	    nj = 0
	    continue
      elif (newcont == 1):
	    q.append(float(l)) # ignores the '\n'
	    nj += 1;
    f.close()

    y = np.array(q); y.shape = (nc, njudge)
    return y
