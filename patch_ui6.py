#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 6: to-do, lock, preview, weekly schedule and high-five JS strings -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:120]))
    text = text.replace(old, new)

# ---------- device lock / claims ----------
rep("toast(lk + ' 기기에서는 ' + kid + ' 항목을 바꿀 수 없어요!');",
    "toast('This device is locked to ' + personLabel(lk) + ' — ' + personLabel(kid) + '\\'s tasks can\\'t be changed here.');")
rep("toast('할 일 체크가 해제되어 오늘 적립된 ' + usd(1) + '도 취소됐어요.');",
    "toast('The check was removed, so today\\'s ' + usd(1) + ' reward was taken back too.');")
rep("toast('오늘 ' + usd(1) + '은 이미 적립했어요. 내일 또 만나요 🌱');",
    "toast('Today\\'s ' + usd(1) + ' was already collected. See you tomorrow 🌱');")
rep("toast('할 일을 전부 체크하면 누를 수 있어요!');",
    "toast('Check every task to unlock this!');")
rep("toast(kid + ' 오늘 할 일 모두 완료! ' + usdSigned(reward) + ' 적립했어요 🪙');",
    "toast(personLabel(kid) + ' finished every task today! ' + usdSigned(reward) + ' collected 🪙');")

# ---------- starting balance ----------
rep("toast('시작 금액을 ' + usd(val) + '로 정했어요');",
    "toast('Starting balance set to ' + usd(val));")
rep("""      ? '지금 시작 금액은 ' + usd(cur) + '이에요. 바꿀 금액을 입력해 주세요'
      : '바꿀 시작 금액을 입력해 주세요');""",
"""      ? 'Starting balance is ' + usd(cur) + '. Type the amount you want instead.'
      : 'Type the starting balance you want');""")
rep("""      '시작 금액을 $0.00으로 바꿀까요?',
      '지금은 ' + usd(cur) + '으로 저장돼 있어요. $0.00으로 바꾸면 모은 돈이 그만큼 줄어들어요.',
      '$0.00으로 바꾸기',""",
"""      'Change the starting balance to $0.00?',
      'It is saved as ' + usd(cur) + ' now. Setting it to $0.00 takes that much out of the saved money.',
      'Change to $0.00',""")
rep("toast('시작 금액은 이미 ' + usd(cur) + '이에요');",
    "toast('The starting balance is already ' + usd(cur));")

# ---------- add / spend ----------
rep("if(amount <= 0){ toast('금액을 먼저 적어주세요'); $('#quickAmount').focus(); return; }",
    "if(amount <= 0){ toast('Type an amount first'); $('#quickAmount').focus(); return; }")
rep("if(!memo) memo = kind === 'deposit' ? '입금' : '사용';",
    "if(!memo) memo = kind === 'deposit' ? 'Added' : 'Spent';")
rep("toast((kind === 'deposit' ? '입금 ' : '사용 ') + usd(amount) + ' 기록했어요');",
    "toast((kind === 'deposit' ? 'Added ' : 'Spent ') + usd(amount));")

# ---------- pinned todo ----------
rep("""var PINNED_TODO_TEXT = '간식통, 물병 가져다 놓기';
function isPinnedTodo(t){ return !!t && String(t.text || '').trim() === PINNED_TODO_TEXT; }""",
"""var PINNED_TODO_TEXTS = ['Unpack snack box & water bottle', '간식통, 물병 가져다 놓기'];
function isPinnedTodo(t){
  return !!t && PINNED_TODO_TEXTS.indexOf(String(t.text || '').trim()) >= 0;
}""")

# ---------- day preview ----------
rep("""  return '👀 ' + (d.getMonth() + 1) + '/' + d.getDate() + ' (' + WEEKDAYS[d.getDay()] + ') 미리 보기 · 체크는 오늘 날짜에만 가능해요';""",
"""  return '👀 Preview of ' + MONTHS_SHORT[d.getMonth()] + ' ' + d.getDate() + ' (' + WEEKDAYS[d.getDay()] + ') · you can only check things off for today';""")
rep("""    var label = i === 0
      ? '오늘 (' + WEEKDAYS[d.getDay()] + ')'
      : WEEKDAYS[d.getDay()] + ' ' + (d.getMonth() + 1) + '/' + d.getDate();""",
"""    var label = i === 0
      ? 'Today (' + WEEKDAYS[d.getDay()] + ')'
      : WEEKDAYS[d.getDay()] + ' ' + (d.getMonth() + 1) + '/' + d.getDate();""")
rep("""  toast((d.getMonth() + 1) + '/' + d.getDate() + ' 미리 보기 중이라 ' + what + ' 안 돼요. \\'오늘\\'로 돌아가서 해주세요!');""",
"""  toast('You are previewing ' + MONTHS_SHORT[d.getMonth()] + ' ' + d.getDate() + ', so ' + what + ' is not possible. Go back to Today first!');""")

# ---------- filter pills ----------
rep("""    if(p === '전체'){
      html += '<button class="pill' + active + '" type="button" data-filter="전체">전체</button>';
    } else {
      html += '<button class="pill' + active + '" type="button" data-filter="' + p + '">' + mascot(p) + esc(p) + '</button>';
    }""",
"""    if(p === '전체'){
      html += '<button class="pill' + active + '" type="button" data-filter="전체">All</button>';
    } else {
      html += '<button class="pill' + active + '" type="button" data-filter="' + p + '">' + mascot(p) + esc(personLabel(p)) + '</button>';
    }""")

