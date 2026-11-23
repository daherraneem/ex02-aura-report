"""Chapter 6 figure: 6-Month Launch Gantt Chart (Dec 2026 - May 2027).

Updated after expert committee review (F5 / BS-06 / BS-07 / BS-12 / DL-05):
- Fixed critical sequence: Formula freeze & focus groups (Month 1, weeks 1-3)
  -> MoH REQ-01 submission (end of Month 1 / Month 2) -> Inventory production (Month 2-3).
- Anchored to Israeli academic calendar (Month 4 = Mar 2027, Spring Semester opening).
- Sized to printed text width (6.5 in) with legible fonts (>= 7.5-8.5 pt).
- Includes 1,500 sealed mini samples (3 bars x 500) and Month 4 Commercial Gate (M4).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from aura_style import AURA, SHADES, heb, apply_style, save

apply_style()

# Tasks: (Hebrew label, start_month, duration_months, is_critical, phase_color)
tasks = [
    ("1.1 נעילת פורמולה וקבוצות מיקוד", 0.0, 1.0, True, SHADES["ruby"]),
    ("1.2 ספר מותג, סימן מסחר ואריזות", 0.0, 1.5, False, SHADES["honey"]),
    ("1.3 הגשה ואישור משרד הבריאות (REQ-01)", 1.0, 2.0, True, SHADES["ruby"]),
    ("1.4 ייצור מלאי (3,000 יח' + 1,500 מיני)", 1.3, 1.5, False, SHADES["honey"]),
    ("2.1 אתר D2C, שאלון גוון ומרקטפלייס", 0.6, 2.1, False, SHADES["honey"]),
    ("2.2 תוכן ASMR, 20–30 יוצרות ו-REQ-02", 1.0, 1.8, False, SHADES["peach"]),
    ("2.3 אישורי 3 קמפוסים והסעדה מאושרת", 1.0, 1.8, False, SHADES["peach"]),
    ("3.1 בדיקת 10 הזמנות (REQ-03) וסקר בסיס", 2.3, 0.7, False, AURA["gold"]),
    ("4.1 השקה: D2C, מרקטפלייס וגל יוצרות", 3.0, 1.0, True, SHADES["ruby"]),
    ("4.2 הפעלת 3 ברי טעימות (1,500 דוגמיות)", 3.1, 1.6, False, SHADES["berry"]),
    ("5.1 אופטימיזציית CAC ומיקוד גוונים (G2)", 4.0, 1.2, True, SHADES["ruby"]),
    ("6.1 מארזי שימור, סקר מסכם ודוח P&L", 5.0, 1.0, True, SHADES["ruby"]),
]

# Milestones: (month_x, task_idx, tag)
milestones = [
    (1.0, 0, "M1"),
    (2.0, 5, "M2"),
    (3.0, 2, "M3"),
    (4.0, 8, "M4"),
    (5.0, 10, "M5"),
    (6.0, 11, "M6"),
]

fig, ax = plt.subplots(figsize=(6.55, 4.45))
plt.subplots_adjust(left=0.41, right=0.97, top=0.87, bottom=0.22)

n = len(tasks)
y_positions = list(range(n - 1, -1, -1))

for m in range(6):
    if m % 2 == 1:
        ax.axvspan(m, m + 1, color=AURA["cream"], alpha=0.65, zorder=0)

# Go-Live vertical divider at start of Month 4 (Mar 2027)
ax.axvline(3.0, color=AURA["plum"], linestyle="--", linewidth=1.2, zorder=2)
ax.text(
    3.0,
    n - 0.10,
    heb("שער Go-Live (M3)"),
    ha="center",
    va="bottom",
    fontsize=7.6,
    fontweight="bold",
    color=AURA["plum"],
    bbox=dict(boxstyle="round,pad=0.20", facecolor=AURA["cream"], edgecolor=AURA["plum"], lw=0.7),
)

for idx, (label, start, dur, is_crit, col) in enumerate(tasks):
    y = y_positions[idx]
    ax.barh(
        y,
        dur,
        left=start,
        height=0.58,
        color=SHADES["ruby"] if is_crit else col,
        alpha=0.92 if is_crit else 0.80,
        edgecolor=AURA["plum"] if is_crit else "white",
        linewidth=1.0 if is_crit else 0.6,
        zorder=3,
    )

for mx, tidx, tag in milestones:
    my = y_positions[tidx]
    ax.scatter(
        [mx],
        [my],
        marker="D",
        s=40,
        color=AURA["gold"],
        edgecolor=AURA["plum"],
        linewidth=0.95,
        zorder=5,
    )
    dx = -0.13 if mx >= 5.9 else 0.12
    ha = "right" if mx >= 5.9 else "left"
    ax.text(
        mx + dx,
        my + 0.32,
        tag,
        ha=ha,
        va="bottom",
        fontsize=7.3,
        fontweight="bold",
        color=AURA["plum"],
        zorder=6,
    )

ax.set_yticks(y_positions)
ax.set_yticklabels([heb(t[0]) for t in tasks], fontsize=7.6)
ax.set_xlim(0.0, 6.22)
ax.set_ylim(-0.7, n + 0.30)
ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
month_labels = [
    "חודש 1\nדצמ'",
    "חודש 2\nינו'",
    "חודש 3\nפבר'",
    "חודש 4\nמרץ",
    "חודש 5\nאפר'",
    "חודש 6\nמאי",
]
ax.set_xticklabels([heb(ml) for ml in month_labels], fontsize=7.8, fontweight="bold", color=AURA["plum"])
ax.tick_params(axis="x", length=0, pad=5)

for b in range(7):
    ax.axvline(b, color=AURA["grid"], linestyle="-", linewidth=0.65, zorder=1)

ax.set_title(
    heb("תרשים גאנט (דצמ' 2026 – מאי 2027): נתיב קריטי ואבני דרך M1–M6"),
    fontsize=9.6,
    fontweight="bold",
    color=AURA["plum"],
    pad=16,
)

legend_handles = [
    mpatches.Patch(facecolor=SHADES["ruby"], edgecolor=AURA["plum"], lw=0.9, label=heb("נתיב קריטי (מרווח 0)")),
    mpatches.Patch(facecolor=SHADES["honey"], alpha=0.82, label=heb("תשתית וייצור מקבילי")),
    mpatches.Patch(facecolor=SHADES["peach"], alpha=0.82, label=heb("תוכן, יוצרות ואישורים")),
    mpatches.Patch(facecolor=SHADES["berry"], alpha=0.82, label=heb("ברי טעימות (סמסטר ב')")),
    Line2D([0], [0], marker="D", color="w", markerfacecolor=AURA["gold"], markeredgecolor=AURA["plum"], markersize=6.5, label=heb("אבן דרך (M1–M6)")),
]
ax.legend(
    handles=legend_handles,
    loc="upper center",
    bbox_to_anchor=(0.46, -0.17),
    ncol=3,
    frameon=False,
    fontsize=7.1,
    handlelength=1.1,
    columnspacing=0.9,
)

save(fig, "gantt_launch")
