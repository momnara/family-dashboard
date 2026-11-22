#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1.11.3 -> 1.11.4 : 📚 단어장에 날짜 이동기(지난 날 단어 복습) 추가.

- Firebase familyDashboard/vocabHistory/{YYYY-MM-DD}.json 을 읽어 지난 날 단어를 보여줘요.
- 오늘 단어(v1/vocab)는 손대지 않아요 (읽기 전용).
"""
import io, sys

PATH = 'index.html'
s = io.open(PATH, encoding='utf-8').read()
orig = s


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit('expected %d match(es), found %d for: %r' % (n, c, old[:120]))
    s = s.replace(old, new)


# ---------------------------------------------------------------- version
rep('<meta name="app-version" content="1.11.3">',
    '<meta name="app-version" content="1.11.4">')
rep('<!-- family-dashboard 1.11.3 · 📝 Quiz: Q-number on each prompt, tap again to unselect before Check Answer, retry uses a different question type -->',
    '<!-- family-dashboard 1.11.4 · 📚 Vocab: date navigator to review a past day\'s 20 words in Study and Quiz (Firebase familyDashboard/vocabHistory) -->')
rep("Our Family Dashboard · v1.11.3", "Our Family Dashboard · v1.11.4")

# ---------------------------------------------------------------- CSS
rep(""".vocab-date{display:inline-flex;align-items:center;gap:4px;font-family:var(--font-title);font-size:12px;color:#8A6530;background:#FFF4D9;border:1.5px solid #F0D9AE;border-radius:999px;padding:5px 11px;white-space:nowrap}
""",
    """/* 📅 날짜 이동기 — 지난 날 단어도 같은 자리에서 복습해요 */
.vocab-datebar{display:flex;align-items:center;gap:7px;margin:0 0 10px}
.vocab-navbtn{flex:0 0 auto;width:44px;height:44px;padding:0;border-radius:15px;border:1.5px solid #F0D9AE;background:#FFFBF0;color:#8A6530;font-size:12px;line-height:1;display:grid;place-items:center;box-shadow:0 2px 0 #F3E6D2;transition:transform .12s ease,box-shadow .12s ease,opacity .12s ease}
.vocab-navbtn:active:not(:disabled){transform:translateY(2px);box-shadow:none}
.vocab-navbtn:disabled{opacity:.38;background:#FBF7F0;border-color:#EEE5D6;color:#B9A98F;box-shadow:none}
.vocab-dateslot{position:relative;flex:1 1 auto;min-width:0}
.vocab-datesel{-webkit-appearance:none;appearance:none;width:100%;min-height:44px;padding:8px 30px;border-radius:999px;border:1.5px solid #F0D9AE;background:#FFF4D9;font-family:var(--font-title);font-size:13.5px;line-height:1.3;color:#8A6530;text-align:center;text-align-last:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vocab-datesel.is-today{color:#A4566A;background:#FFF1F5;border-color:#F5D6DE}
.vocab-datesel:focus-visible{outline:3px solid #EADFFB;outline-offset:2px}
.vocab-dateslot::after{content:'▾';position:absolute;top:50%;right:12px;transform:translateY(-50%);font-size:10px;color:#B08A4C;pointer-events:none}
.vocab-dateslot.single::after{display:none}
.vocab-histhint{margin:-2px 0 10px;font-size:11px;line-height:1.5;color:var(--ink-faint);text-align:center}
.vocab-daymsg{padding:22px 14px;text-align:center;font-size:13px;line-height:1.7;color:var(--ink-soft);background:#FFFCF4;border:2px dashed #EFE1C8;border-radius:16px}
.vocab-daymsg .btn{margin-top:10px}
""")

rep("""  .stamp-grid{gap:5px}
  .sticker-grid{grid-template-columns:repeat(4,1fr)}""",
    """  .stamp-grid{gap:5px}
  .sticker-grid{grid-template-columns:repeat(4,1fr)}
  .vocab-navbtn{width:40px;height:40px;border-radius:13px}
  .vocab-datesel{font-size:12.5px;padding:8px 26px;min-height:40px}""")

# ---------------------------------------------------------------- panel markup
rep("""        <h2><span class="h2-emoji" aria-hidden="true">📚</span>Today's Vocabulary</h2>
        <p class="card-sub">20 new words every day at 12:00 PM. Study them as cards, then take the 20-question quiz.</p>

        <div class="vocab-top">
          <div class="vocab-kids" id="vocabKids" role="group" aria-label="Choose a kid"></div>
          <div class="vocab-meta">
            <span class="vocab-date" id="vocabDate">Loading…</span>
            <span class="vocab-count" id="vocabCount">0 words</span>
          </div>
        </div>
""",
    """        <h2><span class="h2-emoji" aria-hidden="true">📚</span>Vocabulary</h2>
        <p class="card-sub">20 new words every day at 12:00 PM. Study them as cards, then take the 20-question quiz — or tap ◀ ▶ to review a past day.</p>

        <div class="vocab-top">
          <div class="vocab-kids" id="vocabKids" role="group" aria-label="Choose a kid"></div>
          <div class="vocab-meta">
            <span class="vocab-count" id="vocabCount">0 words</span>
          </div>
        </div>

        <div class="vocab-datebar">
          <button class="vocab-navbtn" type="button" id="vocabPrev" aria-label="Previous day's words" disabled><span aria-hidden="true">◀</span></button>
          <div class="vocab-dateslot" id="vocabDateSlot">
            <select class="vocab-datesel" id="vocabDateSel" aria-label="Choose a day of words">
              <option value="">Loading…</option>
            </select>
          </div>
          <button class="vocab-navbtn" type="button" id="vocabNext" aria-label="Next day's words" disabled><span aria-hidden="true">▶</span></button>
        </div>
        <p class="vocab-histhint" id="vocabHistHint" hidden></p>
""")

# ---------------------------------------------------------------- JS: state
rep("var vocab = { kid: '', mode: false, tab: 'study', revealed: {}, loading: false, error: '' };",
    """var vocab = { kid: '', mode: false, tab: 'study', revealed: {}, loading: false, error: '',
  dates: [], sel: '', view: null, cache: {}, datesLoading: false, datesError: '',
  viewLoading: '', viewError: '', viewSeq: 0, liveDate: '' };""")

# ---------------------------------------------------------------- JS: urls
rep("""function vocabBaseUrl(){
  var st = (state && state.settings) ? state.settings : {};
  if(st.localOnly) return '';
  var url = String(st.firebaseUrl || '').trim().replace(/\\/+$/, '');
  if(!url) return '';
  return url + '/' + DB_PATH + '/vocab';
}""",
    """function vocabRootUrl(){
  var st = (state && state.settings) ? state.settings : {};
  if(st.localOnly) return '';
  var url = String(st.firebaseUrl || '').trim().replace(/\\/+$/, '');
  if(!url) return '';
  return url + '/' + DB_PATH;
}
function vocabBaseUrl(){
  var root = vocabRootUrl();
  return root ? root + '/vocab' : '';
}
/* 지난 날 단어 — 오늘 단어(v1/vocab)와 따로, 날짜마다 한 칸씩 보관해요.
   familyDashboard/vocabHistory/2026-11-22.json  { date, updatedAt, stella:[20], luna:[20] } */
function vocabHistBaseUrl(){
  var root = vocabRootUrl();
  return root ? root.replace(/\\/[^/]+$/, '') + '/vocabHistory' : '';
}""")

# ---------------------------------------------------------------- JS: kid list / date text / fresh text
rep("""function vocabKidList(kid){
  var v = (state && state.vocab) || {};
  var list = kid === 'Luna' ? v.luna : v.stella;
  return Array.isArray(list) ? list : [];
}
function vocabDateText(){
  var v = (state && state.vocab) || {};
  var d = String(v.date || '');
  if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(d)) return 'No words yet';
  var dt = new Date(Number(d.slice(0, 4)), Number(d.slice(5, 7)) - 1, Number(d.slice(8, 10)), 12, 0, 0, 0);
  return dateShortLabel(d) + ' (' + WEEKDAYS[dt.getDay()] + ')';
}
/* 12:00 PM에 올라온 단어인지 알려줘요 — 아이들이 '오늘 것'인지 바로 알 수 있게요 */
function vocabFreshText(){
  var v = (state && state.vocab) || {};
  var ts = num(v.updatedAt, 0);""",
    """function vocabKidList(kid){
  var v = vocabViewVocab();
  var list = kid === 'Luna' ? v.luna : v.stella;
  return Array.isArray(list) ? list : [];
}
function vocabDateText(){
  var d = String(vocabViewVocab().date || '');
  if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(d)) return 'No words yet';
  return vocabDateLabel(d) + (d === todayKey() ? ' · Today' : '');
}
/* 12:00 PM에 올라온 단어인지 알려줘요 — 아이들이 '오늘 것'인지 바로 알 수 있게요 */
function vocabFreshText(){
  var v = vocabViewVocab();
  var ts = num(v.updatedAt, 0);""")

# ---------------------------------------------------------------- JS: date navigator block
rep("""function vocabSpeechOk(){""",
    """/* ---------- 📅 지난 날 단어 복습 ----------
   날짜별 단어는 familyDashboard/vocabHistory/{YYYY-MM-DD}.json 에 따로 있어요.
   오늘 단어(state.vocab = v1/vocab)는 그대로 두고, 지난 날은 읽기만 해요. */
function vocabViewVocab(){
  var live = (state && state.vocab) || {};
  var sel = String(vocab.sel || '');
  if(vocab.view && String(vocab.view.date || '') === sel) return vocab.view;
  return live;
}
function vocabDateLabel(date){
  var t = String(date || '');
  if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(t)) return t;
  var d = new Date(Number(t.slice(0, 4)), Number(t.slice(5, 7)) - 1, Number(t.slice(8, 10)), 12, 0, 0, 0);
  return dateShortLabel(t) + ' (' + WEEKDAYS[d.getDay()] + ')';
}
function vocabDateOptionLabel(date){
  return vocabDateLabel(date) + (String(date) === todayKey() ? ' · Today' : '');
}
/* 오늘 날짜는 서버에 아직 없어도 늘 목록에 있어요 (오프라인에서도 오늘이 보이게) */
function vocabDatesNormalize(){
  var seen = {}, out = [];
  function add(d){
    d = String(d || '');
    if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(d) || seen[d]) return;
    seen[d] = 1; out.push(d);
  }
  (vocab.dates || []).forEach(add);
  add(todayKey());
  add((state && state.vocab && state.vocab.date) || '');
  out.sort();
  vocab.dates = out;
  return out;
}
function vocabDefaultDate(){
  var dates = vocabDatesNormalize();
  var live = String((state && state.vocab && state.vocab.date) || '');
  if(live && dates.indexOf(live) >= 0) return live;
  return dates.length ? dates[dates.length - 1] : '';
}
function renderVocabDateNav(){
  var dates = vocabDatesNormalize();
  if(!vocab.sel || dates.indexOf(vocab.sel) < 0) vocab.sel = vocabDefaultDate();
  var selEl = document.getElementById('vocabDateSel');
  var slot = document.getElementById('vocabDateSlot');
  var prev = document.getElementById('vocabPrev');
  var next = document.getElementById('vocabNext');
  var hint = document.getElementById('vocabHistHint');
  if(selEl){
    var opts = dates.map(function(d){
      return '<option value="' + d + '">' + esc(vocabDateOptionLabel(d)) + '</option>';
    }).join('');
    if(selEl.innerHTML !== opts) selEl.innerHTML = opts || '<option value="">No words yet</option>';
    selEl.value = vocab.sel || '';
    selEl.classList.toggle('is-today', !!vocab.sel && vocab.sel === todayKey());
  }
  if(slot) slot.classList.toggle('single', dates.length <= 1);
  var at = dates.indexOf(vocab.sel);
  if(prev) prev.disabled = at <= 0;
  if(next) next.disabled = at < 0 || at >= dates.length - 1;
  if(hint){
    var show = dates.length <= 1;
    hint.hidden = !show;
    hint.textContent = show ? 'Past days will appear here automatically as each day’s words are saved.' : '';
  }
}
/* 앱이 새 날짜의 단어를 받으면, '오늘'을 보던 화면은 새 날짜로 넘어가요 */
function vocabRebaseRef(){
  var live = String((state && state.vocab && state.vocab.date) || '');
  if(!live) return;
  if(vocab.liveDate && vocab.liveDate !== live && vocab.sel === vocab.liveDate){
    vocab.sel = live;
    vocab.view = null;
    vocab.viewLoading = '';
    vocab.revealed = {};
  }
  vocab.liveDate = live;
}
function vocabCachePut(date, v){
  vocab.cache[date] = v;
  var keys = Object.keys(vocab.cache);
  if(keys.length > 40){
    keys.slice(0, keys.length - 40).forEach(function(k){ delete vocab.cache[k]; });
  }
}
/* 지난 날 목록 — familyDashboard/vocabHistory.json?shallow=true 는 { '2026-11-22': true } 꼴이에요 */
function vocabDatesLoad(){
  var base = vocabHistBaseUrl();
  renderVocabDateNav();
  if(!base || typeof fetch !== 'function') return;
  if(vocab.datesLoading) return;
  vocab.datesLoading = true;
  fetch(base + '.json?shallow=true', { cache: 'no-store' }).then(function(res){
    if(!res.ok) throw new Error('HTTP ' + res.status);
    return res.json();
  }).then(function(json){
    vocab.datesLoading = false;
    vocab.datesError = '';
    var list = [];
    if(isObject(json)){
      list = Object.keys(json).filter(function(k){ return /^\\d{4}-\\d{2}-\\d{2}$/.test(k); });
    }
    if(list.length) vocab.dates = list;
    renderVocabDateNav();
    var panel = document.getElementById('panel-vocab');
    if(panel && panel.classList.contains('active') && list.length) renderVocab();
  }).catch(function(){
    vocab.datesLoading = false;
    vocab.datesError = 'dates';
    renderVocabDateNav();
  });
}
/* 날짜를 고르면 그 날 단어를 화면에 올려요 — 오늘은 지금 값(state.vocab), 지난 날은 기록에서 읽어요 */
function vocabSelectDate(date){
  date = String(date || '');
  if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(date)) return;
  var live = String((state && state.vocab && state.vocab.date) || '');
  vocab.sel = date;
  vocab.revealed = {};
  vocab.viewError = '';
  if(date === live){
    vocab.view = null;
    vocab.viewLoading = '';
    vocab.viewSeq++;
    renderVocab();
    return;
  }
  if(vocab.cache[date]){
    vocab.view = vocab.cache[date];
    vocab.viewLoading = '';
    vocab.viewSeq++;
    renderVocab();
    return;
  }
  vocab.view = null;
  vocab.viewLoading = date;
  var seq = ++vocab.viewSeq;
  renderVocab();
  var base = vocabHistBaseUrl();
  if(!base || typeof fetch !== 'function'){
    vocab.viewLoading = '';
    vocab.viewError = date;
    renderVocab();
    return;
  }
  fetch(base + '/' + date + '.json', { cache: 'no-store' }).then(function(res){
    if(!res.ok) throw new Error('HTTP ' + res.status);
    return res.json();
  }).then(function(json){
    if(seq !== vocab.viewSeq) return;
    var v = normalizeVocab(json, null);
    if(!v.date) v.date = date;
    vocabCachePut(date, v);
    vocab.view = v;
    vocab.viewLoading = '';
    vocab.viewError = '';
    renderVocab();
  }).catch(function(){
    if(seq !== vocab.viewSeq) return;
    vocab.viewLoading = '';
    vocab.viewError = date;
    vocab.view = null;
    renderVocab();
  });
}
function vocabStep(dir){
  var dates = vocab.dates || [];
  var at = dates.indexOf(vocab.sel);
  if(at < 0) return;
  var to = at + (dir < 0 ? -1 : 1);
  if(to < 0 || to >= dates.length) return;
  vocabSelectDate(dates[to]);
}
function vocabDayMsgHTML(busy, fail){
  if(busy){
    return '<div class="vocab-daymsg"><span aria-hidden="true">⏳</span> Loading ' + esc(vocabDateLabel(vocab.sel)) + ' words…</div>';
  }
  if(fail){
    return '<div class="vocab-daymsg"><span aria-hidden="true">📡</span> Could not load the words for ' + esc(vocabDateLabel(vocab.sel)) +
      '.<br><button class="btn ghost sm" type="button" data-vretry="1">Try again</button></div>';
  }
  return '';
}
function vocabReloadDay(){
  if(!vocab.sel) return;
  var date = vocab.sel;
  delete vocab.cache[date];
  vocab.view = null;
  vocab.viewError = '';
  vocabSelectDate(date);
  if(date === String((state && state.vocab && state.vocab.date) || '')) vocabLoad();
}
function vocabSpeechOk(){""")

# ---------------------------------------------------------------- JS: vocabLoad keeps past-day view
rep("""    if(!newer) return;
    state.vocab = next;
    writeLocal();
    renderVocab();""",
    """    if(!newer) return;
    state.vocab = next;
    writeLocal();
    renderVocab();""")

# ---------------------------------------------------------------- JS: renderVocab wiring
rep("""  var list = vocabKidList(vocab.kid);
  var dateEl = document.getElementById('vocabDate');
  if(dateEl) dateEl.textContent = vocabDateText();
  var countEl = document.getElementById('vocabCount');
  if(countEl) countEl.textContent = list.length + (list.length === 1 ? ' word' : ' words');""",
    """  vocabRebaseRef();
  renderVocabDateNav();
  var list = vocabKidList(vocab.kid);
  var dayBusy = !!(vocab.viewLoading && vocab.viewLoading === vocab.sel);
  var dayFail = !dayBusy && !!(vocab.viewError && vocab.viewError === vocab.sel);
  var isLiveDay = String(vocab.sel || '') === String((state && state.vocab && state.vocab.date) || '');
  var countEl = document.getElementById('vocabCount');
  if(countEl){
    countEl.textContent = dayBusy
      ? 'Loading…'
      : list.length + (list.length === 1 ? ' word' : ' words');
  }""")

rep("""  var hint = document.getElementById('vocabHint');
  if(hint){
    hint.textContent = !list.length
      ? 'The words for today are not here yet. They are added every day at 12:00 PM.'
      : (vocab.mode""",
    """  var hint = document.getElementById('vocabHint');
  if(hint){
    hint.textContent = dayBusy
      ? 'Loading ' + vocabDateLabel(vocab.sel) + ' words…'
      : (!list.length
        ? (isLiveDay
          ? 'The words for today are not here yet. They are added every day at 12:00 PM.'
          : 'No words were saved for this day.')
        : (vocab.mode""")

rep("""        ? 'Study mode: the meanings are hidden. Tap a card to check yourself, then tap it again to hide it.'
        : 'Turn on study mode to hide the meanings, then tap a card to check yourself. Tap a card or 🔊 to hear the word.');""",
    """          ? 'Study mode: the meanings are hidden. Tap a card to check yourself, then tap it again to hide it.'
          : 'Turn on study mode to hide the meanings, then tap a card to check yourself. Tap a card or 🔊 to hear the word.'));""")

rep("""  if(vocab.tab === 'quiz'){
    vqSync();
    return;
  }
  if(!list.length){
    box.innerHTML = '<div class="empty vocab-empty"><span class="em" aria-hidden="true">' +
      '📚' + '</span>No words yet for ' + esc(vocab.kid) + '.<br>New words come every day at 12:00 PM.</div>';
    return;
  }""",
    """  if(vocab.tab === 'quiz'){
    if(dayBusy || dayFail){
      var qPlay = document.getElementById('quizPlay');
      var qRes = document.getElementById('quizResult');
      if(qPlay) qPlay.hidden = true;
      if(qRes){ qRes.hidden = false; qRes.innerHTML = vocabDayMsgHTML(dayBusy, dayFail); }
      return;
    }
    vqSync();
    return;
  }
  if(dayBusy || dayFail){
    box.innerHTML = vocabDayMsgHTML(dayBusy, dayFail);
    return;
  }
  if(!list.length){
    box.innerHTML = '<div class="empty vocab-empty"><span class="em" aria-hidden="true">' +
      '📚' + '</span>' + (isLiveDay
        ? 'No words yet for ' + esc(vocab.kid) + '.<br>New words come every day at 12:00 PM.'
        : 'No words were saved for ' + esc(vocab.kid) + ' on this day.') + '</div>';
    return;
  }""")

# ---------------------------------------------------------------- JS: quiz signature follows the selected day
rep("""function vqSig(){
  var v = (state && state.vocab) || {};
  return [vocab.kid, String(v.date || ''), Math.round(num(v.updatedAt, 0)), vocabKidList(vocab.kid).length].join('|');
}""",
    """function vqSig(){
  var v = vocabViewVocab();
  return [vocab.kid, String(v.date || ''), Math.round(num(v.updatedAt, 0)), vocabKidList(vocab.kid).length].join('|');
}""")

# ---------------------------------------------------------------- JS: tab open
rep("""  if(name === 'vocab'){
    /* 단어장 탭을 열 때마다 최신 단어를 다시 확인해요 (다른 기기·12시 자동 등록 반영) */
    renderVocab();
    vocabLoad({ force: true });
  }""",
    """  if(name === 'vocab'){
    /* 단어장 탭을 열 때마다 최신 단어와 지난 날 목록을 다시 확인해요 (다른 기기·12시 자동 등록 반영) */
    renderVocab();
    vocabDatesLoad();
    vocabLoad({ force: true });
  }""")

# ---------------------------------------------------------------- JS: events
rep("""  $('#vocabHide').addEventListener('click', function(){""",
    """  $('#vocabPrev').addEventListener('click', function(){ vocabStep(-1); });
  $('#vocabNext').addEventListener('click', function(){ vocabStep(1); });
  $('#vocabDateSel').addEventListener('change', function(){ vocabSelectDate(this.value); });
  $('#panel-vocab').addEventListener('click', function(e){
    var b = e.target.closest ? e.target.closest('[data-vretry]') : null;
    if(!b) return;
    vocabReloadDay();
  });
  $('#vocabHide').addEventListener('click', function(){""")

io.open(PATH, 'w', encoding='utf-8').write(s)
print('patched %s: %d -> %d bytes' % (PATH, len(orig), len(s)))
