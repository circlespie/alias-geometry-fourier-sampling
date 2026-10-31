"""C01 first variation: finite checks, not a proof of the general statement."""
from common import *
r=Report("C01")

rng=np.random.default_rng(4101)
for shape,band in [((7,),(4,)),((5,5),(4,3))]:
 x=product_grid(shape);lam=frequency_box(band);S=len(x);e=rng.normal(size=x.shape);z=rng.normal(size=S);z-=z.mean();z/=S
 h=2e-6
 fd=(G(lam,x+h*e,np.ones(S)/S+h*z)-G(lam,x-h*e,np.ones(S)/S-h*z))/(2*h)
 r.close(f'G exact {shape}',G(lam,x),np.eye(len(lam)),1e-13,0)
 r.close(f'first derivative {shape}',fd,X(lam,x,e)+Y(lam,x,z),2e-8,2e-8)

r.finish()
