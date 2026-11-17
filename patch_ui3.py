#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 3: To-Do / Weekly schedule / Chat / Timer markup -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:90]))
    text = text.replace(old, new)

# ---------- to-do ----------
rep('<!-- ============ 3. 할 일 ============ -->', '<!-- ============ 3. To-do ============ -->')
rep('<section class="panel" id="panel-todo" aria-label="할 일 체크">',
    '<section class="panel" id="panel-todo" aria-label="To-do list">')
rep('<span class="h2-emoji" aria-hidden="true">✅</span>할 일 체크</h2>',
    '<span class="h2-emoji" aria-hidden="true">✅</span>To-Do</h2>')
rep('<p class="card-sub">한 아이의 오늘 할 일을 <b>모두</b> 끝내면 용돈 +$1.00 (하루 한 번) · 다 끝내면 하이파이브 🙌</p>',
    '<p class="card-sub">Finish <b>all</b> of a kid\'s tasks today for +$1.00 (once a day) · finish everything for a high five 🙌</p>')
rep('role="group" aria-label="요일별 할 일 미리 보기">', 'role="group" aria-label="Preview tasks by day">')
rep('role="group" aria-label="사람별로 보기">', 'role="group" aria-label="Filter by person">')
rep('<button class="btn ghost sm" id="todoDailyReset" type="button">🔄 오늘 체크 초기화</button>',
    '<button class="btn ghost sm" id="todoDailyReset" type="button">🔄 Reset today\'s checks</button>')
rep('<span class="small muted">새로운 하루를 시작할 때 눌러요</span>',
    '<span class="small muted">Tap when a new day begins</span>')

# ---------- weekly schedule ----------
rep('<span class="h2-emoji" aria-hidden="true">🗓️</span>주간 스케줄</h2>',
    '<span class="h2-emoji" aria-hidden="true">🗓️</span>Weekly Schedule</h2>')
rep('<p class="card-sub">이번 주 수업과 가족 일정을 한눈에 봐요. 오늘 수업은 위에 모아 보여주고, 수업을 누르면 지울 수 있어요. 휴강한 수업은 회색 <b>휴강</b>으로 표시돼요.</p>',
    '<p class="card-sub">This week\'s classes and family plans at a glance. Today\'s classes are gathered at the top — tap one to remove it. A skipped class shows as a grey <b>Skipped</b>.</p>')
rep('<label class="sr-only" for="lessonKid">누구 수업</label>', '<label class="sr-only" for="lessonKid">Whose class</label>')
rep('id="lessonKid" aria-label="누구 수업">', 'id="lessonKid" aria-label="Whose class">')
rep('<label class="sr-only" for="lessonDay">무슨 요일</label>', '<label class="sr-only" for="lessonDay">Which day</label>')
rep('id="lessonDay" aria-label="무슨 요일">', 'id="lessonDay" aria-label="Which day">')
rep('<label class="sr-only" for="lessonTime">몇 시</label>', '<label class="sr-only" for="lessonTime">What time</label>')
rep('aria-label="몇 시 수업">', 'aria-label="What time the class starts">')
rep('<label class="sr-only" for="lessonSubject">과목</label>', '<label class="sr-only" for="lessonSubject">Subject</label>')
rep('placeholder="과목 (예: 영어)" maxlength="12"', 'placeholder="Subject (e.g. English)" maxlength="12"')

# ---------- chat ----------
rep('<section class="panel" id="panel-chat" aria-label="가족 채팅방">',
    '<section class="panel" id="panel-chat" aria-label="Family chat">')
rep('<h2>🐣 우리 가족 채팅</h2>', '<h2>🐣 Family Chat</h2>')
rep('<span class="online">다 같이</span>', '<span class="online">Everyone</span>')
rep('title="가족 채팅 알림 설정">🔔 알림 받기</button>', 'title="Family chat notification settings">🔔 Notifications</button>')
rep('role="group" aria-label="지금 사용하는 사람">', 'role="group" aria-label="Who is using this device">')
rep('<span class="small muted" id="chatLockState">프로필을 골라주세요</span>',
    '<span class="small muted" id="chatLockState">Choose a profile</span>')
rep('              이 기기 잠금\n', '              Lock this device\n')
rep('aria-label="스티커 고르기">😊</button>', 'aria-label="Choose a sticker">😊</button>')
rep('<label class="sr-only" for="chatInput">메시지</label>', '<label class="sr-only" for="chatInput">Message</label>')
rep('placeholder="메시지를 입력해요" maxlength="200"', 'placeholder="Type a message" maxlength="200"')
rep('aria-label="음성 메시지 녹음">🎙️</button>', 'aria-label="Record a voice message">🎙️</button>')
rep('aria-label="보내기">➤</button>', 'aria-label="Send">➤</button>')
rep('<span>녹음 중… 다시 누르면 보내요</span>', '<span>Recording… tap again to send</span>')
rep('<p class="chat-note" id="chatNote">가족이 함께 봐요 · 마이크는 허락한 순간에만 켜져요</p>',
    '<p class="chat-note" id="chatNote">Everyone in the family sees this · the mic only turns on when you allow it</p>')

