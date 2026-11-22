% =====================================================================
%  aura-report.cls  --  AURA preparatory-report class (Hebrew RTL + English)
%  Engine: XeLaTeX + biber.  Team: Raneem Daher & Raghad Rabah.
% =====================================================================
%
%  VERSION / CHANGELOG
%    v0.1  2026-11-22  First version: fonts, Hebrew/English switching,
%                      AURA colors, cover, chapter openers, header/footer,
%                      four box types, styled tables, diagrams, captions,
%                      abbreviations, keywords, IEEE bibliography.
%
%  COMMAND LIST  (use only these in chapter files)
%  --- Direction -------------------------------------------------------
%    \en{text}            English word, name, acronym or phrase (one unit)
%    \ltr{text}           number, decimal, range, percent, date, price,
%                         version, unit:  \ltr{1.0}  \ltr{10--20}  \ltr{35\%}
%    \mathheb{text}       Hebrew inside a formula; put brackets INSIDE:
%                         \mathheb{(ציון סיכון)}
%    \begin{diagram} ... \end{diagram}
%                         LTR, centered wrapper for TikZ / images.
%                         Hebrew labels inside: \texthebrew{...}
%  --- Boxes (never split across pages) --------------------------------
%    \begin{insightbox}[title]     plum    - insight / "in our project"
%    \begin{definitionbox}[title]  gold    - definition of a term
%    \begin{warningbox}[title]     ruby    - warning / risk
%    \begin{keymessage}[title]     peach   - one key message for managers
%  --- Tables ----------------------------------------------------------
%    \headrow \hcell{..} & \hcell{..} \\   plum header row, white bold text
%    \auratablestripes                     cream / white alternating rows
%    (first column is on the right automatically; caption ABOVE table;
%     use r or p{} columns: Hebrew text is right-aligned, never l)
%  --- Front matter ----------------------------------------------------
%    \reporttitle{he}{en}  \reportsubtitle{he}  \reportdate{..}
%    \course{he}{en}  \institution{he}{en}  \lecturer{he}{en}
%    \authors{he}{en}  \copyrightholder{en}
%    \makecover                      cover page (no page number)
%    \keywords{a \sep b \sep c}      keyword line under the summary
%    \begin{abbreviations} \abbr{PCB}{definition} ... \end{abbreviations}
%    \printreferences                Hebrew heading + IEEE list (LTR)
%  --- Drafting (remove before submission) ------------------------------
%    \draftnote{text}                dashed gray box: what a section must prove
% =====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{aura-report}[2026/11/22 v0.1 AURA preparatory report]

\LoadClass[12pt,a4paper,oneside,openany]{book}

% ---------------------------------------------------------------------
%  Packages (order matters: bidi, loaded by polyglossia, comes last)
% ---------------------------------------------------------------------
\RequirePackage{iftex}
\RequireXeTeX
\RequirePackage{fontspec}
\RequirePackage{amsmath}
\RequirePackage[
  a4paper, top=2.5cm, bottom=2.5cm,
  left=2.5cm, right=3.0cm,          % 2.5 cm + 0.5 cm binding on the right (Hebrew)
  headheight=26pt, headsep=0.8cm, footskip=1.2cm
]{geometry}
\RequirePackage[table]{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,calc,fadings,shadows}
\RequirePackage[most]{tcolorbox}
\RequirePackage{booktabs}
\RequirePackage{array}
\RequirePackage{caption}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{setspace}
\RequirePackage{needspace}
\RequirePackage{lastpage}
\RequirePackage[hidelinks,unicode]{hyperref}   % before bidi
\RequirePackage{polyglossia}                   % loads bidi
\RequirePackage[backend=biber,style=ieee,sorting=none,language=english]{biblatex} % after polyglossia

% ---------------------------------------------------------------------
%  Languages and fonts  (all fonts ship with Windows)
% ---------------------------------------------------------------------
\setdefaultlanguage{hebrew}
\setotherlanguage{english}

\setmainfont{Cambria}[Scale=0.92]                 % English serif
\setsansfont{Calibri}                             % English sans
\setmonofont{Consolas}[Scale=0.88]
\newfontfamily\hebrewfont{David}[Script=Hebrew, Ligatures=TeX,  % Hebrew body
  ItalicFont=David, ItalicFeatures={FakeSlant=0.18}]  % David has no italic
