#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Step 4: JS constants, display helpers and seed data -> English (data keys preserved)."""
import io

PATH = 'index.html'
text = io.open(PATH, encoding='utf-8').read()

def rep(old, new, count=1):
    global text
    c = text.count(old)
    if c != count:
        raise SystemExit('COUNT MISMATCH (%d != %d) for: %r' % (c, count, old[:90]))
    text = text.replace(old, new)

# ---------- constants + label helpers ----------
rep("var WEEKDAYS = ['일', '월', '화', '수', '목', '금', '토'];",
    """var WEEKDAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
var MONTHS_SHORT = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
/* The saved data still uses the Korean names ('엄마', '아빠', '가족') and Korean subjects
   ('영어', '중국어', '바이올린'), so anything that reaches the screen goes through these
   helpers. Only the labels change — the stored values stay exactly as they are. */
var PERSON_LABELS = { '엄마': 'Mom', '아빠': 'Dad', '가족': 'Family', '루나': 'Luna', '스텔라': 'Stella' };
var SUBJECT_LABELS = {
  '영어': 'English', '중국어': 'Chinese', '바이올린': 'Violin', '피아노': 'Piano',
  '수학': 'Math', '국어': 'Korean', '과학': 'Science', '사회': 'Social Studies',
  '미술': 'Art', '음악': 'Music', '체육': 'PE', '태권도': 'Taekwondo', '코딩': 'Coding'
};
function personLabel(who){
  var s = String(who == null ? '' : who);
  return PERSON_LABELS[s] || s;
}
/* 글자 하나라도 저장된 이름과 겹치면 그 이름으로 봐요 ('Stella·Luna' → 둘 다) */
function personLabelList(who){
  var s = String(who == null ? '' : who);
  var names = ['Stella', 'Luna', 'Mom', 'Dad'];
  var hits = names.filter(function(n){
    if(s.indexOf(n) >= 0) return true;
    var key = n === 'Mom' ? '엄마' : (n === 'Dad' ? '아빠' : (n === 'Luna' ? '루나' : '스텔라'));
    return s.indexOf(key) >= 0;
  });
  return hits.length ? hits.join(' & ') : personLabel(s);
}
function subjectLabel(sub){
  var s = String(sub == null ? '' : sub).trim();
  return SUBJECT_LABELS[s] || s;
}
/* 준비 숙제는 영어·중국어 수업에만 떠요 — 저장된 한국어 이름과 새로 적은 영어 이름 둘 다 알아봐요 */
function isPrepSubject(sub){
  var s = String(sub == null ? '' : sub);
  return s.indexOf('영어') >= 0 || s.indexOf('중국어') >= 0 || /english|chinese/i.test(s);
}
function monthName(m, short){
  var i = Math.round(num(m, 0));
  if(i < 0 || i > 11) return '';
  return short ? MONTHS_SHORT[i] : MONTHS[i];
}
/* '2026-11-18' → 'Nov 18' */
function dateShortLabel(key){
  var p = String(key || '').split('-');
  if(p.length !== 3) return String(key || '');
  return monthName(Number(p[1]) - 1, true) + ' ' + Number(p[2]);
}""")

# ---------- family events (display names in English, Korean aliases kept) ----------
rep("""var FAMILY_EVENTS = [
  { id:'mom',    name:'엄마',   kind:'birthday', solar:[1, 7],   aliases:['엄마', '어머니', 'mom'] },
  { id:'luna',   name:'루나',   kind:'birthday', solar:[1, 16],  aliases:['루나', '수아', 'luna'] },
  { id:'dad',    name:'아빠',   kind:'birthday', solar:[4, 15],  aliases:['아빠', '아버지', 'dad'] },
  { id:'stella', name:'스텔라', kind:'birthday', solar:[9, 7],   aliases:['스텔라', '지아', 'stella'] },
  { id:'wonil',  name:'이원일', kind:'birthday', solar:[2, 18] },
  { id:'mingi',  name:'김민기', kind:'birthday', solar:[4, 26] },
  { id:'lee-rite', name:'이문복 할아버지', kind:'memorial', label:'제사', mark:'🕯️', solar:[10, 10] },
  { id:'lee',    name:'이문복 할아버지', kind:'memorial', solar:[10, 11] },
  { id:'kim',    name:'김광인 할아버지', kind:'birthday', label:'생신', lunar:[4, 26] },
  { id:'park',   name:'박순자 할머니',   kind:'birthday', label:'생신', lunar:[4, 13] },
  { id:'ahn',    name:'안옥희 할머니',   kind:'birthday', label:'생신', lunar:[11, 25] }
];""",
"""var FAMILY_EVENTS = [
  { id:'mom',    name:'Mom',   kind:'birthday', solar:[1, 7],   aliases:['엄마', '어머니', 'mom', 'mother'] },
  { id:'luna',   name:'Luna',  kind:'birthday', solar:[1, 16],  aliases:['루나', '수아', 'luna'] },
  { id:'dad',    name:'Dad',   kind:'birthday', solar:[4, 15],  aliases:['아빠', '아버지', 'dad', 'father'] },
  { id:'stella', name:'Stella', kind:'birthday', solar:[9, 7],  aliases:['스텔라', '지아', 'stella'] },
  { id:'wonil',  name:'Wonil Lee', kind:'birthday', solar:[2, 18], aliases:['이원일'] },
  { id:'mingi',  name:'Mingi Kim', kind:'birthday', solar:[4, 26], aliases:['김민기'] },
  { id:'lee-rite', name:'Grandpa Munbok Lee', kind:'memorial', label:'Memorial rite', mark:'🕯️', solar:[10, 10], aliases:['이문복 할아버지'] },
  { id:'lee',    name:'Grandpa Munbok Lee', kind:'memorial', solar:[10, 11], aliases:['이문복 할아버지'] },
  { id:'kim',    name:'Grandpa Gwangin Kim', kind:'birthday', label:'Birthday', lunar:[4, 26], aliases:['김광인 할아버지'] },
  { id:'park',   name:'Grandma Sunja Park',   kind:'birthday', label:'Birthday', lunar:[4, 13], aliases:['박순자 할머니'] },
  { id:'ahn',    name:'Grandma Okhee Ahn',   kind:'birthday', label:'Birthday', lunar:[11, 25], aliases:['안옥희 할머니'] }
];""")

