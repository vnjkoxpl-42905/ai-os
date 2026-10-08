---
type: operating-layer
subject: Protected records
updated: 2026-10-08
aliases: []
---

# Protected records: current policy and retired design

Current policy is [HANDLING](HANDLING.md) and the root operating manuals. Credentials and bank/account information belong only in the git-ignored root `.env`; government IDs stay outside this OS. Student notes, transcripts and correspondence belong in their normal domain homes. Do not recreate a private records tier, encrypted APFS bundle or Keychain store.

The following is preserved historical documentation from 2026-07-16. It describes the retired design, not available storage or a current access route. The old missing-image statement is historical and has not been reverified during this repair.

## Retired 2026-07-16 design


Sensitive records are intentionally not linked file-by-file from Git-tracked pages.

- Applicant/response and financial Google pointers are stored under the private records area.
- Card and identity imagery belongs only in the encrypted records bundle. The two expected source images remain unrecoverable after the bounded iCloud recovery procedure.
- The encrypted bundle was created and its APFS filesystem verified. Its password is held in the macOS Keychain.

Access private records only when Joshua explicitly requests it. See [[HANDLING]].

