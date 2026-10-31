"""C18 determinant: finite checks, not a proof of the general statement."""
from common import *
r=Report("C18")

rng=np.random.default_rng(4118);s=7;x=product_grid((s,));lam=frequency_box((s,));e=.1*rng.normal(size=x.shape);z=.01*rng.normal(size=s);z-=z.mean();t=1e-4
for sign in [-1,1]:
 a=fourier_matrix(lam,x+sign*t*e);v=np.ones(s)/s+sign*t*z;g=G(lam,x+sign*t*e,v)
 r.close('(64) log determinant separation',np.linalg.slogdet(g)[1],2*np.linalg.slogdet(a)[1]+sum(np.log(v)),1e-13,0)
f=lambda t:np.linalg.slogdet(G(lam,x+t*e,np.ones(s)/s+t*z))[1]
r.close('(65) logdet Hessian',(f(t)+f(-t)-2*f(0))/t**2,-np.linalg.norm(X(lam,x,e)+Y(lam,x,z))**2,2e-6,0)
r.close('mixed Hessian orthogonality',np.vdot(X(lam,x,e),Y(lam,x,z)).real,0,1e-14,0)

r.finish()
