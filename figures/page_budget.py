"""Figure: page budget of the report body (booklet page map, table 1.1).

Run from the project root:  python figures/page_budget.py
Output: figures/page_budget.pdf
"""
import matplotlib.pyplot as plt

from aura_style import AURA, apply_style, heb, save

# (chapter, pages) from the booklet's page map; body = 40 pages
BUDGET = [
    ("מבוא ורקע", 3),
    ("הבעיה והיעדים", 4),
    ("ספרות ומאמר דגל", 9),
    ("חקר שוק", 6),
    ("חלופות השקה", 8),
    ("תוכנית עבודה", 4),
    ("ניהול סיכונים", 2),
    ("סיכום", 1),
    ("מקורות", 3),
]
FOCUS = {"ספרות ומאמר דגל", "חקר שוק", "חלופות השקה"}  # > half the body


def main() -> None:
    apply_style()
    labels = [heb(name) for name, _ in BUDGET]
    pages = [p for _, p in BUDGET]
    colors = [AURA["plum"] if name in FOCUS else AURA["gold"] for name, _ in BUDGET]

    fig, ax = plt.subplots(figsize=(5.4, 3.1))
    y = range(len(BUDGET))
    ax.barh(y, pages, color=colors, height=0.62, edgecolor="white", linewidth=2)

    # Right-to-left reading: bars grow to the left, labels on the right
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.yaxis.tick_right()
    ax.set_yticks(list(y), labels)
    ax.tick_params(axis="y", length=0, pad=6)
    for i, p in enumerate(pages):
        ax.text(p + 0.15, i, str(p), va="center", ha="right",
                color=AURA["ink"], fontsize=12)

    ax.set_xlim(max(pages) + 1.2, 0)
    ax.set_xticks([])
    for side in ("left", "top", "bottom"):
        ax.spines[side].set_visible(False)
    ax.spines["right"].set_visible(True)
    ax.spines["right"].set_color(AURA["muted"])
    ax.set_title(heb("עמודים לפרק (סך הכול 40)"), loc="right",
                 color=AURA["ink"], fontsize=12, pad=8)
    save(fig, "page_budget")


if __name__ == "__main__":
    main()
