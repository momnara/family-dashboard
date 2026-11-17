#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 1: document head, header, tabs -> English."""
import io, sys

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:90]))
    text = text.replace(old, new)

# ---------- head ----------
rep('<html lang="ko">', '<html lang="en">')
rep('<meta name="apple-mobile-web-app-title" content="우리 가족">',
    '<meta name="apple-mobile-web-app-title" content="Our Family">')
rep('<meta name="description" content="우리 가족 대시보드 - 공부 용돈, 할 일, 가족 달력, 도장판, 가족 채팅, 공부 타이머">',
    '<meta name="description" content="Our family dashboard - allowance, to-do list, family calendar, photos, family chat and study timer">')
rep('<meta name="app-version" content="1.10.5">', '<meta name="app-version" content="1.10.6">')
rep('<!-- family-dashboard 1.10.5 · 아이들 할 일을 모두 영어로 (Stella·Luna) -->',
    '<!-- family-dashboard 1.10.6 · English UI everywhere + photos visible to the whole family -->')
rep('<title>우리 가족 대시보드 🐥</title>', '<title>Our Family Dashboard 🐥</title>')

# ---------- header ----------
rep('<h1>우리 가족 대시보드</h1>', '<h1>Our Family Dashboard</h1>')
rep('<p>오늘도 사이좋게, 조금씩 자라요 🌱</p>', '<p>Growing together, a little every day 🌱</p>')
rep('title="동기화 상태 · 눌러서 설정">🟡 연결 중</button>',
    'title="Sync status · tap for settings">🟡 Connecting</button>')
rep('<button class="icon-btn" id="refreshBtn" type="button" aria-label="새로고침" title="새로고침">🔄</button>',
    '<button class="icon-btn" id="refreshBtn" type="button" aria-label="Refresh" title="Refresh">🔄</button>')
rep('<button class="icon-btn" id="settingsBtn" type="button" aria-label="설정 열기">⚙️</button>',
    '<button class="icon-btn" id="settingsBtn" type="button" aria-label="Open settings">⚙️</button>')

# ---------- tabs ----------
rep('<nav class="tabs" id="tabs" aria-label="메뉴">', '<nav class="tabs" id="tabs" aria-label="Menu">')
rep('<span class="ico" aria-hidden="true">📅</span>달력</button>', '<span class="ico" aria-hidden="true">📅</span>Calendar</button>')
rep('<span class="ico" aria-hidden="true">✅</span>할 일</button>', '<span class="ico" aria-hidden="true">✅</span>To-Do</button>')
rep('<span class="ico" aria-hidden="true">💰</span>용돈</button>', '<span class="ico" aria-hidden="true">💰</span>Allowance</button>')
rep('<span class="ico" aria-hidden="true">📸</span>사진첩</button>', '<span class="ico" aria-hidden="true">📸</span>Photos</button>')
rep('<span class="ico" aria-hidden="true">💬</span>채팅</button>', '<span class="ico" aria-hidden="true">💬</span>Chat</button>')
rep('<span class="ico" aria-hidden="true">⏰</span>타이머</button>', '<span class="ico" aria-hidden="true">⏰</span>Timer</button>')

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step1 ok')
