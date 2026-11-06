# Source and attribution

Mosaic is a standalone Standard Notes editor by the IM-style-editor project author.
Copyright (c) 2026 joshuazang. No separate license grant is made by publishing
this source repository, consistent with the existing IM-style-editor repository.

The shared format-3 reader/writer, acknowledged save queue, lean reply helpers,
clipboard helpers and message-transfer code come from
[IM-style-editor](https://github.com/joshuazang/IM-style-editor), revision
`7e063e3e028f050fa37b09092b5982619d0c5197`. File checksums are recorded in
`docs/shared-core.json`. The format, queue and transfer files are unmodified.

`src/relay.js` is Mosaic's small, readable implementation of the public Standard
Notes component protocol, informed by the established
[Standard Notes component-relay](https://github.com/standardnotes/component-relay)
implementation and the existing IM editor's host integration. It supports only
the integration Mosaic uses, with origin binding, parent-window checks, session
keys, random message IDs and mobile JSON transport. The full implementation is
included in readable source; no compiled SDK, UUID library, remote theme loader
or third-party JavaScript runtime is bundled.

The new board UI, layout model, CSS and SVG UI artwork are original Mosaic code.
OpenKeep was a visual reference; no OpenKeep application code, storage layer,
cloud integration, analytics, assets or dependencies are included.

The complete application source is in the public GitHub repository, including its
release tag. `python3 tools/build.py` reproduces the release without downloading
dependencies.
