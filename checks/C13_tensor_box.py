"""C13 tensor box: finite checks, not a proof of the general statement."""
from common import *
r=Report("C13")

ms=(3,2,2);ss=(4,4,3);lam=frequency_box(ms);x=product_grid(ss);cls=alias_classes(lam,ss)
per=[alias_classes(frequency_box((ma,)),(sa,)) for ma,sa in zip(ms,ss)]
for key,mem in cls.items():
 masses=[N_r(per[a][(key[a],)]) for a in range(3)]
 pred=np.diag([C_r(per[a][(key[a],)],1)[0,0]*np.prod([masses[b] for b in range(3) if b!=a]) for a in range(3)])
 r.close(f'(74) mass {key}',N_r(mem),np.prod(masses),0,0)
 r.close(f'(75)-(76) covariance {key}',C_r(mem,3),pred,1e-12,0)
 if N_r(mem):r.close(f'center {key}',p_bar_r(mem,3),[p_bar_r(per[a][(key[a],)],1)[0] for a in range(3)],1e-14,0)
u=np.kron(character_transform(x,list(cls))*np.sqrt(len(x)),np.eye(3))
r.close('(77) 3D dense operator vs factored blocks',u@Q_red(lam,x)@u.conj().T,block_matrix(cls,3),2e-10,1e-11)
r.truth('example includes empty coordinate classes',any(not mem for mem in per[1].values()))

r.finish()
