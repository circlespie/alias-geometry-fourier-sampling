"""Proposition 6 and singleton Jacobian symbol (19)-(21)."""
from common import *
r=Report('C21');rng=np.random.default_rng(4121)
shape=(5,5);x=product_grid(shape);lam=frequency_box((4,3));S=len(x);cls=alias_classes(lam,shape);keys=list(cls);F=character_transform(x,keys)
e=rng.normal(size=x.shape);eh=F@e;centers=np.array([p_bar_r(mem,2) for mem in cls.values()])
a=centers+np.column_stack([.2*np.sin(2*np.pi*np.array(keys)[:,0]/5),.3*np.sin(2*np.pi*np.array(keys)[:,1]/5)])
eta_hat=-1j*np.einsum('ij,ij->i',a,eh);eta=S*F.conj().T@eta_hat
r.close('real admissible weight tangent',eta.imag,0,2e-14,0);r.close('normalized weight tangent',eta.real.sum(),0,2e-14,0)
direct=np.linalg.norm(X(lam,x,e)+Y(lam,x,eta.real/S))**2
q=reduced_energy(lam,x,e,shape)
excess=sum(N_r(mem)*abs(np.dot(a[i]-centers[i],eh[i]))**2 for i,mem in enumerate(cls.values()))
r.close('(20) prescribed symbol = optimum + excess',direct,q+excess,1e-10,1e-12)
optimal_eta=S*F.conj().T@(-1j*np.einsum('ij,ij->i',centers,eh))
xm,ym=variation_matrices(lam,x);Z=zero_sum_basis(S);ls=Z@np.linalg.lstsq(realify(ym@Z),-realify(xm@e.ravel()),rcond=1e-12)[0]
r.close('(15) optimal symbol vs dense least squares',optimal_eta.real/S,ls,1e-13,0)
for i,(key,mem) in enumerate(cls.items()):
 if len(mem)==1:
  p=mem[0][0];r.close(f'(21) singleton uses raw representative {key}',centers[i],p,0,0)
r.finish()
