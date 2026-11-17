#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 8: chat who pills, chat list, notifications modal, voice -> English."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

# ---------- who pills + lock state ----------
rep("      mascot(p) + esc(p) + '</button>';", "      mascot(p) + esc(personLabel(p)) + '</button>';")
rep("""  $('#chatLockState').textContent = locked
    ? (me + '로 사용 중이에요 🔒')
    : '지금은 ' + me + '(으)로 말해요';""",
"""  $('#chatLockState').textContent = locked
    ? ('Locked as ' + personLabel(me) + ' 🔒')
    : ('Using ' + personLabel(me));""")

# ---------- chat list ----------
rep("box.innerHTML = '<div class=\"empty\"><span class=\"em\">🐥</span>아직 대화가 없어요.<br>첫 메시지를 남겨보세요!</div>';",
    "box.innerHTML = '<div class=\"empty\"><span class=\"em\">🐥</span>No messages yet.<br>Say something to start!</div>';")
rep("aria-label=\"음성 메시지 재생\">▶</button>", "aria-label=\"Play voice message\">▶</button>")
rep("esc(m.who) + '</span>' +", "esc(personLabel(m.who)) + '</span>' +")
rep("data-heart=\"' + esc(m.id) + '\" aria-label=\"하트 반응\"", "data-heart=\"' + esc(m.id) + '\" aria-label=\"Add a heart\"")
rep("aria-label=\"이 메시지 지우기\" title=\"이 메시지 지우기\">×</button>", "aria-label=\"Delete this message\" title=\"Delete this message\">×</button>")

# ---------- ntfy ----------
rep("title: String(o.title || '💬 가족 채팅').slice(0, 120),", "title: String(o.title || '💬 Family Chat').slice(0, 120),")
rep("  var who = msg.who || '가족';", "  var who = personLabel(msg.who || '가족');")
rep("message:'스티커를 보냈어요!'", "message:'sent a sticker!'")
rep("message:'음성 메시지를 보냈어요! (' + String(msg.dur || '0:00') + ')'", "message:'sent a voice message (' + String(msg.dur || '0:00') + ')'")
rep("b.title = on ? '가족 채팅 알림 켜짐 · 눌러서 설정' : '가족 채팅 알림 꺼짐 · 눌러서 설정';",
    "b.title = on ? 'Family chat notifications are on · tap for settings' : 'Family chat notifications are off · tap for settings';")
rep("b.title = me + '(으)로 잠긴 기기예요';", "b.title = 'This device is locked as ' + personLabel(me);")

# ---------- notifications modal ----------
rep("'<h2>🔔 가족 채팅 알림</h2>' +", "'<h2>🔔 Family Chat Notifications</h2>' +")
rep("'<p class=\"modal-sub\">가족이 채팅을 보내면 아이폰·아이패드 알림창에 바로 떠요. 무료 ntfy 앱을 쓰고, 가입은 필요 없어요.</p>' +",
    "'<p class=\"modal-sub\">When someone in the family sends a chat, it pops up right on the iPhone and iPad. It uses the free ntfy app — no sign-up needed.</p>' +")
rep("(on ? '🔔 알림 켜짐' : '🔕 알림 꺼짐') + '</div>' +", "(on ? '🔔 Notifications on' : '🔕 Notifications off') + '</div>' +")
rep("<span>가족 채팅 알림 보내기</span></label>", "<span>Send family chat notifications</span></label>")
rep("'<h3>우리 가족 토픽</h3>' +", "'<h3>Our Family Topic</h3>' +")
rep("'<p>이 이름을 아는 기기만 알림을 받아요. 가족끼리만 나눠주세요.</p>' +",
    "'<p>Only devices that know this name get the notifications. Keep it just for the family.</p>' +")
rep("id=\"topicCopy\">토픽 복사</button>", "id=\"topicCopy\">Copy topic</button>")
rep("'<h3>알림 받는 방법</h3>' +", "'<h3>How to Get Notifications</h3>' +")
rep("'<li>App Store에서 <b>ntfy</b> 무료 앱 설치</li>' +", "'<li>Install the free <b>ntfy</b> app from the App Store</li>' +")
rep("'<li>앱 열고 <b>+</b> 눌러서 위 토픽 이름 입력해 구독</li>' +",
    "'<li>Open the app, tap <b>+</b>, and subscribe with the topic name above</li>' +")
rep("'<li>이제 가족 채팅이 오면 아이폰·아이패드 알림창에 바로 떠요!</li>' +",
    "'<li>Now family chat messages pop up on the iPhone and iPad right away!</li>' +")
rep("'<p class=\"howto-tip\">알림이 안 보이면 아이폰 설정 → ntfy → 알림을 ‘허용’으로 바꿔주세요.</p>' +",
    "'<p class=\"howto-tip\">If notifications do not show up, go to iPhone Settings → ntfy → Notifications and allow them.</p>' +")
