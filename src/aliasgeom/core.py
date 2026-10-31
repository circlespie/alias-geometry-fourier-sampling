"""Finite Fourier rules using the paper's positive-exponent convention.

Nodes are S-by-d arrays in radians; frequencies are M-by-d integer arrays.
Vector fields flatten in node-major order. Complex matrix spaces use the real
Frobenius inner product. Q_red is an operator in the reference-weighted metric,
not the Euclidean matrix of the quadratic form. Empty alias classes have zero
mass, center and covariance, as in Theorem 5.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import numpy as np
from scipy.linalg import block_diag


def frequency_box(shape):
    """Cartesian frequency box, equation (71)."""
    return np.array(list(product(*(range(m) for m in shape))), dtype=int)


def product_grid(shape):
    """Subgroup nodes 2*pi*k_a/s_a, Section 3.1 and (71)."""
    return 2*np.pi*frequency_box(shape)/np.array(shape)


def fourier_matrix(frequencies, nodes):
    """A_{ell,k}=exp(i ell.x_k), Section 2.1."""
    return np.exp(1j*np.asarray(frequencies)@np.asarray(nodes).T)


def G(frequencies, nodes, weights=None):
    """Weighted Gram matrix G=A diag(v) A*, Section 2.1 (not G-I)."""
    a=fourier_matrix(frequencies,nodes)
    if weights is None: weights=np.full(len(nodes),1/len(nodes))
    return (a*np.asarray(weights))@a.conj().T


def gram_defect(frequencies,nodes,weights=None):
    """G-I, the unscaled Gram defect in Section 2.1."""
    return G(frequencies,nodes,weights)-np.eye(len(frequencies))


def variation_matrices(frequencies,nodes,weights=None):
    """Column matrices for X and unrestricted Y, equations (5) and (4)."""
    lam=np.asarray(frequencies);nodes=np.asarray(nodes);S,d=nodes.shape
    if weights is None: weights=np.full(S,1/S)
    diff=(lam[:,None,:]-lam[None,:,:]).reshape(-1,d)
    y=np.exp(1j*diff@nodes.T)
    x=(1j*y[:,:,None]*np.asarray(weights)[None,:,None]*diff[:,None,:]).reshape(len(diff),S*d)
    return x,y


def X(frequencies,nodes,epsilon,weights=None):
    """Node first variation X epsilon, equation (5)."""
    return (variation_matrices(frequencies,nodes,weights)[0]@np.asarray(epsilon).ravel()).reshape(len(frequencies),-1)


def Y(frequencies,nodes,zeta):
    """Weight first variation Y zeta, equation (4); admissible zeta sums to zero."""
    return (variation_matrices(frequencies,nodes)[1]@np.asarray(zeta)).reshape(len(frequencies),-1)


def realify(a):
    """Isometry from complex matrix entries to real Frobenius coordinates."""
    return np.concatenate([a.real,a.imag],axis=0)


def zero_sum_basis(S):
    """Basis for the real admissible weight space 1^T zeta=0, Section 2.3."""
    return np.vstack([np.eye(S-1),-np.ones(S-1)])


def image_basis(a,tol=1e-12):
    """Numerical orthonormal basis for a real map's image, stated relative cutoff."""
    u,s,_=np.linalg.svd(a,full_matrices=False)
    return u[:,s>tol*max(1.,s[0] if len(s) else 0.)]


def P_Y(frequencies,nodes):
    """Real Frobenius orthogonal projector onto Y{1^T zeta=0}, Section 2.3."""
    y=variation_matrices(frequencies,nodes)[1]@zero_sum_basis(len(nodes))
    u=image_basis(realify(y));return u@u.T


def Q_red(frequencies,nodes,weights=None):
    """X^sharp(I-P_Y)X in the weighted node metric (10), Section 2.3.

    At uniform weights the Euclidean quadratic-form matrix is Q_red/S.
    """
    S,d=np.shape(nodes)
    if weights is None: weights=np.full(S,1/S)
    x=realify(variation_matrices(frequencies,nodes,weights)[0]);u=image_basis(realify(variation_matrices(frequencies,nodes)[1]@zero_sum_basis(S)))
    residual=x-u@(u.T@x)
    return (residual.T@residual)/np.repeat(weights,d)[:,None]


