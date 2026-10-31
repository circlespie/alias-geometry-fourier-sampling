"""Reference-weight reparametrization (23)-(25), including nonzero obstruction."""
from common import *
r=Report('C22');rng=np.random.default_rng(4122)
for band in [(3,2),(4,2)]:
 x=product_grid((5,5));lam=frequency_box(band);S=len(x);v=1/S+.005*np.cos(2*x[:,1]);e=rng.normal(size=x.shape);scaled=S*v[:,None]*e
 r.close(f'exact alternative reference {band}',G(lam,x,v),np.eye(len(lam)),2e-14,0)
 r.close(f'(23) node variation {band}',X(lam,x,e,v),X(lam,x,scaled),1e-14,0)
 q=Q_red(lam,x,v);value=e.ravel()@(np.repeat(v,2)*(q@e.ravel()));uniform=reduced_energy(lam,x,scaled,(5,5))
 r.close(f'(24) reduced energy {band}',value,uniform,1e-11,1e-12)
 r.truth(f'(25) same zero/nonzero obstruction {band}',(np.linalg.norm(q)<1e-9)==(np.linalg.norm(Q_red(lam,x))<1e-9))
r.finish()
