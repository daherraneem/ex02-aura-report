"""Chapter 5 figure: Weighted Decision Matrix Breakdown & Sensitivity Analysis.

Updated after expert committee review (F4 / BS-02 / MP-11 / DL-05 / DL-06):
- RTL panel order: Panel א (Breakdown) on the RIGHT, Panel ב (Sensitivity) on the LEFT.
- Honest re-scored Alternative C (7.65 vs A=7.40, B=6.45) with anchored rubric.
- Panel ב tests BOTH weighting scenarios AND a -1 score-sensitivity check on C's Sensory
  score (explicitly revealing the 7.40 tie break-even with Alt A).
- Sized to printed text width (6.5 in) with legible fonts (>= 7.5-8.5 pt) and dark text
  on light segments.
"""
import numpy as np
import matplotlib.pyplot as plt
from aura_style import AURA, SHADES, heb, apply_style, save

apply_style()

# Criteria and baseline weights (sum = 1.00)
criteria = [
    ("התאמה חושית ופרסונה (0.25)", 0.25, SHADES["berry"], "white"),
    ("ויראליות ומודעות (0.20)", 0.20, SHADES["peach"], AURA["ink"]),
    ("יעילות תקציבית והחזר (0.20)", 0.20, SHADES["honey"], AURA["ink"]),
    ("זמן הגעה לשוק (0.15)", 0.15, AURA["gold"], AURA["ink"]),
    ("המרה ראשונית (0.10)", 0.10, SHADES["ruby"], "white"),
    ("שליטה ונתוני צד ראשון (0.10)", 0.10, AURA["plum"], "white"),
]

# Raw scores (1-10): [Sensory, Viral, Budget, TTM, Conv, Data]
scores = {
    "alt2": np.array([9, 5, 4, 6, 8, 7], dtype=float),
    "alt1": np.array([5, 8, 8, 9, 6, 10], dtype=float),
    "alt3": np.array([8, 8, 7, 7, 8, 8], dtype=float),
}
alt_labels = [
    heb("חלופה ב'\nקמפוס וחוויה"),
    heb("חלופה א'\nדיגיטל (D2C)"),
    heb("חלופה ג'\nהיברידית"),
]
alt_keys = ["alt2", "alt1", "alt3"]

# RTL order: ax_left = Panel ב (Sensitivity), ax_right = Panel א (Breakdown)
fig, (ax_left, ax_right) = plt.subplots(
    1, 2, figsize=(6.55, 3.85), gridspec_kw={"width_ratios": [1.05, 1.15]}
)
plt.subplots_adjust(left=0.07, right=0.86, wspace=0.40, bottom=0.31, top=0.85)

# ------------------------------------------------------------------
# Panel א (RIGHT): Stacked weighted score contributions
# ------------------------------------------------------------------
y_pos = np.arange(len(alt_keys))
lefts = np.zeros(len(alt_keys))

for idx, (cname, w, col, txt_col) in enumerate(criteria):
    vals = np.array([scores[k][idx] * w for k in alt_keys])
    ax_right.barh(
        y_pos,
        vals,
        left=lefts,
        height=0.52,
        color=col,
        edgecolor="white",
        linewidth=0.7,
        label=heb(cname),
    )
    for row_i, v in enumerate(vals):
        if v >= 0.58:
            ax_right.text(
                lefts[row_i] + v / 2,
                y_pos[row_i],
                f"{v:.2f}",
                ha="center",
                va="center",
                fontsize=6.7,
                fontweight="bold",
                color=txt_col,
            )
    lefts += vals

for row_i, tot in enumerate(lefts):
    is_winner = row_i == 2
    ax_right.text(
        tot + 0.16,
        y_pos[row_i],
        f"{tot:.2f}",
        ha="left",
        va="center",
        fontsize=9.2 if is_winner else 8.5,
        fontweight="bold",
        color=AURA["plum"] if is_winner else AURA["ink"],
    )

