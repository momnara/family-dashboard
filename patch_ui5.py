#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 5: sync status, storing, allowance ledger JS strings -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:120]))
    text = text.replace(old, new)

# ---------- sync labels ----------
rep("""function syncModeLabel(mode){
  if(mode === 'live') return '🟢 실시간 동기화';
  if(mode === 'connecting') return '🟡 연결 중';
  return '⚪ 이 기기만 저장';
}
function syncModeDetail(mode){
  if(mode === 'live') return '가족 모두 같은 내용을 함께 보고 있어요.';
  if(mode === 'connecting') return '가족 데이터에 연결하는 중이에요.';
  return '이 기기에만 저장하고 있어요. 연결되면 자동으로 맞춰요.';
}""",
"""function syncModeLabel(mode){
  if(mode === 'live') return '🟢 Live sync';
  if(mode === 'connecting') return '🟡 Connecting';
  return '⚪ This device only';
}
function syncModeDetail(mode){
  if(mode === 'live') return 'Everyone in the family sees the same thing.';
  if(mode === 'connecting') return 'Connecting to the family data.';
  return 'Saving on this device only. It will catch up when it connects.';
}""")
rep("badge.setAttribute('title', detail + ' · 눌러서 설정');",
    "badge.setAttribute('title', detail + ' · tap for settings');")
rep("toast('이 기기의 저장 공간이 가득 찼어요. 채팅의 긴 녹음을 지워주세요 🙈');",
    "toast('This device is out of storage. Please delete some long voice messages 🙈');")
rep("toast('실시간 동기화에 연결하지 못했어요. 이 기기에 저장해둘게요');",
    "toast('Could not connect to live sync. Saving on this device for now');")

# ---------- allowance ledger ----------
rep("'지금 시작 금액은 <b>' + esc(usd(tt.start)) + '</b>이에요. 새 금액을 넣고 저장을 눌러 주세요.'",
    "'Starting balance is <b>' + esc(usd(tt.start)) + '</b>. Type a new amount and tap Save.'")
rep("""        ? '<span class="coin" aria-hidden="true">✅</span>오늘 적립 완료! <b>(내일 다시)</b>'
        : (mode === 'B'
          ? '<span class="coin" aria-hidden="true">🔒</span>할 일 모두 체크하면 열려요! <b>(' + st.done + '/' + st.total + ' 완료)</b>'
          : '<span class="coin" aria-hidden="true">💰</span>오늘 적립 완료! <b>+$1.00 받기</b>');""",
"""        ? '<span class="coin" aria-hidden="true">✅</span>Collected today! <b>(again tomorrow)</b>'
        : (mode === 'B'
          ? '<span class="coin" aria-hidden="true">🔒</span>Check every task to unlock <b>(' + st.done + '/' + st.total + ' done)</b>'
          : '<span class="coin" aria-hidden="true">💰</span>All tasks done! <b>Collect +$1.00</b>');""")
rep("if(lb) lb.textContent = '(' + st.done + '/' + st.total + ' 완료)';",
    "if(lb) lb.textContent = '(' + st.done + '/' + st.total + ' done)';")
rep("""    ? '오늘 적립 ' + ts.count + '번 · ' + usd(ts.amount) + ' 모았어요'
    : '오늘은 아직 공부 기록이 없어요. 첫 적립을 해볼까요?';""",
"""    ? 'Today: ' + ts.count + (ts.count === 1 ? ' reward' : ' rewards') + ' · ' + usd(ts.amount)
    : 'No rewards yet today. Shall we start?';""")

# ledger names / memos (old Korean memos are translated for display only)
rep("""function ledgerName(e){
  if(e.memo) return e.memo;
  if(e.type === 'study') return '공부 완료';
  if(e.type === 'deposit') return '입금';
  return '사용';
}""",
"""/* 예전에 저장된 한국어 메모도 화면에서는 영어로 보여줘요 (저장값은 그대로 둬요) */
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
}
function ledgerName(e){
  if(e.memo) return ledgerMemoLabel(e.memo);
  if(e.type === 'study') return 'Tasks done';
  if(e.type === 'deposit') return 'Added';
  return 'Spent';
}""")
rep("return k === 'deposit' ? '입금' : (k === 'spend' ? '사용' : '적립');",
    "return k === 'deposit' ? 'Added' : (k === 'spend' ? 'Spent' : 'Reward');")
rep("box.innerHTML = '<div class=\"empty\"><span class=\"em\">🐣</span>아직 내역이 없어요.<br>할 일을 마치고 적립하거나 입금·사용을 기록하면<br>여기에 날짜별로 차곡차곡 쌓여요.</div>';",
    "box.innerHTML = '<div class=\"empty\"><span class=\"em\">🐣</span>Nothing here yet.<br>Finish tasks to earn rewards, or add money in and out,<br>and it will all stack up here day by day.</div>';")
rep("esc(g.date ? dayLabel(g.date) : '날짜 없음')", "esc(g.date ? dayLabel(g.date) : 'No date')")
rep("aria-label=\"이 기록 지우기\">×</button>", "aria-label=\"Delete this record\">×</button>")

# study-done memo helpers (accept old Korean and new English)
rep("""function studyDoneMemo(dayKeyStr){
  var p = String(dayKeyStr || todayKey()).split('-');
  return Number(p[1]) + '/' + Number(p[2]) + ' 할일완료';
}
function isStudyDoneMemo(text){
  var t = String(text || '').trim();
  if(!t) return false;
  if(t === '오늘 할 일 모두 완료') return true;
  return /^\\d{1,2}\\/\\d{1,2}\\s*할일완료$/.test(t);
}""",
"""function studyDoneMemo(dayKeyStr){
  var p = String(dayKeyStr || todayKey()).split('-');
  return Number(p[1]) + '/' + Number(p[2]) + ' tasks done';
}
/* 새 메모('11/16 tasks done'), 영어 표기, 그리고 예전에 적힌 한국어 메모까지 같은 적립으로 알아봐요 */
function isStudyDoneMemo(text){
  var t = String(text || '').trim();
  if(!t) return false;
  if(t === '오늘 할 일 모두 완료' || t === 'All tasks done' || t === 'Tasks done') return true;
  return /^\\d{1,2}\\/\\d{1,2}\\s*(할일완료|tasks? done)$/i.test(t);
}""")
rep("addLedger(kid, 'study', reward, (memo || '공부 완료').slice(0, 30));",
    "addLedger(kid, 'study', reward, (memo || 'Tasks done').slice(0, 30));")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step5 ok')
