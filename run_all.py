#!/usr/bin/env python3
"""Run all independent checks and regenerate Figures 1-4; no external data."""
from pathlib import Path
import subprocess,sys,os,time,json
ROOT=Path(__file__).resolve().parent

def main():
    start=time.perf_counter();env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',MPLCONFIGDIR=str(ROOT/'.cache'/'matplotlib'))
    report=['# Claims report','','Numerical checks illustrate the paper; they do not replace its proofs.','',f'Python {sys.version.split()[0]}. Fixed seeds are recorded in each script.','','| Check | Status | Tests | Seconds |','|---|---|---:|---:|']
    details=[];failures=[]
    jobs=sorted((ROOT/'checks').glob('C[0-9][0-9]_*.py'))+sorted((ROOT/'figures').glob('figure[1-4].py'))
    for job in jobs:
        t=time.perf_counter();result=subprocess.run([sys.executable,str(job)],cwd=ROOT,env=env,capture_output=True,text=True)
        elapsed=time.perf_counter()-t;status='PASS' if result.returncode==0 else 'FAIL';lines=result.stdout.splitlines()
        records=[json.loads(l.removeprefix('RESULT_JSON ')) for l in lines if l.startswith('RESULT_JSON ')]
        if job.parent.name=='checks' and (not records or any(v['status']!='PASS' for v in records)):
            status='FAIL'
        count=sum(len(v['checks']) for v in records)
        report.append(f'| {job.relative_to(ROOT)} | {status} | {count or "figure"} | {elapsed:.2f} |')
        print(f'{status} {job.relative_to(ROOT)} ({elapsed:.2f}s)',flush=True)
        if status=='FAIL':
            failures.append(str(job.relative_to(ROOT)));print(result.stdout[-5000:]+result.stderr[-5000:],flush=True)
        details.extend(['',f'## {job.stem}',''])
        if records:
            details.extend(['| Test | Claimed | Computed | Maximum error | Tolerance | Status |','|---|---|---|---:|---:|---|'])
            for rec in records:
                for row in rec['checks']:
                    clean=lambda x:str(x).replace('|','/').replace('\n',' ')
                    details.append('| '+' | '.join(clean(row[k]) for k in ['name','claimed','computed','error','tolerance','status'])+' |')
        else:details.extend(['```text',result.stdout.strip(),result.stderr.strip(),'```'])
    total=time.perf_counter()-start
    report+=['',f'Total runtime: {total:.2f} seconds.',f'Overall: {"FAIL" if failures else "PASS"}.']+details
    (ROOT/'CLAIMS_REPORT.md').write_text('\n'.join(report)+'\n')
    print(f'Total {total:.2f}s; report: CLAIMS_REPORT.md',flush=True)
    return bool(failures)
if __name__=='__main__':raise SystemExit(main())
