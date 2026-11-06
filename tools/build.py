"""Dependency-free, reproducible release packaging for GitHub Pages and Standard Notes."""
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.0.0'
BASE = 'https://joshuazang.github.io/Mosaic/'
ORDER = ['src/note-format.js', 'src/host-bridge.js', 'src/relay.js',
         'src/note-storage.js', 'src/message-transfer.js', 'src/clipboard.js',
         'src/model.js', 'src/icons.js', 'src/app.js']
script = ('\n"use strict";\n' + '\n'.join((ROOT / name).read_text() for name in ORDER)).encode()
style = (ROOT / 'src/styles.css').read_bytes()
files = {}
for data, suffix in [(script, '.js'), (style, '.css')]:
    path = 'assets/mosaic-' + hashlib.sha256(data).hexdigest()[:12] + suffix
    (ROOT / path).write_bytes(data)
    files[path] = data
    if suffix == '.js': js_path = path
    else: css_path = path
for old in (ROOT / 'assets').glob('mosaic-*'):
    if old.suffix in ['.js','.css'] and str(old.relative_to(ROOT)) not in files:
        old.unlink()
html = (ROOT / 'index.template.html').read_text().replace('__JS__', './' + js_path).replace('__CSS__', './' + css_path)
(ROOT / 'index.html').write_text(html)
files['index.html'] = html.encode()
files['icon.svg'] = (ROOT / 'icon.svg').read_bytes()
metadata = {
    'identifier': 'com.joshuazang.mosaic', 'name': 'Mosaic', 'content_type': 'SN|Component',
    'area': 'editor-editor', 'version': VERSION,
    'description': 'A private plain-text card board for Standard Notes. Open the same format-3 notes in Mosaic and IM-style-editor 4 without conversion.',
    'url': BASE + 'index.html?v=' + VERSION,
    'download_url': BASE + 'Mosaic-' + VERSION + '.zip',
    'latest_url': BASE + 'mosaic.ext.json',
    'marketing_url': 'https://github.com/joshuazang/Mosaic',
    'thumbnail_url': BASE + 'icon.svg'
}
encoded = (json.dumps(metadata, indent=2) + '\n').encode()
for name in ['mosaic.ext.json', 'mosaic-' + VERSION + '.ext.json']:
    (ROOT / name).write_bytes(encoded)
files['mosaic.ext.json'] = encoded
files['NOTICE.md'] = (ROOT / 'NOTICE.md').read_bytes()
entries = {'Mosaic-' + VERSION + '/dist/' + name: data for name, data in files.items()}
entries['Mosaic-' + VERSION + '/package.json'] = (json.dumps({
    'name': 'mosaic-standard-notes', 'version': VERSION, 'private': True,
    'sn': {'main': 'dist/index.html'}
}, indent=2) + '\n').encode()
with ZipFile(ROOT / ('Mosaic-' + VERSION + '.zip'), 'w', ZIP_DEFLATED) as archive:
    for name, data in sorted(entries.items()):
        info = ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, data)
with ZipFile(ROOT / ('Mosaic-' + VERSION + '.zip')) as archive:
    assert archive.testzip() is None
    for name, data in entries.items(): assert archive.read(name) == data
print(json.dumps({'version': VERSION, 'script': js_path, 'script_bytes': len(script),
                  'css': css_path, 'css_bytes': len(style),
                  'zip_bytes': (ROOT / ('Mosaic-' + VERSION + '.zip')).stat().st_size}, indent=2))
