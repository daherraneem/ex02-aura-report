"""Chapter 4 figure: Price vs. Non-Price Positioning Map in Israel (incl. Mid-Tier Brands).

Updated after expert committee review (F4 / BS-04 / BS-05 / MP-09 / DL-05):
- Includes 3 verified mid-tier brands sold in Israel (NYX, Maybelline, Clinique)
  alongside discount (Essence) and imported premium (Rhode, Rare, Fenty, Benefit).
- Y-axis is a strictly non-price subjective expert positioning index (no price/ml
  on both axes).
- Plots AURA as a target range (7.4-8.4) rather than an unproven single top point.
- Sized to printed text width (~6.4 in) with legible fonts (>= 8.5 pt) and Hebrew ש"ח.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from aura_style import AURA, SHADES, heb, apply_style, save

apply_style()

# Verified Israeli prices (min, mid, max in ILS) vs Non-Price Expert Index (Table 4.3, 0-10)
# Index = Culinary Narrative (2.5) + Moisturizing Formula (2.5) + Social Currency (2.5) + Local Trial/Availability (2.5)
competitors = [
    # (name, p_min, p_mid, p_max, score, channel_type, dx, dy, ha)
    ("Essence\n(What a Tint!)", 14, 15, 16, 4.3, "local", 4, -0.55, "left"),
    ("NYX\n(Fat Oil)", 38, 40, 42, 6.2, "local", 4, 0.28, "left"),
    ("Maybelline\n(Teddy Tint)", 46, 52, 58, 6.0, "local", 5, -0.62, "left"),
    ("Clinique\n(Black Honey)", 77, 96, 115, 7.0, "local", 2, -0.45, "center"),
    ("Benefit\n(Benetint)", 99, 112, 125, 4.4, "remote", 0, -0.66, "center"),
    ("Rare Beauty\n(Soft Pinch)", 110, 125, 140, 6.3, "remote", 0, -0.68, "center"),
    ("Fenty Beauty\n(Poutsicle)", 130, 145, 160, 6.1, "remote", 0, 0.42, "center"),
    ("Rhode\n(Peptide Tint)", 155, 165, 175, 7.9, "remote", -4, 0.36, "right"),
]

fig, ax = plt.subplots(figsize=(6.5, 4.35))
plt.subplots_adjust(left=0.11, right=0.97, top=0.89, bottom=0.23)

# Shaded Masstige target zone (45-95 ILS)
zone = mpatches.FancyBboxPatch(
    (45, 7.10),
    48,
    2.02,
    boxstyle="round,pad=0.10",
    facecolor=AURA["cream"],
    edgecolor=AURA["gold"],
    linewidth=1.2,
    linestyle="--",
    zorder=1,
)
ax.add_patch(zone)
ax.text(
    69,
    9.02,
    heb("אזור יעד Masstige מקומי (45–95 ש\"ח)"),
    ha="center",
    va="top",
    fontsize=8.2,
    fontweight="bold",
    color=SHADES["cocoa"],
    zorder=2,
)

# Plot competitors
for name, pmin, pmid, pmax, sc, ctype, dx, dy, ha in competitors:
    col = SHADES["honey"] if ctype == "local" else AURA["muted"]
    mk = "o" if ctype == "local" else "D"
    ax.plot([pmin, pmax], [sc, sc], color=col, linewidth=1.6, alpha=0.6, zorder=3)
    ax.scatter(pmid, sc, s=46, color=col, marker=mk, edgecolor="white", linewidth=0.7, zorder=4)
    ax.text(
        pmid + dx,
        sc + dy,
        name,
        fontsize=7.6,
        ha=ha,
        va="center",
        color=AURA["ink"],
        linespacing=1.05,
        zorder=5,
    )

# Plot AURA as a vertical target range (7.4 - 8.4) at 69 ILS
ax.plot([69, 69], [7.4, 8.4], color=SHADES["berry"], linewidth=4.2, solid_capstyle="round", zorder=5)
ax.scatter(69, 7.9, s=115, color=SHADES["berry"], marker="*", edgecolor=AURA["plum"], linewidth=0.7, zorder=6)
ax.text(
    65.5,
    7.90,
    heb("AURA\n69 ש\"ח\n(7.4–8.4)"),
    ha="right",
    va="center",
    fontsize=7.9,
    fontweight="bold",
    color=AURA["plum"],
    linespacing=1.1,
    zorder=6,
)

ax.set_xlim(0, 185)
ax.set_ylim(3.2, 9.35)
ax.set_xlabel(heb("מחיר קמעונאי בפועל לצרכנית בישראל (ש\"ח, כולל מע\"מ)"), fontsize=9.2)
ax.set_ylabel(heb("מדד מיצוב חושי-מותגי וזמינות (הערכת צוות, 0–10)"), fontsize=9.0)
ax.set_title(
    heb("מפת מיצוב: מחיר בישראל מול מדד ערך לא-מחירי (כולל מותגי ביניים)"),
    fontsize=10.2,
    fontweight="bold",
    color=AURA["plum"],
    pad=10,
)
ax.grid(True, color=AURA["grid"], linestyle="--", linewidth=0.65)
ax.set_axisbelow(True)

# Clean legend below x-axis
handles = [
    plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=SHADES["honey"], markersize=7, label=heb("זמינות מקומית בפארם / אתר ישראלי")),
    plt.Line2D([0], [0], marker="D", color="w", markerfacecolor=AURA["muted"], markersize=6.5, label=heb("יבוא מקביל / חו\"ל (ללא התנסות מקומית)")),
    plt.Line2D([0], [0], marker="*", color=SHADES["berry"], markerfacecolor=SHADES["berry"], markeredgecolor=AURA["plum"], markersize=9, lw=2.5, label=heb("AURA — טווח יעד מתוכנן (7.4–8.4)")),
]
ax.legend(
    handles=handles,
    loc="upper center",
    bbox_to_anchor=(0.48, -0.18),
    ncol=2,
    frameon=False,
    fontsize=7.9,
    handlelength=1.4,
    columnspacing=1.0,
)

save(fig, "price_positioning")
