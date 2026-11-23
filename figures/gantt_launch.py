"""Chapter 6 figure: 6-Month Launch Gantt Chart with Milestones & Critical Path.

Consistent with Chapter 5 (Omnichannel Hybrid, 150K ILS) and Chapter 2
(REQ-01 on the critical path, REQ-03 by Month 3, 3 campus tasting bars,
20-30 micro-influencers, G1-G5 goals, active sales in Months 4-6).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from aura_style import AURA, SHADES, heb, apply_style, save

apply_style()

# Tasks: (Hebrew label, start_month, duration_months, is_critical, phase_color)
# Timeline runs from 0.0 (start of Month 1) to 6.0 (end of Month 6)
tasks = [
    ("1.1 ספר מותג, אריזות וייצור מלאי (5 גוונים)", 0.0, 2.4, False, SHADES["honey"]),
    ("1.2 הודעות שיווק למשרד הבריאות (REQ-01)", 0.0, 3.0, True, SHADES["ruby"]),
    ("1.3 הקמת אתר D2C, סליקה ומרקטפלייס", 0.4, 2.3, False, SHADES["honey"]),
    ("2.1 צילומי ASMR והטמעת AI Sommelier", 1.0, 1.6, False, SHADES["peach"]),
    ("2.2 גיוס 20–30 יוצרות ובקרת סימון (REQ-02)", 1.0, 1.8, False, SHADES["peach"]),
    ("2.3 תיאום ואישורי 3 ברי טעימות בקמפוסים", 1.0, 1.9, False, SHADES["peach"]),
    ("3.1 בדיקת 10 הזמנות (REQ-03), טיזרים וסקר בסיס", 2.3, 0.7, False, AURA["gold"]),
    ("4.1 השקה: D2C, מרקטפלייס וגל יוצרות (Go-Live)", 3.0, 1.0, True, SHADES["ruby"]),
    ("4.2 הפעלת 3 ברי טעימות (3,000 דוגמיות, G3)", 3.2, 1.6, False, SHADES["berry"]),
    ("5.1 אופטימיזציית CAC, רימרקטינג ותוכן גולשות (G2)", 4.0, 1.3, True, SHADES["ruby"]),
    ("6.1 מארזי שימור, סקר מסכם (G1) ודוח ROI", 5.0, 1.0, True, SHADES["ruby"]),
]

# Milestones: (month_x, task_index_for_y, tag)
milestones = [
    (1.0, 0, "M1"),
    (2.0, 4, "M2"),
    (3.0, 1, "M3"),
    (4.0, 7, "M4"),
    (5.0, 9, "M5"),
    (6.0, 10, "M6"),
]

fig, ax = plt.subplots(figsize=(9.5, 4.75))
plt.subplots_adjust(left=0.39, right=0.97, top=0.87, bottom=0.19)

n = len(tasks)
y_positions = list(range(n - 1, -1, -1))

# Subtle alternating month shading
for m in range(6):
    if m % 2 == 1:
        ax.axvspan(m, m + 1, color=AURA["cream"], alpha=0.65, zorder=0)

# Vertical Go-Live dashed divider at start of Month 4 (x = 3.0)
ax.axvline(3.0, color=AURA["plum"], linestyle="--", linewidth=1.35, zorder=2)
ax.text(
    3.0,
    n - 0.12,
    heb("שער Go-Live (M3)"),
    ha="center",
    va="bottom",
    fontsize=8.6,
    fontweight="bold",
    color=AURA["plum"],
    bbox=dict(boxstyle="round,pad=0.22", facecolor=AURA["cream"], edgecolor=AURA["plum"], lw=0.8),
)

# Plot task bars
for idx, (label, start, dur, is_crit, col) in enumerate(tasks):
    y = y_positions[idx]
    ax.barh(
        y,
        dur,
        left=start,
        height=0.58,
        color=SHADES["ruby"] if is_crit else col,
        alpha=0.92 if is_crit else 0.78,
        edgecolor=AURA["plum"] if is_crit else "white",
        linewidth=1.2 if is_crit else 0.7,
        zorder=3,
    )

# Plot milestone diamonds
for mx, tidx, tag in milestones:
    my = y_positions[tidx]
    ax.scatter(
        [mx],
        [my],
        marker="D",
        s=58,
        color=AURA["gold"],
        edgecolor=AURA["plum"],
        linewidth=1.1,
        zorder=5,
    )
    dx = -0.14 if mx >= 5.9 else 0.13
    ha = "right" if mx >= 5.9 else "left"
    ax.text(
        mx + dx,
        my + 0.34,
        tag,
        ha=ha,
        va="bottom",
        fontsize=8.0,
        fontweight="bold",
        color=AURA["plum"],
        zorder=6,
    )

# Axes formatting
ax.set_yticks(y_positions)
ax.set_yticklabels([heb(t[0]) for t in tasks], fontsize=8.8)
ax.set_xlim(0.0, 6.22)
ax.set_ylim(-0.7, n + 0.25)
ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
ax.set_xticklabels(
    [heb(f"חודש {i}") for i in range(1, 7)],
    fontsize=9.6,
    fontweight="bold",
    color=AURA["plum"],
)
ax.tick_params(axis="x", length=0, pad=6)

# Vertical month grid lines at integer boundaries
for b in range(7):
    ax.axvline(b, color=AURA["grid"], linestyle="-", linewidth=0.75, zorder=1)

ax.set_title(
    heb("תרשים גאנט להשקת AURA (6 חודשים): משימות, נתיב קריטי ואבני דרך M1–M6"),
    fontsize=11.3,
    fontweight="bold",
    color=AURA["plum"],
    pad=18,
)

# Legend cleanly below the chart
legend_handles = [
    mpatches.Patch(facecolor=SHADES["ruby"], edgecolor=AURA["plum"], lw=1.1, label=heb("משימה בנתיב הקריטי (מרווח 0)")),
    mpatches.Patch(facecolor=SHADES["honey"], alpha=0.82, label=heb("תשתית והכנה מקבילה")),
    mpatches.Patch(facecolor=SHADES["peach"], alpha=0.82, label=heb("תוכן, יוצרות ואישורי שטח")),
    mpatches.Patch(facecolor=SHADES["berry"], alpha=0.82, label=heb("הפעלת ברי טעימות בקמפוסים")),
    Line2D([0], [0], marker="D", color="w", markerfacecolor=AURA["gold"], markeredgecolor=AURA["plum"], markersize=7.5, label=heb("אבן דרך (M1–M6)")),
]
ax.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.48, -0.11),
    ncol=3,
    frameon=False,
    fontsize=8.2,
    handlelength=1.2,
    columnspacing=1.1,
)

save(fig, "gantt_launch")