# ---------- timer ----------
rep('<!-- ============ 6. 타이머 ============ -->', '<!-- ============ 6. Timer ============ -->')
rep('<section class="panel" id="panel-timer" aria-label="공부 타이머와 태블릿 알람">',
    '<section class="panel" id="panel-timer" aria-label="Study timer and tablet alarm">')
rep('<h2 style="justify-content:center">⏳ 공부 타이머</h2>', '<h2 style="justify-content:center">⏳ Study Timer</h2>')
rep('<div class="timer-state" id="timerState">준비됐어요</div>', '<div class="timer-state" id="timerState">Ready</div>')
rep('role="group" aria-label="시간 고르기">', 'role="group" aria-label="Pick a time">')
rep('data-min="15">15분</button>', 'data-min="15">15 min</button>')
rep('data-min="20">20분</button>', 'data-min="20">20 min</button>')
rep('data-min="25">25분</button>', 'data-min="25">25 min</button>')
rep('data-min="30">30분</button>', 'data-min="30">30 min</button>')
rep('data-min="50">50분</button>', 'data-min="50">50 min</button>')
rep('<span>직접</span>', '<span>Custom</span>')
rep('placeholder="분"><span class="unit">분</span>', 'placeholder="min"><span class="unit">min</span>')
rep('<button class="btn sm ghost" id="timerCustomApply" type="button">적용</button>',
    '<button class="btn sm ghost" id="timerCustomApply" type="button">Set</button>')
rep('<button class="btn primary" id="timerStartBtn" type="button">시작</button>',
    '<button class="btn primary" id="timerStartBtn" type="button">Start</button>')
rep('<button class="btn ghost" id="timerResetBtn" type="button">리셋</button>',
    '<button class="btn ghost" id="timerResetBtn" type="button">Reset</button>')
rep('<span class="h2-emoji" aria-hidden="true">🌙</span>태블릿 끄는 알람</h2>',
    '<span class="h2-emoji" aria-hidden="true">🌙</span>Tablet Wind-Down Alarm</h2>')
rep('<span id="alarmToggleLabel">꺼짐</span>', '<span id="alarmToggleLabel">Off</span>')
rep('<p class="card-sub" style="margin-top:6px">정한 시간에 다 같이 쓰는 태블릿을 잠깐 쉬게 해요. 화면을 켜두면 종이 울려요.</p>',
    '<p class="card-sub" style="margin-top:6px">At the time you set, the family tablet takes a short break. Keep this screen open to hear the chime.</p>')
rep('role="group" aria-label="알람 방식">', 'role="group" aria-label="Alarm mode">')
rep('<button type="button" data-mode="clock" class="active">시각 맞추기</button>',
    '<button type="button" data-mode="clock" class="active">Set a time</button>')
rep('<button type="button" data-mode="countdown">몇 분 뒤</button>',
    '<button type="button" data-mode="countdown">In a few minutes</button>')
rep('<span>울리는 시각</span>', '<span>Ring at</span>')
rep('value="21:00" aria-label="알람 시각">', 'value="21:00" aria-label="Alarm time">')
rep('<span>지금부터 몇 분 뒤</span>', '<span>Minutes from now</span>')
rep('inputmode="numeric" aria-label="몇 분 뒤">', 'inputmode="numeric" aria-label="Minutes from now">')
rep('<div class="alarm-status" id="alarmStatus">🌙 알람이 꺼져 있어요</div>',
    '<div class="alarm-status" id="alarmStatus">🌙 Alarm is off</div>')
rep('<button class="btn ghost sm" id="alarmTestBtn" type="button">🔔 소리 미리 듣기</button>',
    '<button class="btn ghost sm" id="alarmTestBtn" type="button">🔔 Preview the sound</button>')
rep('<button class="btn ghost sm" id="alarmPreviewBtn" type="button">🌛 화면 미리 보기</button>',
    '<button class="btn ghost sm" id="alarmPreviewBtn" type="button">🌛 Preview the screen</button>')
rep('<p class="small muted" style="text-align:center;margin-top:14px">만든 날: 2026년 11월 · 우리 집 전용 💛</p>',
    '<p class="small muted" style="text-align:center;margin-top:14px">Made in November 2026 · just for our family 💛</p>')

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step3 ok')
