param([string]$u)
# Bass Recorder helper: opens a folder link (bassrec-open:<url-encoded path>) in your file manager.
# Only existing folders inside $root are opened (no network paths, no '..'); nothing is ever executed.
$root = 'D:\6_personal\4_bass\_recordings'
$tc = ''   # e.g. 'C:\totalcmd\TOTALCMD64.EXE' to always use Total Commander; empty = Windows default folder handler
try { $p = [uri]::UnescapeDataString(($u -replace '^bassrec-open:(//)?', '')) } catch { exit 1 }
if ($p -notmatch '^[A-Za-z]:\\') { exit 1 }                       # local drive paths only (blocks \\server\share)
$full = [IO.Path]::GetFullPath($p).TrimEnd('\')
$r = [IO.Path]::GetFullPath($root).TrimEnd('\')
if (-not ($full -ieq $r -or $full.StartsWith($r + '\', [StringComparison]::OrdinalIgnoreCase))) { exit 1 }
if (-not (Test-Path -LiteralPath $full -PathType Container)) { exit 1 }
if ($tc) { & $tc /O /T "/L=$full" } else { Invoke-Item -LiteralPath $full }
