"""Regenerate paper Figure 3, using aliasgeom only; no frozen data inputs."""
from style import *

def figure4():
    m, s = 8, 10
    d = 2 * m - s
    assert d == 6
    data = [c for c in class_data_1d(m, s) if len(c[1]) > 1]
    data.sort(key=lambda c: c[0])
    expect_C = [Fraction(250, 3), Fraction(400, 3), Fraction(150), Fraction(400, 3),
                Fraction(250, 3)]
    expect_pbar = [Fraction(4, 3), Fraction(2, 3), Fraction(0), Fraction(-2, 3),
                   Fraction(-4, 3)]
    pairs = []
    for j, (r, ps, Nr, pbar, C) in enumerate(data, start=1):
        assert r == s - m + j
        pp, pm = r, r - s
        assert sorted(ps) == [pm, pp] and pm == j - m
        assert (m - abs(pp), m - abs(pm)) == (d - j, j)
        assert Nr == d
        assert pbar == Fraction((m - d) * (d - 2 * j), d) == expect_pbar[j - 1]
        assert C == Fraction(s * s, d) * j * (d - j) == expect_C[j - 1]
        pairs.append((j, r, pp, pm, pbar, C))
    assert [(p[2], p[3]) for p in pairs] == [(3, -7), (4, -6), (5, -5), (6, -4), (7, -3)]
    singles = [c for c in class_data_1d(m, s) if len(c[1]) == 1]
    assert all(C == 0 for *_, C in singles)

    fig, (axa, axb) = plt.subplots(
        2, 1, figsize=(0.9 * TEXTWIDTH, 4.2),
        gridspec_kw={"height_ratios": [1.35, 1.0], "hspace": 0.62})

    # (a) raw differences with collided pairs joined by arcs
    collided = {p for pair in pairs for p in pair[2:4]}
    for p in range(-(m - 1), m):
        n = m - abs(p)
        coll = p in collided
        axa.scatter(p, 0, s=8 + 9 * n, facecolor="white" if coll else LIGHT,
                    edgecolor=INK if coll else MID, lw=0.9 if coll else 0.7, zorder=4)
        axa.text(p, -0.55, f"{n}", ha="center", va="top", fontsize=7, color=DARK)
        axa.text(p, -1.05, f"{p % s}", ha="center", va="top", fontsize=7,
                 color=INK if coll else DARK, fontweight="bold" if coll else "normal")
    axa.text(-8.05, -0.55, r"$N_p$:", ha="right", va="top", fontsize=7, color=DARK)
    axa.text(-8.05, -1.05, r"$p\ \mathrm{mod}\ s$:", ha="right", va="top", fontsize=7)
    styles = ["-", (0, (5, 2)), (0, (1, 1.2)), (0, (5, 2, 1, 2)), (0, (3, 1, 1, 1, 1, 1))]
    for (j, r, pp, pm, pbar, C), ls in zip(pairs, styles):
        h = 0.45 + 0.5 * j
        mid = (pp + pm) / 2
        axa.add_patch(Arc((mid, 0), pp - pm, 2 * h, theta1=0, theta2=180, lw=1.0,
                          color=INK, ls=ls, zorder=2))
        xb = float(pbar)
        yb = h * np.sqrt(max(0.0, 1 - ((xb - mid) / ((pp - pm) / 2)) ** 2))
        axa.plot(xb, yb, marker="D", ms=3.8, mfc=INK, mec=INK, zorder=5)
        axa.text(mid, h + 0.06, rf"$j={j}$", fontsize=6.5, ha="center", va="bottom",
                 bbox=dict(fc="white", ec="none", pad=0.15), zorder=6)
    axa.plot([], [], ls="none", marker="D", ms=3.8, color=INK, label=r"class centre $\bar p_j$")
    axa.scatter([], [], s=40, facecolor="white", edgecolor=INK, label="collided difference")
    axa.scatter([], [], s=40, facecolor=LIGHT, edgecolor=MID, label="singleton class")
    axa.axhline(0, color=MID, lw=0.6, zorder=1)
    axa.set_xlim(-8.9, 8.9)
    axa.set_ylim(-1.55, 3.45)
    axa.set_yticks([])
    for sp in ("left", "right", "top"):
        axa.spines[sp].set_visible(False)
    axa.set_xticks(range(-7, 8))
    axa.set_xlabel(r"raw difference $p\in\Delta=\{-7,\ldots,7\}$")
    axa.legend(loc="upper left", frameon=False, fontsize=7, handletextpad=0.3,
               borderaxespad=0.0, bbox_to_anchor=(-0.01, 1.07))
    panel_label(axa, r"(a)  collided pairs, $m=8$, $s=10$")

    # (b) covariance coefficients against centred frequency
    ns = np.arange(-(s // 2) + 1, s // 2 + 1)                    # -4..5
    Cvals = {}
    for j, r, *_rest, C in pairs:
        n = r if r <= s // 2 else r - s
        Cvals[n] = (float(C), j)
    axb.axvspan(-(s - m) - 0.5, (s - m) + 0.5, facecolor="0.92", edgecolor=LIGHT,
                hatch="\\\\\\\\", lw=0, zorder=0)
    axb.text(0, 165, r"protected band $|n|\leq s-m=2$", ha="center", va="center",
             fontsize=7.5, bbox=dict(fc="0.92", ec="none", pad=0.5))
    for n in ns:
        val, j = Cvals.get(int(n), (0.0, None))
        if j is None:
            axb.plot(n, 0, marker="o", ms=3.5, mfc=LIGHT, mec=MID, zorder=3)
        else:
            axb.vlines(n, 0, val, color=INK, lw=2.2, zorder=3)
            axb.plot(n, val, marker="o", ms=3.5, mfc=INK, mec=INK, zorder=4)
            label = {250 / 3: r"$\frac{250}{3}$", 400 / 3: r"$\frac{400}{3}$", 150.0: r"$150$"}
            key = min(label, key=lambda v: abs(v - val))
            axb.text(n, val + 9, label[key] + rf" $(j={j})$", ha="center", va="bottom",
                     fontsize=7)
    axb.axhline(0, color=INK, lw=0.7)
    axb.set_xticks(ns)
    axb.set_xlim(-4.8, 5.8)
    axb.set_ylim(0, 205)
    axb.set_yticks([0, 50, 100, 150])
    axb.set_xlabel(r"centred frequency $n$ (residue $r\equiv n\ (\mathrm{mod}\ 10)$)")
    axb.set_ylabel(r"$C_{r_j}=\frac{s^2}{\delta}\,j(\delta-j)$")
    panel_label(axb, r"(b)  covariance coefficients, $\delta=2m-s=6$")

    savefig(fig, "Figure3.pdf")
    CHECKS["figure4"] = {"pairs": [(p[2], p[3]) for p in pairs],
                         "pbar": [str(p[4]) for p in pairs], "C": [str(p[5]) for p in pairs]}

if __name__ == "__main__":
    figure4()
    print("PASS Figure3.pdf: all numerical assertions passed")
