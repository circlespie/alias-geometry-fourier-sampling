"""C03 alias geometry: finite checks, not a proof of the general statement."""
from common import *
r=Report("C03")

from fractions import Fraction
lam=frequency_box((4,3));mem=alias_classes(lam,(5,5))[(3,0)];mass,pb,c=class_stats(mem)
r.truth('multiplicities 3,6',dict(mem)=={(3,0):3,(-2,0):6})
r.truth('exact center (-1/3,0)',pb==[Fraction(-1,3),0])
r.truth('exact covariance diag(50,0)',c==[[50,0],[0,0]])
r.close('alias gap',np.array([3,0])-np.array([-2,0]),[5,0],0,0)
r.close('class mass',mass,9,0,0)
th=np.linspace(0,np.pi,361);z=np.column_stack([np.cos(th),np.sin(th)])
r.close('50 cos^2 theta',np.einsum('ia,ab,ib->i',z,np.array(c,float),z),50*np.cos(th)**2,2e-14,0)

r.finish()
