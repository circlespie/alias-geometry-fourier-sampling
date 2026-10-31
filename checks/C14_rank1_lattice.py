"""C14 rank1 lattice: finite checks, not a proof of the general statement."""
from common import *
r=Report("C14")

from itertools import product
lam=np.array([k for k in product(range(-3,4),repeat=2) if (1+abs(k[0]))*(1+abs(k[1]))<=4]);S=23;z=np.array([1,5]);x=2*np.pi*np.arange(S)[:,None]*z/S
cls=alias_classes(lam,(S,),z)
r.close('M',len(lam),17,0,0);r.close('distinct resolved characters',len(set(lam@z%S)),17,0,0)
r.close('|Delta|',len(difference_multiplicities(lam)),69,0,0)
r.close('ranks (0,1,2)',np.bincount([np.linalg.matrix_rank(C_r(mem,2),tol=1e-9) for mem in cls.values()],minlength=3),[1,2,20],0,0)
r.truth('(81) representatives and multiplicities',dict(cls[2])=={(-3,1):4,(-1,-4):2,(0,5):2,(2,0):7})
r.close('(82) center',p_bar_r(cls[2],2),[0,.4],1e-14,0)
r.close('affine augmented rank',np.linalg.matrix_rank(np.column_stack([np.ones(4),[p for p,n in cls[2]]])),3,0,0)
r.close('exact rule',G(lam,x),np.eye(17),3e-14,0)
rng=np.random.default_rng(4114);worst=0
xm,ym=variation_matrices(lam,x);a=realify(ym@zero_sum_basis(S))
for _ in range(5):
 e=rng.normal(size=x.shape);b=realify(xm@e.ravel());v=np.linalg.lstsq(a,-b,rcond=1e-12)[0];dense=np.linalg.norm(b+a@v)**2;block=reduced_energy(lam,x,e,(S,),z);worst=max(worst,abs(dense-block)/dense)
r.close('dense/block relative error <1e-14',worst,0,1e-14,0)

r.finish()
