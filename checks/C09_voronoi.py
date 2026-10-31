"""C09 voronoi: finite checks, not a proof of the general statement."""
from common import *
r=Report("C09")

rng=np.random.default_rng(4109)
for m,s in [(8,8),(8,10),(8,15),(16,16),(16,20),(16,31)]:
 x=product_grid((s,))[:,0];e=rng.normal(size=s);h=1e-6
 eta=s*(voronoi_weights(x+h*e)-voronoi_weights(x-h*e))/(2*h)
 r.close(f'(57) FD Voronoi symbol {m},{s}',np.fft.ifft(eta),-1j*voronoi_symbol(s,np.arange(s))*np.fft.ifft(e),2e-9,0)
 for residue,ps,mass,pb,c in class_data_1d(m,s):
  a=voronoi_symbol(s,residue);direct=sum((m-abs(p))*(p-a)**2 for p in ps)
  r.close(f'(58) excess {m},{s},r={residue}',direct,float(c)+mass*(a-float(pb))**2,1e-10,1e-12)
  if len(ps)==2:
   delta=2*m-s;j=residue-(s-m);formula=delta*(a-(m-delta)*(delta-2*j)/delta)**2
   r.close(f'(59) collided excess {m},{s},r={residue}',direct-float(c),formula,1e-10,1e-12)
 fx,op,vo=dense_expected_energies(m,s)
 r.close(f'Figure 4 Voronoi dense energy {m},{s}',vo,damage_voronoi(m,s),1e-9,1e-11)
r.truth('critical Voronoi repair fraction negative',1-damage_voronoi(16,16)/float(damage_fixed(16,16))<0)

for s in range(16,32):
 r.close(f'full Figure 4 Voronoi curve s={s}',dense_expected_energies(16,s)[2],damage_voronoi(16,s),1e-9,1e-11)
for s in [8,9,16]:
 zeros=np.flatnonzero(abs(voronoi_symbol(s,np.arange(s)))<1e-12)
 r.truth(f'critical Voronoi zero modes s={s}',list(zeros)==([0,s//2] if s%2==0 else [0]))
x=sp.symbols('x');r.truth('low-mode symbol sin(x)=x+O(x^3)',sp.series(sp.sin(x),x,0,3).removeO()==x)
r.finish()
