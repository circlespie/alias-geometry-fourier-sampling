"""C19 frame and reconstruction: finite checks, not a proof of the general statement."""
from common import *
r=Report("C19")

rng=np.random.default_rng(4119);x=product_grid((8,))+.02*rng.normal(size=(8,1));lam=frequency_box((5,));v=rng.uniform(.8,1.2,len(x));v/=sum(v);a=fourier_matrix(lam,x);g=G(lam,x,v);h=g-np.eye(5)
fp=np.sum(v[:,None]*v[None,:]*abs(a.conj().T@a)**2)
r.close('(7) frame potential',np.linalg.norm(h)**2,fp-5,1e-13,0)
# Exact expectation for uniform sampling of coordinate unit vectors, covariance I/M.
r.close('(8) isotropic reconstruction MSE',np.mean([np.linalg.norm(h[:,j])**2 for j in range(5)]),np.linalg.norm(h)**2/5,1e-14,0)
r.truth('spectral norm <= Frobenius norm',np.linalg.norm(h,2)<=np.linalg.norm(h))

x=product_grid((7,));lam=frequency_box((3,));e=rng.normal(size=x.shape);xm,ym=variation_matrices(lam,x);Z=zero_sum_basis(7)
z=Z@np.linalg.lstsq(realify(ym@Z),-realify(xm@e.ravel()),rcond=1e-12)[0]
r.close('q-null optimized linear path',X(lam,x,e)+Y(lam,x,z),0,1e-14,0)
errors=[]
for t in [1e-4,5e-5]:
 g=G(lam,x+t*e,np.ones(7)/7+t*z);errors.append([np.linalg.norm(g-np.eye(3),2)/t,(np.linalg.cond(g)-1)/t])
r.close('(9) normalized spectral error halves with t',np.array(errors[1])/np.array(errors[0]),[.5,.5],.002,0)
r.finish()
