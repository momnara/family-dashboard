#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 2: Allowance / Photos / Calendar markup -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:90]))
    text = text.replace(old, new)

# ---------- allowance ----------
rep('<!-- ============ 1. 용돈 ============ -->', '<!-- ============ 1. Allowance ============ -->')
rep('<section class="panel" id="panel-allowance" aria-label="공부 용돈 적립과 용돈기입장">',
    '<section class="panel" id="panel-allowance" aria-label="Allowance, rewards and spending log">')
rep('role="group" aria-label="아이 선택"></div>', 'role="group" aria-label="Choose a kid"></div>')
rep('<p class="label">지금 모은 돈</p>', '<p class="label">Saved so far</p>')
rep('<span class="chip">시작 금액 <b id="chipStart">$0.00</b></span>',
    '<span class="chip">Starting balance <b id="chipStart">$0.00</b></span>')
rep('<span class="chip">공부·숙제 적립 <b id="chipStudy" class="plus">+$0.00</b></span>',
    '<span class="chip">Task rewards <b id="chipStudy" class="plus">+$0.00</b></span>')
rep('<span class="chip">입금 <b id="chipDep" class="plus">+$0.00</b></span>',
    '<span class="chip">Added <b id="chipDep" class="plus">+$0.00</b></span>')
rep('<span class="chip">사용 <b id="chipSpend" class="minus">-$0.00</b></span>',
    '<span class="chip">Spent <b id="chipSpend" class="minus">-$0.00</b></span>')
rep('<label for="allowStart">시작 금액 ($)</label>', '<label for="allowStart">Starting balance ($)</label>')
rep('placeholder="0" aria-label="시작 금액(달러)" aria-describedby="allowStartHint">',
    'placeholder="0" aria-label="Starting balance in dollars" aria-describedby="allowStartHint">')
rep('<button class="mini-btn" id="allowStartSave" type="button">저장</button>',
    '<button class="mini-btn" id="allowStartSave" type="button">Save</button>')
rep('<p class="field-hint" id="allowStartHint">지금 시작 금액은 <b>$0.00</b>이에요. 새 금액을 넣고 저장을 눌러 주세요.</p>',
    '<p class="field-hint" id="allowStartHint">Starting balance is <b>$0.00</b>. Type a new amount and tap Save.</p>')
rep('<span>공부 1회 적립</span>', '<span>Reward per task day</span>')
rep('role="group" aria-label="공부 1회 적립 금액">', 'role="group" aria-label="Reward per task day amount">')
rep('aria-label="공부 1회에 $1.00 적립">$1.00</button>', 'aria-label="Earn $1.00 per task day">$1.00</button>')
rep('<span class="coin" aria-hidden="true">🪙</span>공부 완료! <b id="studyRewardLabel">+$1.00</b></button>',
    '<span class="coin" aria-hidden="true">🪙</span>All done today? <b id="studyRewardLabel">+$1.00</b></button>')
rep('<p class="today-line" id="todayLine">오늘 공부 0번 · $0.00 적립했어요</p>',
    '<p class="today-line" id="todayLine">Today: 0 rewards · $0.00</p>')
rep('<span class="h2-emoji" aria-hidden="true">💸</span>입금 / 사용</h2>',
    '<span class="h2-emoji" aria-hidden="true">💸</span>Add / Spend</h2>')
rep('<label for="quickAmount">금액 ($)</label>', '<label for="quickAmount">Amount ($)</label>')
rep('placeholder="예: 5.00">', 'placeholder="e.g. 5.00">')
rep('<label for="quickMemo">메모 (선택)</label>', '<label for="quickMemo">Note (optional)</label>')
rep('placeholder="예: 할머니 용돈, 문구점" maxlength="30">', 'placeholder="e.g. gift from Grandma, stationery" maxlength="30">')
rep('<button class="btn mint" id="quickDeposit" type="button">＋ 입금</button>',
    '<button class="btn mint" id="quickDeposit" type="button">+ Add</button>')
rep('<button class="btn pink" id="quickSpend" type="button">－ 사용</button>',
    '<button class="btn pink" id="quickSpend" type="button">− Spend</button>')
rep('<span class="h2-emoji" aria-hidden="true">📒</span>용돈·적립 내역</h2>',
    '<span class="h2-emoji" aria-hidden="true">📒</span>Allowance History</h2>')
rep('<p class="card-sub">할 일 완료 적립, 입금, 사용 내역이 날짜별로 최신순으로 보여요.</p>',
    '<p class="card-sub">Task rewards, money added and money spent — newest first, grouped by day.</p>')

# ---------- photos markup ----------
rep('<!-- ============ 📸 사진첩 ============ -->', '<!-- ============ 📸 Photos ============ -->')
rep('<section class="panel" id="panel-photos" aria-label="가족 사진첩">',
    '<section class="panel" id="panel-photos" aria-label="Family photos">')
rep('<span class="h2-emoji" aria-hidden="true">📸</span>우리 가족 사진첩</h2>',
    '<span class="h2-emoji" aria-hidden="true">📸</span>Our Family Photos</h2>')
