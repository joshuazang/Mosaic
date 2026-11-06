# Mosaic

A plain-text card board for Standard Notes.

**[Preview](https://joshuazang.github.io/Mosaic/?preview=1) · [Install manifest](https://joshuazang.github.io/Mosaic/mosaic.ext.json) · [Download 1.0.0](https://joshuazang.github.io/Mosaic/Mosaic-1.0.0.zip)**

Install Mosaic using Standard Notes' custom-plugin installer with this URL:

```text
https://joshuazang.github.io/Mosaic/mosaic.ext.json
```

Mosaic has its own plugin identifier. Keep IM-style-editor installed alongside it,
and choose either editor for the same note using Standard Notes' editor picker.
Both editors use **IM-style-editor format 3**, used by IM-style-editor 4.x. No
conversion or second copy is required. Archive's format-2 notes are intentionally
unsupported; export their messages from Archive and import them into a new note.

## The same text, another view

Each bubble becomes one card. Its first line is displayed as the title; everything
below it is the body. Title and body are not saved separately. One-line messages
are title-only cards. Viewing a note does not rewrite it. Existing blank lines,
emoji, literal format markers, dates, statuses, tags, pins, quoted replies,
provenance, unknown metadata, settings, and unsent drafts stay in the shared text.

The board shows pins first and newer cards near the top. This does not change
the saved message order or the IM timeline. This release does not implement
drag rearranging. It is a board of messages in the **current Standard Notes note**,
not a dashboard that reads every note in the account.

## Included

- Responsive masonry cards, with only nearby previews mounted in the page.
- Search, emoji filters, and a persistent “Take a note…” field on both desktop and phone.
- Click outside the capture field to add the card. Enter inserts a line break;
  Command/Ctrl+Enter also adds the card. The first line becomes its title.
- Full-text reader, plain-text editing, and a shared capture draft saved as you type.
- Emoji tags, search, untagged filtering, and multiple pins.
- Selection, filtered Select all, copy, export, import, merge, and confirmed deletion.
- Selective clearing of Copied, Exported, Imported and Edited indicators.
- Replies with quoted snapshots and navigation to the original card.
- Manual clipboard clearing and Import and clear clipboard, with confirmation.
- Keyboard-accessible menus, native modal focus management, Escape to exit selection,
  reduced-motion support, and light/dark themes. Native browser Find is left alone.

Reminders, photos, checkboxes, Markdown interpretation and rich-text formatting
are outside this release. Text such as HTML or Markdown is shown literally.

## Saving and data safety

New-card drafts save immediately after input events, through the same ordered,
acknowledged queue as the IM editor. One write may be in flight; newer waiting
versions replace older waiting versions. Idle time causes no saves. Clicking
outside the capture field submits the final message without a forced preliminary draft save. Its input is
retained until the host acknowledges saving; newer typing survives late replies.
Failed writes show a Retry save notice. No new browser-storage fallback is used.

Existing-card edits are explicit: choose **Save changes before switching editors**.
Closing an edit keeps it in working memory under More options → Resume unfinished
edit while the iframe remains alive. It is not a durable edit-history backup.
New-card draft text, unlike an unfinished existing-card edit, uses the shared saved
draft field. A destroyed iframe or app crash can still interrupt an unacknowledged
write; the plugin cannot promise zero loss for every possible abrupt shutdown.

Malformed notes stay read-only. A different host version arriving while local
changes are unconfirmed pauses writes and offers both versions for review.
Metadata-only sync notifications never replace content with an old draft.
Deleted notes cannot be edited. Destructive changes require confirmation.
Copy/export statuses are applied only after a programmatic clipboard write
succeeds; no attempt is made to detect pasting elsewhere. Manual native copying
from a fallback field cannot be verified and does not claim a successful status.

Standard Notes still receives a **complete note on each actual save**. Mosaic's
small bundle and windowed rendering do not eliminate bandwidth limits for large,
frequently edited notes. Prefer a smaller active capture note when necessary.

## Privacy

No analytics, tracking, accounts, AI services, remote fonts, independent cloud
storage or browser-storage copies. All application assets are bundled. The page
policy blocks independent network connections. The editor sends note data only
to its registered parent host through the Standard Notes component protocol.
Selection preferences contain IDs only and use Standard Notes' component data.

Standard Notes performs storage, encryption and sync; Mosaic does not implement
another encryption system or hold the account password. Readable note text must
exist in the editor's working memory while displayed. Initial loading/installing
and updates may contact GitHub Pages; offline availability depends on Standard
Notes' installed-plugin handling or the browser's cache. Encryption at rest and
device protection depend on the Standard Notes client and device settings.

See [security notes](docs/security.md) and [shared-core provenance](docs/shared-core.json).
This release is tested with a simulated official component host in desktop and
mobile-sized Chromium, including opaque sandbox and mobile JSON messages. These
checks do not substitute for a physical iPhone or macOS Standard Notes app test.

## Build and test

No npm install or framework build is required. Python 3 and Node are sufficient
for packaging and the data tests; the browser tests additionally need Python
Playwright and Chromium.

```sh
python3 tools/build.py
node tests/model.test.cjs
node tests/save-queue.test.cjs src/note-storage.js
node tests/save-dedup.test.cjs
node tests/save-snapshot.test.cjs
node tests/host-bridge.test.cjs
node tests/relay.test.cjs
python3 tests/browser.py
```

The synthetic browser tests also use the existing IM build for editor round trips
when `IM_EDITOR_ROOT` points to that checkout. No actual account notes are used.

## Source attribution

See [NOTICE.md](NOTICE.md) for source provenance and ownership.
