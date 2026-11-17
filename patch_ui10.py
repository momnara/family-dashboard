#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 10: calendar render, family events, photos -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

# ---------- family events ----------
rep("function eventLabel(ev){ return ev.label || (ev.kind === 'memorial' ? '기일' : '생일'); }",
    "function eventLabel(ev){ return ev.label || (ev.kind === 'memorial' ? 'Memorial' : 'Birthday'); }")
rep("function eventTitle(ev){ return ev.name + ' ' + eventLabel(ev); }",
    "function eventTitle(ev){ return personLabel(ev.name) + '\\'s ' + eventLabel(ev).toLowerCase(); }")
rep("""  if(ev.lunar) return '음력 ' + md[0] + '월 ' + md[1] + '일 · 해마다 양력 날짜가 달라져요';
  return '매년 ' + md[0] + '월 ' + md[1] + '일';""",
"""  if(ev.lunar) return 'Lunar ' + md[0] + '/' + md[1] + ' · the date changes every year';
  return 'Every year on ' + md[0] + '/' + md[1];""")
# birthday-memo matching also understands the English notes the family writes now
rep("""function memoCompareText(t){
  return String(t || '')
    .replace(/[\\u{1F000}-\\u{1FAFF}\\u{2190}-\\u{2BFF}\\u{FE00}-\\u{FE0F}\\u{200D}\\u{20E3}]/gu, '')
    .replace(/[\\s~!.,·…\\-_()（）]/g, '')
    .toLowerCase();
}""",
"""function memoCompareText(t){
  return String(t || '')
    .replace(/[\\u{1F000}-\\u{1FAFF}\\u{2190}-\\u{2BFF}\\u{FE00}-\\u{FE0F}\\u{200D}\\u{20E3}]/gu, '')
    .replace(/[\\s~!.,·…\\-_()（）'’]/g, '')
    .toLowerCase();
}""")
rep("""      return text === al + '생일' || text === al + 'birthday' || text === al + '생일이에요';""",
"""      return text === al + '생일' || text === al + 'birthday' || text === al + '생일이에요' ||
        text === al + 'sbirthday' || text === al + 'birthdaytoday';""")

# ---------- calendar render ----------
rep("title.textContent = calView.y + '년 ' + (calView.m + 1) + '월';",
    "title.textContent = monthName(calView.m) + ' ' + calView.y;")
rep("""    var label = (calView.m + 1) + '월 ' + i + '일 (' + WEEKDAYS[wd] + ') ';""",
"""    var label = monthName(calView.m) + ' ' + i + ' (' + WEEKDAYS[wd] + ') ';""")
rep("""    if(lessons.length) extra.push('수업 ' + lessons.length + '개');
    if(money.length) extra.push('용돈 기록 ' + money.length + '개');
    if(memos.length) extra.push('메모 ' + memos.length + '개');
    dailyDone.forEach(function(k){ extra.push(k + ' 할 일 완료'); });""",
"""    if(lessons.length) extra.push(lessons.length + (lessons.length === 1 ? ' class' : ' classes'));
    if(money.length) extra.push(money.length + ' allowance');
    if(memos.length) extra.push(memos.length + (memos.length === 1 ? ' memo' : ' memos'));
    dailyDone.forEach(function(k){ extra.push(personLabel(k) + ' all tasks done'); });""")
rep("if(t) t.textContent = Number(p[1]) + '월 ' + Number(p[2]) + '일 (' + WEEKDAYS[wd] + ')';",
    "if(t) t.textContent = monthName(Number(p[1]) - 1) + ' ' + Number(p[2]) + ' (' + WEEKDAYS[wd] + ')';")
rep("""    if(key === todayKey()) rel = '오늘';
    else if(key === dateKey(daysAgo(1))) rel = '어제';
    else if(key === dateKey(daysAgo(-1))) rel = '내일';""",
"""    if(key === todayKey()) rel = 'Today';
    else if(key === dateKey(daysAgo(1))) rel = 'Yesterday';
    else if(key === dateKey(daysAgo(-1))) rel = 'Tomorrow';""")
