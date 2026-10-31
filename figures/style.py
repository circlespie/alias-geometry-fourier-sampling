"""Shared publication plotting style; numerical objects come from aliasgeom."""
import os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR',str(ROOT.parent/'.cache'/'matplotlib'))
sys.path.insert(0,str(ROOT.parent/'src'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction
from matplotlib.patches import Arc,FancyArrowPatch
from aliasgeom import *
from aliasgeom import shear_gram_norm as gram_defect
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
TEXTWIDTH=6.5
INK='black'
DARK='0.25'
MID='0.5'
LIGHT='0.82'
LW=1.2
CHECKS={}
plt.rcParams.update({
    "font.family": "STIXGeneral",
    "mathtext.fontset": "stix",
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.linewidth": 0.7,
    "xtick.major.width": 0.7,
    "ytick.major.width": 0.7,
    "lines.linewidth": LW,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.dpi": 300,
})


def panel_label(ax,text):
    ax.set_title(text,loc='left',fontsize=9,fontweight='bold')
def savefig(fig,name):
    fig.savefig(OUT/name,bbox_inches='tight',pad_inches=.02,metadata={'CreationDate':None,'ModDate':None,'Creator':None,'Producer':None})
    plt.close(fig)
def close(a,b,tol=1e-12):
    return abs(float(a)-float(b))<=tol*max(1.,abs(float(b)))
