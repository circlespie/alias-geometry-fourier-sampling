"""C15 spectral objective: finite checks, not a proof of the general statement."""
from common import *
r=Report("C15")

I=sp.I;lam=range(4);xs=[sp.pi*k/2 for k in range(4)];e=[1,0,-1,0];z=[0,sp.Rational(1,4),0,-sp.Rational(1,4)]
h=sp.Matrix(4,4,lambda a,b:sp.simplify(I*(a-b)*sum(e[k]*sp.exp(I*(a-b)*xs[k]) for k in range(4))/4))
y=sp.Matrix(4,4,lambda a,b:sp.simplify(sum(z[k]*sp.exp(I*(a-b)*xs[k]) for k in range(4))))
t=sp.symbols('lambda')
r.truth('(83) characteristic polynomial',sp.expand(h.charpoly(t).as_expr()-(t*t-t-1)*(t*t+t-1))==0)
r.truth('(84) corrected square=2I',sp.simplify((h+y)**2-2*sp.eye(4))==sp.zeros(4))
r.close('squared Frobenius norms',list(map(float,[sp.trace(h*h),sp.trace((h+y)**2)])),[6,8],0,0)
expected=sorted([float(v) for v in [(1+sp.sqrt(5))/2,-(1+sp.sqrt(5))/2,(1-sp.sqrt(5))/2,-(1-sp.sqrt(5))/2]])
r.close('eigenvalues',np.linalg.eigvalsh(np.array(h,complex)),expected,1e-14,0)
r.close('improved spectral half-spread',np.linalg.norm(np.array(h+y,complex),2),np.sqrt(2),1e-14,0)

r.finish()