rep("(key === todayKey() ? '<span class=\"cb-now\">' + (ev.kind === 'memorial' ? '오늘' : '오늘 🎉') + '</span>' : '') +",
    "(key === todayKey() ? '<span class=\"cb-now\">' + (ev.kind === 'memorial' ? 'Today' : 'Today 🎉') + '</span>' : '') +")
rep("'<span class=\"cc-main\"><b>' + esc(l.kid) + '</b> · ' + esc(l.subject) +",
    "'<span class=\"cc-main\"><b>' + esc(personLabel(l.kid)) + '</b> · ' + esc(subjectLabel(l.subject)) +")
rep("(done ? '<span class=\"cc-done\">완료 ✓</span>' : '') +", "(done ? '<span class=\"cc-done\">Done ✓</span>' : '') +")
rep("'<div class=\"cal-empty\">이날은 수업이 없어요 🐣</div>'", "'<div class=\"cal-empty\">No classes on this day 🐣</div>'")
rep("""        '<span class="cd-main"><b>' + esc(k) + '</b> ' + (key === todayKey() ? '오늘 ' : '') + '할 일 모두 완료' +
        '<span class="cd-note">' + esc(doneEmoji(k)) + ' · ' + esc(claimed ? '용돈 ' + usd(1) + '도 받았어요' : '할 일을 모두 끝냈어요') + '</span></span>' +""",
"""        '<span class="cd-main"><b>' + esc(personLabel(k)) + '</b> · ' + (key === todayKey() ? 'today · ' : '') + 'All tasks done' +
        '<span class="cd-note">' + esc(doneEmoji(k)) + ' · ' + esc(claimed ? 'collected the ' + usd(1) + ' reward too' : 'finished every task') + '</span></span>' +""")
rep("'<div class=\"cal-empty\">이날은 용돈 기록이 없어요</div>'", "'<div class=\"cal-empty\">No allowance records on this day</div>'")
rep("'<span class=\"cm-who\">' + esc(m.kid) + ' · ' + esc(m.e.time || '') + '</span></span>' +",
    "'<span class=\"cm-who\">' + esc(personLabel(m.kid)) + ' · ' + esc(logTimeLabel(m.e.time) || '') + '</span></span>' +")
rep("'<span class=\"cm-meta\">' + esc(m.who || '가족') + (when ? ' · ' + esc(when) : '') + '</span></span>' +",
    "'<span class=\"cm-meta\">' + esc(personLabel(m.who || '가족')) + (when ? ' · ' + esc(when) : '') + '</span></span>' +")
rep("aria-label=\"이 메모 지우기\">×</button>", "aria-label=\"Delete this memo\">×</button>")
rep("'<div class=\"cal-empty\">아직 메모가 없어요. 이 날에 가족 메모를 남겨보세요 ✏️</div>'",
    "'<div class=\"cal-empty\">No memos yet. Leave a family memo for this day ✏️</div>'")
rep("'<div class=\"cal-bday-merged\">🎂 이날 생일 메모는 위 생일로 합쳐 보여요</div>'",
    "'<div class=\"cal-bday-merged\">🎂 The birthday note for this day is shown in the birthday above</div>'")
rep("if(!text){ toast('메모 내용을 적어주세요'); input.focus(); return; }",
    "if(!text){ toast('Please write the memo'); input.focus(); return; }")
rep("toast('메모를 남겼어요 📝');", "toast('Memo saved 📝');")
rep("toast('메모를 지웠어요');", "toast('Memo deleted');")

# ---------- photos ----------
rep("return Number(p[0]) + '년 ' + Number(p[1]) + '월';",
    "return monthName(Number(p[1]) - 1) + ' ' + Number(p[0]);")
rep("if(err) photos.error[m] = '불러오지 못했어요';", "if(err) photos.error[m] = 'Could not load';")
rep("if(err) toast('사진첩을 불러오지 못했어요. 잠시 뒤 다시 해볼게요');",
    "if(err) toast('Could not load the photos. I will try again in a moment');")
