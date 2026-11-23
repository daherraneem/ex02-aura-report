"""Chapter 5 figure: Weighted Decision Matrix Breakdown & Sensitivity Analysis.

Panel A: Stacked horizontal bars showing weighted contribution of each of the
6 decision criteria (weights summing to 1.00) for the 3 AURA launch alternatives.
Panel B: Sensitivity analysis across 4 weighting scenarios verifying robustness
of Alternative 3 (Omnichannel Hybrid).
"""
import numpy as np
import matplotlib.pyplot as plt
from aura_style import AURA, SHADES, heb, apply_style, save

apply_style()

# Criteria and baseline weights (sum = 1.00) - pure Hebrew + numeric weights for clean BiDi
criteria = [
    ("התאמה חושית ופרסונה (0.25)", 0.25, SHADES["berry"]),
    ("ויראליות ומודעות (0.20)", 0.20, SHADES["peach"]),
    ("יעילות תקציבית והחזר (0.20)", 0.20, SHADES["honey"]),
    ("זמן הגעה לשוק (0.15)", 0.15, AURA["gold"]),
    ("המרה ראשונית (0.10)", 0.10, SHADES["ruby"]),
    ("שליטה ונתוני צד ראשון (0.10)", 0.10, AURA["plum"]),
]

# Raw scores (1-10) for each alternative: [Sensory, Viral, Budget, TTM, Conv, Data]
scores = {
    "alt2": np.array([9, 5, 4, 6, 8, 7], dtype=float),
    "alt1": np.array([5, 8, 8, 9, 6, 10], dtype=float),
    "alt3": np.array([9, 9, 7, 7, 9, 7], dtype=float),
}
alt_labels = [
    heb("חלופה ב'\nקמפוס וחוויה תחילה"),
    heb("חלופה א'\nדיגיטל תחילה (D2C)"),
    heb("חלופה ג' (נבחרת)\nאומניצ'אנל היברידי"),
]
alt_keys = ["alt2", "alt1", "alt3"]

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(9.6, 4.1), gridspec_kw={"width_ratios": [1.18, 1.12]}
)
plt.subplots_adjust(wspace=0.34, bottom=0.27, top=0.84)

# ------------------------------------------------------------------
# Panel A: Stacked weighted score contributions
# ------------------------------------------------------------------
y_pos = np.arange(len(alt_keys))
lefts = np.zeros(len(alt_keys))

for idx, (cname, w, col) in enumerate(criteria):
    vals = np.array([scores[k][idx] * w for k in alt_keys])
    ax1.barh(
        y_pos,
        vals,
        left=lefts,
        height=0.52,
        color=col,
        edgecolor="white",
        linewidth=0.8,
        label=heb(cname),
    )
    for row_i, v in enumerate(vals):
        if v >= 0.58:
            txt_col = "white" if col in (SHADES["berry"], SHADES["ruby"], AURA["plum"]) else AURA["ink"]
            ax1.text(
                lefts[row_i] + v / 2,
                y_pos[row_i],
                f"{v:.2f}",
                ha="center",
                va="center",
                fontsize=7.9,
                fontweight="bold",
                color=txt_col,
            )
    lefts += vals

for row_i, tot in enumerate(lefts):
    is_winner = row_i == 2
    ax1.text(
        tot + 0.16,
        y_pos[row_i],
        f"{tot:.2f}",
        ha="left",
        va="center",
        fontsize=11.5 if is_winner else 10.5,
        fontweight="bold",
        color=AURA["plum"] if is_winner else AURA["ink"],
    )

ax1.set_yticks(y_pos)
ax1.set_yticklabels(alt_labels, fontsize=9.8)
ax1.set_xlim(0, 9.5)
ax1.set_xlabel(heb("ציון משוקלל כולל (מתוך 10)"), fontsize=10.2)
ax1.set_title(heb("א. פירוק הציון המשוקלל לפי קריטריון"), fontsize=11.2, fontweight="bold", color=AURA["plum"], pad=10)
ax1.grid(axis="x", color=AURA["grid"], linestyle="--", linewidth=0.7)
ax1.set_axisbelow(True)

# Highlight winner bar with plum border
ax1.barh(
    [2],
    [lefts[2]],
    height=0.55,
    facecolor="none",
    edgecolor=AURA["plum"],
    linewidth=1.5,
)

ax1.legend(
    loc="upper center",
    bbox_to_anchor=(0.45, -0.23),
    ncol=2,
    frameon=False,
    fontsize=8.2,
    handlelength=1.1,
    columnspacing=0.9,
)

# ------------------------------------------------------------------
# Panel B: Sensitivity analysis across 4 weighting scenarios
# ------------------------------------------------------------------
scenarios = [
    ("בסיס\n(מאוזן)", np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])),
    ("תקציב\nמחמיר", np.array([0.20, 0.15, 0.35, 0.10, 0.10, 0.10])),
    ("עדיפות\nחושית", np.array([0.35, 0.20, 0.15, 0.10, 0.10, 0.10])),
    ("מהירות\nונתונים", np.array([0.15, 0.15, 0.15, 0.25, 0.10, 0.20])),
]

x = np.arange(len(scenarios))
w_bar = 0.27

s_alt1 = [float(np.dot(scores["alt1"], w)) for _, w in scenarios]
s_alt2 = [float(np.dot(scores["alt2"], w)) for _, w in scenarios]
s_alt3 = [float(np.dot(scores["alt3"], w)) for _, w in scenarios]

b1 = ax2.bar(x - w_bar, s_alt1, width=w_bar * 0.92, color=SHADES["honey"], label=heb("חלופה א' (דיגיטל D2C)"))
b2 = ax2.bar(x, s_alt2, width=w_bar * 0.92, color=AURA["muted"], alpha=0.82, label=heb("חלופה ב' (קמפוס וחוויה)"))
b3 = ax2.bar(x + w_bar, s_alt3, width=w_bar * 0.92, color=AURA["plum"], label=heb("חלופה ג' (אומניצ'אנל היברידי)"))

for bars, col, dy in [(b1, SHADES["cocoa"], 0.08), (b2, AURA["muted"], 0.08), (b3, AURA["plum"], 0.08)]:
    for bar in bars:
        h = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            h + dy,
            f"{h:.2f}",
            ha="center",
            va="bottom",
            fontsize=7.3,
            fontweight="bold" if col == AURA["plum"] else "normal",
            color=col,
        )

ax2.set_xticks(x)
ax2.set_xticklabels([heb(name) for name, _ in scenarios], fontsize=9.2)
ax2.set_ylim(5.0, 9.0)
ax2.set_ylabel(heb("ציון משוקלל"), fontsize=10.2)
ax2.set_title(heb("ב. ניתוח רגישות לשינוי משקלים"), fontsize=11.2, fontweight="bold", color=AURA["plum"], pad=10)
ax2.grid(axis="y", color=AURA["grid"], linestyle="--", linewidth=0.7)
ax2.set_axisbelow(True)

ax2.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.23),
    ncol=1,
    frameon=False,
    fontsize=8.3,
    handlelength=1.2,
)

save(fig, "decision_matrix_scores")
