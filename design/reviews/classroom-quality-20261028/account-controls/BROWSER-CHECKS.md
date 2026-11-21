# Actual synthetic browser checks, 2026-10-28

All checks used localhost8152, real TeacherHomeView/AccessSheet/BookingSheet with in-memory DeskActions. Launcher has pre-load Vite replacement of src/integrations/supabase/client.ts; from/rpc/functions/auth throw. No production account changes.

- Visible Home > Students at a glance > Student accounts action group. Open/select/cancel leave visible Simulated mutations0.
- Credits Lydia4remaining, default1, summary4→5; custom1.5 submit disabled; explicit1 add gives5 and verified result. Existinglink controls absent in credits mode.
- Reopen after selecting10 returns Choose a student; selecting Lydia again shows1, balance4→5, mutation0.
- AccessCelia checkboxgrant+confirm saves; secondfeatureedit+confirm succeeds in same panel, visible counter2 and savedverified. Close returns focus to Account access.
- ExistingLydialink mode shows Open/Copy/Revoke and no add-credit action, counterunchanged. No-passCelia initial-create step itself does not mutate; finalconfirmcreates1initialsession in memory. Fictional URLs never opened/copied/shared.
- Actual screenshots opened at1440CSS desktop,390 and320CSS phones. Credit dialog fits390/320 with document and dialogscrollWidth==clientWidth. Identity repeated in untruncated accountdetails. Desktopdark accountactions and accesspanel readable; screenshotssaved.
- Native picker is retained; it is not a customstyled popup. No real auth/mobileproduction shell, backendexecution/allstudentRLS proof.
- Source corrections after these browser checks may need affected repeat; directrowblankselect case covered in final Home tests and additional browser check if performed.

Additional actual checks: account search zoe leaves only Zoë Adams, then celia selects named Celia; cancel leaves counter0 and focus Account access.

Final correction actual browser: Find a student Celia > Edit access > Choose a student leaves Student access sheet open and mutation0. ReselectCelia, grantDrill, confirm, close returns exact Edit access rowtrigger and mutation1.

Final L2 actualbrowser: native date locator fill updated DOM but did not dispatch Reactchange; real keyboard ArrowUp+Tab committed2001-01-01 and showed Choose a future expirydate orleaveblank withdisabledconfirmation, mutation0. Duration10 actionableerroralsoobserved.

Finalguard actual: explicit1credit4→5 gives counter1, verifiednotice+balance and Add more sessions, no Confirm add sessions. Explicitrearmshowsdefault1and5→6preview, counterstill1. No secondwriteperformed. Guardimagecredits-verified-final.png.
