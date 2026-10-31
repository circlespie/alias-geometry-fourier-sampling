"""C08 iid jitter: finite checks, not a proof of the general statement."""
from common import *
r=Report("C08")

m,s,j,delta=sp.symbols('m s j delta',integer=True,positive=True);k=sp.symbols('k',positive=True)
opt=sp.simplify(s/delta*sp.summation(j*(delta-j),(j,1,delta-1)))
fixed=sp.simplify(2/s*sp.summation((m-j)*j**2,(j,1,m-1)))
r.truth('(53) exact expected reduced energy',sp.simplify(opt-s*(delta**2-1)/6)==0)
r.truth('(53) exact fixed energy',sp.simplify(fixed-m**2*(m**2-1)/(6*s))==0)
r.truth('(54) symbolic ratio',sp.simplify(opt/fixed-s**2*(delta**2-1)/(m**2*(m**2-1)))==0)
r.truth('(55) symbolic proportional limit',sp.simplify(sp.limit((opt/fixed).subs(delta,2*m-s).subs(s,k*m),m,sp.oo)-k**2*(2-k)**2)==0)
rng=np.random.default_rng(4108);trials=60000
for s in [16,24,31]:
 e=rng.normal(size=(trials,s));eh=np.fft.ifft(e,axis=1);c=deficit_coefficients(16,s)
 cls=alias_classes(frequency_box((16,)),(s,));d=np.array([D_r(mem,1)[0,0] for mem in cls.values()])
 for name,vals,expected in [('optimal',abs(eh)**2@c,float(damage_opt(16,s))),('fixed',abs(eh)**2@d,float(damage_fixed(16,s)))]:
  # Fixed-seed Monte Carlo, six estimated standard errors, not a proof.
  se=vals.std(ddof=1)/np.sqrt(trials)
  r.close(f'MC m=16,s={s} {name}',vals.mean(),expected,6*se+1e-10,0)
 r.close(f'MC ratio s={s}',(abs(eh)**2@c).mean()/(abs(eh)**2@d).mean(),float(rho_closed(16,s)),.015,0)

r.finish()