\newfontfamily\hebrewfontsf{Gisha}[Script=Hebrew, Ligatures=TeX] % Hebrew headings
\newfontfamily\hebrewfonttt{Courier New}[Script=Hebrew]
\newfontfamily\aurawordmark{Georgia}[LetterSpace=18.0]

% David's colon has a wide side bearing ("word :"). Pull the colon back
% to the word, only when the current font is David (other fonts untouched).
\XeTeXinterchartokenstate=1
\newXeTeXintercharclass\aura@colonclass
\XeTeXcharclass`\:=\aura@colonclass
\def\aura@colonfix{%
  \edef\aura@test{\noexpand\in@{\detokenize{avid}}{\fontname\font}}%
  \aura@test\ifin@\kern-0.17em\fi}
\XeTeXinterchartoks 0 \aura@colonclass{\aura@colonfix}
% (no 4095 rule: the kern resets the class to 4095 -> endless loop)

% ---------------------------------------------------------------------
%  AURA palette (from Exercise 1)
% ---------------------------------------------------------------------
\definecolor{AuraCream}{HTML}{FFF6EC}
\definecolor{AuraGold}{HTML}{D9A441}
\definecolor{AuraPlum}{HTML}{4A1E3A}
\definecolor{AuraHoney}{HTML}{E69217}  % 01 Golden Honey Glaze
\definecolor{AuraPeach}{HTML}{F26C4B}  % 02 Velvet Peach Nectar
\definecolor{AuraBerry}{HTML}{D42663}  % 03 Berry Crush Elixir
\definecolor{AuraRuby}{HTML}{BA1128}   % 04 Ruby Pomegranate Jewel
\definecolor{AuraCocoa}{HTML}{784121}  % 05 Silk Cocoa Glaze
\definecolor{AuraInk}{HTML}{2B1A24}    % body text: very dark plum
\definecolor{AuraMuted}{HTML}{8A7480}

% Each chapter gets one of the five shades, in order
\newcommand{\aurachaptercolor}{%
  \ifcase\numexpr\value{chapter}-5*((\value{chapter}-1)/5)\relax
    AuraPlum\or AuraHoney\or AuraPeach\or AuraBerry\or AuraRuby\or AuraCocoa\else AuraPlum\fi}

% ---------------------------------------------------------------------
%  Body text: 1.5 spacing, justified, dark-plum ink
% ---------------------------------------------------------------------
\setstretch{1.5}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em plus 0.2em}
\AtBeginDocument{\color{AuraInk}}
\setlist{itemsep=0.15em, topsep=0.4em}
\setlist[itemize]{label=\textcolor{AuraGold}{\small$\bullet$}}
\setlist[enumerate]{label=\textcolor{AuraPlum}{\bfseries\arabic*.}}
\clubpenalty=10000 \widowpenalty=10000

% ---------------------------------------------------------------------
%  Direction commands
% ---------------------------------------------------------------------
% \leavevmode: a paragraph that starts with English stays an RTL paragraph.
% \aura@peekcolon: "\en{SOM}:" gets the same David colon fix (looks ahead
% with \futurelet, so it never swallows the space after the unit).
\def\aura@peekcolon{\futurelet\aura@next\aura@peekcolon@}
\def\aura@peekcolon@{\ifx\aura@next:\aura@colonfix\fi}
\newcommand{\en}[1]{\leavevmode\textenglish{#1}\aura@peekcolon}
\newcommand{\ltr}[1]{\leavevmode\LR{#1}\aura@peekcolon}
\newcommand{\mathheb}[1]{\text{\texthebrew{#1}}}
\newenvironment{diagram}{\par\centering\begin{LTR}}{\end{LTR}\par}

% ---------------------------------------------------------------------
%  Chapter and section headings
% ---------------------------------------------------------------------
\newcommand{\aurastrip}{%
  \noindent{\color{AuraHoney}\rule{0.2\linewidth}{3.5pt}}\hspace{0pt}%
  {\color{AuraPeach}\rule{0.2\linewidth}{3.5pt}}\hspace{0pt}%
  {\color{AuraBerry}\rule{0.2\linewidth}{3.5pt}}\hspace{0pt}%
  {\color{AuraRuby}\rule{0.2\linewidth}{3.5pt}}\hspace{0pt}%
  {\color{AuraCocoa}\rule{0.2\linewidth}{3.5pt}}}

\newcommand{\aurachapterlabel}{\aurastrip\par\vspace{14pt}%
   {\large\color{AuraMuted}\chaptertitlename}\hspace{0.5em}%
   {\fontsize{40}{40}\selectfont\bfseries\color{\aurachaptercolor}\thechapter}}
\titleformat{\chapter}[display]
  {\sffamily\color{AuraPlum}}
  {\aurachapterlabel}
  {6pt}
  {\fontsize{25}{31}\selectfont\bfseries}
  [\vspace{2pt}{\color{AuraGold}\titlerule[0.8pt]}]
\titleformat{name=\chapter,numberless}[display]
  {\sffamily\color{AuraPlum}}
  {\aurastrip}
  {14pt}
  {\fontsize{25}{31}\selectfont\bfseries}
  [\vspace{2pt}{\color{AuraGold}\titlerule[0.8pt]}]
\titlespacing*{\chapter}{0pt}{0pt}{22pt}

\titleformat{\section}
  {\needspace{5\baselineskip}\sffamily\Large\bfseries\color{AuraPlum}}
  {\textcolor{\aurachaptercolor}{\thesection}}{0.7em}{}
\titleformat{\subsection}
  {\needspace{4\baselineskip}\sffamily\large\bfseries\color{AuraPlum}}
  {\textcolor{AuraGold}{\thesubsection}}{0.7em}{}
\titleformat{\subsubsection}
  {\sffamily\normalsize\bfseries\color{AuraPlum}}{}{0pt}{}
\titlespacing*{\section}{0pt}{1.4em}{0.5em}
\titlespacing*{\subsection}{0pt}{1.1em}{0.35em}
\setcounter{tocdepth}{2}     % TOC down to level 3 (chapter/section/subsection)
\setcounter{secnumdepth}{2}
% TOC and lists: tighter line spacing than the body
\let\aura@toc\tableofcontents \let\aura@lof\listoffigures \let\aura@lot\listoftables
\renewcommand{\tableofcontents}{\begingroup\setstretch{1.1}\aura@toc\endgroup}
\renewcommand{\listoffigures}{\begingroup\setstretch{1.1}\aura@lof\endgroup}
\renewcommand{\listoftables}{\begingroup\setstretch{1.1}\aura@lot\endgroup}

% ---------------------------------------------------------------------
%  Captions: figure caption below, table caption above, numbered by chapter
% ---------------------------------------------------------------------
\captionsetup{font={small,sf}, labelfont={bf,color=AuraPlum},
  labelsep=colon, justification=centering, skip=6pt}
\captionsetup[table]{position=top}

% ---------------------------------------------------------------------
%  Tables
% ---------------------------------------------------------------------
\newcommand{\headrow}{\rowcolor{AuraPlum}}
\newcommand{\hcell}[1]{\textcolor{white}{\bfseries\sffamily #1}}
\newcommand{\auratablestripes}{\rowcolors{2}{AuraCream}{white}}
\renewcommand{\arraystretch}{1.25}
\setlength{\aboverulesep}{0pt}\setlength{\belowrulesep}{0pt}
\arrayrulecolor{AuraGold}

% ---------------------------------------------------------------------
%  Boxes  (unbreakable, frame LTR, content RTL)
% ---------------------------------------------------------------------
\tcbset{aurabase/.style={enhanced, unbreakable, boxrule=0pt, arc=3pt,
  left=10pt, right=10pt, top=6pt, bottom=6pt,
  fonttitle=\sffamily\bfseries, before skip=10pt, after skip=10pt}}

\newtcolorbox{insightbox}[1][תובנה]{aurabase,
  colback=AuraCream, colframe=AuraPlum, coltitle=AuraCream,
  boxrule=0.6pt, title={#1}}
\newtcolorbox{definitionbox}[1][הגדרה]{aurabase,
  colback=AuraGold!10, colframe=AuraGold, coltitle=AuraPlum,
  boxrule=0.6pt, title={#1}}
\newtcolorbox{warningbox}[1][שימו לב]{aurabase,
  colback=AuraRuby!6, colframe=AuraRuby, coltitle=white,
  boxrule=0.6pt, title={#1}}
\newtcolorbox{keymessage}[1][המסר המרכזי]{aurabase,
  colback=AuraPeach!9, colframe=AuraPeach!9, coltitle=AuraPlum,
  colbacktitle=AuraPeach!9, titlerule=0pt, toptitle=2pt, bottomtitle=0pt,
  right=14pt, fonttitle=\sffamily\bfseries\large,
  overlay={\fill[AuraPeach] (frame.north east) rectangle
    ([xshift=-5pt]frame.south east);},
  title={#1}}

\newcommand{\draftnote}[1]{%
  \begin{tcolorbox}[enhanced, unbreakable, colback=white, colframe=AuraMuted,
    boxrule=0.5pt, arc=2pt, borderline={0.5pt}{0pt}{AuraMuted,dashed},
    frame hidden, fontupper=\small\sffamily\color{AuraMuted},
    left=8pt, right=8pt, top=4pt, bottom=4pt]
    \textbf{טיוטה:} #1
  \end{tcolorbox}}

% ---------------------------------------------------------------------
%  Header and footer
% ---------------------------------------------------------------------
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\renewcommand{\headrule}{{\color{AuraGold}\hrule height \headrulewidth}}
\fancypagestyle{aura}{%
  \fancyhf{}%
  \fancyhead[R]{\small\sffamily\color{AuraPlum}\leftmark}%
  \fancyhead[L]{\small\sffamily\color{AuraGold}\en{AURA}\enspace·\enspace דוח מכין}%
  \fancyfoot[C]{\small\sffamily\color{AuraMuted}%
    עמוד \ltr{\thepage} מתוך \ltr{\pageref*{LastPage}}}%
  \renewcommand{\headrulewidth}{0.5pt}}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\small\sffamily\color{AuraMuted}%
    \if@mainmatter עמוד \ltr{\thepage} מתוך \ltr{\pageref*{LastPage}}\else\thepage\fi}%
  \renewcommand{\headrulewidth}{0pt}}

% Front matter: Hebrew letters (א, ב, ג...);  body: 1, 2, 3...
\def\@aurahebrew#1{\hebrewnumeral{#1}}
\renewcommand{\frontmatter}{\cleardoublepage\@mainmatterfalse
  \pagenumbering{aurahebrew}\pagestyle{plain}}
\renewcommand{\mainmatter}{\cleardoublepage\@mainmattertrue
  \pagenumbering{arabic}\pagestyle{aura}}

% ---------------------------------------------------------------------
%  Cover page
% ---------------------------------------------------------------------
\newcommand{\@titlehe}{}\newcommand{\@titleen}{}\newcommand{\@subtitlehe}{}
\newcommand{\@coursehe}{}\newcommand{\@courseen}{}
\newcommand{\@insthe}{}\newcommand{\@insten}{}
\newcommand{\@lecturerhe}{}\newcommand{\@lectureren}{}
\newcommand{\@authorshe}{}\newcommand{\@authorsen}{}
\newcommand{\@reportdate}{\today}\newcommand{\@copyrightholder}{}
\newcommand{\reporttitle}[2]{\renewcommand{\@titlehe}{#1}\renewcommand{\@titleen}{#2}}
\newcommand{\reportsubtitle}[1]{\renewcommand{\@subtitlehe}{#1}}
\newcommand{\course}[2]{\renewcommand{\@coursehe}{#1}\renewcommand{\@courseen}{#2}}
\newcommand{\institution}[2]{\renewcommand{\@insthe}{#1}\renewcommand{\@insten}{#2}}
\newcommand{\lecturer}[2]{\renewcommand{\@lecturerhe}{#1}\renewcommand{\@lectureren}{#2}}
\newcommand{\authors}[2]{\renewcommand{\@authorshe}{#1}\renewcommand{\@authorsen}{#2}}
\newcommand{\reportdate}[1]{\renewcommand{\@reportdate}{#1}}
\newcommand{\copyrightholder}[1]{\renewcommand{\@copyrightholder}{#1}}

% one soft "aura" glow: \auraglow{x}{y}{radius}{color}
\newcommand{\auraglow}[4]{%
  \fill[#4, opacity=0.75, path fading=circle with fuzzy edge 20 percent]
    (#1,#2) circle (#3);}

\newcommand{\makecover}{%
  \begin{titlepage}
  \thispagestyle{empty}%
  \begin{LTR}%
  \begin{tikzpicture}[remember picture, overlay]
    \coordinate (C) at (current page.center);
    % background and bands
    \fill[AuraCream] (current page.south west) rectangle (current page.north east);
    \fill[AuraPlum] (current page.north west) rectangle
      ([yshift=-2.6cm]current page.north east);
    \fill[AuraPlum] (current page.south west) rectangle
      ([yshift=1.5cm]current page.south east);
    \fill[AuraGold] ([yshift=-2.6cm]current page.north west) rectangle
      ([yshift=-2.75cm]current page.north east);
    % institution / course (top band)
    \node[anchor=north east, text=AuraCream, align=right, font=\sffamily]
      at ([xshift=-2.2cm,yshift=-0.75cm]current page.north east)
      {\texthebrew{\large\bfseries\@insthe}\\[2pt]\texthebrew{\small\@coursehe}};
    \node[anchor=north west, text=AuraCream, align=left, font=\sffamily]
      at ([xshift=2.2cm,yshift=-0.75cm]current page.north west)
      {{\large\bfseries\@insten}\\[2pt]{\small\@courseen}};
    % five shade glows behind the wordmark
    \begin{scope}[shift={($(C)+(0,6.0)$)}]
      \auraglow{-4.4}{-0.2}{1.9}{AuraHoney}
      \auraglow{-2.2}{0.45}{2.0}{AuraPeach}
      \auraglow{0}{-0.1}{2.2}{AuraBerry}
      \auraglow{2.2}{0.45}{2.0}{AuraRuby}
      \auraglow{4.4}{-0.2}{1.9}{AuraCocoa}
      \node[text=AuraPlum] at (0,0.1)
        {\fontsize{78}{78}\selectfont\aurawordmark AURA};
      \node[text=AuraPlum] at (0,-1.55)
        {\large\itshape Your glow, freshly made.};
    \end{scope}
    % titles
    \node[text=AuraPlum, align=center, text width=15cm, font=\sffamily]
      at ($(C)+(0,1.15)$)
      {\texthebrew{\fontsize{24}{32}\selectfont\bfseries\@titlehe}};
    \node[text=AuraPlum!80, align=center, text width=15cm]
      at ($(C)+(0,-0.6)$)
      {\texthebrew{\large\@subtitlehe}};
    \node[text=AuraPlum, align=center, text width=15cm]
      at ($(C)+(0,-1.85)$)
      {\Large\itshape\@titleen};
    % document type tag
    \node[fill=AuraGold, text=AuraPlum, rounded corners=9pt, inner xsep=14pt,
      inner ysep=6pt, font=\sffamily\bfseries]
      at ($(C)+(0,-3.3)$)
      {\texthebrew{דוח מכין}\enspace·\enspace Preparatory Report};
    % team, lecturer, date
    \node[text=AuraPlum, align=center, font=\sffamily]
      at ($(C)+(0,-6.6)$)
      {\texthebrew{\small מגישות}\\[2pt]
       \texthebrew{\large\bfseries\@authorshe}\\[1pt]
       {\normalsize\@authorsen}\\[10pt]
       \texthebrew{\small מרצה: \@lecturerhe}\enspace|\enspace{\small\@lectureren}\\[4pt]
       \texthebrew{\small\@reportdate}};
    % copyright (bottom band, English font)
    \node[text=AuraCream, font=\small\sffamily]
      at ([yshift=0.75cm]current page.south)
      {\textcopyright\ \the\year\ \@copyrightholder. All rights reserved.};
  \end{tikzpicture}%
  \end{LTR}%
  \end{titlepage}}

% ---------------------------------------------------------------------
%  Keywords, abbreviations, references
% ---------------------------------------------------------------------
\newcommand{\sep}{\enspace\textcolor{AuraGold}{\textbullet}\enspace}
\newcommand{\keywords}[1]{\par\medskip\noindent
  {\sffamily\bfseries\color{AuraPlum}מילות מפתח:}\enspace #1\par}

\newenvironment{abbreviations}
  {\begin{center}\auratablestripes
   \begin{tabular}{>{\raggedleft\arraybackslash}p{3cm} p{10.5cm}}
   \headrow \hcell{קיצור} & \hcell{פירוש} \\}
  {\end{tabular}\end{center}}
\newcommand{\abbr}[2]{\en{#1} & #2 \\}

\newcommand{\printreferences}{%
  \chapter*{מקורות}\addcontentsline{toc}{chapter}{מקורות}%
  \markboth{מקורות}{}%
  \begin{english}\printbibliography[heading=none]\end{english}}

% ---------------------------------------------------------------------
\pagestyle{aura}
\endinput