rep("""    sub.textContent = photos.loading[m]
      ? '불러오는 중…'
      : (photos.error[m]
        ? '불러오지 못했어요'
        : (list ? (list.length ? list.length + '장' : '아직 사진이 없어요') : ''));""",
"""    sub.textContent = photos.loading[m]
      ? 'Loading…'
      : (photos.error[m]
        ? 'Could not load'
        : (list ? (list.length ? list.length + (list.length === 1 ? ' photo' : ' photos') : 'No photos yet') : ''));""")
rep("'<div class=\"empty photo-empty\"><span class=\"em\">📷</span>사진을 불러오는 중이에요…</div>'",
    "'<div class=\"empty photo-empty\"><span class=\"em\">📷</span>Loading photos…</div>'")
rep("'<div class=\"empty photo-empty\"><span class=\"em\">😢</span>사진을 불러오지 못했어요.<br>' +",
    "'<div class=\"empty photo-empty\"><span class=\"em\">😢</span>Could not load the photos.<br>' +")
rep("'<button class=\"btn ghost sm photo-retry\" type=\"button\">다시 불러오기</button></div>';",
    "'<button class=\"btn ghost sm photo-retry\" type=\"button\">Try again</button></div>';")
rep("'<div class=\"empty photo-empty\"><span class=\"em\">📸</span>이 달에는 아직 사진이 없어요.<br>위에서 사진을 찍거나 앨범에서 골라보세요!</div>'",
    "'<div class=\"empty photo-empty\"><span class=\"em\">📸</span>No photos this month yet.<br>Take a photo or pick one from the album above!</div>'")
rep("""    var alt = p.who + ' 사진 ' + photoDateLabel(p.date) + (p.comment ? ' · ' + p.comment : '');
    return '<button class="photo-cell" type="button" data-photo="' + esc(p.id) + '" aria-label="' + esc(alt + ' 크게 보기') + '">' +""",
"""    var alt = personLabel(p.who) + ' photo ' + photoDateLabel(p.date) + (p.comment ? ' · ' + p.comment : '');
    return '<button class="photo-cell" type="button" data-photo="' + esc(p.id) + '" aria-label="' + esc(alt + ' — view larger') + '">' +""")
rep("        '<span class=\"ph-who\" data-who=\"' + esc(p.who) + '\">' + esc(p.who) + '</span>' +",
    "        '<span class=\"ph-who\" data-who=\"' + esc(p.who) + '\">' + esc(personLabel(p.who)) + '</span>' +")
rep("toast('이번 달이 마지막이에요');", "toast('This is the latest month');")
rep("toast('사진 파일(이미지)만 올릴 수 있어요');", "toast('You can only add image files');")
rep("toast('사진이 너무 커요. 25MB 이하 사진으로 해주세요');", "toast('That photo is too big. Please use one under 25MB');")
rep("toast('사진을 작게 줄이는 중이에요…');", "toast('Shrinking the photo…');")
rep("toast('사진을 읽지 못했어요. 다른 사진으로 해보세요');", "toast('Could not read that photo. Try another one');")
rep("""    return '<option value="' + esc(w) + '"' + (w === '가족' ? ' selected' : '') + '>' + esc(w) + '</option>';""",
"""    return '<option value="' + esc(w) + '"' + (w === '가족' ? ' selected' : '') + '>' + esc(personLabel(w)) + '</option>';""")
rep("'<h2>📸 사진 올리기</h2>' +", "'<h2>📸 Add a Photo</h2>' +")
rep("'<p class=\"modal-sub\">사진은 긴 변 ' + PHOTO_MAX_EDGE + 'px로 줄여서 그 달 사진첩에만 따로 올라가요. (할 일·채팅 데이터는 그대로예요)</p>' +",
    "'<p class=\"modal-sub\">Photos are shrunk to ' + PHOTO_MAX_EDGE + 'px on the long side and saved for that month. Everyone in the family can see them. (To-dos and chat are not touched.)</p>' +")