rep("id=\"notifTest\">테스트 알림 보내기</button>", "id=\"notifTest\">Send a test notification</button>")
rep("data-modal-close>닫기</button>", "data-modal-close>Close</button>", 2)
rep("stateBox.textContent = nowOn ? '🔔 알림 켜짐' : '🔕 알림 꺼짐';",
    "stateBox.textContent = nowOn ? '🔔 Notifications on' : '🔕 Notifications off';")
rep("toast(nowOn ? '가족 채팅 알림을 켰어요 🔔' : '가족 채팅 알림을 껐어요 🔕');",
    "toast(nowOn ? 'Family chat notifications are on 🔔' : 'Family chat notifications are off 🔕');")
rep("btn.textContent = '✓ 복사됨';", "btn.textContent = '✓ Copied';")
rep("toast('토픽 이름을 복사했어요');", "toast('Topic name copied');")
rep("toast('복사가 안 됐어요. 토픽 이름을 길게 눌러 복사해주세요');",
    "toast('Could not copy. Press and hold the topic name to copy it');")
rep("setTimeout(function(){ btn.textContent = '토픽 복사'; }, 1800);",
    "setTimeout(function(){ btn.textContent = 'Copy topic'; }, 1800);")
rep("btn.textContent = '보내는 중…';", "btn.textContent = 'Sending…';")
rep("title: '💬 가족 채팅 알림 테스트',", "title: '💬 Family chat test notification',")
rep("message: (state.chat.me || '가족') + ' 알림 테스트! 잘 도착했어요 🎉',",
    "message: personLabel(state.chat.me || '가족') + ' here — the test notification arrived 🎉',")
rep("btn.textContent = '테스트 알림 보내기';", "btn.textContent = 'Send a test notification';")
rep("note.textContent = '보냈어요! 구독한 아이폰·아이패드 알림창을 확인해보세요 🔔';",
    "note.textContent = 'Sent! Check the notification on the iPhone or iPad that subscribed 🔔';")
rep("toast('테스트 알림을 보냈어요 🔔');", "toast('Test notification sent 🔔');")
rep("note.textContent = '알림을 보내지 못했어요. 인터넷 연결을 확인하고 다시 눌러주세요.';",
    "note.textContent = 'Could not send the notification. Check the internet connection and try again.';")

# ---------- stickers / messages / voice ----------
rep("toast('스티커를 보냈어요 ✨');", "toast('Sticker sent ✨');")
rep("toast('내가 보낸 메시지만 지울 수 있어요 🔒');", "toast('You can only delete your own messages 🔒');")
rep("var sub = '스티커를 지울까요?';", "var sub = 'Delete this sticker?';")
rep("var sub = '음성 메시지를 지울까요?';", "var sub = 'Delete this voice message?';")
rep("confirmModal('메시지를 지울까요?', m.who + ' · ' + sub, '지우기', function(){",
    "confirmModal('Delete this message?', personLabel(m.who) + ' · ' + sub, 'Delete', function(){")
rep("toast('메시지를 지웠어요');", "toast('Message deleted');")
rep("toast('샘플 음성이라 재생되지 않아요. 직접 녹음하면 들을 수 있어요 🎧');",
    "toast('This is a sample voice message, so it will not play. Record your own to hear it 🎧');")
rep("toast('이 기기에서 소리를 재생할 수 없어요');", "toast('This device cannot play the sound');")
rep("toast('이 브라우저에서는 음성을 재생할 수 없어요');", "toast('This browser cannot play voice messages');")
rep("showVoiceFallback('이 브라우저에서는 녹음을 쓸 수 없어요. 글자나 스티커로 마음을 전해보세요 🙈');",
    "showVoiceFallback('This browser cannot record. Send a message or a sticker instead 🙈');")
rep("$('#voiceBtn').setAttribute('aria-label', '녹음 멈추기');", "$('#voiceBtn').setAttribute('aria-label', 'Stop recording');")
rep("showVoiceFallback('마이크 사용을 허락하지 않으셨어요. 브라우저 설정에서 마이크를 허락하면 녹음돼요 🎙️');",
    "showVoiceFallback('The microphone was not allowed. Allow the mic in browser settings to record 🎙️');")
rep("showVoiceFallback('이 기기에서 마이크를 찾지 못했어요 🎙️');", "showVoiceFallback('No microphone was found on this device 🎙️');")
rep("showVoiceFallback('녹음을 시작할 수 없어요. 글자나 스티커로 마음을 전해보세요 🙈');",
    "showVoiceFallback('Could not start recording. Send a message or a sticker instead 🙈');")
rep("$('#voiceBtn').setAttribute('aria-label', '음성 메시지 녹음');", "$('#voiceBtn').setAttribute('aria-label', 'Record a voice message');")
rep("toast('너무 짧아요. 1초 이상 말해주세요 🙂');", "toast('Too short — please talk for at least a second 🙂');")
rep("toast('녹음이 너무 길어요. 20초 안으로 다시 해주세요');", "toast('That recording is too long. Please keep it under 20 seconds');")
rep("toast('음성 메시지를 보냈어요 🎙️');", "toast('Voice message sent 🎙️');")
rep("toast('녹음을 저장하지 못했어요');", "toast('Could not save the recording');")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step8 ok')
