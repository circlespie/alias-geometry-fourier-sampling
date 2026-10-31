"""C12 second order: finite checks, not a proof of the general statement."""
from common import *
r=Report("C12")

rng=np.random.default_rng(4112)
for shape in [(4,4),(3,5)]:
 x=product_grid(shape);lam=frequency_box(shape)
 for trial in range(3):
  g=rng.normal(size=shape[0]);f=rng.normal(size=shape[1]);inds=frequency_box(shape)
  e=np.column_stack([f[inds[:,1]],g[inds[:,0]]])
  r.close(f'q-null {shape}/{trial}',np.linalg.norm(X(lam,x,e)),0,2e-13,0)
  r.close(f'Phi_opt product {shape}/{trial}',second_order_minimum(lam,x,e),E_s(g)*E_s(f),1e-9,2e-11)
for a,b in [(1,1),(1,.5),(.5,.5),(1,0),(0,1)]:
 x,lam=square_nodes();e=eps_ab(a,b)
 r.close(f'Phi_opt=36a^2b^2 {a},{b}',second_order_minimum(lam,x,e),36*a*a*b*b,1e-11,0)
 t=10**-3.5
 if a*b:r.close(f'Fig2 straight-path limit {a},{b}',shear_gram_norm(a,b,t)/t**2,6*abs(a*b),1e-5,0)
 else:r.close(f'Fig2 pure shear exact {a},{b}',max(shear_gram_norm(a,b,t) for t in np.logspace(-3.5,-.5,25)),0,1e-13,0)

r.finish()
