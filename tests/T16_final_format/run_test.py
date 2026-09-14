from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

assert ROOT.name == 'AI-character-embodiment-ltx2-final', ROOT.name

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
assert re.fullmatch(r'\d+\.\d+\.\d+', version), version

skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n')
m = re.search(r'(?m)^version:\s*([^\s]+)\s*$', skill)
assert m and m.group(1) == version, (m.group(1) if m else None, version)

required = [
    'SKILL.md','README.md','SOURCES.md','VERSION',
    'FINAL_FORMAT_CONTRACT.md','PACKAGE_MANIFEST.md','BUILD_AUDIT.md',
    'ASSET_STORAGE_POLICY.md',
    'compiler','adapters','references','templates','validators',
    'tests','tools','video_engine','evaluation','case_library','distribution'
]
for rel in required:
    assert (ROOT / rel).exists(), rel

# No historical release clutter at root.
for p in ROOT.iterdir():
    assert not re.match(r'^(RELEASE_NOTES_v|MIGRATION_v|BUILD_AUDIT_v)', p.name), p.name
    assert not re.search(r'_v\d+\.\d+(?:\.\d+)?(?=\.)', p.name), p.name

# No version suffixes in knowledge/document filenames anywhere.
for p in ROOT.rglob('*'):
    assert not re.search(r'_v\d+\.\d+(?:\.\d+)?(?=\.)', p.name), str(p)

print('T16 final format PASS')
