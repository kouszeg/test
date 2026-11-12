param([string]$u)
# Bass Recorder helper: opens a folder link (bassrec-open:<url-encoded path>) in your file manager.
# Only existing folders are opened, nothing else is ever run.
$tc = ''   # e.g. 'C:\totalcmd\TOTALCMD64.EXE' to always use Total Commander; empty = Windows default folder handler
$p = [uri]::UnescapeDataString(($u -replace '^bassrec-open:(//)?', ''))
if (-not $p -or -not (Test-Path -LiteralPath $p -PathType Container)) { exit 1 }
if ($tc) { & $tc /O /T "/L=$p" } else { Invoke-Item -LiteralPath $p }
