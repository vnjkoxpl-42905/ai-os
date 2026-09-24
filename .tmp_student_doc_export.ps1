function Get-DocText($doc,$tabIndex){
  $out=[System.Collections.Generic.List[string]]::new()
  foreach($block in $doc.tabs[$tabIndex].documentTab.body.content){
    $parts=[System.Collections.Generic.List[string]]::new()
    foreach($el in $block.paragraph.elements){if($el.textRun){$parts.Add($el.textRun.content)}}
    if($parts.Count -gt 0){$out.Add(($parts -join ''))}
  }
  return ($out -join '')
}
$specs=@(
@{student='sofia';date='2026-09-04';id='1EYM5Xvz5jx_-qJSUGqbTzzXDVNPlfYVPpQmlr2Icdm0';local='2026-09-04-sofia-notes-by-gemini.md'},
@{student='sofia';date='2026-09-09';id='178QAdgpV_Bx728psI9ZJ4x2ZSTAW8BC2ZvQy0hfDR9E';local='2026-09-09-sofia-notes-by-gemini.md'},
@{student='sofia';date='2026-09-11';id='1xwLbEPHGHOWhg-FvzXQfnhFH1f6MlMFKR7jae14cpH8';local='2026-09-11-sofia-notes-by-gemini.md'},
@{student='sofia';date='2026-09-15';id='1JUYdkLlWfJEeFqDpvRZ1TgkCLvHkbpWIuXOhddEG6oM'},
@{student='sofia';date='2026-09-18';id='1ANFhV5xXI9U-L9DWK3h76ZRYZrfjyw6MdquXDTRafc8'},
@{student='sofia';date='2026-09-23';id='1O-gl6f5tMIXUDXKaYs3LqNUNmA1H_T4kAjsX2mW7OSI'},
@{student='charles-moore';date='2026-09-03';id='1yrbldTzXCRPACqTdQzj8azX3t9oGdgX44tHkxCsWPiU';local='2026-09-03-charles-moore-notes-by-gemini.md'},
@{student='charles-moore';date='2026-09-14';id='1TNtcJz-qWMg_GNm4duV37AqYgb8SVxbZ_D6u4cFirEU'},
@{student='ore';date='2026-09-11';id='16ejBCD1WgUv1nU18nRjplcTEn6tBjKEv2wzuWjqAwGo';local='2026-09-11-ore-notes-by-gemini.md'},
@{student='asia';date='2026-08-25';id='1f_kk4kcUFq85EDQ3b8ZSp5ULg3RVu_cmF0uMpaExYl8';local='2026-08-25-asia-notes-by-gemini.md'},
@{student='avneet-natt';date='2026-09-08';id='1MJd5U8lAoN6EOlu8T9wUrTaCF_kHFQJKc5RXEkkj5zE';local='2026-09-08-avneet-natt-notes-by-gemini.md'},
@{student='yahunatan-zetvy';date='2026-09-02';id='126ktrgakkCCGa0RUCE5ejsJzU1AaptVZSJA9eVodacs'},
@{student='yahunatan-zetvy';date='2026-09-16';id='1ZPdB1LBKXC-bVtxSJikWvwe0cC04Q9fHWl6no_Cggeg'}
)
foreach($s in $specs){
 $p='{"documentId":"'+$s.id+'","includeTabsContent":true}'; $raw=gws docs documents get --params $p --format json | Out-String; $doc=$raw | ConvertFrom-Json
 $ti=0; for($j=0;$j -lt @($doc.tabs).Count;$j++){if($doc.tabs[$j].tabProperties.title -eq 'Transcript'){$ti=$j;break}}
 $si=if($ti -gt 1){1}else{0}; $trans=Get-DocText $doc $ti; $summ=Get-DocText $doc $si
 if($s.local){$source=Get-Content "students/$($s.student)/transcript-downloads/$($s.local)" -Raw; $transIndex=[regex]::Match($source,'(?m)^\d{2}:\d{2}:\d{2}\s*$').Index; if($transIndex -gt 0){$trans=$source.Substring($transIndex)}; $sumStart=$source.IndexOf('Summary');$transStart=[regex]::Match($source,'(?m)^\d{2}:\d{2}:\d{2}\s*$').Index; if($sumStart -ge 0 -and $transStart -gt $sumStart){$summ=$source.Substring($sumStart,$transStart-$sumStart)}}
 foreach($pair in @(@('transcript',$trans),@('summary',$summ))){$dest=Join-Path (Get-Location).Path "temp_$($pair[0])_$($s.student)_$($s.date).txt"; Set-Content -LiteralPath $dest -Value $pair[1] -NoNewline}
 "OK $($s.student) $($s.date) $($trans.Length) $($summ.Length) $($doc.title)"
}