# shortDate / dayLabel
rep("""function shortDate(key){
  var p = String(key).split('-');
  return Number(p[1]) + '월 ' + Number(p[2]) + '일';
}""",
"""function shortDate(key){ return dateShortLabel(key); }""")
rep("""function dayLabel(key){
  if(key === todayKey()) return '오늘';
  if(key === dateKey(daysAgo(1))) return '어제';
  return shortDate(key) + ' (' + weekdayOf(key) + ')';
}""",
"""function dayLabel(key){
  if(key === todayKey()) return 'Today';
  if(key === dateKey(daysAgo(1))) return 'Yesterday';
  return shortDate(key) + ' (' + weekdayOf(key) + ')';
}""")

# confirmModal cancel
rep("'<div class=\"modal-actions\"><button class=\"btn ghost\" type=\"button\" data-modal-close>취소</button>' +",
    "'<div class=\"modal-actions\"><button class=\"btn ghost\" type=\"button\" data-modal-close>Cancel</button>' +")

# mascot / chick aria labels
rep("'<svg viewBox=\"0 0 100 100\" role=\"img\" aria-label=\"' + who + ' 캐릭터\">' +",
    "'<svg viewBox=\"0 0 100 100\" role=\"img\" aria-label=\"' + esc(personLabel(who)) + ' character\">' +")
rep("'<svg viewBox=\"0 0 100 100\" role=\"img\" aria-label=\"병아리\">' +",
    "'<svg viewBox=\"0 0 100 100\" role=\"img\" aria-label=\"baby chick\">' +")

# stickers labels
rep("""var STICKERS = [
  { id:'happy',   label:'방긋',   bg:'#FFF6DC' },
  { id:'love',    label:'하트뿅', bg:'#FFEFF3' },
  { id:'cry',     label:'엉엉',   bg:'#EAF4FF' },
  { id:'sleep',   label:'쿨쿨',   bg:'#F1ECFF' },
  { id:'angry',   label:'부글',   bg:'#FFEFE6' },
  { id:'wow',     label:'깜짝',   bg:'#EAFBF0' },
  { id:'fighting',label:'화이팅', bg:'#FFF9E3' },
  { id:'hungry',  label:'배고파', bg:'#FFF3E4' }
];""",
"""var STICKERS = [
  { id:'happy',   label:'Smile',    bg:'#FFF6DC' },
  { id:'love',    label:'Love',     bg:'#FFEFF3' },
  { id:'cry',     label:'Crying',   bg:'#EAF4FF' },
  { id:'sleep',   label:'Sleeping', bg:'#F1ECFF' },
  { id:'angry',   label:'Grumpy',   bg:'#FFEFE6' },
  { id:'wow',     label:'Surprised', bg:'#EAFBF0' },
  { id:'fighting',label:'You can do it!', bg:'#FFF9E3' },
  { id:'hungry',  label:'Hungry',   bg:'#FFF3E4' }
];""")

# seed lessons -> English subjects
rep("""      lessons: [
        { id:'ls1', kid:'Stella', day:0, time:'20:00', subject:'영어' },
        { id:'ls2', kid:'Stella', day:3, time:'20:00', subject:'영어' },
        { id:'ls3', kid:'Stella', day:4, time:'17:00', subject:'바이올린' },
        { id:'ls4', kid:'Stella', day:5, time:'19:00', subject:'중국어' },
        { id:'ls5', kid:'Luna', day:1, time:'20:00', subject:'영어' }
      ]""",
"""      lessons: [
        { id:'ls1', kid:'Stella', day:0, time:'20:00', subject:'English' },
        { id:'ls2', kid:'Stella', day:3, time:'20:00', subject:'English' },
        { id:'ls3', kid:'Stella', day:4, time:'17:00', subject:'Violin' },
        { id:'ls4', kid:'Stella', day:5, time:'19:00', subject:'Chinese' },
        { id:'ls5', kid:'Luna', day:1, time:'20:00', subject:'English' }
      ]""")

io.open(PATH, 'w', encoding='utf-8').write(text)
print('step4 ok')
