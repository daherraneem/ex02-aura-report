"""Figure: Israel cosmetics market forecast (2026-2031) and AURA TAM/SAM/SOM funnel.

Run from the project root:  python figures/market_growth_tam_sam_som.py
Output: figures/market_growth_tam_sam_som.pdf

Sources:
- Mordor Intelligence (2026): Israel Cosmetic Products Market $408.53M (2026) -> $511.64M (2031), CAGR 4.60%.
- Bank of Israel / market rate (Nov 2026): ~3.35 ILS/USD -> TAM ~1,369M ILS.
- CHE (2026) & CBS (2024): 350,900 students x 60.3% women = ~211.6K female students;
  70% digital/lip adoption (~148.1K) x 2.5 units/yr x 69 ILS = SAM ~25.55M ILS;
  Year-1 SOM target (2.0% of SAM) = ~0.51M ILS.
"""
import matplotlib.pyplot as plt
import numpy as np

from aura_style import AURA, SHADES, apply_style, heb, save


def main() -> None:
    apply_style()

    fig, (ax_l, ax_r) = plt.subplots(
        1, 2, figsize=(8.2, 3.55), gridspec_kw={"width_ratios": [1.0, 1.08]}
    )
    fig.subplots_adjust(wspace=0.74)

    # ------------------------------------------------------------------
    # Right panel (read first in Hebrew RTL): Israel Cosmetics Forecast
    # ------------------------------------------------------------------
    years = np.array([2026, 2027, 2028, 2029, 2030, 2031])
    base_2026 = 408.53
    cagr = 0.046
    values_usd = np.array([base_2026 * ((1 + cagr) ** i) for i in range(len(years))])
    values_usd[-1] = 511.64  # exact published 2031 endpoint

    bar_colors = [
        AURA["plum"],
        AURA["gold"],
        AURA["gold"],
        AURA["gold"],
        AURA["gold"],
        SHADES["berry"],
    ]
    bars = ax_r.bar(years, values_usd, color=bar_colors, width=0.56,
                    edgecolor="white", linewidth=1.2, zorder=3)

    ax_r.set_xlim(2025.35, 2031.65)
    ax_r.set_ylim(0, 640)
    ax_r.set_xticks(years)
    ax_r.set_xticklabels([str(y) for y in years], fontsize=9.8)
    ax_r.set_ylabel(heb("מיליוני דולר (USD)"), fontsize=10.5, color=AURA["ink"], labelpad=6)
    ax_r.grid(axis="y", linestyle="--", color=AURA["grid"], linewidth=0.8, zorder=0)
    ax_r.tick_params(axis="y", labelsize=9.5)

    for idx, (bar, val) in enumerate(zip(bars, values_usd)):
        weight = "bold" if idx in (0, len(years) - 1) else "normal"
        col = AURA["ink"] if idx in (0, len(years) - 1) else AURA["muted"]
        fs = 9.5 if idx in (0, len(years) - 1) else 8.5
        ax_r.text(
            bar.get_x() + bar.get_width() / 2,
            val + 12,
            f"${val:.0f}M" if idx not in (0, len(years) - 1) else f"${val:.1f}M",
            ha="center", va="bottom", fontsize=fs, fontweight=weight, color=col,
        )

    # CAGR badge well above bars
    ax_r.annotate(
        heb("CAGR: 4.60%"),
        xy=(2028.3, 582),
        ha="center", va="center",
        fontsize=9.5, fontweight="bold", color=AURA["plum"],
        bbox=dict(boxstyle="round,pad=0.35", facecolor=AURA["cream"],
                  edgecolor=AURA["gold"], linewidth=1.1),
    )
    ax_r.set_title(
        heb("א. תחזית שוק הקוסמטיקה בישראל"),
        loc="right", fontsize=11.5, fontweight="bold", color=AURA["plum"], pad=10,
    )

    # ------------------------------------------------------------------
    # Left panel (read second in Hebrew RTL): TAM / SAM / SOM (log scale)
    # ------------------------------------------------------------------
    levels = [
        ("TAM\nקוסמטיקה בישראל", 1368.6, "₪1,369M", AURA["plum"]),
        ("SAM\nסטודנטיות (דיגיטל)", 25.55, "₪25.5M", AURA["gold"]),
        ("SOM\nיעד שנה א' (2%)", 0.51, "₪0.51M", SHADES["berry"]),
    ]

    y_pos = np.arange(len(levels))
    vals_ils = [item[1] for item in levels]
    colors_l = [item[3] for item in levels]
    labels_l = [heb(item[0]) for item in levels]

    ax_l.barh(y_pos, vals_ils, color=colors_l, height=0.50,
              edgecolor="white", linewidth=1.5, zorder=3)
    ax_l.set_xscale("log")
    ax_l.set_xlim(0.1, 14000)
    ax_l.invert_xaxis()  # RTL: bars grow right-to-left
    ax_l.invert_yaxis()
    ax_l.yaxis.tick_right()
    ax_l.set_yticks(y_pos)
    ax_l.set_yticklabels(labels_l, fontsize=9.6, linespacing=1.15)
    ax_l.tick_params(axis="y", length=0, pad=7)

    ax_l.set_xticks([1, 10, 100, 1000])
    ax_l.set_xticklabels(["1", "10", "100", "1,000"], fontsize=9.5)
    ax_l.set_xlabel(heb('מיליוני ש"ח (סקאלה לוגריתמית)'), fontsize=10, color=AURA["ink"], labelpad=6)
    ax_l.grid(axis="x", linestyle="--", color=AURA["grid"], linewidth=0.8, zorder=0)

    # Spines for RTL horizontal bars
    ax_l.spines["left"].set_visible(False)
    ax_l.spines["top"].set_visible(False)
    ax_l.spines["right"].set_visible(True)
    ax_l.spines["right"].set_color(AURA["muted"])

    for i, (_, val, txt, _) in enumerate(levels):
        ax_l.text(
            val * 1.4, i, txt,
            va="center", ha="right",
            fontsize=9.8, fontweight="bold", color=AURA["ink"],
        )

    ax_l.set_title(
        heb("ב. גזירת TAM / SAM / SOM ל-AURA"),
        loc="right", fontsize=11.5, fontweight="bold", color=AURA["plum"], pad=10,
    )

    save(fig, "market_growth_tam_sam_som")


if __name__ == "__main__":
    main()
