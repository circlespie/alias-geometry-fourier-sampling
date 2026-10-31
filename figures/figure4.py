"""Regenerate paper Figure 4, using aliasgeom only; no frozen data inputs."""
from style import *

def figure3():
    # Closed forms against class data and against dense brute force.
    for m in (4, 6, 8, 16, 64):
        for s in range(m, 2 * m):
            d = 2 * m - s
            assert damage_fixed(m, s) == Fraction(m * m * (m * m - 1), 6 * s)
            assert damage_opt(m, s) == Fraction(s * (d * d - 1), 6)  # sigma^2 = 1
            assert damage_opt(m, s) / damage_fixed(m, s) == rho_closed(m, s)
    dense = {}
    for m, s in [(8, 8), (8, 10), (8, 15), (6, 9), (16, 16), (16, 20)]:
        fx, op, vo = dense_expected_energies(m, s)
        assert close(fx, float(damage_fixed(m, s)), 1e-10), (m, s)
        assert close(op, float(damage_opt(m, s)), 1e-9), (m, s)
        assert close(vo, damage_voronoi(m, s), 1e-10), (m, s)
        dense[f"{m},{s}"] = {"fixed": fx, "opt": op, "voronoi": vo}
    vor = lambda m, s: 1 - damage_voronoi(m, s) / float(damage_fixed(m, s))
    rep = lambda m, s: float(1 - rho_closed(m, s))
    assert vor(16, 16) < 0 and rep(16, 16) == 0
    assert all(rep(m, 2 * m - 1) == 1 for m in (8, 16, 64))       # delta = 1 gives rho = 0

    k = np.linspace(1, 2, 400)
    lim = repair_limit(k)
    for m in (64,):
        ss = np.arange(m, 2 * m)
        assert np.max(np.abs([rep(m, s) - (1 - (s / m) ** 2 * (2 - s / m) ** 2)
                              for s in ss])) < 0.05

    fig, ax = plt.subplots(figsize=(0.66 * TEXTWIDTH, 2.75))
    ax.axhspan(-0.2, 0, facecolor="0.93", edgecolor=LIGHT, hatch="////", lw=0, zorder=0)
    ax.text(1.985, -0.11, "worse than fixed weights", ha="right", va="center",
            fontsize=7.5, color=DARK, bbox=dict(fc="0.93", ec="none", pad=0.5))
    ax.axhline(0, color=INK, lw=0.9, zorder=1)
    ax.plot(k, lim, color=INK, lw=1.4, label=r"limit $\kappa\to$ (Cor.)", zorder=3)
    for m, mk in [(8, "o"), (16, "s"), (64, "^")]:
        ss = np.arange(m, 2 * m)
        ax.plot(ss / m, [rep(m, int(s)) for s in ss], ls="none", marker=mk, ms=3.6,
                mfc="white", mec=INK, mew=0.8, label=rf"optimal, $m={m}$", zorder=4)
    ss = np.arange(16, 32)
    vv = [vor(16, int(s)) for s in ss]
    ax.plot(ss / 16, vv, ls=(0, (4, 2)), marker="x", ms=4, color=DARK, lw=1.0,
            label=r"Voronoi, $m=16$", zorder=4)
    ax.set_xlabel(r"oversampling ratio $\kappa=s/m$")
    ax.set_ylabel("repairable fraction")
    ax.set_xlim(0.97, 2.0)
    ax.set_ylim(-0.2, 1.08)
    ax.set_yticks([-0.2, 0, 0.25, 0.5, 0.75, 1.0])
    h, l = ax.get_legend_handles_labels()
    l[0] = "optimal, limit"
    ax.legend(h, l, loc="upper left", frameon=False, handlelength=2.2)
    savefig(fig, "Figure4.pdf")
    CHECKS["figure3"] = {"dense_vs_closed": dense, "R_vor_16_16": vor(16, 16),
                         "R_opt_s_2m_minus_1": 1.0, "min_voronoi_m16": min(vv)}

if __name__ == "__main__":
    figure3()
    print("PASS Figure4.pdf: all numerical assertions passed")
