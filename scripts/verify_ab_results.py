"""Verify the main conversion comparison. Python 3.9+, standard library only."""
import argparse,csv,json,math
from pathlib import Path
def analyse(path):
 groups={'control':{'n':0,'converted':0},'treatment':{'n':0,'converted':0}};seen=set();raw=mismatch=duplicates=0
 with Path(path).open(newline='',encoding='utf-8-sig') as f:
  for r in csv.DictReader(f):
   raw+=1
   if (r['group'],r['landing_page']) not in {('control','old_page'),('treatment','new_page')}:mismatch+=1;continue
   if r['user_id'] in seen:duplicates+=1;continue
   seen.add(r['user_id']);g=groups[r['group']];g['n']+=1;g['converted']+=int(r['converted'])
 old,new=groups['control'],groups['treatment'];p0=old['converted']/old['n'];p1=new['converted']/new['n'];d=p1-p0
 pooled=(old['converted']+new['converted'])/(old['n']+new['n']);z=d/math.sqrt(pooled*(1-pooled)*(1/old['n']+1/new['n']))
 se=math.sqrt(p0*(1-p0)/old['n']+p1*(1-p1)/new['n'])
 return dict(raw_rows=raw,mismatched_rows=mismatch,duplicate_users_removed=duplicates,analysed_users=len(seen),control=old,treatment=new,old_rate=p0,new_rate=p1,new_minus_old_pp=d*100,normal_approx_95pct_ci_pp=[(d-1.959963984540054*se)*100,(d+1.959963984540054*se)*100],pooled_z_new_minus_old=z,one_sided_p_new_greater_than_old=.5*math.erfc(z/math.sqrt(2)))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',default='ab_data.csv');r=analyse(p.parse_args().data)
 assert r['raw_rows']==294478 and r['analysed_users']==290584
 assert r['control']=={'n':145274,'converted':17489} and r['treatment']=={'n':145310,'converted':17264}
 print(json.dumps(r,indent=2))
