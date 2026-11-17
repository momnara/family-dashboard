#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 11: remaining event handlers, init, allowance-history date labels -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

# ---------- allowance history: just the memo, no Today/Yesterday labels ----------
rep("""/* 예전에 저장된 한국어 메모도 화면에서는 영어로 보여줘요 (저장값은 그대로 둬요) */
function ledgerMemoLabel(memo){
  var s = String(memo == null ? '' : memo).trim();
  if(!s) return '';
  if(s === '공부 완료') return 'Tasks done';
  if(s === '오늘 할 일 모두 완료') return 'All tasks done';
  if(s === '입금') return 'Added';
  if(s === '사용') return 'Spent';
  var m = s.match(/^(\\d{1,2})\\/(\\d{1,2})\\s*할일완료$/);
  if(m) return m[1] + '/' + m[2] + ' tasks done';
  return s;
}""",
"""/* 용돈 적립 내역은 메모를 적힌 그대로 보여줘요 (예: '11/15 할일완료').
   날짜 메모는 손대지 않고, 예전 기본값 메모만 영어로 바꿔요. */
function ledgerMemoLabel(memo){
  var s = String(memo == null ? '' : memo).trim();
  if(!s) return '';
  if(s === '공부 완료') return 'Tasks done';
  if(s === '오늘 할 일 모두 완료') return 'All tasks done';
  if(s === '입금') return 'Added';
  if(s === '사용') return 'Spent';
  return s;
}
/* 내역 묶음의 날짜 제목 — '오늘/어제' 대신 '11/15'처럼 숫자로만 보여줘요 */
function ledgerDayLabel(key){
  var p = String(key || '').split('-');
  if(p.length !== 3) return String(key || '');
  return Number(p[1]) + '/' + Number(p[2]);
}""")
rep("'<span class=\"dtext\">' + esc(g.date ? dayLabel(g.date) : 'No date') + '</span>' +",
    "'<span class=\"dtext\">' + esc(g.date ? ledgerDayLabel(g.date) : 'No date') + '</span>' +")

# ---------- remaining handlers ----------
rep("toast('공부 1회에 ' + usd(state.allowance[currentKid()].reward) + ' 적립해요');",
    "toast('Earns ' + usd(state.allowance[currentKid()].reward) + ' per task day');")
rep("if(!isMom()){ toast('지우는 건 엄마만 할 수 있어요 🔒'); return; }",
    "if(!isMom()){ toast('Only Mom can delete 🔒'); return; }", 2)
rep("if(del && !isMom()){ toast('지우는 건 엄마만 할 수 있어요 🔒'); return; }",
    "if(del && !isMom()){ toast('Only Mom can delete 🔒'); return; }")
rep("toast('기록을 지웠어요');", "toast('Record deleted');")
rep("if(del && blockInPreview('할 일 지우기')) return;", "if(del && blockInPreview('deleting tasks')) return;")
rep("toast('할 일을 지웠어요');", "toast('Task deleted');")
rep("if(!subject){ toast('무슨 수업인지 적어주세요'); $('#lessonSubject').focus(); return; }",
    "if(!subject){ toast('Please type the subject'); $('#lessonSubject').focus(); return; }")
rep("toast(kid + ' ' + WEEKDAYS[day] + '요일 ' + timeLabel(time) + ' ' + subject + ' 추가했어요 🗓️');",
    "toast(personLabel(kid) + ' · ' + WEEKDAYS[day] + ' ' + timeLabel(time) + ' ' + subjectLabel(subject) + ' added 🗓️');")
rep("confirmModal('수업을 지울까요?', les.kid + ' ' + WEEKDAYS[les.day] + '요일 ' + timeLabel(les.time) + ' ' + les.subject + ' 수업이에요.', '지우기', function(){",
    "confirmModal('Delete this class?', personLabel(les.kid) + ' · ' + WEEKDAYS[les.day] + ' ' + timeLabel(les.time) + ' ' + subjectLabel(les.subject) + '.', 'Delete', function(){")
rep("toast('수업을 지웠어요');", "toast('Class deleted');")
rep("if(state.chat.locked){ toast('이 기기가 잠겨 있어요. 잠금을 끄면 바꿀 수 있어요 🔒'); return; }",
    "if(state.chat.locked){ toast('This device is locked. Turn the lock off to change it 🔒'); return; }")
rep("toast('이제 ' + state.chat.me + '(으)로 말해요');", "toast('Now using ' + personLabel(state.chat.me));")
rep("toast(this.checked ? '이 기기를 ' + state.chat.me + '로 잠갔어요 🔒' : '잠금을 풀었어요');",
    "toast(this.checked ? 'This device is locked as ' + personLabel(state.chat.me) + ' 🔒' : 'Device lock is off');")
rep("if(v <= 0){ toast('몇 분 공부할지 적어주세요'); return; }", "if(v <= 0){ toast('Type how many minutes to study'); return; }")
rep("toast(v + '분 타이머를 준비했어요');", "toast(v + '-minute timer ready');")
rep("toast('타이머를 처음으로 돌렸어요');", "toast('Timer reset');")
rep("toast(alarmTargetText(state.alarm.targetTs) + '에 알려드릴게요');",
    "toast('I will chime at ' + alarmTargetText(state.alarm.targetTs));")
rep("toast('이렇게 종이 울려요 🔔');", "toast('This is how the chime sounds 🔔');")
rep("esc(s.label) + ' 스티커\"", "esc(s.label) + ' sticker\"")
rep("if(note) note.textContent = '이 브라우저는 녹음을 지원하지 않아요 · 글자와 스티커는 잘 돼요';",
    "if(note) note.textContent = 'This browser cannot record · messages and stickers work fine';")

# ---------- section comments that show on screen? (none) : keep behaviour, tidy the app description ----------
rep('   우리 가족 대시보드 — single file app', '   Our Family Dashboard — single file app')

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step11 ok')