rep('<p class="card-sub">사진은 자동으로 작게 줄여서 달마다 따로 보관해요. 찍은 날짜와 대상, 한 줄 코멘트를 남겨보세요.</p>',
    '<p class="card-sub">Photos are shrunk automatically and kept month by month. Add the date, who it is for, and a short note. Everyone in the family sees all photos.</p>')
rep('<span aria-hidden="true">📸</span> 사진 찍기</button>', '<span aria-hidden="true">📸</span> Take a photo</button>')
rep('<span aria-hidden="true">🖼️</span> 앨범에서 고르기</button>', '<span aria-hidden="true">🖼️</span> Choose from album</button>')
rep('capture="environment" aria-label="카메라로 사진 찍기">', 'capture="environment" aria-label="Take a photo with the camera">')
rep('aria-label="앨범에서 사진 고르기">', 'aria-label="Choose a photo from the album">')
rep('aria-label="이전 달 보기">◀</button>', 'aria-label="Previous month">◀</button>')
rep('aria-label="다음 달 보기">▶</button>', 'aria-label="Next month">▶</button>')
rep('<b id="photoMonthTitle">오늘</b>', '<b id="photoMonthTitle">Today</b>')
rep('<span id="photoMonthSub">사진을 불러오는 중…</span>', '<span id="photoMonthSub">Loading photos…</span>')

# ---------- calendar markup ----------
rep('<!-- ============ 2. 가족 달력 ============ -->', '<!-- ============ 2. Family calendar ============ -->')
rep('<section class="panel active" id="panel-calendar" aria-label="가족 달력">',
    '<section class="panel active" id="panel-calendar" aria-label="Family calendar">')
rep('aria-label="이전 달">◀</button>', 'aria-label="Previous month">◀</button>')
rep('aria-label="다음 달">▶</button>', 'aria-label="Next month">▶</button>')
rep('<b id="calTitle">오늘</b>', '<b id="calTitle">Today</b>')
rep('<span id="calSub">수업 · 생일 · 용돈 · 가족 메모를 한눈에</span>',
    '<span id="calSub">Classes, birthdays, allowance and memos at a glance</span>')
rep('<button class="cal-today" id="calTodayBtn" type="button">오늘</button>',
    '<button class="cal-today" id="calTodayBtn" type="button">Today</button>')
rep('<span>일</span><span>월</span><span>화</span><span>수</span><span>목</span><span>금</span><span>토</span>',
    '<span>Sun</span><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span>')
rep('role="grid" aria-label="월간 달력"></div>', 'role="grid" aria-label="Monthly calendar"></div>')
rep('<span><i class="cc-dot s"></i>Stella 수업</span>', "<span><i class=\"cc-dot s\"></i>Stella's class</span>")
rep('<span><i class="cc-dot l"></i>Luna 수업</span>', "<span><i class=\"cc-dot l\"></i>Luna's class</span>")
rep('<span><span class="cc-cake-key" aria-hidden="true">🎂</span>생일·생신</span>',
    '<span><span class="cc-cake-key" aria-hidden="true">🎂</span>Birthday</span>')
rep('<span><span class="cc-cake-key" aria-hidden="true">🕊️</span><span class="cc-cake-key" aria-hidden="true">🕯️</span>기일·제사</span>',
    '<span><span class="cc-cake-key" aria-hidden="true">🕊️</span><span class="cc-cake-key" aria-hidden="true">🕯️</span>Memorial</span>')
rep('<span><i class="cc-dot m"></i>용돈 기록</span>', '<span><i class="cc-dot m"></i>Allowance</span>')
rep('<span><i class="cc-dot e"></i>가족 메모</span>', '<span><i class="cc-dot e"></i>Family memo</span>')
rep('<span><span class="cc-name-tag s">Stella</span> <span class="cc-name-tag l">Luna</span> 할 일 모두 완료</span>',
    '<span><span class="cc-name-tag s">Stella</span> <span class="cc-name-tag l">Luna</span> All tasks done</span>')
rep('<span id="calSelTitle">오늘</span></h2>', '<span id="calSelTitle">Today</span></h2>')
rep('<span class="cal-tag" id="calSelTag" hidden>오늘</span>', '<span class="cal-tag" id="calSelTag" hidden>Today</span>')
rep('<h3><span aria-hidden="true">🎒</span>오늘 수업</h3>', '<h3><span aria-hidden="true">🎒</span>Classes</h3>')
rep('<h3><span aria-hidden="true">✅</span>이날 할 일 모두 완료</h3>',
    '<h3><span aria-hidden="true">✅</span>All Tasks Done</h3>')
rep('<h3><span aria-hidden="true">🪙</span>오늘 용돈기록</h3>', '<h3><span aria-hidden="true">🪙</span>Allowance</h3>')
rep('<h3><span aria-hidden="true">📝</span>가족 메모</h3>', '<h3><span aria-hidden="true">📝</span>Family Memo</h3>')
rep('<label class="sr-only" for="calMemoInput">가족 메모</label>',
    '<label class="sr-only" for="calMemoInput">Family memo</label>')
rep('placeholder="가족 메모를 적어주세요" autocomplete="off">', 'placeholder="Write a family memo" autocomplete="off">')
rep('<button class="btn primary sm" type="submit">추가</button>', '<button class="btn primary sm" type="submit">Add</button>', 2)

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step2 ok')
