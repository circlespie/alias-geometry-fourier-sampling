"""C05 exact persistence: finite checks, not a proof of the general statement."""
from common import *
r=Report("C05")

rng=np.random.default_rng(4105)
for shape,band in [((7,),(3,)),((4,),(3,)),((5,5),(3,3)),((5,5),(4,3))]:
 lam=frequency_box(band);x=product_grid(shape);cls=alias_classes(lam,shape);injective=all(len(v)<=1 for v in cls.values())
 r.truth(f'injective iff zero reduced form {shape},{band}',injective==(np.linalg.norm(Q_red(lam,x))<1e-9))
 if injective:
  for j in range(3):
   xp=x+1e-3*rng.normal(size=x.shape);v=exact_weights(lam,xp)
   r.close(f'(22) G=I {shape}/{j}',G(lam,xp,v),np.eye(len(lam)),3e-14,0)
   r.close(f'normalization {shape}/{j}',sum(v),1,1e-14,0);r.truth(f'positive weights {shape}/{j}',min(v)>0)

r.finish()
