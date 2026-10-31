"""Regenerate paper Figure 1, using aliasgeom only; no frozen data inputs."""
from style import *

def figure1():
    Lambda = [(i, j) for i in range(4) for j in range(3)]
    moduli = (5, 5)
    N = difference_multiplicities(Lambda)
    classes = alias_classes(Lambda, moduli)

    members = sorted(classes[(3, 0)], key=lambda t: -t[0][0])
    Nr, pbar, C = class_stats(members)
    assert [m[0] for m in members] == [(3, 0), (-2, 0)]
    assert [m[1] for m in members] == [3, 6]
    assert Nr == 9
    assert pbar == [Fraction(-1, 3), Fraction(0)]
    assert C == [[50, 0], [0, 0]]
    g = tuple(a - b for a, b in zip(members[0][0], members[1][0]))
    assert g == (5, 0)
    a, b = 3, 6
    assert Fraction(a * b, a + b) * g[0] ** 2 == 50  # rank-one form ab/(a+b) g g^T
    assert len(N) == 35 and len(classes) == 25
    collided = sorted(r for r, mem in classes.items() if len(mem) > 1)
    assert collided == [(r1, r2) for r1 in (2, 3) for r2 in range(5)]

    fig, (ax, axb) = plt.subplots(
        1, 2, figsize=(0.82 * TEXTWIDTH, 2.9),
        gridspec_kw={"width_ratios": [1.85, 1.0], "wspace": 0.38})

    # (a) raw difference set, collided points open, highlighted class bold
    for p, n in N.items():
        is_coll = len(classes[tuple(pa % 5 for pa in p)]) > 1
        if p in ((3, 0), (-2, 0)):
            continue
        ax.scatter(p[0], p[1], s=6 + 4.5 * n,
                   facecolor="white" if is_coll else LIGHT,
                   edgecolor=MID, lw=0.7, zorder=2)
    hl = {(3, 0): ("s", 3), (-2, 0): ("o", 6)}
    for p, (mk, n) in hl.items():
        ax.scatter(p[0], p[1], s=6 + 4.5 * n * 3.2, marker=mk, facecolor=DARK,
                   edgecolor=INK, lw=0.9, zorder=4)
    # labels for the two representatives sit in a strip below the lattice
    ax.text(-2, -2.55, r"$p_2=(-2,0)$" + "\n" + r"$N_{p_2}=6$", ha="center", va="top",
            fontsize=8)
    ax.text(3.5, -2.55, r"$p_1=(3,0)$" + "\n" + r"$N_{p_1}=3$", ha="right", va="top",
            fontsize=8)
    for x in (-2, 3):
        ax.plot([x, x], [2.5, 0.3], ls=(0, (1, 1.5)), lw=0.6, color=MID, zorder=1)
    # alias gap in a strip above the lattice
    ax.add_patch(FancyArrowPatch((-2, 2.6), (3, 2.6), arrowstyle="<->",
                                 mutation_scale=9, lw=1.0, color=INK, zorder=5,
                                 shrinkA=0, shrinkB=0))
    ax.text(3.5, 2.78, r"$g=p_1-p_2=(5,0)$", ha="right", va="bottom", fontsize=8)
    xc = float(pbar[0])
    ax.plot([xc, xc], [-2.4, 2.4], ls=(0, (4, 2)), lw=1.0, color=INK, zorder=3)
    ax.scatter(xc, 0, marker="X", s=55, facecolor="white", edgecolor=INK, lw=1.0, zorder=6)
    ax.text(xc - 0.1, 0.5, r"$\bar p_r=(-1/3,\,0)$", ha="right", va="center", fontsize=8,
            bbox=dict(fc="white", ec="none", pad=0.3), zorder=6)
    ax.text(xc + 0.1, -2.55, r"$\ker C_r\perp g$", ha="left", va="top", fontsize=8)
    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-3.35, 3.3)
    ax.set_xticks(range(-3, 4))
    ax.set_yticks(range(-2, 3))
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(r"$p_1$")
    ax.set_ylabel(r"$p_2$")
    panel_label(ax, r"(a)  $\Delta=\Lambda-\Lambda$, class $r=(3,0)$")

    # (b) defect of a unit polarization z = (cos t, sin t): z^* C_r z = 50 cos^2 t
    th = np.linspace(0, np.pi, 361)
    Cm = np.array(C, dtype=float)
    vals = np.array([np.array([np.cos(t), np.sin(t)]) @ Cm @ np.array([np.cos(t), np.sin(t)])
                     for t in th])
    assert np.allclose(vals, 50 * np.cos(th) ** 2, atol=1e-12)
    axb.plot(th, vals, color=INK, lw=LW)
    axb.axvline(np.pi / 2, ls=(0, (4, 2)), lw=1.0, color=INK)
    axb.text(np.pi / 2 + 0.08, 44, r"$z\in\ker C_r$", fontsize=8, ha="left")
    axb.set_xticks([0, np.pi / 2, np.pi])
    axb.set_xticklabels([r"$0$", r"$\pi/2$", r"$\pi$"])
    axb.set_yticks([0, 25, 50])
    axb.set_xlim(0, np.pi)
    axb.set_ylim(0, 55)
    axb.set_xlabel(r"polarization angle $\theta$")
    axb.set_ylabel(r"$z^*C_rz=50\cos^2\theta$")
    panel_label(axb, r"(b)  $z=(\cos\theta,\sin\theta)$")

    savefig(fig, "Figure1.pdf")
    CHECKS["figure1"] = {"N_r": Nr, "pbar": [str(x) for x in pbar], "C": C, "g": g,
                         "collided_classes": len(collided), "Delta_size": len(N)}

if __name__ == "__main__":
    figure1()
    print("PASS Figure1.pdf: all numerical assertions passed")
