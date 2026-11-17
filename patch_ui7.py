#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 7 (line-based): to-do render, high five, toggles -> English."""
import io

PATH = 'index.html'
lines = io.open(PATH, encoding='utf-8').read().split('\n')

def repline(n, marker, new):
    """Replace 1-indexed line n; assert the old line still contains marker."""
    old = lines[n - 1]
    if marker not in old:
        raise SystemExit('LINE %d marker missing. old=%r' % (n, old[:160]))
    lines[n - 1] = new

def rep(old, new, count=1):
    global lines
    whole = '\n'.join(lines)
    c = whole.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:120]))
    lines = whole.replace(old, new).split('\n')

# progress line
repline(3161, '미리 보기', "    ? ('Preview · ' + total + (total === 1 ? ' task' : ' tasks'))")
repline(3162, '완료', "    : (done + ' / ' + total + ' done');")

# prep homework row
repline(3168, '내일', "      '<button class=\"check\" type=\"button\"' + (preview ? ' disabled' : '') + ' aria-pressed=\"' + (pdone ? 'true' : 'false') + '\" aria-label=\"' + esc('Homework for tomorrow\\'s ' + subjectLabel(l.subject) + ' class') + (preview ? ' (preview, cannot check)' : ' mark done') + '\">✓</button>' +")
repline(3169, '내일', "      '<span class=\"t-text\">Tomorrow\\'s ' + esc(subjectLabel(l.subject)) + ' homework <span class=\"prep-when\">(' + esc(WEEKDAYS[l.day]) + ' ' + esc(l.time) + ')</span></span>' +")
repline(3170, 'esc(l.kid)', "      '<span class=\"t-owner\">' + mascot(l.kid) + esc(personLabel(l.kid)) + (locked ? '<span class=\"t-lock\" aria-hidden=\"true\">🔒</span>' : '') + '</span>' +")

# empty states
repline(3178, '할 일이 없어요', "        ? 'No tasks on this day. Take it easy 🍃'")
repline(3179, 'todoFilter', "        : (state.ui.todoFilter === '전체' ? 'No tasks.' : 'No tasks for ' + esc(personLabel(state.ui.todoFilter)) + '.')) +")

# normal todo row
repline(3186, '주중)', "        '<button class=\"check\" type=\"button\"' + (preview ? ' disabled' : '') + ' aria-pressed=\"' + ((t.done && !preview) ? 'true' : 'false') + '\" aria-label=\"' + esc(t.text) + (t.weekdaysOnly ? ' (weekdays)' : '') + (preview ? ' (preview, cannot check)' : ' mark done') + '\">✓</button>' +")
repline(3187, 'wd-tag', "        '<span class=\"t-text\">' + (t.weekdaysOnly ? '<span class=\"wd-tag\" title=\"Only on weekdays, Monday to Friday\">Weekdays</span> ' : '') + esc(t.text) + (t.done && paid ? ' <span class=\"done-tag\">Done</span>' : '') + '</span>' +")
repline(3188, 'esc(t.owner)', "        '<span class=\"t-owner\">' + mascot(t.owner) + esc(personLabel(t.owner)) + (locked ? '<span class=\"t-lock\" aria-hidden=\"true\">🔒</span>' : '') + '</span>' +")
repline(3189, 'tdel', "        (isMom() && !preview ? '<button class=\"t-del\" type=\"button\" data-tdel=\"' + esc(t.id) + '\" aria-label=\"Delete task\">×</button>' : '') +")

# high five banner
rep("  var who = whoOverride || (f === '전체' ? '우리 가족' : f);",
    "  var who = personLabel(whoOverride || (f === '전체' ? '가족' : f));")
rep("    '<h3>하이파이브!</h3>' +\n    '<p>' + esc(who) + ' 할 일을 모두 끝냈어요. 정말 잘했어요!</p>' +\n    '<button class=\"hf-close\" type=\"button\" aria-label=\"닫기\" data-hf-close>✕</button>' +",
    "    '<h3>High five!</h3>' +\n    '<p>' + esc(who) + ' finished every task today. Awesome job!</p>' +\n    '<button class=\"hf-close\" type=\"button\" aria-label=\"Close\" data-hf-close>✕</button>' +")

# prep toggle
rep("if(blockInPreview('준비 숙제 체크')) return;", "if(blockInPreview('checking homework')) return;")
rep("toast(nowDone ? '내일 ' + les.subject + ' 수업 숙제 완료! ✓' : '체크를 풀었어요');",
    "toast(nowDone ? 'Tomorrow\\'s ' + subjectLabel(les.subject) + ' homework done! ✓' : 'Check removed');")
rep("""    toast(claimedToday(les.kid)
      ? '할 일 모두 완료! 오늘 ' + usd(1) + '은 이미 받았어요 ✓'
      : '할 일 모두 완료! 용돈 탭에서 오늘 ' + usd(1) + ' 적립 버튼을 눌러보세요!');""",
"""    toast(claimedToday(les.kid)
      ? 'All tasks done! Today\\'s ' + usd(1) + ' was already collected ✓'
      : 'All tasks done! Tap the collect button in Allowance for today\\'s ' + usd(1) + '!');""", 1)
rep("""    toast(claimedToday(t.owner)
      ? '할 일 모두 완료! 오늘 ' + usd(1) + '은 이미 받았어요 ✓'
      : '할 일 모두 완료! 용돈 탭에서 오늘 ' + usd(1) + ' 적립 버튼을 눌러보세요!');""",
"""    toast(claimedToday(t.owner)
      ? 'All tasks done! Today\\'s ' + usd(1) + ' was already collected ✓'
      : 'All tasks done! Tap the collect button in Allowance for today\\'s ' + usd(1) + '!');""", 1)

# normal todo toggle
rep("if(blockInPreview('할 일 체크')) return;", "if(blockInPreview('checking tasks')) return;")
rep("""      ? '완료! ' + t.text + ' ✓ (' + left + '개 남았어요)'
      : '완료! ' + t.text + ' ✓');""",
"""      ? 'Done! ' + t.text + ' ✓ (' + left + ' left)'
      : 'Done! ' + t.text + ' ✓');""")

# reset checks
rep("toast(cleared ? '오늘 체크를 모두 풀었어요. 새로운 하루 시작! 🌤️' : '이미 모두 체크가 풀려 있어요');",
    "toast(cleared ? 'All of today\\'s checks are cleared. Fresh start! 🌤️' : 'Everything is already unchecked');")

io.open(PATH, 'w', encoding='utf-8').write('\n'.join(lines))
print('step7 ok')
