"""C17 local optimum: finite checks, not a proof of the general statement."""
from common import *
r=Report("C17")

rng=np.random.default_rng(4117);x=product_grid((5,5));lam=frequency_box((4,3));S=len(x);e=rng.normal(size=x.shape);xm,ym=variation_matrices(lam,x);Z=zero_sum_basis(S);a=realify(ym@Z);b=realify(xm@e.ravel());z=Z@np.linalg.lstsq(a,-b,rcond=1e-12)[0]
q=np.linalg.norm(b+realify(ym)@z)**2
for t in [1e-4,5e-5]:
 xp=x+t*e;yp=realify(variation_matrices(lam,xp)[1]@Z);bp=realify(gram_defect(lam,xp).ravel());corr=Z@np.linalg.lstsq(yp,-bp,rcond=1e-12)[0]
 r.truth(f'positive local optimum t={t}',min(1/S+corr)>0)
 r.close(f'Prop2 optimum F/t^2 t={t}',np.linalg.norm(bp+realify(variation_matrices(lam,xp)[1])@corr)**2/t**2,q,.02,0)
 r.close(f'Prop2 derivative v_* t={t}',corr/t,z,3e-4,0)
 arbitrary=rng.normal(size=S)/S;arbitrary-=arbitrary.mean()
 r.truth(f'Cor3 arbitrary positive weights above fixed-node minimum t={t}',np.linalg.norm(gram_defect(lam,xp,np.ones(S)/S+t*arbitrary))**2>=np.linalg.norm(bp+realify(variation_matrices(lam,xp)[1])@corr)**2)

r.finish()
