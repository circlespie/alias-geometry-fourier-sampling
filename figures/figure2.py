"""Regenerate paper Figure 2, using aliasgeom only; no frozen data inputs."""
from style import *

def figure2():
    s = 4
    xk = 2 * np.pi * np.arange(s) / s
    assert close(E_s(np.cos(xk), s), 6.0)
    phi = lambda a, b: E_s(b * np.cos(xk), s) * E_s(a * np.cos(xk), s)  # E(g) E(f)
    for a, b in [(1, 1), (0.5, -2), (1, 0), (0.3, 0.7)]:
        assert close(phi(a, b), 36 * a * a * b * b)

    # (a) map of Phi_* = 36 alpha^2 beta^2
    grid = np.linspace(-1, 1, 241)
    Z = phi(1, 1) * np.outer(grid ** 2, grid ** 2)  # rows beta, cols alpha
    assert close(Z.max(), 36.0)

    # (b) straight uniform-weight paths
    ts = np.logspace(-3.5, -0.5, 25)
    pure = {(1.0, 0.0): [], (0.0, 1.0): []}
    for key in pure:
        pure[key] = [gram_defect(*key, t) for t in ts]
        assert max(pure[key]) < 1e-13, (key, max(pure[key]))
    mixed_pairs = [(1.0, 1.0), (1.0, 0.5), (0.5, 0.5)]
    mixed = {}
    for a, b in mixed_pairs:
        ratio = np.array([gram_defect(a, b, t) / t ** 2 for t in ts])
        target = 6 * abs(a * b)
        err = np.abs(ratio - target)
        assert err[0] / target < 1e-5, (a, b, err[0])          # t ~ 3e-4
        assert np.all(np.diff(err[:15]) > 0), (a, b)           # error grows with t
        assert np.polyfit(np.log(ts[:12]), np.log(err[:12]), 1)[0] > 1.8  # O(t^2)
        mixed[(a, b)] = ratio

    fig = plt.figure(figsize=(0.9 * TEXTWIDTH, 2.85))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.1], height_ratios=[2.1, 1.0],
                          wspace=0.62, hspace=0.12)
    axa = fig.add_subplot(gs[:, 0])
    axb = fig.add_subplot(gs[0, 1])
    axc = fig.add_subplot(gs[1, 1], sharex=axb)
    im = axa.imshow(Z, origin="lower", extent=[-1, 1, -1, 1], cmap="Greys",
                    vmin=0, vmax=40, aspect="equal", interpolation="bilinear")
    cs = axa.contour(grid, grid, Z, levels=[1, 4, 9, 16, 25], colors=DARK, linewidths=0.5)
    axa.clabel(cs, fmt="%d", fontsize=6.5, inline=True)
    axa.plot([-1, 1], [0, 0], color=INK, lw=2.2, solid_capstyle="butt")
    axa.plot([0, 0], [-1, 1], color=INK, lw=2.2, solid_capstyle="butt")
    axa.text(0.97, 0.06, "exact\nrow shears", ha="right", va="bottom", fontsize=7.5,
             bbox=dict(fc="white", ec="none", pad=0.6))
    axa.text(0.07, -0.97, "exact column\nshears", ha="left", va="bottom", fontsize=7.5,
             bbox=dict(fc="white", ec="none", pad=0.6))
    axa.set_xlabel(r"$\alpha$")
    axa.set_ylabel(r"$\beta$")
    axa.set_xticks([-1, 0, 1])
    axa.set_yticks([-1, 0, 1])
    cb = fig.colorbar(im, ax=axa, shrink=0.8, pad=0.04)
    cb.set_label(r"$\Phi_*(\alpha,\beta)=36\alpha^2\beta^2$")
    cb.ax.tick_params(labelsize=7)
    panel_label(axa, r"(a)  $\Phi_*$ on $\ker q$")

    # (b) top: mixed shears, ||G - I||_F / t^2 tends to sqrt(Phi_*) = 6|alpha beta|
    styles = [("-", "o"), ("--", "s"), (":", "^")]
    for ((a, b), ratio), (ls, mk) in zip(mixed.items(), styles):
        target = 6 * abs(a * b)
        axb.axhline(target, color=MID, lw=0.6, ls=(0, (1, 1.5)), zorder=1)
        axb.semilogx(ts, ratio, ls=ls, marker=mk, ms=3.2, mfc="white", color=INK, lw=LW,
                     markevery=3, label=rf"$({a:g},{b:g})$", zorder=3)
        axb.text(ts[-1] * 1.25, target, rf"${target:g}$", fontsize=7, va="center",
                 ha="left", clip_on=False)
    axb.text(ts[-1] * 1.25, 7.0, r"$\sqrt{\Phi_*}$", fontsize=7, va="center", ha="left",
             clip_on=False)
    axb.set_ylim(0, 7.6)
    axb.set_yticks([0, 2, 4, 6])
    axb.set_ylabel(r"$\|G-I\|_F\,/\,t^2$")
    axb.legend(loc="center", bbox_to_anchor=(0.5, 0.5), ncol=3, frameon=False,
               handlelength=2.0, columnspacing=0.8, handletextpad=0.4, fontsize=7.5)
    axb.text(0.5, 0.575, r"mixed shears $(\alpha,\beta)$", transform=axb.transAxes,
             ha="center", va="bottom", fontsize=7.5)
    plt.setp(axb.get_xticklabels(), visible=False)
    panel_label(axb, r"(b)  paths $x^0+t\epsilon_{\alpha,\beta}$, uniform weights")

    # (b) bottom: pure shears stay exact, so ||G - I||_F itself is at roundoff
    for key, mk in [((1.0, 0.0), "x"), ((0.0, 1.0), "+")]:
        vals = np.maximum(np.array(pure[key]), 1e-17)
        axc.loglog(ts, vals, ls="none", marker=mk, ms=3.8, color=INK, markevery=2,
                   label=rf"pure $({key[0]:g},{key[1]:g})$")
    axc.set_ylim(1e-18, 1e-13)
    axc.set_yticks([1e-16, 1e-14])
    axc.set_ylabel(r"$\|G-I\|_F$", labelpad=1)
    axc.set_xlabel(r"$t$")
    axc.set_xlim(ts[0], ts[-1])
    axc.legend(loc="lower left", frameon=False, fontsize=7.5, ncol=2, borderaxespad=0.2,
               columnspacing=1.0, handletextpad=0.3)

    savefig(fig, "Figure2.pdf")
    CHECKS["figure2"] = {
        "E_4(cos)": 6.0, "pure_shear_max_defect": max(max(v) for v in pure.values()),
        "mixed_ratio_at_smallest_t": {f"{a},{b}": float(r[0]) for (a, b), r in mixed.items()},
        "mixed_targets": {f"{a},{b}": 6 * abs(a * b) for a, b in mixed},
    }

if __name__ == "__main__":
    figure2()
    print("PASS Figure2.pdf: all numerical assertions passed")
