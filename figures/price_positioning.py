"""Figure: Price vs. Sensory-Brand-Accessibility Value Positioning Map in Israel.

Run from the project root:  python figures/price_positioning.py
Output: figures/price_positioning.pdf

Prices are real verified Israeli consumer prices (ILS, Nov 2026) with min-max ranges.
Value index (1-10) is the sum of four transparent 0-2.5 criteria documented in Ch. 4.
"""
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from aura_style import AURA, SHADES, apply_style, heb, save

# (name, mid_price_ils, low_ils, high_ils, value_score, is_local, color, dx, dy, ha)
COMPETITORS = [
    ("Essence\n(What a Tint!)", 15, 10, 20, 4.8, True, AURA["muted"], 4, 0.62, "center"),
    ("Benefit\n(Benetint 6ml)", 112, 99, 125, 4.8, False, SHADES["cocoa"], 0, -0.65, "center"),
    ("Rare Beauty\n(Soft Pinch)", 125, 110, 140, 6.5, False, SHADES["peach"], -10, -0.68, "center"),
    ("Fenty Beauty\n(Poutsicle)", 145, 130, 160, 6.6, False, SHADES["ruby"], 10, 0.56, "center"),
    ("Rhode\n(Peptide Lip Tint)", 165, 155, 175, 7.9, False, AURA["plum"], -4, 0.55, "center"),
]

AURA_POINT = ("AURA (יעד השקה)", 69, 8.8)


def main() -> None:
    apply_style()

    fig, ax = plt.subplots(figsize=(6.9, 4.65))

    # Shaded Masstige White Space opportunity zone (generous padding inside)
    opp_box = patches.FancyBboxPatch(
        (38, 7.15), 62, 2.75,
        boxstyle="round,pad=0.12,rounding_size=0.35",
        facecolor=AURA["cream"], edgecolor=AURA["gold"],
        linewidth=1.5, linestyle="--", alpha=0.88, zorder=1,
    )
    ax.add_patch(opp_box)
    ax.text(
        69, 7.38, heb("חלל הזדמנות: Masstige מקומי"),
        ha="center", va="bottom", fontsize=9.2, fontweight="bold",
        color=AURA["plum"], zorder=2,
    )

    # Subtle background grid
    ax.grid(True, linestyle=":", color=AURA["grid"], linewidth=0.9, zorder=0)

    # Plot competitors with verified Israeli price range bars
    for name, mid, low, high, score, is_local, color, dx, dy, ha in COMPETITORS:
        xerr = [[mid - low], [high - mid]]
        ax.errorbar(
            mid, score, xerr=xerr, fmt="none",
            ecolor=color, elinewidth=1.8, capsize=3.5, alpha=0.65, zorder=3,
        )
        marker = "o" if is_local else "D"
        ax.scatter(
            mid, score, s=95, marker=marker, color=color,
            edgecolors="white", linewidths=1.3, zorder=4,
        )
        price_lbl = f"₪{low}–{high}" if low != high else f"₪{mid}"
        ax.text(
            mid + dx, score + dy,
            f"{name}\n{price_lbl}",
            ha=ha, va="center", fontsize=8.8, color=AURA["ink"],
            linespacing=1.15, zorder=5,
        )

    # Plot AURA with soft golden aura halo
    ax.scatter(
        AURA_POINT[1], AURA_POINT[2], s=600, color=AURA["gold"],
        alpha=0.28, edgecolors="none", zorder=4,
    )
    ax.scatter(
        AURA_POINT[1], AURA_POINT[2], s=260, color=SHADES["berry"],
        marker="*", edgecolors=AURA["plum"], linewidths=0.9, zorder=5,
    )
    ax.text(
        AURA_POINT[1], AURA_POINT[2] + 0.30,
        heb("AURA (יעד השקה)") + "\n₪69",
        ha="center", va="bottom", fontsize=9.8, fontweight="bold",
        color=SHADES["berry"], linespacing=1.15, zorder=6,
    )

    # Axes styling
    ax.set_xlim(0, 195)
    ax.set_ylim(3.5, 10.25)
    ax.set_xlabel(heb('מחיר בפועל לצרכנית בישראל (ש"ח)'), fontsize=11, labelpad=6)
    ax.set_ylabel(heb("מדד ערך חושי-מותגי ונגישות (1–10)"), fontsize=11, labelpad=6)
    ax.set_title(
        heb("מיצוב AURA מול המתחרים: מחיר בישראל מול ערך כולל"),
        loc="right", fontsize=12, fontweight="bold", color=AURA["plum"], pad=10,
    )
    ax.tick_params(labelsize=9.8)

    # Legend cleanly below axes (guaranteed zero overlap with any data point)
    legend_handles = [
        Line2D([0], [0], marker="*", color="w", label=heb("AURA (יעד השקה, מקומי)"),
               markerfacecolor=SHADES["berry"], markeredgecolor=AURA["plum"], markersize=11),
        Line2D([0], [0], marker="o", color="w", label=heb("זמינות מקומית בפארם"),
               markerfacecolor=AURA["muted"], markersize=8),
        Line2D([0], [0], marker="D", color="w", label=heb("יבוא מקביל / משלוח מחו\"ל"),
               markerfacecolor=AURA["plum"], markersize=7.5),
        Line2D([0], [0], color=AURA["muted"], lw=1.8, label=heb("טווח מחיר מאומת בישראל")),
    ]
    ax.legend(
        handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, -0.16),
        ncol=2, frameon=True, facecolor="white", edgecolor=AURA["grid"],
        fontsize=8.8, columnspacing=1.6, handletextpad=0.6,
    )

    save(fig, "price_positioning")


if __name__ == "__main__":
    main()
