#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 9: timer, sleep alarm, settings -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

# ---------- timer finished modal ----------
rep("'<h2 style=\"justify-content:center\">공부 끝! 잘했어요 🎉</h2>' +",
    "'<h2 style=\"justify-content:center\">Time\\'s up — great job! 🎉</h2>' +")
rep("'<p class=\"modal-sub\" style=\"text-align:center\">' + minutes + '분 동안 정말 집중했어요.<br>눈도 쉬어주고, 물 한 컵 마셔요!</p>' +",
    "'<p class=\"modal-sub\" style=\"text-align:center\">You focused for ' + minutes + ' minutes.<br>Rest your eyes and drink a glass of water!</p>' +")
rep("data-modal-close>좋아요</button>", "data-modal-close>Nice</button>")
rep("if(timer.running) st.textContent = '공부 중 ✏️';", "if(timer.running) st.textContent = 'Studying ✏️';")
rep("else if(timer.remaining <= 0) st.textContent = '다 했어요! 🎉';", "else if(timer.remaining <= 0) st.textContent = 'All done! 🎉';")
rep("else if(timer.remaining < timer.total) st.textContent = '잠깐 멈췄어요';", "else if(timer.remaining < timer.total) st.textContent = 'Paused';")
rep("else st.textContent = '준비됐어요';", "else st.textContent = 'Ready';")
rep("startBtn.textContent = timer.running ? '일시정지' : (timer.remaining < timer.total && timer.remaining > 0 ? '계속하기' : '시작');",
    "startBtn.textContent = timer.running ? 'Pause' : (timer.remaining < timer.total && timer.remaining > 0 ? 'Resume' : 'Start');")

# ---------- sleep screen ----------
rep("aria-label=\"잠자는 달\">", "aria-label=\"sleeping moon\">")
rep("wrap.setAttribute('aria-label', '태블릿 쉬는 시간');", "wrap.setAttribute('aria-label', 'Tablet break time');")
rep("'<h2>태블릿 쉬는 시간이에요! 🌙</h2>' +", "'<h2>Time for the tablet to rest! 🌙</h2>' +")
rep("'<p>오늘도 많이 했어요. 이제 화면을 잠깐 덮고<br>가족과 이야기해볼까요?</p>' +",
    "'<p>You did a lot today. Let\\'s put the screen down for a bit<br>and talk with the family.</p>' +")
rep("'<button class=\"btn\" type=\"button\" id=\"sleepClose\">알겠어요</button>' +",
    "'<button class=\"btn\" type=\"button\" id=\"sleepClose\">Okay</button>' +")
rep("'<p class=\"sleep-small\">소리를 끄려면 알겠어요를 눌러주세요</p>';",
    "'<p class=\"sleep-small\">Tap Okay to stop the sound</p>';")

# ---------- alarm ----------
rep("if(dk === todayKey()) return '오늘 ' + hm(d);", "if(dk === todayKey()) return 'Today ' + hm(d);")
rep("if(dk === dateKey(daysAgo(-1))) return '내일 ' + hm(d);", "if(dk === dateKey(daysAgo(-1))) return 'Tomorrow ' + hm(d);")
rep("if(lab) lab.textContent = a.on ? '켜짐' : '꺼짐';", "if(lab) lab.textContent = a.on ? 'On' : 'Off';")
rep("status.textContent = '🌙 알람이 꺼져 있어요';", "status.textContent = '🌙 Alarm is off';")
rep("status.textContent = '⏰ ' + alarmTargetText(a.targetTs || nextClockTs(a.time)) + '에 알려드릴게요';",
    "status.textContent = '⏰ I will chime at ' + alarmTargetText(a.targetTs || nextClockTs(a.time));")
rep("status.textContent = '⏳ ' + Math.max(1, Math.ceil(left / 60000)) + '분 뒤(' + alarmTargetText(a.targetTs || Date.now()) + ')에 알려드릴게요';",
    "status.textContent = '⏳ Chimes in ' + Math.max(1, Math.ceil(left / 60000)) + ' min (' + alarmTargetText(a.targetTs || Date.now()) + ')';")
rep("""  toast(a.mode === 'clock'
    ? alarmTargetText(a.targetTs) + '에 태블릿 알람을 맞췄어요 🌙'
    : '지금부터 ' + Math.round((a.targetTs - Date.now()) / 60000) + '분 뒤에 알려드릴게요 🌙');""",
"""  toast(a.mode === 'clock'
    ? 'Tablet alarm set for ' + alarmTargetText(a.targetTs) + ' 🌙'
    : 'I will chime in ' + Math.round((a.targetTs - Date.now()) / 60000) + ' minutes 🌙');""")
rep("toast('태블릿 알람을 껐어요');", "toast('Tablet alarm turned off');")
rep("status.textContent = '⏳ ' + Math.max(1, Math.ceil(left / 60000)) + '분 뒤(' + alarmTargetText(a.targetTs) + ')에 알려드릴게요';",
    "status.textContent = '⏳ Chimes in ' + Math.max(1, Math.ceil(left / 60000)) + ' min (' + alarmTargetText(a.targetTs) + ')';")