def difference_multiplicities(frequencies):
    """N_p counts ordered frequency pairs with difference p, Section 3.1."""
    return dict(Counter(tuple(a-b) for a in np.asarray(frequencies) for b in np.asarray(frequencies)))


def alias_classes(frequencies,moduli,generator=None):
    """Delta_r with N_p, (11); product grids or rank-1 cyclic lattice.

    Product keys are tuples; cyclic keys are integers. Empty classes are included.
    For a cyclic lattice pass moduli=(S,), generator=z.
    """
    if generator is None:
        out={tuple(r):[] for r in frequency_box(moduli)}
        key=lambda p:tuple(np.array(p)%np.array(moduli))
    else:
        out={r:[] for r in range(moduli[0])}
        key=lambda p:int(np.dot(p,generator)%moduli[0])
    for p,n in difference_multiplicities(frequencies).items():out[key(p)].append((p,n))
    return out


def N_r(members):
    """Class mass N_r=sum N_p, equation (14)."""
    return sum(n for _,n in members)


def p_bar_r(members,dimension):
    """Multiplicity-weighted class center, (14); zero for empty classes."""
    mass=N_r(members)
    if not mass:return np.zeros(dimension)
    return sum(n*np.array(p) for p,n in members)/mass


def C_r(members,dimension):
    """Multiplicity-weighted covariance C_r, equation (16)."""
    center=p_bar_r(members,dimension)
    return sum((n*np.outer(np.array(p)-center,np.array(p)-center) for p,n in members),start=np.zeros((dimension,dimension)))


def D_r(members,dimension):
    """Uncentered moment D_r, equation (51)."""
    return sum((n*np.outer(p,p) for p,n in members),start=np.zeros((dimension,dimension)))


def class_stats(members):
    """Exact rational mass, center and covariance, equations (14),(16)."""
    if not members:raise ValueError('use p_bar_r/C_r with dimension for empty classes')
    mass=N_r(members);d=len(members[0][0])
    center=[Fraction(int(sum(n*p[a] for p,n in members)),mass) for a in range(d)]
    c=[[sum(n*(p[a]-center[a])*(p[b]-center[b]) for p,n in members) for b in range(d)] for a in range(d)]
    return mass,center,c


def character_transform(nodes,residues):
    """Positive-exponent F, normalized by 1/S, Section 3.1."""
    return np.exp(1j*np.asarray(residues)@np.asarray(nodes).T)/len(nodes)


def block_matrix(classes,dimension):
    """Direct sum of C_r in dictionary order, Theorem 5."""
    return block_diag(*(C_r(mem,dimension) for mem in classes.values()))


def reduced_energy(frequencies,nodes,epsilon,moduli,generator=None):
    """q=sum eps_hat* C_r eps_hat, equation (17)."""
    classes=alias_classes(frequencies,moduli,generator);d=nodes.shape[1]
    if generator is None:phases=character_transform(nodes,list(classes))
    else:phases=np.exp(2j*np.pi*np.outer(list(classes),np.arange(len(nodes)))/len(nodes))/len(nodes)
    eh=phases@epsilon
    return float(sum(np.vdot(eh[i],C_r(mem,d)@eh[i]).real for i,mem in enumerate(classes.values())))


def exact_weights(frequencies,nodes,reference=None):
    """Smooth real right-inverse weights, equation (22), Theorem 7."""
    S=len(nodes)
    if reference is None:reference=np.ones(S)/S
    ps=[p for p in difference_multiplicities(frequencies) if any(p) and next(v for v in p if v)>0]
    phase=np.exp(1j*np.array(ps)@nodes.T)
    mr=np.vstack([np.ones(S),phase.real,phase.imag]);b=np.zeros(len(mr));b[0]=1
    return reference+mr.T@np.linalg.solve(mr@mr.T,b-mr@reference)


def deficit_coefficients(m,s):
    """Equation (48): C_{s-m+j}=s^2*j*(delta-j)/delta; includes delta=1."""
    if not m<=s<=2*m-1:raise ValueError('requires m<=s<=2m-1')
    delta=2*m-s;c=np.zeros(s)
    for j in range(1,delta):c[s-m+j]=s*s*j*(delta-j)/delta
    return c


