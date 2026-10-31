"""C16 stationary jitter: finite checks, not a proof of the general statement."""
from common import *
r=Report("C16")

# Exact covariance propagation for a stationary vector moving-average field.
shape=(5,5);x=product_grid(shape);lam=frequency_box((4,3));S=len(x);d=2
rng=np.random.default_rng(4116);base=rng.normal(size=(d,d));mix=np.array([[.3,-.2],[.4,.1]])
T=np.kron(np.eye(S),base)
for i,ij in enumerate(frequency_box(shape)):
 j=np.ravel_multi_index(((ij[0]+1)%5,ij[1]),shape);T[i*d:(i+1)*d,j*d:(j+1)*d]+=mix
cov=T@T.T;cls=alias_classes(lam,shape);F=character_transform(x,list(cls));TF=np.kron(F,np.eye(d));spec=TF@cov@TF.conj().T
H=Q_red(lam,x)/S;xm=realify(variation_matrices(lam,x)[0]);eq=ef=0
K=np.array([cov[i*d:(i+1)*d,:d] for i in range(S)])
for i,(key,mem) in enumerate(cls.items()):
 sr=spec[i*d:(i+1)*d,i*d:(i+1)*d];sf=np.einsum('k,kab->ab',np.exp(1j*x@key)/S,K)
 r.close(f'(50) positive-exponent normalization {key}',sr,sf,2e-14,0)
 cr=C_r(mem,d);dr=D_r(mem,d);mass=N_r(mem);pb=p_bar_r(mem,d)
 r.close(f'(51) uncentered decomposition {key}',dr,cr+mass*np.outer(pb,pb),1e-12,0)
 eq+=np.trace(cr@sr).real;ef+=np.trace(dr@sr).real
r.close('Prop15 E q',np.trace(H@cov),eq,2e-10,1e-12);r.close('Prop15 E fixed',np.trace(xm.T@xm@cov),ef,2e-10,1e-12)
r.truth('0<=rho_stat<=1',0<=eq/ef<=1)
# Covariance supported in the protected scalar band is annihilated exactly.
s=10;xx=product_grid((s,));v=np.cos(xx[:,0]);c=deficit_coefficients(8,s)
r.close('protected-band stationary energy',sum(c*abs(np.fft.ifft(v))**2),0,1e-26,0)

r.finish()