# ---------- weekly schedule ----------
rep("daySel.innerHTML = WEEKDAYS.map(function(n, i){ return '<option value=\"' + i + '\">' + n + '요일</option>'; }).join('');",
    "daySel.innerHTML = WEEKDAYS.map(function(n, i){ return '<option value=\"' + i + '\">' + n + '</option>'; }).join('');")
rep("""        '<span class="st-who"><b>' + esc(ev.name) + '</b> ' + esc(eventLabel(ev)) +
        '<span class="st-time">' + esc(ev.lunar ? '음력 ' + ev.lunar[0] + '월 ' + ev.lunar[1] + '일' : '매년 ' + ev.solar[0] + '월 ' + ev.solar[1] + '일') + '</span></span>' +""",
"""        '<span class="st-who"><b>' + esc(personLabel(ev.name)) + '</b> · ' + esc(eventLabel(ev)) +
        '<span class="st-time">' + esc(eventWhen(ev)) + '</span></span>' +""")
rep("""            '<span class="st-who"><b>' + esc(l.kid) + '</b> · ' + esc(l.subject) +""",
"""            '<span class="st-who"><b>' + esc(personLabel(l.kid)) + '</b> · ' + esc(subjectLabel(l.subject)) +""")
rep("""              ? '<button class="lesson-done done" type="button" data-lesson-done="' + esc(l.id) + '" aria-label="' + esc(l.kid + ' ' + l.subject + ' 수업 완료 취소') + '">수업 완료 ✓</button>'
              : '<button class="lesson-done" type="button" data-lesson-done="' + esc(l.id) + '" aria-label="' + esc(l.kid + ' ' + l.subject + ' 수업 완료로 표시') + '">수업 완료</button>') +""",
"""              ? '<button class="lesson-done done" type="button" data-lesson-done="' + esc(l.id) + '" aria-label="' + esc('Undo class done for ' + personLabel(l.kid) + ' ' + subjectLabel(l.subject)) + '">Class done ✓</button>'
              : '<button class="lesson-done" type="button" data-lesson-done="' + esc(l.id) + '" aria-label="' + esc('Mark ' + personLabel(l.kid) + ' ' + subjectLabel(l.subject) + ' class done') + '">Class done</button>') +""")
rep("'<div class=\"st-empty\">오늘은 수업이 없어요. 느긋한 하루 🐣</div>'",
    "'<div class=\"st-empty\">No classes today. Take it easy 🐣</div>'")
rep("'<span class=\"dc-empty\">일정 없음</span></div></div>'", "'<span class=\"dc-empty\">Nothing planned</span></div></div>'")
rep("""        var chipInner = '<span class="lc-time">' + esc(timeLabel(l.time)) + '</span>' +
          '<span class="lc-who">' + esc(l.kid) + ' ·</span>' +
          '<span class="lc-sub">' + esc(l.subject) + '</span>' +
          (skipped ? '<span class="lc-skip">휴강</span>' : '');
        var chipClass = 'lc-chip' + (l.completedDate === todayK ? ' lc-done' : '') + (skipped ? ' lc-off' : '');
        var chipLabel = l.kid + ' ' + l.subject + ' ' + timeLabel(l.time) + (skipped ? ' · 이번 주 휴강' : '');
        if(!isMom()) return '<span class="' + chipClass + '" data-kid="' + esc(l.kid) + '" title="' + esc(chipLabel) + '">' + chipInner + '</span>';
        return '<button class="' + chipClass + '" type="button" data-lesson="' + esc(l.id) + '" data-kid="' + esc(l.kid) + '" aria-label="' + esc(chipLabel) + ' 수업 지우기">' +""",
"""        var chipInner = '<span class="lc-time">' + esc(timeLabel(l.time)) + '</span>' +
          '<span class="lc-who">' + esc(personLabel(l.kid)) + ' ·</span>' +
          '<span class="lc-sub">' + esc(subjectLabel(l.subject)) + '</span>' +
          (skipped ? '<span class="lc-skip">Skipped</span>' : '');
        var chipClass = 'lc-chip' + (l.completedDate === todayK ? ' lc-done' : '') + (skipped ? ' lc-off' : '');
        var chipLabel = personLabel(l.kid) + ' ' + subjectLabel(l.subject) + ' ' + timeLabel(l.time) + (skipped ? ' · skipped this week' : '');
        if(!isMom()) return '<span class="' + chipClass + '" data-kid="' + esc(l.kid) + '" title="' + esc(chipLabel) + '">' + chipInner + '</span>';
        return '<button class="' + chipClass + '" type="button" data-lesson="' + esc(l.id) + '" data-kid="' + esc(l.kid) + '" aria-label="' + esc(chipLabel) + ' · remove class">' +""")
rep("""        var who = String(m.who || '가족');
        var text = String(m.text || '');
        return '<span class="dc-event" title="' + esc(who + ' · ' + text) + '">' +""",
"""        var who = personLabel(m.who || '가족');
        var text = String(m.text || '');
        return '<span class="dc-event" title="' + esc(who + ' · ' + text) + '">' +""")
rep("toast(les.kid + ' ' + les.subject + ' 수업 완료를 취소했어요');",
    "toast('Undid class done for ' + personLabel(les.kid) + ' ' + subjectLabel(les.subject));")
rep("toast(les.kid + ' ' + les.subject + ' 수업 완료! ✓');",
    "toast(personLabel(les.kid) + ' ' + subjectLabel(les.subject) + ' class done! ✓');")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step6 ok')
