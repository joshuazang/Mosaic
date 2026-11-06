# Mosaic 1.0.0 validation

Validation used synthetic notes only, on 2026-11-06. No account notes, passwords,
tokens or user-generated private data were used or added to the repository.

All six Node suites passed: model/format interoperability, save queue, save
deduplication, save snapshot isolation, lean reply records, and relay security.
The model suite includes 500 generated Unicode/whitespace/reserved-marker cases,
exact no-op title/body round trips, CRLF preservation, metadata retention, import
deduplication, merge reply navigation and malformed-note refusal.

The Chromium suite passed in opaque sandboxed iframes at 1100, 390 and 320 pixels,
including the official mobile JSON message transport. It checked:

- Persistent capture, click-outside submission, immediate draft saving and zero
  idle writes. No saves occur simply from opening an existing format-3 note.
- Retaining input after rejected final submissions, retry without duplicate
  cards, and retaining newer input after an earlier acknowledgment.
- Waiting for IME composition before auto-submitting the final Chinese text.
- Metadata-only stale snapshots and different content arriving during pending
  writes; the latter pauses saving and exposes both versions for review.
- Filtered Select all/Export, selection restoration after note switches,
  ID-only component preferences, and literal rendering of hostile-looking HTML.
- Pin/unpin, tag-only edits without false Edited status, clipboard-confirmed
  status marking, reply snapshots, merge, status clearing and cancelled deletion.
- Export/import/deduplication, import-and-clear confirmation after acknowledgment,
  manual clipboard clearing, and solid manual-copy fallback when copying fails.
- A 5,000-card note initially mounted **13 card previews and 278 DOM elements**.
  Searching and editing an off-screen card succeeded.
- Switching **Mosaic → the published IM-style-editor 4.1.5 build → Mosaic** on
  the same note. Card changes, shared drafts and message metadata survived.
- No independent external requests during these local browser flows.

The standalone preview was inspected at 1280 and 390 pixels. It has search,
emoji filters, a persistent capture field and cards, with no slogans, large
heading, brand block, footer or separate New card button. Preview changes stay
in memory and are clearly labeled as not saved.

The release ZIP was reproduced twice with identical bytes:

```text
SHA-256 fb4bba036bd120308093078a1368ecbb4e7b0bf2a5edd6d0459530434d12583e
```

These are controlled browser tests, not tests on a physical iPhone or the native
macOS Standard Notes app. Full-note save bandwidth limits still apply. Host
acknowledgment confirms acceptance by Standard Notes, not successful server sync.
See README and security notes for lifecycle and encryption boundaries.
