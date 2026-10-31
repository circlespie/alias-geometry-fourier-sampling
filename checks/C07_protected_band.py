"""C07 protected band: finite checks, not a proof of the general statement."""
from common import *
r=Report("C07")

for m in [4,8,16]:
 for s in range(m,2*m):
  c=deficit_coefficients(m,s);r.close(f'kernel dimension m={m},s={s}',sum(c==0),2*(s-m)+1,0,0)
  signed=np.where(np.arange(s)<=s//2,np.arange(s),np.arange(s)-s)
  r.truth(f'protected modes m={m},s={s}',np.array_equal(c==0,abs(signed)<=s-m))

r.finish()
