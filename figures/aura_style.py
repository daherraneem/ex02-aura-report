"""Shared AURA style for all Python figures of the report.

Usage in a figure script (run from the project root):
    from aura_style import AURA, SHADES, heb, apply_style, save
"""
import re
from pathlib import Path

import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parent

# Palette from Exercise 1 (same values as aura-report.cls)
AURA = {
    "cream": "#FFF6EC",
    "gold": "#D9A441",
    "plum": "#4A1E3A",
    "ink": "#2B1A24",
    "muted": "#8A7480",
    "grid": "#E9DCCF",
}
SHADES = {  # 01..05, main color of each shade
    "honey": "#E69217",
    "peach": "#F26C4B",
    "berry": "#D42663",
    "ruby": "#BA1128",
    "cocoa": "#784121",
}

_LTR_RUN = re.compile(r"[A-Za-z0-9][A-Za-z0-9.,%/$+\-]*")
_MIRROR = str.maketrans("()[]{}<>", ")(][}{><")


def _has_bidi() -> bool:
    """matplotlib >= 3.11 lays out text with libraqm, which handles BiDi."""
    from matplotlib import ft2font
    return hasattr(ft2font, "__libraqm_version__")


HAS_BIDI = _has_bidi()


def heb(text: str) -> str:
    """Return a Hebrew label that matplotlib will display correctly.

    New matplotlib (libraqm) does BiDi itself: the text is returned as is.
    Old matplotlib draws characters in memory order, so the label is put in
    visual order: English words and numbers stay left-to-right, Hebrew runs
    are reversed. Good for short labels and titles, not long paragraphs.
    """
    if HAS_BIDI:
        return text
    tokens, pos = [], 0
    for m in _LTR_RUN.finditer(text):
        if m.start() > pos:
            tokens.append((False, text[pos:m.start()]))
        tokens.append((True, m.group()))
        pos = m.end()
    if pos < len(text):
        tokens.append((False, text[pos:]))
    out = []
    for is_ltr, tok in reversed(tokens):
        out.append(tok if is_ltr else tok[::-1].translate(_MIRROR))
    return "".join(out)


def apply_style() -> None:
    """Fonts and quiet axes that match the report (David for Hebrew)."""
    plt.rcParams.update({
        "font.family": ["David", "Arial"],
        "font.size": 13,
        "axes.edgecolor": AURA["muted"],
        "axes.labelcolor": AURA["ink"],
        "xtick.color": AURA["ink"],
        "ytick.color": AURA["ink"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "pdf.fonttype": 42,  # embed TrueType fonts
    })


def save(fig, name: str) -> Path:
    """Save as vector PDF next to this file (figures/<name>.pdf)."""
    path = FIG_DIR / f"{name}.pdf"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"saved {path.relative_to(FIG_DIR.parent)}")
    return path
