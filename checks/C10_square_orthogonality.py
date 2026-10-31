"""C10 square orthogonality: finite checks, not a proof of the general statement."""
from common import *
r=Report("C10")

rng=np.random.default_rng(4110)
for s in [3,5,8]:
 x=product_grid((s,))+rng.uniform(0,2*np.pi);x=x[rng.permutation(s)];lam=(rng.permutation(s)+s*rng.integers(-3,4,size=s))[:,None]
 r.close(f'random exact square G {s}',G(lam,x),np.eye(s),2e-13,0)
 r.close(f'P_Y X {s}',P_Y(lam,x)@realify(variation_matrices(lam,x)[0]),0,2e-11,0)
x=product_grid((4,4));lam=frequency_box((4,4));x[:,0]+=.2*np.cos(x[:,1])
r.close('exact sheared 4x4 square G',G(lam,x),np.eye(16),5e-14,0)
r.close('P_Y X sheared 4x4',P_Y(lam,x)@realify(variation_matrices(lam,x)[0]),0,2e-12,0)

r.finish()
