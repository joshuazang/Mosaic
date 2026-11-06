# Security boundaries

- The current note is supplied by Standard Notes; the plugin never requests a
  stream of all account notes. The relay binds its transport to the registered
  host origin and session, retains random message IDs, rejects sibling-window
  messages, and supports the official mobile string transport.
- The relay does not load remote themes. CSP uses
  `connect-src 'none'`, `script-src 'self'`, `object-src 'none'`, `base-uri 'none'`,
  `form-action 'none'` and `worker-src 'none'`. Styles and images are local. Inline
  styles are needed for card geometry. No user-controlled script is generated.
- Note titles, text, tags, previews, errors and imports are inserted as text or
  textarea values. The only `innerHTML` assignment is a fixed, original SVG icon
  dictionary; no note field enters it. HTML-looking text remains literal text.
- There are no fetch/XHR/WebSocket calls, telemetry, localStorage, sessionStorage,
  IndexedDB, service workers, account credentials or separate recovery stores in
  the application. Selection IDs use the official component-data preference
  API; success acknowledgment is not available for that host API.
- The format parser rejects invalid structures, IDs and metadata. Existing IM
  validation and reserved-marker escaping remain byte-identical to the source
  core. It does not evaluate imported content. Unknown supported metadata is
  preserved. Format-2 notes are not silently converted.
- Acknowledgments, immutable save snapshots, per-note ordering, deduplication,
  coalescing, timeouts, retry and departing-frame submission use the existing IM
  queue. Host acknowledgment is not proof of successful server sync; Standard
  Notes reports sync separately. Metadata-only events are not acknowledgments.
- New-card input persists to the draft field on every edit. Final submission
  keeps the input until acknowledgment. A newer input revision is not cleared
  by an older successful save. Existing-card edits are explicitly submitted;
  a failed save retains the editor contents and unconfirmed local snapshot.
  Click-outside submission waits for IME composition to finish. App/window
  deactivation alone does not automatically send a draft; it uses normal draft
  persistence, since the plugin cannot safely control a parent-app note switch.
- Unexpected different content during a pending/failed save or unfinished card
  edit pauses saving. It does not automatically replace either version. The
  review dialog offers the local content and the incoming saved content.
- Clipboard reads and writes follow explicit actions. Import previews and
  validates before merging. Clearing is manual and confirmed after the import
  acknowledgment, with no delayed clipboard API claims. The clipboard is outside
  Standard Notes encryption; OS clipboard history cannot be erased by this UI.
- A public editor can be inspected by anyone. Note data is not bundled with it.
  Hosting and future code updates remain part of the trust boundary, as with
  other hosted plugins. This repository contains synthetic fixtures only.

These are code and test properties, not a guarantee against a compromised OS,
malicious browser extensions, a malicious parent host, an altered plugin update,
or every possible app crash. Encryption of synced data and local databases is
the responsibility of the official Standard Notes client. Working memory and
the active system clipboard necessarily contain readable text when used.