def class_data_1d(m,s):
    """Exact class data used by Figures 3-4, omitting the zero class."""
    result=[]
    for (r,),members in alias_classes(np.arange(m)[:,None],(s,)).items():
        if r==0 or not members:continue
        mass,center,c=class_stats(members)
        result.append((r,[p[0] for p,_ in members],mass,center[0],c[0][0]))
    return result


def damage_fixed(m,s):
    """E||H^(0)||_F^2 for unit iid variance, equation (53)."""
    return Fraction(m*m*(m*m-1),6*s)


def damage_opt(m,s):
    """E q for unit iid variance, equation (53), including delta=1."""
    return Fraction(s*((2*m-s)**2-1),6)


def rho_closed(m,s):
    """Ratio of expected energies, not expected ratios, equation (54)."""
    return damage_opt(m,s)/damage_fixed(m,s)


def repair_limit(kappa):
    """Proportional-limit repairable fraction, equation (55)."""
    return 1-np.asarray(kappa)**2*(2-np.asarray(kappa))**2


def voronoi_symbol(s,residues):
    """a_r^Vor=s/(2*pi) sin(2*pi*r/s), equation (57)."""
    return s/(2*np.pi)*np.sin(2*np.pi*np.asarray(residues)/s)


def voronoi_weights(nodes):
    """Periodic ordered 1D Voronoi weights, equation (56)."""
    nodes=np.asarray(nodes);gaps=np.diff(np.r_[nodes,nodes[0]+2*np.pi])
    return (gaps+np.roll(gaps,1))/(4*np.pi)


def damage_voronoi(m,s):
    """Expected unit-variance Voronoi energy from (58)-(59)."""
    return sum(float(c)+mass*(voronoi_symbol(s,r)-float(pb))**2 for r,_,mass,pb,c in class_data_1d(m,s))/s


def E_s(values,s=None):
    """Square DFT energy E_s, equations (36),(66); positive-exponent ifft."""
    values=np.asarray(values);s=len(values) if s is None else s
    r=np.arange(s);return float(s*np.sum(r*(s-r)*np.abs(np.fft.ifft(values))**2))


def square_nodes(s=4):
    """Tensor reference for Figure 2."""
    return product_grid((s,s)),frequency_box((s,s))


def eps_ab(alpha,beta,s=4):
    """Figure 2 shear epsilon=(alpha cos x2,beta cos x1)."""
    x,_=square_nodes(s);return np.column_stack([alpha*np.cos(x[:,1]),beta*np.cos(x[:,0])])


def shear_gram_norm(alpha,beta,t,s=4):
    """Direct straight-path Gram norm for Figure 2(b)."""
    x,lam=square_nodes(s);return float(np.linalg.norm(gram_defect(lam,x+t*eps_ab(alpha,beta,s))))


def second_order_residual(frequencies,nodes,epsilon):
    """Uncorrected t^2 Gram coefficient -E[(p.eps)^2 exp(ip.x)]/2, Section 5.3."""
    lam=np.asarray(frequencies);d=nodes.shape[1];diff=(lam[:,None,:]-lam[None,:,:]).reshape(-1,d)
    return -.5*np.mean((diff@epsilon.T)**2*np.exp(1j*diff@nodes.T),axis=1)


def second_order_minimum(frequencies,nodes,epsilon):
    """Direct real least squares over (xi,omega), Proposition 12; numerical illustration only."""
    x,y=variation_matrices(frequencies,nodes);a=realify(np.column_stack([x,y@zero_sum_basis(len(nodes))]));b=realify(second_order_residual(frequencies,nodes,epsilon))
    correction=np.linalg.lstsq(a,-b,rcond=1e-12)[0];return float(np.linalg.norm(b+a@correction)**2)


def dense_expected_energies(m,s):
    """Independent dense trace evaluations of fixed, optimal and Voronoi iid energies."""
    x=product_grid((s,));lam=frequency_box((m,));xm,ym=variation_matrices(lam,x)
    v=np.zeros((s,s))
    for k in range(s):v[k,(k+1)%s]+=1/(4*np.pi);v[k,(k-1)%s]-=1/(4*np.pi)
    return float(np.linalg.norm(xm)**2),float(np.trace(Q_red(lam,x))/s),float(np.linalg.norm(xm+ym@v)**2)
