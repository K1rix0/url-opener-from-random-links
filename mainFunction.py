#program to put links in file, then randomly get a yt video link and play it

from fileDeals import *
from linkPicking import *
from playingVideo import *

theList = gettingLinks()
theLink = linkPick(theList)
playVideo(theLink)
