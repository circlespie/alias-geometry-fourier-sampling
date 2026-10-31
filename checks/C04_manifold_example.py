"""C04 manifold example: finite checks, not a proof of the general statement."""
from common import *
r=Report("C04")

lam=frequency_box((4,3));x=product_grid((5,5));cls=alias_classes(lam,(5,5));q=Q_red(lam,x)
r.close('|Delta|',len(difference_multiplicities(lam)),35,0,0)
r.close('occupied classes',sum(bool(v) for v in cls.values()),25,0,0)
rank=np.linalg.matrix_rank(q,tol=1e-9)
r.close('rank Q_red',rank,10,0,0);r.close('kernel dimension',50-rank,40,0,0)
r.truth('all representatives affinely independent',all(np.linalg.matrix_rank(np.column_stack([np.ones(len(mem)),np.array([p for p,n in mem])]))==len(mem) for mem in cls.values()))
y=realify(variation_matrices(lam,x)[1]@zero_sum_basis(25));r.close('unique weight: rank Y',np.linalg.matrix_rank(y,tol=1e-9),24,0,0)

r.finish()
