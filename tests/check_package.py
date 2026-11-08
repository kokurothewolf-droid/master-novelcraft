#!/usr/bin/env python3
"""Validate the public distribution, not agent writing behavior."""
from pathlib import Path
import hashlib
import re
import sys

base = Path(__file__).resolve().parents[1]
errors = []
for rel in ['SKILL.md', 'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
            'PUBLIC_EDITION_NOTES.md', 'UPLOAD_TO_GITHUB.md', 'MANIFEST.sha256']:
    if not (base / rel).is_file(): errors.append('Missing: ' + rel)
for folder in ['agents', 'references', 'templates', 'examples', 'tests', 'sources']:
    if not (base / folder).is_dir(): errors.append('Missing folder: ' + folder)
main = (base / 'SKILL.md').read_text()
for rel in re.findall(r'`(references/[^`]+\.md)`', main):
    if not (base / rel).is_file(): errors.append('Broken skill reference: ' + rel)
source_dirs = list((base / 'sources/sw').glob('sw-*'))
if len(source_dirs) != 19: errors.append('Expected 19 imported source folders')
for d in source_dirs:
    if not (d / 'source-skill.md').is_file(): errors.append('Missing source guide: ' + d.name)
manifest = base / 'MANIFEST.sha256'
listed = set()
if manifest.is_file():
    for line in manifest.read_text().splitlines():
        digest, rel = line.split('  ', 1)
        listed.add(rel)
        p = base / rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            errors.append('Manifest mismatch: ' + rel)
    actual = {p.relative_to(base).as_posix() for p in base.rglob('*')
              if p.is_file() and p.name != 'MANIFEST.sha256'
              and '__pycache__' not in p.parts and '.git' not in p.parts}
    if listed != actual: errors.append('Manifest file list differs from package')
print('Imported source folders:', len(source_dirs))
print('Errors:', len(errors))
for e in errors: print('FAIL:', e)
sys.exit(bool(errors))
