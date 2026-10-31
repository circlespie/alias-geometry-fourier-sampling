"""C02 fourier blocks: finite checks, not a proof of the general statement."""
from common import *
r=Report("C02")

rng=np.random.default_rng(4102)
s1=int(rng.integers(7,12));shape2=tuple(map(int,rng.integers(4,7,size=2)))
cases=[((5,5),frequency_box((4,3))),((s1,),rng.choice(s1,5,replace=False)[:,None]),(shape2,frequency_box(shape2)[rng.choice(np.prod(shape2),8,replace=False)])]
for shape,lam in cases:
 x=product_grid(shape);d=len(shape);S=len(x);classes=alias_classes(lam,shape)
 u=np.kron(character_transform(x,list(classes))*np.sqrt(S),np.eye(d));q=Q_red(lam,x)
 r.close(f'F Q F^-1 direct sum {shape}',u@q@u.conj().T,block_matrix(classes,d),1e-10,1e-11)
 e=rng.normal(size=x.shape)
 r.close(f'quadratic form {shape}',e.ravel()@q@e.ravel()/S,reduced_energy(lam,x,e,shape),1e-10,1e-11)

r.finish()
