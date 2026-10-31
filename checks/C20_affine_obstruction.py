"""C20 affine obstruction: finite checks, not a proof of the general statement."""
from common import *
r=Report("C20")

x,lam=square_nodes();cls=alias_classes(lam,(4,4));mem=cls[(1,1)];ps=np.array([p for p,n in mem]);A=np.vstack([np.ones(len(ps)),ps.T]);_,_,vt=np.linalg.svd(A);weights=vt[-1];e=eps_ab(1,1)
M=np.einsum('ka,kb,k->ab',e,e,np.exp(1j*x@np.array([1,1])))/len(x)
ob=sum(w*p@M@p for w,p in zip(weights,ps))
r.close('(26) affine relation annihilates constant/linear terms',A@weights,0,1e-14,0)
r.truth('(29) mixed shear violates second-order condition',abs(ob)>1)
for a,b in [(1,0),(0,1)]:
 e=eps_ab(a,b);M=np.einsum('ka,kb,k->ab',e,e,np.exp(1j*x@np.array([1,1])))/len(x)
 r.close(f'(29) pure shear satisfies condition {a},{b}',sum(w*p@M@p for w,p in zip(weights,ps)),0,1e-14,0)
# General square tensor covariance (30), including the non-square example.
for shape in [(4,4),(3,5)]:
 for key,mem in alias_classes(frequency_box(shape),shape).items():
  r.close(f'(30) tensor square block {shape},{key}',C_r(mem,2),np.prod(shape)*np.diag([key[a]*(shape[a]-key[a]) for a in range(2)]),1e-12,0)

r.finish()