rep("alt=\"올릴 사진 미리보기\">", "alt=\"Photo preview\">")
rep("<label for=\"photoDate\">날짜</label>", "<label for=\"photoDate\">Date</label>")
rep("<label for=\"photoWho\">대상</label>", "<label for=\"photoWho\">Who is it for?</label>")
rep("<label for=\"photoComment\">한 줄 코멘트 (선택)</label>", "<label for=\"photoComment\">One-line note (optional)</label>")
rep("placeholder=\"예: 첫눈 온 날\"", "placeholder=\"e.g. the first snow\"")
rep("data-modal-close>취소</button>", "data-modal-close>Cancel</button>", 1)
rep("data-photo-save>올리기</button>", "data-photo-save>Add photo</button>")
rep("if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(dateStr)){ toast('사진 날짜를 골라주세요'); return; }",
    "if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(dateStr)){ toast('Please pick the photo date'); return; }")
rep("if(dateStr > todayKey()){ toast('아직 오지 않은 날짜는 고를 수 없어요'); return; }",
    "if(dateStr > todayKey()){ toast('You cannot pick a date that has not come yet'); return; }")
rep("saveBtn.textContent = '올리는 중…';", "saveBtn.textContent = 'Adding…';")
rep("saveBtn.textContent = '올리기';", "saveBtn.textContent = 'Add photo';")
rep("toast('사진을 올리지 못했어요. 인터넷 연결을 확인해 주세요');", "toast('Could not add the photo. Please check the internet connection');")
rep("toast('사진을 사진첩에 올렸어요 📸');", "toast('Photo added — the whole family can see it 📸');")
rep("aria-label=\"사진 크게 보기\">", "aria-label=\"View photo larger\">")
rep("data-pl-close aria-label=\"닫기\">✕</button>", "data-pl-close aria-label=\"Close\">✕</button>")
rep("esc(p.who + ' 사진 ' + photoDateLabel(p.date))", "esc(personLabel(p.who) + ' photo ' + photoDateLabel(p.date))")
rep("esc(photoDateLabel(p.date)) + ' · ' + esc(p.who) + '</span>'", "esc(photoDateLabel(p.date)) + ' · ' + esc(personLabel(p.who)) + '</span>'")
rep("'<span class=\"pl-meta\">' + esc(p.who) + ' · 올린 사람 ' + esc(p.by || '가족') + ' · ' + esc(photoDateLabel(p.date)) + '</span>' +",
    "'<span class=\"pl-meta\">' + esc(personLabel(p.who)) + ' · added by ' + esc(personLabel(p.by || '가족')) + ' · ' + esc(photoDateLabel(p.date)) + '</span>' +")
rep("data-pl-del>🗑️ 지우기</button>", "data-pl-del>🗑️ Delete</button>")
rep("'<p>이 사진을 지울까요?<br><span class=\"small muted\">지우면 가족 모두의 사진첩에서 사라져요.</span></p>' +",
    "'<p>Delete this photo?<br><span class=\"small muted\">It disappears from everyone\\'s photos too.</span></p>' +")
rep("data-pl-cancel>취소</button>", "data-pl-cancel>Cancel</button>")
rep("data-pl-ok>지우기</button>", "data-pl-ok>Delete</button>")
rep("ok.textContent = '지우는 중…';", "ok.textContent = 'Deleting…';")
rep("ok.textContent = '지우기';", "ok.textContent = 'Delete';")
rep("toast('사진을 지우지 못했어요. 잠시 뒤 다시 해주세요');", "toast('Could not delete the photo. Please try again in a moment');")
rep("toast('사진을 지웠어요');", "toast('Photo deleted');")
rep("toast('지우는 건 엄마나 올린 사람만 할 수 있어요 🔒');", "toast('Only Mom or the person who added it can delete it 🔒');")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step10 ok')
