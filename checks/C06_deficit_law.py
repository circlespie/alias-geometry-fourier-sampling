"""C06 deficit law: finite checks, not a proof of the general statement."""
from common import *
r=Report("C06")

worst=0
for m in [4,8,16]:
 for s in range(m,2*m):
  x=product_grid((s,));lam=frequency_box((m,));u=character_transform(x,np.arange(s)[:,None])*np.sqrt(s)
  dense=u@Q_red(lam,x)@u.conj().T;pred=np.diag(deficit_coefficients(m,s));worst=max(worst,np.max(abs(dense-pred)))
r.close('all m=4,8,16, m<=s<=2m-1 dense vs (47)',worst,0,3e-10,0)
c=deficit_coefficients(8,10)
r.close('Figure 3 collided coefficients',c[3:8],[250/3,400/3,150,400/3,250/3],1e-12,0)
r.close('Figure 3 class centers',[float(v[3]) for v in class_data_1d(8,10) if len(v[1])==2],[4/3,2/3,0,-2/3,-4/3],1e-14,0)

r.finish()
