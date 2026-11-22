"""Run SKILL/scripts/tts.py with Edge TTS going through $HTTPS_PROXY (aiohttp ignores proxy env vars)."""
import os, sys, runpy, edge_tts
_orig = edge_tts.Communicate.__init__
def _init(self, *a, **k):
    k.setdefault('proxy', os.environ.get('HTTPS_PROXY'))
    _orig(self, *a, **k)
edge_tts.Communicate.__init__ = _init
script = sys.argv[1]; sys.argv = sys.argv[1:]
runpy.run_path(script, run_name='__main__')
