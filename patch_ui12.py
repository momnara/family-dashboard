#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 12: allowance study memos as 'M/D(요일) 할일완료'."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

rep("var MONTHS = ['January'",
    "var WEEKDAYS_KO = ['일', '월', '화', '수', '목', '금', '토'];\nvar MONTHS = ['January'")

rep("""function studyDoneMemo(dayKeyStr){
  var p = String(dayKeyStr || todayKey()).split('-');
  return Number(p[1]) + '/' + Number(p[2]) + ' tasks done';
}""",
"""/* 적립 메모는 '11/16(월) 할일완료' 모양으로 적어요 — 용돈 내역에 그대로 보여요 */
function studyDoneMemo(dayKeyStr){
  var p = String(dayKeyStr || todayKey()).split('-');
  var d = new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]), 12, 0, 0, 0);
  return Number(p[1]) + '/' + Number(p[2]) + '(' + WEEKDAYS_KO[d.getDay()] + ') 할일완료';
}""")

rep("""  if(t === '오늘 할 일 모두 완료' || t === 'All tasks done' || t === 'Tasks done') return true;
  return /^\\d{1,2}\\/\\d{1,2}\\s*(할일완료|tasks? done)$/i.test(t);""",
"""  if(t === '오늘 할 일 모두 완료' || t === 'All tasks done' || t === 'Tasks done') return true;
  return /^\\d{1,2}\\/\\d{1,2}(\\(.+\\))?\\s*(할일완료|tasks? done)$/i.test(t);""")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step12 ok')
