# Local package contract

Run with Python 3, no third-party libraries:

```powershell
python .agents/skills/lsat-lab-lecture-transcribe/scripts/package_lecture.py --manifest <manifest.json> --transcript <captured-transcript.txt> --output <lecture-folder>
```

The transcript is copied byte-for-byte into `transcript.md` on initial preservation. It can contain timestamps; use its actual physical lines in `source_lines`. If an existing source differs, the helper stops. Screenshots must already exist beneath the output folder's `screenshots/` directory. The output folder must be dedicated to this lecture.

```json
{
  "title": "Example lecture",
  "instructor": "Verified instructor",
  "lecture_date": "2026-08-27",
  "video_id": "33013",
  "source_url": "https://app.lsatlab.com/video-library/?videoid=33013",
  "duration_seconds": 3600,
  "capture_date": "2026-09-30",
  "transcript_method": "native automated captions, checked against playback",
  "source_complete": false,
  "verification_notes": ["Opening and ending checked; remaining review pending"],
  "gaps": ["Question 2 final board not yet captured"],
  "omissions": ["Greetings and student names removed from reading script"],
  "teaching_points": [{"id": "linking", "description": "Link compatible conditional rules", "segment_ids": ["concept-1"]}],
  "segments": [{
    "id": "concept-1", "title": "Link the rules", "kind": "concept",
    "start_seconds": 60, "end_seconds": 120,
    "source_lines": [3, 8], "concepts": ["conditional-linking"],
    "script": "First, look for the term that the two rules share.\n\nThat term gives us the connection.",
    "cues": ["Pause for the student to identify the shared term"],
    "images": [{"path": "screenshots/01-concept-board.png", "at_seconds": 95, "kind": "concept_board", "caption": "Initial linking board"}]
  }]
}
```

Segment `kind`: `concept`, `question`, or `closing`. Question segments require `question_id`. Image `kind`: `concept_board`, `question`, or `annotated_board`. Every question ID requires at least one `question` image; capture all text even if this needs several images. The first question must be preceded by a `concept_board` image in a concept segment. Image timestamps must fall within their segment. Split long explanations into separate segments if helpful. Segment times must be chronological and non-overlapping; deliberate transcript omissions are listed separately. Each teaching point must map to existing segments. Coverage proves referenced points have mappings, not that an agent identified every point.

Use `source_complete: false` plus specific gaps while capture is unfinished. Verification notes must say what was actually checked. The helper rejects missing/misplaced images, invalid source ranges, unmapped teaching points, and inconsistent timestamps before writing deliverables. It checks previous source hashes before repackaging. Derived files can be regenerated; preserved source cannot be silently changed.
