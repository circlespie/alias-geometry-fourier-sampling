"""C11 square energy: finite checks, not a proof of the general statement."""
from common import *
r=Report("C11")

rng=np.random.default_rng(4111);worst=0
for s in range(2,65):
 e=rng.normal(size=s);i,j=np.indices((s,s));mask=i!=j
 node=.25*np.sum((e[i[mask]]-e[j[mask]])**2/np.sin(np.pi*(i[mask]-j[mask])/s)**2)
 r.close(f'(66)=(67) s={s}',node,E_s(e),1e-8,1e-12)
 d=np.arange(1,s)
 for rr in range(s):worst=max(worst,abs(np.sum(np.sin(np.pi*rr*d/s)**2/np.sin(np.pi*d/s)**2)-rr*(s-rr)))
r.close('Fejer identity all s<=64',worst,0,2e-10,0)
for s in range(2,9):
 for rr in range(s):
  val=sp.trigsimp(sum(sp.sin(sp.pi*rr*d/s)**2/sp.sin(sp.pi*d/s)**2 for d in range(1,s)))
  # Number-field reduction proves equality exactly, not a decimal test.
  r.truth(f'exact Fejer s={s},r={rr}',sp.simplify(sp.expand_trig(val)-rr*(s-rr))==0 or sp.polys.numberfields.to_number_field(val-rr*(s-rr)).coeffs()==[0])
for s in [16,32,64,128,256]:
 x=2*np.pi*np.arange(s)/s;e=np.cos(x)+.4*np.sin(3*x)
 target=.5+3*.4**2/2;correction=(.5+9*.4**2/2)/s
 r.close(f'(68)-(69) trigonometric polynomial s={s}',E_s(e)/s**2,target-correction,1e-13,0)

# The log-Vandermonde Hessian is an independent node-space construction.
s=6;x=product_grid((s,))[:,0];H=np.zeros((s,s))
for j in range(s):
 for k in range(j):
  a=.5/np.sin((x[j]-x[k])/2)**2
  H[j,j]+=a;H[k,k]+=a;H[j,k]-=a;H[k,j]-=a
r.close('log-Vandermonde Hessian = Euclidean reduced form',H,Q_red(frequency_box((s,)),x[:,None])/s,1e-12,0)
r.close('classical Hessian spectrum',np.linalg.eigvalsh(H),sorted(j*(s-j) for j in range(s)),1e-12,0)
r.finish()