# ---------- settings ----------
rep("var where = sync.mode === 'live' ? '가족 모두 + 이 기기' : '이 기기 브라우저';",
    "var where = sync.mode === 'live' ? 'The whole family + this device' : 'This device\\'s browser';")
rep("'<h2>⚙️ 설정</h2>' +", "'<h2>⚙️ Settings</h2>' +")
rep("'<h3>실시간 동기화</h3>' +", "'<h3>Live Sync</h3>' +")
rep("'<p>같은 주소를 쓰는 폰과 태블릿이 용돈·할 일·달력·도장·채팅을 함께 봐요. 인터넷이 잠깐 끊겨도 이 기기에 저장했다가 다시 연결되면 맞춰요.</p>' +",
    "'<p>Phones and tablets on the same address share the allowance, to-dos, calendar, photos and chat. If the internet drops for a moment, changes are saved on this device and catch up when it reconnects.</p>' +")
rep("'<div class=\"kv\"><span>지금 상태</span><b id=\"syncStateLine\">'",
    "'<div class=\"kv\"><span>Status</span><b id=\"syncStateLine\">'")
rep("placeholder=\"https://내-프로젝트.firebaseio.com\"", "placeholder=\"https://my-project.firebaseio.com\"")
rep(">기본 주소</button>", ">Default address</button>")
rep(">이 기기만</button>", ">This device only</button>")
rep("id=\"fbSave\">연결</button>", "id=\"fbSave\">Connect</button>")
rep("'<p class=\"small muted\" style=\"margin-top:9px\">🔒 \\'이 기기 잠금\\'과 내 프로필은 이 기기에만 저장돼요. 다른 기기와 섞이지 않아요.</p>' +",
    "'<p class=\"small muted\" style=\"margin-top:9px\">🔒 \\'Lock this device\\' and your own profile are saved on this device only. They never mix with other devices.</p>' +")
rep("'<h3>내 기록</h3>' +", "'<h3>My Records</h3>' +")
rep("'<div class=\"kv\"><span>저장 위치</span><b>'", "'<div class=\"kv\"><span>Saved in</span><b>'")
rep("'<div class=\"kv\"><span>용돈 기록</span><b>' + logCount + '개</b></div>' +",
    "'<div class=\"kv\"><span>Allowance records</span><b>' + logCount + '</b></div>' +")
rep("'<div class=\"kv\"><span>채팅 메시지</span><b>' + msgCount + '개</b></div>' +",
    "'<div class=\"kv\"><span>Chat messages</span><b>' + msgCount + '</b></div>' +")
rep("'<div class=\"kv\"><span>쓰는 공간</span><b>약 ' + bytesLabel(storageBytes()) + '</b></div>' +",
    "'<div class=\"kv\"><span>Space used</span><b>about ' + bytesLabel(storageBytes()) + '</b></div>' +")
rep("id=\"exportBtn\">📤 내보내기</button>", "id=\"exportBtn\">📤 Export</button>")
rep("id=\"resetBtn\">처음으로</button>", "id=\"resetBtn\">Start over</button>")
rep("'<p class=\"small muted\" style=\"text-align:center;margin-top:4px\">우리 가족 대시보드 · 실시간 동기화 1.1 버전</p>' +",
    "'<p class=\"small muted\" style=\"text-align:center;margin-top:4px\">Our Family Dashboard · live sync v1.1</p>' +")
rep("toast('주소를 적어주세요. 이 기기에만 저장하려면 \\'이 기기만\\'을 눌러요');",
    "toast('Please type the address. To keep everything on this device, tap \\'This device only\\'');")
rep("toast('주소는 https:// 로 시작해야 해요');", "toast('The address must start with https://');")
rep("toast('실시간 동기화를 시작할게요');", "toast('Starting live sync');")
rep("toast('우리 가족 주소로 연결할게요');", "toast('Connecting to our family address');")
rep("toast('이제 이 기기에만 저장해요');", "toast('Now saving on this device only');")
rep("a.download = '우리-가족-대시보드-백업.json';", "a.download = 'family-dashboard-backup.json';")
rep("toast('백업 파일을 내려받았어요');", "toast('Backup file downloaded');")
rep("}catch(e){ toast('내보내기를 할 수 없어요'); }", "}catch(e){ toast('Could not export'); }")
rep("confirmModal('처음 데이터로 돌아갈까요?', '용돈 기록, 도장, 채팅이 모두 지워지고 처음 예시 데이터로 돌아가요. 같이 쓰는 기기에서도 똑같이 바뀌어요.', '처음으로', function(){",
    "confirmModal('Start over with fresh data?', 'Allowance records, stamps and chat will all be cleared and the starter data comes back. Shared devices change the same way.', 'Start over', function(){")
rep("toast('처음 데이터로 돌아갔어요');", "toast('Back to the starter data');")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step9 ok')
