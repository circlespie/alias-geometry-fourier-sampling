"""Deterministic check reporting. Every assertion has an explicit tolerance."""
import os
for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[name]='1'
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import sympy as sp
from aliasgeom import *

class Report:
    def __init__(self,claim): self.claim=claim;self.rows=[]
    def close(self,name,computed,expected,atol=1e-10,rtol=1e-10):
        a=np.asarray(computed);b=np.asarray(expected)
        error=float(np.max(np.abs(a-b))) if a.size else 0.
        bound=float(atol+rtol*(np.max(np.abs(b)) if b.size else 0.))
        ok=bool(error<=bound)
        show=lambda v:np.array2string(np.asarray(v),precision=12,threshold=12).replace('\n',' ')
        row=dict(name=name,claimed=show(b),computed=show(a),error=error,tolerance=bound,status='PASS' if ok else 'FAIL')
        self.rows.append(row)
        print(f"{row['status']} {name}: claimed={row['claimed']}; computed={row['computed']}; max_error={error:.3g}; tolerance={bound:.3g}")
    def truth(self,name,condition): self.close(name,int(bool(condition)),1,0,0)
    def finish(self):
        print('RESULT_JSON '+json.dumps(dict(claim=self.claim,status='PASS' if all(r['status']=='PASS' for r in self.rows) else 'FAIL',checks=self.rows)))
        if any(r['status']=='FAIL' for r in self.rows):raise SystemExit(1)

def relative(a,b):return np.linalg.norm(a-b)/max(np.linalg.norm(b),1e-30)
