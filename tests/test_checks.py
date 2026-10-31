"""Run every published check in an isolated process with a fixed thread count."""
from pathlib import Path
import os,subprocess,sys
import pytest
ROOT=Path(__file__).resolve().parents[1]
CHECKS=sorted((ROOT/'checks').glob('C[0-9][0-9]_*.py'))

@pytest.mark.parametrize('script',CHECKS,ids=lambda p:p.stem)
def test_claim(script):
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    result=subprocess.run([sys.executable,str(script)],cwd=ROOT,env=env,capture_output=True,text=True,timeout=120)
    assert result.returncode==0,result.stdout+result.stderr
    assert 'RESULT_JSON ' in result.stdout
    assert 'FAIL' not in result.stdout
