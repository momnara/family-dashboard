#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 13: photo auto-refresh (so everyone's photos show up), prep subject helper, small fixes."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:130]))
    text = text.replace(old, new)

# sticker aria label
rep("esc(s ? s.label : id) + ' 스티커\">'", "esc(s ? s.label : id) + ' sticker\">'")

# prep subjects: use the helper that knows Korean and English names
rep("""    var sub = String(l.subject || '');
    return sub.indexOf('영어') >= 0 || sub.indexOf('중국어') >= 0;""",
"""    return isPrepSubject(l.subject);""")

# settings footer shows the running version
rep("'<p class=\"small muted\" style=\"text-align:center;margin-top:4px\">Our Family Dashboard · live sync v1.1</p>' +",
    "'<p class=\"small muted\" style=\"text-align:center;margin-top:4px\">Our Family Dashboard · v1.10.6</p>' +")

# ---------- photos: everyone's photos, always fresh ----------
rep("""var photos = {
  month: '',            /* 지금 보고 있는 달 'YYYY-MM' */""",
"""var photoRefreshTimer = null;
var photos = {
  month: '',            /* 지금 보고 있는 달 'YYYY-MM' */""")

rep("""  if(name === 'photos'){
    /* 사진첩 탭을 열 때만 그 달 사진을 불러와요 */
    renderPhotos();
    photosLoad(photoMonth());
  }""",
"""  if(name === 'photos'){
    /* 사진첩 탭을 열 때마다 다시 불러와요 — 다른 기기에서 올린 사진도 바로 보이게 */
    renderPhotos();
    photosLoad(photoMonth(), { force: true });
    photosStartAutoRefresh();
  }""")

rep("""function photosMove(delta){""",
"""/* 사진첩을 보고 있는 동안에는 가끔 새로 불러와요 —
   다른 사람이 자기 기기에서 올린 사진도 새로고침 없이 다 같이 보여요. */
function photosStartAutoRefresh(){
  if(photoRefreshTimer) return;
  photoRefreshTimer = setInterval(function(){
    if(!state || !state.ui || state.ui.tab !== 'photos') return;
    if(document.visibilityState === 'hidden') return;
    photosLoad(photoMonth(), { force: true });
  }, 20000);
}
/* 앱으로 돌아오면 사진첩을 한 번 새로 불러와요 */
document.addEventListener('visibilitychange', function(){
  if(document.visibilityState === 'visible' && state && state.ui && state.ui.tab === 'photos'){
    photosLoad(photoMonth(), { force: true });
  }
});

function photosMove(delta){""")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step13 ok')