ax_right.yaxis.tick_right()
ax_right.set_yticks(y_pos)
ax_right.set_yticklabels(alt_labels, fontsize=8.0)
ax_right.spines["left"].set_visible(False)
ax_right.spines["right"].set_visible(True)
ax_right.set_xlim(0, 9.2)
ax_right.set_xlabel(heb("ציון משוקלל (מתוך 10)"), fontsize=8.5)
ax_right.set_title(heb("א. פירוק הציון לפי קריטריון"), fontsize=9.4, fontweight="bold", color=AURA["plum"], pad=8)
ax_right.grid(axis="x", color=AURA["grid"], linestyle="--", linewidth=0.6)
ax_right.set_axisbelow(True)

ax_right.barh(
    [2],
    [lefts[2]],
    height=0.55,
    facecolor="none",
    edgecolor=AURA["plum"],
    linewidth=1.3,
)

ax_right.legend(
    loc="upper center",
    bbox_to_anchor=(0.48, -0.25),
    ncol=2,
    frameon=False,
    fontsize=7.0,
    handlelength=1.0,
    columnspacing=0.6,
)

# ------------------------------------------------------------------
# Panel ב (LEFT): Weight + Score Sensitivity Analysis
# ------------------------------------------------------------------
# 4 scenarios: Baseline, Sensory-First, Budget-Strict, and C Sensory -1 (Score Sensitivity)
base_w = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.10])
sens_w = np.array([0.35, 0.20, 0.15, 0.10, 0.10, 0.10])
budg_w = np.array([0.20, 0.15, 0.35, 0.10, 0.10, 0.10])
alt3_minus1 = np.array([7, 8, 7, 7, 8, 8], dtype=float)

scen_labels = [
    heb("בסיס"),
    heb("עדיפות\nחושית"),
    heb("תקציב\nמחמיר"),
    heb("חלופה ג'\nחושי -1"),
]
s_a = [float(np.dot(scores["alt1"], base_w)), float(np.dot(scores["alt1"], sens_w)), float(np.dot(scores["alt1"], budg_w)), float(np.dot(scores["alt1"], base_w))]
s_b = [float(np.dot(scores["alt2"], base_w)), float(np.dot(scores["alt2"], sens_w)), float(np.dot(scores["alt2"], budg_w)), float(np.dot(scores["alt2"], base_w))]
s_c = [float(np.dot(scores["alt3"], base_w)), float(np.dot(scores["alt3"], sens_w)), float(np.dot(scores["alt3"], budg_w)), float(np.dot(alt3_minus1, base_w))]

x = np.arange(len(scen_labels))
w_bar = 0.26

b1 = ax_left.bar(x - w_bar, s_a, width=w_bar * 0.90, color=SHADES["honey"], label=heb("חלופה א' (D2C)"))
b2 = ax_left.bar(x, s_b, width=w_bar * 0.90, color=AURA["muted"], alpha=0.82, label=heb("חלופה ב' (קמפוס)"))
b3 = ax_left.bar(x + w_bar, s_c, width=w_bar * 0.90, color=AURA["plum"], label=heb("חלופה ג' (היברידית)"))

for bars, col in [(b1, SHADES["cocoa"]), (b2, AURA["muted"]), (b3, AURA["plum"])]:
    for bar in bars:
        h = bar.get_height()
        ax_left.text(
            bar.get_x() + bar.get_width() / 2,
            h + 0.08,
            f"{h:.2f}",
            ha="center",
            va="bottom",
            fontsize=6.8,
            fontweight="bold" if col == AURA["plum"] else "normal",
            color=col,
        )

ax_left.set_xticks(x)
ax_left.set_xticklabels(scen_labels, fontsize=7.6)
ax_left.set_ylim(5.5, 8.65)
ax_left.set_ylabel(heb("ציון משוקלל"), fontsize=8.5)
ax_left.set_title(heb("ב. רגישות משקלים וציון"), fontsize=9.4, fontweight="bold", color=AURA["plum"], pad=8)
ax_left.grid(axis="y", color=AURA["grid"], linestyle="--", linewidth=0.6)
ax_left.set_axisbelow(True)

ax_left.legend(
    loc="upper center",
    bbox_to_anchor=(0.48, -0.25),
    ncol=1,
    frameon=False,
    fontsize=7.3,
    handlelength=1.1,
)

save(fig, "decision_matrix_scores")
