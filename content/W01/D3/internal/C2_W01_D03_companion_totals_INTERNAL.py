"""Compute the companion simulator's totals: every combination of the day's five cleaning decisions.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_companion_totals_INTERNAL.py > /tmp/combos.json

The companion page embeds only these totals, never a record, so a learner can move each decision
without the page carrying anything planted in the export.
"""
import csv, json, itertools
rows=list(csv.DictReader(open('content/W01/D3/data/C2_W01_D03_orders_STUDENT.csv')))
for n,r in enumerate(rows,2): r['line']=n
def conv(v):
    try: return int(v)
    except: return None
out={}
for amt,key,pref,bulk,status in itertools.product(['log','zero'],['line','record','order_id'],['first','validates'],['keep','remove'],['flag','drop','default']):
    recs=[]; logged=0
    for r in rows:
        a=conv(r['amount'])
        if a is None and amt=='zero': a=0
        recs.append(dict(r,amt=a))
    kept={}; aside=0
    for r in recs:
        if key=='line': k=tuple(sorted((f,v) for f,v in r.items() if f!='amt'))
        elif key=='record': k=tuple(sorted((f,v) for f,v in r.items() if f not in('amt','line')))
        else: k=r['order_id']
        if k not in kept: kept[k]=r
        elif pref=='validates' and kept[k]['amt'] is None and r['amt'] is not None: kept[k]=r; aside+=1
        else: aside+=1
    clean=list(kept.values())
    rej=[r for r in clean if r['amt'] is None]; clean=[r for r in clean if r['amt'] is not None]
    aside+=len(rej)
    q2=[r for r in clean if r['quarter']=='Q2']
    if bulk=='remove':
        top=max(q2,key=lambda r:r['amt']); clean=[r for r in clean if r is not top]; aside+=1
    miss=[r for r in clean if r['status']=='']
    if status=='drop': clean=[r for r in clean if r['status']!='']; aside+=len(miss)
    Q1=sum(r['amt'] for r in clean if r['quarter']=='Q1'); Q2=sum(r['amt'] for r in clean if r['quarter']=='Q2')
    deliv=sum(1 for r in clean if r['quarter']=='Q2' and (r['status']=='delivered' or (status=='default' and r['status']=='')))
    def opc(q):
        x=[r for r in clean if r['quarter']==q and r['segment']=='Retail-Plus']; return len(x)/len({r['customer_id'] for r in x})
    exp=sum(conv(r['amount']) or 0 for r in rows if r['quarter']=='Q1')
    out['|'.join([amt,key,pref,bulk,status])]=dict(kept=len(clean),aside=aside,q1=Q1,q2=Q2,
        drop=round(100*(1-Q2/Q1),1),gap=Q1-19000000,zeros=sum(1 for r in clean if r['amt']==0),
        logged=len(rej)+(0),deliv=deliv,rp=round(100*(opc('Q2')/opc('Q1')-1),1),exp=exp,rowsok=len(clean)+aside==len(rows))
print(json.dumps(out, separators=(',', ':')))

# Test inputs and expected outcomes
# --------------------------------
# The honest pass, key "log|order_id|validates|keep|flag"
#     kept 186, aside 15, q1 19000000, q2 18700000, drop 1.6, gap 0, rp -35.0
# The first-copy pass, key "log|order_id|first|keep|flag"
#     kept 185, aside 16, q1 18998210, gap -1790
# The fenced pass, key "log|order_id|validates|remove|flag"
#     q2 15754540, drop 17.1
