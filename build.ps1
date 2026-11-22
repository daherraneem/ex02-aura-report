# Build the AURA report: Python figures -> xelatex -> biber -> xelatex x2
# Usage (from the project root):  .\build.ps1          full build
#                                 .\build.ps1 -Quick   one xelatex pass only
param([switch]$Quick)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

function Invoke-Step($exe, [string[]]$arguments) {
    & $exe @arguments | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "FAILED: $exe $arguments  (see main.log / main.blg)" -ForegroundColor Red
        exit 1
    }
}

$tex = @("-interaction=nonstopmode", "-halt-on-error", "main.tex")
if ($Quick) {
    Invoke-Step xelatex $tex
} else {
    Get-ChildItem figures -Filter *.py | Where-Object Name -ne "aura_style.py" |
        ForEach-Object { Invoke-Step python @($_.FullName) }
    Invoke-Step xelatex $tex
    Invoke-Step biber @("main")
    Invoke-Step xelatex $tex
    Invoke-Step xelatex $tex
}
$pages = (Select-String -Path main.log -Pattern "Output written on main.pdf \((\d+) pages").Matches.Groups[1].Value
Write-Host "OK: main.pdf, $pages pages" -ForegroundColor Green
