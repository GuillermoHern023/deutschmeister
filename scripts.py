# JavaScript Logic for DeutschMeister (Busuu-Inspired Architecture)

JS_CONTENT = """
/* ============================================
   DEUTSCHMEISTER - JAVASCRIPT CORE ENGINE
   ============================================ */

const STORAGE_KEY = 'deutschmeister_state_v3';
const MODULES = [
  { id: 1, title: "Gefühle & Beziehungen", titleEn: "Feelings & Relationships", icon: "❤️", desc: "Lerne über Gefühle zu sprechen, Emotionen auszudrücken und Alltagsbeziehungen in Berlin zu beschreiben.", lessons: [1,2,3,4], level: "A2.1" },
  { id: 2, title: "Wohnen, Stadt & Bürgeramt", titleEn: "Living, City & Registration", icon: "🏠", desc: "Wohnungssuche in Berlin, Mietvertrag verstehen, Nachbarn kennenlernen und Anmeldung beim Bürgeramt.", lessons: [5,6,7,8,9], level: "A2.1" },
  { id: 3, title: "Gesundheit & Sport", titleEn: "Health, Doctor & Fitness", icon: "⚽", desc: "Arztbesuch bei Doctolib, Symptome und Schmerzen beschreiben, Sportarten und Fitness-Routinen.", lessons: [10,11,12,13], level: "A2.1" },
  { id: 4, title: "Kultur & Arbeit", titleEn: "Culture & Work", icon: "🎨", desc: "Museumsbesuche in Berlin, Kulturleben, Berufsalltag und formelle Kommunikation mit Kollegen.", lessons: [14,15,16], level: "A2.1" },
  { id: 5, title: "Zukunft & Modalverben", titleEn: "Future & Modal Verbs", icon: "🔮", desc: "Zukunftspläne schmieden, Wünsche äußern und alle Modalverben im Präteritum und Perfekt meistern.", lessons: [17,18,19,20], level: "A2.1" },
  { id: 6, title: "Essen & Restaurant", titleEn: "Food & Dining Out", icon: "🌭", desc: "Bestellen im Restaurant, Berliner Street Food, Essgewohnheiten und Rezepte auf Deutsch erklären.", lessons: [21,22,23,24], level: "A2.2" },
  { id: 7, title: "Reisen & Mobilität", titleEn: "Travel, Hotel & Train", icon: "🗺️", desc: "Deutsche Bahn Tickets buchen, Hotelreservierungen, Wegbeschreibungen und Städtetrips.", lessons: [25,26,27,28], level: "A2.2" },
  { id: 8, title: "Medien & Technologie", titleEn: "Media & Tech", icon: "💻", desc: "Soziale Medien, IT im Büro, E-Mails schreiben und technische Probleme am Arbeitsplatz schildern.", lessons: [29,30,31,32], level: "A2.2" },
  { id: 9, title: "Natur, Umwelt & Wünsche", titleEn: "Nature & Wishes (Konjunktiv II)", icon: "🌲", desc: "Wetter, Umwelt, Ausflüge ins Berliner Umland und Höflichkeit mit Konjunktiv II (hätte, wäre, würde).", lessons: [33,34,35,36], level: "A2.2" },
  { id: 10, title: "Geld, Bank & Bewerbung", titleEn: "Money, Bank & CV", icon: "💶", desc: "Bankkonto eröffnen, Überweisungen tätigen, Lebenslauf erstellen und Vorstellungsgespräche führen.", lessons: [37,38,39,40], level: "A2.2" },
  { id: 11, title: "Beruf & Projektmanagement", titleEn: "Career & Project Management", icon: "💼", desc: "Projektleitung in Deutschland, Fristen und Budgets besprechen, Standup-Meetings und Feedback.", lessons: [41,42,43,44], level: "B1" },
  { id: 12, title: "B1 Grammatik-Meister", titleEn: "B1 Grammar Mastery", icon: "🔗", desc: "Konnektoren (weil, obwohl, deshalb, trotzdem), Infinitiv mit zu, Verben mit festen Präpositionen.", lessons: [45,46,47,48,61,62,63,64], level: "B1" },
  { id: 13, title: "Nachrichten & Gesellschaft", titleEn: "News & Society", icon: "📰", desc: "Zeitungsberichte verstehen, gesellschaftliche Themen diskutieren und eigene Meinung argumentieren.", lessons: [49,50,51,52], level: "B1" },
  { id: 14, title: "Umwelt & Nachhaltigkeit", titleEn: "Environment & Sustainability", icon: "♻️", desc: "Klimaschutz, erneuerbare Energien, Mülltrennung und nachhaltiges Leben in Deutschland.", lessons: [53,54,55,56], level: "B1" },
  { id: 15, title: "Geschichte & Meisterschaft", titleEn: "History & Goethe B1 Final", icon: "🏆", desc: "Deutsche Geschichte (Mauerfall), Goethe B1 Prüfungs-Simulation und offizielle Zertifikatsreife.", lessons: [57,58,59,60], level: "B1" }
];

const LESSONS = __LESSON_DATA_PLACEHOLDER__;

/* State */
function getDefaultState() {
  return {
    completedLessons: {}, // { [id]: { stars: 3, score: 100, completedAt: '...' } }
    xp: 0,
    streak: 1,
    lastActiveDate: new Date().toISOString().split('T')[0],
    activeLevel: 'A2.1',
    freeMode: false,
    soundEnabled: true,
    activeNavMode: 'course',
    currentLesson: null
  };
}

let state = loadState();

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return { ...getDefaultState(), ...JSON.parse(raw) };
  } catch(e) {}
  return getDefaultState();
}

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch(e) {}
}

/* Audio Synthesizer (Zero-dependency Web Audio API) */
class SoundEngine {
  constructor() {
    this.ctx = null;
  }
  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }
  playTone(freq, type, duration, delay = 0, gainLevel = 0.15) {
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    const now = this.ctx.currentTime + delay;

    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);

    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(gainLevel, now + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start(now);
    osc.stop(now + duration);
  }
  correct() {
    // Uplifting major triad: C5 (523Hz), E5 (659Hz), G5 (784Hz)
    this.playTone(523.25, 'sine', 0.18, 0, 0.18);
    this.playTone(659.25, 'sine', 0.18, 0.08, 0.18);
    this.playTone(783.99, 'sine', 0.28, 0.16, 0.22);
  }
  wrong() {
    // Gentle low buzz: A3 (220Hz) -> F3 (174Hz)
    this.playTone(220, 'triangle', 0.2, 0, 0.2);
    this.playTone(174.61, 'triangle', 0.28, 0.1, 0.22);
  }
  click() {
    this.playTone(800, 'sine', 0.03, 0, 0.06);
  }
  fanfare() {
    // Victory fanfare: C5 -> E5 -> G5 -> C6
    this.playTone(523.25, 'sine', 0.15, 0, 0.2);
    this.playTone(659.25, 'sine', 0.15, 0.12, 0.2);
    this.playTone(783.99, 'sine', 0.2, 0.24, 0.25);
    this.playTone(1046.50, 'sine', 0.45, 0.4, 0.3);
  }
}

const soundEngine = new SoundEngine();

function toggleSound() {
  state.soundEnabled = !state.soundEnabled;
  saveState();
  const btn = document.getElementById('btn-sound-toggle');
  if (btn) btn.innerText = state.soundEnabled ? '🔊 Ton: An' : '🔇 Ton: Aus';
  if (state.soundEnabled) soundEngine.click();
}

/* Web Speech API German Voice Engine */
let deVoice = null;
function initSpeech() {
  if (!('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return;
  const updateVoices = () => {
    const voices = window.speechSynthesis.getVoices();
    deVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Google') || v.name.includes('Katja') || v.name.includes('Stefan') || v.name.includes('Anna'))) 
              || voices.find(v => v.lang.startsWith('de')) || null;
  };
  updateVoices();
  if (window.speechSynthesis.onvoiceschanged !== undefined) {
    window.speechSynthesis.onvoiceschanged = updateVoices;
  }
}
initSpeech();

function speakGerman(text, rate = 1.0) {
  if (!('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return;
  window.speechSynthesis.cancel();
  const clean = text.replace(/<[^>]*>/g, '').trim();
  if (!clean) return;

  const utter = new SpeechSynthesisUtterance(clean);
  utter.lang = 'de-DE';
  utter.rate = rate;
  if (deVoice) utter.voice = deVoice;
  window.speechSynthesis.speak(utter);
}

function playAudio(text, rate = 1.0) {
  speakGerman(text, rate);
}

/* XP, Streak & Level Helpers */
function addXp(amount) {
  state.xp += amount;
  saveState();
  updateXpDisplay();
}

function updateXpDisplay() {
  const currentLevel = Math.floor(state.xp / 100) + 1;
  const xpInLevel = state.xp % 100;
  
  const xpCurrentEl = document.getElementById('xp-current');
  const xpNextEl = document.getElementById('xp-next');
  const xpBarFillEl = document.getElementById('xp-bar-fill');
  const levelBadgeEl = document.getElementById('level-badge');
  const streakBadgeEl = document.getElementById('streak-badge');

  if (xpCurrentEl) xpCurrentEl.innerText = `${state.xp} XP`;
  if (xpNextEl) xpNextEl.innerText = `${currentLevel * 100} XP`;
  if (xpBarFillEl) xpBarFillEl.style.width = `${xpInLevel}%`;
  if (levelBadgeEl) levelBadgeEl.innerText = `⭐ Level ${currentLevel}`;
  if (streakBadgeEl) streakBadgeEl.innerText = `🔥 ${state.streak} Tage`;
}

function updateStreak() {
  const today = new Date().toISOString().split('T')[0];
  if (state.lastActiveDate !== today) {
    const yesterday = new Date(Date.now() - 86400000).toISOString().split('T')[0];
    if (state.lastActiveDate === yesterday) {
      state.streak += 1;
    } else {
      state.streak = 1;
    }
    state.lastActiveDate = today;
    saveState();
  }
  updateXpDisplay();
}

function toggleFreeMode() {
  state.freeMode = !state.freeMode;
  saveState();
  const btn = document.getElementById('btn-unlock-toggle');
  if (btn) btn.innerText = state.freeMode ? '🔓 Alle freigeschaltet' : '🔒 Schritt für Schritt';
  showDashboard();
}

function changeLevel(level) {
  state.activeLevel = level;
  saveState();
  document.querySelectorAll('.level-tab-btn').forEach(b => {
    b.classList.toggle('active', b.innerText.includes(level));
  });
  showDashboard();
}

function switchNavMode(mode) {
  state.activeNavMode = mode;
  saveState();
  document.querySelectorAll('.nav-mode-btn').forEach(b => b.classList.remove('active'));
  const targetBtn = document.getElementById(`nav-mode-${mode}`);
  if (targetBtn) targetBtn.classList.add('active');

  if (mode === 'course') showDashboard();
  else if (mode === 'survival') renderSurvivalSimulator();
  else if (mode === 'goethe') renderGoetheCenter();
  else if (mode === 'trainer') renderDrillTrainer();

  if (window.innerWidth <= 900) {
    document.getElementById('sidebar')?.classList.remove('open');
  }
}

function isLessonUnlocked(id) {
  if (state.freeMode) return true;
  if (id === 1) return true;
  const prevLesson = LESSONS.find(l => l.id === id - 1);
  if (!prevLesson) return true;
  return isLessonCompleted(prevLesson.id);
}

function isLessonCompleted(id) {
  return !!state.completedLessons[id];
}

function getLessonStars(id) {
  return state.completedLessons[id]?.stars || 0;
}

function getLessonLevel(id) {
  if (id <= 20) return 'A2.1';
  if (id <= 40) return 'A2.2';
  return 'B1';
}

/* Spanish Speaker Context Helpers (Custom-tailored for Guillermo) */
function getSpanishTip(lesson) {
  const id = lesson.id;
  if (id === 1) {
    return "💡 <strong>Ojo hispanohablantes:</strong> En español decimos <em>enojado CON</em> o <em>satisfecho CON</em>. En alemán, las preposiciones cambian: <strong>wütend auf + Akkusativ</strong> (enojado con) y <strong>zufrieden mit + Dativ</strong> (satisfecho con).";
  }
  if (id >= 5 && id <= 9) {
    return "💡 <strong>Wechselpräpositionen (en vs. a):</strong> En español usamos 'en' para posición y movimiento ('estoy en la cocina' vs 'voy en la cocina'). En alemán: <strong>Wo? (¿Dónde?) = Dativ</strong> (<em>in der Küche</em>), <strong>Wohin? (¿A dónde?) = Akkusativ</strong> (<em>in die Küche</em>).";
  }
  if (id >= 17 && id <= 20) {
    return "💡 <strong>Verbo al final con modales:</strong> En español dices 'debo <em>trabajar</em> hoy a las seis'. En alemán, el verbo modal va en 2ª posición y el infinitivo SIEMPRE al final absoluto: <em>Ich muss heute um sechs Uhr <strong>arbeiten</strong></em>.";
  }
  if (id === 21) {
    return "💡 <strong>Género contrastante:</strong> Cuidado con los géneros: <em>la sopa</em> = <strong>die Suppe</strong>, pero <em>el pan</em> = <strong>das Brot</strong> (neutro) y <em>la cerveza</em> = <strong>das Bier</strong> (neutro).";
  }
  if (id === 25) {
    return "💡 <strong>Medios de transporte:</strong> En español decimos 'voy <em>en</em> tren'. En alemán nunca se usa 'in', sino <strong>mit dem Zug</strong> / <strong>mit der U-Bahn</strong> (+ Dativ).";
  }
  if (id === 61) {
    return "💡 <strong>La regla de oro B1:</strong> <em>weil</em> (porque) y <em>obwohl</em> (aunque) lanzan el verbo conjugado al <strong>FINAL ABSOLUTO</strong> de la frase. <em>... weil ich in Berlin <strong>lebe</strong></em>.";
  }
  if (id === 62) {
    return "💡 <strong>Infinitivo con 'zu':</strong> Equivale a 'para + infinitivo' en español: <strong>um ... zu</strong> (<em>Ich lerne Deutsch, um einen Job zu finden</em>).";
  }
  return "💡 <strong>Tipp für Guillermo:</strong> Achte auf das grammatikalische Geschlecht (der/die/das) und sprich die Beispielsätze laut mit, um Akzent und Sprachmelodie zu festigen!";
}

/* ============================================
   BUSUU TIMELINE VIEW (THE CORE DASHBOARD)
   ============================================ */
function showDashboard() {
  state.currentLesson = null;
  state.activeNavMode = 'course';
  saveState();
  updateXpDisplay();

  const activeLevel = state.activeLevel || "A2.1";
  const levelModules = MODULES.filter(m => m.level === activeLevel);
  const levelLessons = LESSONS.filter(l => getLessonLevel(l.id) === activeLevel);
  const completedCount = levelLessons.filter(l => isLessonCompleted(l.id)).length;
  const pctTotal = Math.round((completedCount / (levelLessons.length || 1)) * 100);

  // Find next up lesson
  const nextLesson = levelLessons.find(l => !isLessonCompleted(l.id) && isLessonUnlocked(l.id)) || levelLessons[0];

  let html = `
    <!-- Top Sticky Navigation Pill on Main Content -->
    <div class="timeline-top-nav">
      <div style="display:flex;justify-content:space-between;align-items:center;width:100%;flex-wrap:wrap;gap:14px">
        <div class="course-identity">
          <div class="flag-avatar">🇩🇪</div>
          <div>
            <div class="course-name">Deutsch ${activeLevel} • Alltag & Goethe</div>
            <div class="course-sub">Dein persönlicher Weg zur echten Sprachbeherrschung in Berlin</div>
          </div>
        </div>

        <div class="top-stats-row">
          <div class="stat-pill streak" title="Tage Lern-Serie">🔥 ${state.streak} Tage</div>
          <div class="stat-pill xp" title="Gesamt-Erfahrungspunkte">⚡ ${state.xp} XP</div>
          <div class="stat-pill level" title="Fortschritt im aktuellen Level">📚 ${completedCount}/${levelLessons.length} (${pctTotal}%)</div>
          <button class="sound-toggle-btn" onclick="toggleSound()" title="Soundeffekte an/aus">
            ${state.soundEnabled ? '🔊' : '🔇'}
          </button>
        </div>
      </div>

      <!-- Quick Level Switcher Tabs -->
      <div style="display:flex;gap:8px;margin-top:14px;width:100%">
        <button class="level-tab-btn ${activeLevel === 'A2.1' ? 'active' : ''}" style="padding:10px 14px;font-size:0.84rem" onclick="changeLevel('A2.1')">
          Stufe 1 • A2.1 Grundlagen
        </button>
        <button class="level-tab-btn ${activeLevel === 'A2.2' ? 'active' : ''}" style="padding:10px 14px;font-size:0.84rem" onclick="changeLevel('A2.2')">
          Stufe 2 • A2.2 Alltag & Beruf
        </button>
        <button class="level-tab-btn ${activeLevel === 'B1' ? 'active' : ''}" style="padding:10px 14px;font-size:0.84rem" onclick="changeLevel('B1')">
          Stufe 3 • B1 Goethe-Meisterschaft
        </button>
      </div>
    </div>

    <!-- Hero Card: Next Recommended Lesson -->
    <div style="background:linear-gradient(135deg, rgba(37,99,235,0.18), rgba(30,41,59,0.9));border:1px solid rgba(59,130,246,0.35);border-radius:var(--radius-lg);padding:24px 28px;margin-bottom:36px;box-shadow:var(--shadow-lg);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:18px">
      <div>
        <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(59,130,246,0.25);color:#93c5fd;font-size:0.75rem;font-weight:800;padding:4px 12px;border-radius:var(--radius-full);margin-bottom:10px;letter-spacing:0.05em">
          🚀 NÄCHSTE LEKTION (EMPFOHLEN)
        </div>
        <h2 style="font-size:1.4rem;font-weight:800;color:#fff;margin-bottom:4px">
          ${nextLesson.icon} Lektion ${nextLesson.id}: ${nextLesson.titleDe}
        </h2>
        <div style="font-size:0.9rem;color:var(--text-secondary)">
          ${nextLesson.title} • ⏱️ ca. 4–5 Min. • Wortschatz, Grammatik-Bisschen & Dialog
        </div>
      </div>
      <button class="btn-primary" style="padding:14px 28px;font-size:1rem" onclick="startLessonFlow(${nextLesson.id})">
        ▶ Lektion ${nextLesson.id} jetzt starten →
      </button>
    </div>

    <!-- Busuu Vertical Stepping-Stone Timeline -->
    <div class="busuu-timeline">
  `;

  // Render chapters with stepping stones
  levelModules.forEach((mod, modIdx) => {
    const modLessons = mod.lessons.map(id => LESSONS.find(l => l.id === id)).filter(Boolean);
    const modCompleted = modLessons.filter(l => isLessonCompleted(l.id)).length;
    const modPct = Math.round((modCompleted / (modLessons.length || 1)) * 100);

    html += `
      <div class="timeline-chapter" id="chapter-${mod.id}">
        <!-- Chapter Banner Card -->
        <div class="chapter-banner">
          <div class="chapter-badge">Kapitel ${mod.id} • ${activeLevel}</div>
          <div class="chapter-title">${mod.icon} ${mod.title}</div>
          <div class="chapter-desc">${mod.desc}</div>
          <div class="chapter-progress-box">
            <span>${modCompleted} von ${modLessons.length} Lektionen abgeschlossen</span>
            <div class="chapter-progress-bar">
              <div class="chapter-progress-fill" style="width:${modPct}%"></div>
            </div>
            <span>${modPct}%</span>
          </div>
        </div>

        <!-- Path Track with Stepping Stones -->
        <div class="path-track">
    `;

    // Stepping stones with natural stagger
    const staggerClasses = ['stagger-center', 'stagger-left', 'stagger-center', 'stagger-right'];

    modLessons.forEach((lesson, lIdx) => {
      const unlocked = isLessonUnlocked(lesson.id);
      const completed = isLessonCompleted(lesson.id);
      const isActive = nextLesson && nextLesson.id === lesson.id;
      const stars = getLessonStars(lesson.id);
      const stagger = staggerClasses[lIdx % staggerClasses.length];

      let stateClass = 'locked';
      let centerIcon = '🔒';
      if (completed) {
        stateClass = 'completed';
        centerIcon = '✓';
      } else if (unlocked) {
        stateClass = isActive ? 'active' : 'unlocked';
        centerIcon = isActive ? '▶' : lesson.icon;
      }

      html += `
        <div class="stone-row ${stagger}">
          <div class="stone-container" onclick="${unlocked ? `startLessonFlow(${lesson.id})` : `alert('Schließe zuerst die vorherige Lektion ab oder aktiviere Alle freischalten in der Seitenleiste!')`}">
            ${isActive ? `<div class="start-here-beacon">🚀 START HIER</div>` : ''}
            
            <div class="stone-circle ${stateClass}" title="${lesson.titleDe}">
              ${centerIcon}
            </div>

            ${completed ? `
              <div class="stone-stars">${'⭐'.repeat(stars || 3)}</div>
            ` : ''}

            <div class="stone-card-preview">
              <div class="stone-card-title">${lesson.id}. ${lesson.titleDe}</div>
              <div class="stone-card-sub">${lesson.title}</div>
              <div class="stone-card-meta">⏱️ 4–5 Min. • Wortschatz & Dialog</div>
            </div>
          </div>
        </div>
      `;
    });

    // Chapter Milestone Checkpoint Stone at end of chapter
    const allModDone = modCompleted === modLessons.length;
    html += `
          <!-- Chapter Milestone Checkpoint -->
          <div class="stone-row stagger-center" style="margin-top:16px">
            <div class="stone-container" onclick="openChapterMilestone(${mod.id})">
              <div class="milestone-beacon">🏆 MEILENSTEIN</div>
              <div class="milestone-stone-circle" title="Kapitel-Abschlussprüfung">
                ${allModDone ? '👑' : '🏆'}
              </div>
              <div class="stone-card-preview" style="border-color:var(--brand-amber)">
                <div class="stone-card-title">Kapitel ${mod.id} Goethe-Check</div>
                <div class="stone-card-sub">Zusammenfassender Abschlusstest</div>
                <div class="stone-card-meta" style="color:#fbbf24">🏅 +50 XP Bonus</div>
              </div>
            </div>
          </div>

        </div><!-- /.path-track -->
      </div><!-- /.timeline-chapter -->
    `;
  });

  html += `</div><!-- /.busuu-timeline -->`;

  document.getElementById('main-content').innerHTML = html;
  renderSidebarChapters(levelModules);
}

/* Sidebar Chapter Quick Jump */
function renderSidebarChapters(modules) {
  const container = document.getElementById('sidebar-chapters');
  if (!container) return;
  container.innerHTML = `
    <div style="font-size:0.75rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:8px">Kapitel im Überblick:</div>
    ${modules.map(m => `
      <div style="padding:7px 10px;border-radius:8px;font-size:0.8rem;color:var(--text-secondary);cursor:pointer;display:flex;align-items:center;gap:8px;transition:var(--transition);margin-bottom:4px"
           onmouseover="this.style.background='var(--bg-surface-elevated)';this.style.color='var(--text-primary)'"
           onmouseout="this.style.background='transparent';this.style.color='var(--text-secondary)'"
           onclick="scrollToChapter(${m.id})">
        <span>${m.icon}</span>
        <span style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${m.title}</span>
      </div>
    `).join('')}
  `;
}

function scrollToChapter(chapterId) {
  const el = document.getElementById(`chapter-${chapterId}`);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/* ============================================
   BUSUU MICRO-LESSON RUNNER (CARD-BY-CARD FLOW)
   ============================================ */
let runnerState = {
  lesson: null,
  steps: [],
  currentStepIndex: 0,
  score: 0,
  viewMode: 'flow' // 'flow' | 'reference'
};

function startLessonFlow(lessonId) {
  const lesson = LESSONS.find(l => l.id === lessonId);
  if (!lesson) return;
  if (!isLessonUnlocked(lessonId)) return;

  state.currentLesson = lessonId;
  saveState();
  soundEngine.click();

  // Extract lesson assets to construct 6 to 7 Busuu micro-learning steps
  const vocabItems = extractVocabItems(lesson);
  const grammarSection = (lesson.lectureContent || []).find(s => s.type === 'grammar');
  const dialogueLines = lesson.dialogue || [];
  const exercises = lesson.exercises || [];

  const steps = [];

  // Step 1: Vocab Discovery (Target word 1)
  const v1 = vocabItems[0] || { de: lesson.titleDe, en: lesson.title, ex: 'Ich lerne Deutsch in Berlin.' };
  steps.push({
    type: 'vocab_intro',
    title: 'Neues Wort entdecken',
    word: v1.de,
    gender: guessGender(v1.de),
    meaning: v1.en,
    example: v1.ex,
    exampleEn: v1.exEn || 'Example in context',
    spanishTip: getSpanishTip(lesson)
  });

  // Step 2: Immediate Recall Micro-Drill
  const recallOptions = buildRecallOptions(v1, vocabItems);
  steps.push({
    type: 'micro_drill',
    instruction: 'Wähle die richtige Bedeutung:',
    prompt: v1.de,
    options: recallOptions.options,
    correctIndex: recallOptions.correctIndex,
    explanation: `"${v1.de}" bedeutet auf Englisch "${v1.en}".`
  });

  // Step 3: Busuu Grammar Snapshot
  if (grammarSection) {
    steps.push({
      type: 'grammar_snapshot',
      title: 'Busuu Grammatik-Tipp',
      sectionTitle: grammarSection.sectionTitle,
      htmlContent: grammarSection.content,
      lessonId: lesson.id
    });
  }

  // Step 4: Native Dialogue in Action
  if (dialogueLines.length > 0) {
    steps.push({
      type: 'dialogue',
      title: 'Echtes Gespräch in Berlin',
      dialogue: dialogueLines
    });
  }

  // Step 5: Sentence Builder (Word Tiles)
  const reorderEx = exercises.find(e => e.type === 'reorder') || {
    answer: v1.ex || `${v1.de} ist wichtig für mich.`
  };
  steps.push({
    type: 'sentence_builder',
    title: 'Satzbau-Meister',
    targetSentence: reorderEx.answer
  });

  // Step 6: Active Production (Speaking / Writing with Herr Professor)
  steps.push({
    type: 'active_production',
    title: 'Jetzt bist du dran: Sprich oder schreibe!',
    prompt: lesson.goetheWriting?.situation || `Schreibe oder sprich 1–2 Sätze über das Thema "${lesson.titleDe}".`,
    points: lesson.goetheWriting?.points || ['Beschreibe kurz deine Situation.', 'Nutze weil oder deshalb.'],
    modelAnswer: lesson.goetheWriting?.modelAnswer || 'Hallo! Ich bin in Berlin und lerne Deutsch.'
  });

  // Step 7: Celebration Screen
  steps.push({
    type: 'celebration',
    title: 'Lektion abgeschlossen!',
    lessonId: lesson.id
  });

  runnerState = {
    lesson: lesson,
    steps: steps,
    currentStepIndex: 0,
    score: 0,
    viewMode: 'flow'
  };

  renderRunner();
}

function renderRunner() {
  const { lesson, steps, currentStepIndex, viewMode } = runnerState;
  const currentStep = steps[currentStepIndex];
  const progressPct = Math.round(((currentStepIndex) / (steps.length - 1)) * 100);

  let html = `
    <div class="busuu-runner">
      <!-- Runner Top Bar -->
      <div class="runner-topbar">
        <button class="btn-runner-close" onclick="showDashboard()" title="Zurück zum Lernpfad">✕</button>
        
        <div class="runner-progress-container" title="Fortschritt">
          <div class="runner-progress-fill" style="width:${progressPct}%"></div>
        </div>

        <div class="runner-step-badge">
          Schritt ${currentStepIndex + 1} von ${steps.length}
        </div>

        <button class="runner-mode-toggle" onclick="toggleRunnerViewMode()">
          ${viewMode === 'flow' ? '📖 Alle Inhalte (Referenz)' : '⚡ Busuu Flow'}
        </button>
      </div>
  `;

  if (viewMode === 'reference') {
    html += renderReferenceView(lesson);
  } else {
    html += `
      <div class="runner-card" id="runner-card-content">
        ${renderRunnerStepContent(currentStep, currentStepIndex)}
      </div>
    `;
  }

  html += `</div>`;
  document.getElementById('main-content').innerHTML = html;

  // Auto-play audio on Step 1 (Vocab) if sound enabled
  if (currentStep.type === 'vocab_intro' && state.soundEnabled) {
    setTimeout(() => speakGerman(currentStep.word), 400);
  }

  // Trigger celebration effects on final step
  if (currentStep.type === 'celebration') {
    onLessonCompleted(lesson.id);
  }
}

function toggleRunnerViewMode() {
  runnerState.viewMode = runnerState.viewMode === 'flow' ? 'reference' : 'flow';
  renderRunner();
}

function renderRunnerStepContent(step, idx) {
  if (step.type === 'vocab_intro') {
    return `
      <div class="vocab-stage">
        <div class="vocab-category-tag">💬 Neues Wort entdecken</div>
        <div class="vocab-word-hero">${step.word}</div>
        <div class="vocab-gender-pill gender-${step.gender}">${step.gender.toUpperCase()}</div>
        
        <button class="audio-hero-btn" onclick="speakGerman('${step.word.replace(/'/g, "\\'")}')" title="Anhören">
          🔊
        </button>

        <div class="vocab-meaning">${step.meaning}</div>

        <div class="spanish-helper-box">
          <div class="spanish-helper-header">🇪🇸 Für Guillermo (Spanisch-Sprecher)</div>
          <div class="spanish-helper-text">${step.spanishTip}</div>
        </div>

        <div class="berlin-example-box">
          <div class="berlin-example-label">📍 Im Berliner Alltag</div>
          <div class="berlin-example-de">
            <span>„${step.example}“</span>
            <button class="audio-btn" onclick="speakGerman('${step.example.replace(/'/g, "\\'")}')">🔊</button>
          </div>
          <div class="berlin-example-en">${step.exampleEn}</div>
        </div>

        <button class="btn-primary" style="width:100%;margin-top:auto" onclick="nextRunnerStep()">
          Weiter →
        </button>
      </div>
    `;
  }

  if (step.type === 'micro_drill') {
    return `
      <div class="micro-drill-stage">
        <div class="drill-instruction">${step.instruction}</div>
        <div class="drill-question-box">
          <div class="drill-question-text">${step.prompt}</div>
          <button class="audio-btn" style="margin-top:8px" onclick="speakGerman('${step.prompt.replace(/'/g, "\\'")}')">🔊 Anhören</button>
        </div>

        <div class="drill-options-grid" id="drill-options">
          ${step.options.map((opt, oIdx) => `
            <button class="drill-option-btn" id="drill-opt-${oIdx}" onclick="handleDrillAnswer(${oIdx}, ${step.correctIndex}, '${step.explanation.replace(/'/g, "\\'")}')">
              <span style="color:var(--text-muted);font-size:0.85rem">${String.fromCharCode(65 + oIdx)}.</span>
              <span>${opt}</span>
            </button>
          `).join('')}
        </div>

        <div id="drill-feedback-container"></div>
      </div>
    `;
  }

  if (step.type === 'grammar_snapshot') {
    return `
      <div class="grammar-snapshot-stage">
        <div class="vocab-category-tag" style="background:rgba(245,158,11,0.15);color:#fbbf24">
          📖 ${step.title}
        </div>
        
        <div class="grammar-hero-card">
          <h3 style="color:#fbbf24;margin-bottom:12px">${step.sectionTitle}</h3>
          <div class="grammar-rule-summary">
            ${step.htmlContent}
          </div>
        </div>

        <div class="spanish-helper-box">
          <div class="spanish-helper-header">💡 Satzbau-Geheimnis</div>
          <div class="spanish-helper-text">
            Im Deutschen ist die Verbstellung entscheidend! Im Hauptsatz steht das konjugierte Verb an <strong>Position 2</strong>. In Nebensätzen mit <em>weil/obwohl/dass</em> wandert das Verb ans <strong>Satzende</strong>.
          </div>
        </div>

        <button class="btn-primary" style="width:100%;margin-top:auto" onclick="nextRunnerStep()">
          Verstanden! Weiter →
        </button>
      </div>
    `;
  }

  if (step.type === 'dialogue') {
    return `
      <div class="dialogue-stage">
        <div class="vocab-category-tag" style="background:rgba(16,185,129,0.15);color:#34d399">
          🎧 ${step.title}
        </div>

        <div style="display:flex;justify-content:flex-end;margin-bottom:12px">
          <button class="btn-secondary" style="font-size:0.8rem;padding:6px 14px" onclick="playAllDialogue()">
            ▶ Gespräch ganz abspielen
          </button>
        </div>

        <div class="dialogue-chat-box">
          ${step.dialogue.map((line, dIdx) => {
            const isRight = dIdx % 2 !== 0;
            return `
              <div class="chat-msg-row ${isRight ? 'right' : 'left'}">
                <div class="chat-avatar">${isRight ? '🧑‍💼' : '🙋‍♂️'}</div>
                <div class="chat-bubble">
                  <div class="chat-speaker">${line.speaker || (isRight ? 'Guillermo' : 'Lukas')}</div>
                  <div class="chat-text-de">
                    ${line.de}
                    <button class="play-chat-audio-btn" onclick="speakGerman('${line.de.replace(/'/g, "\\'")}')" title="Anhören">🔊</button>
                  </div>
                  <div class="chat-text-en">${line.en}</div>
                </div>
              </div>
            `;
          }).join('')}
        </div>

        <button class="btn-primary" style="width:100%;margin-top:auto" onclick="nextRunnerStep()">
          Weiter zur Übung →
        </button>
      </div>
    `;
  }

  if (step.type === 'sentence_builder') {
    const rawTokens = step.targetSentence.replace(/[.!?]/g, '').trim().split(/\s+/);
    // Shuffle tokens
    const shuffled = [...rawTokens].sort(() => Math.random() - 0.5);
    window.currentSentenceTokens = rawTokens;
    window.currentDropTokens = [];

    return `
      <div class="tiles-stage">
        <div class="vocab-category-tag" style="background:rgba(139,92,246,0.15);color:#c4b5fd">
          ⚡ ${step.title}
        </div>

        <div style="font-size:0.9rem;color:var(--text-secondary);margin-bottom:12px">
          Tippe auf die Wörter in der richtigen Reihenfolge, um den deutschen Satz zu bilden:
        </div>

        <div class="tiles-drop-area" id="tiles-dropzone" onclick="removeLastTile()">
          <span style="color:var(--text-muted);font-size:0.85rem" id="dropzone-hint">Wähle Wörter unten aus...</span>
        </div>

        <div class="tiles-bank" id="tiles-bank">
          ${shuffled.map((word, wIdx) => `
            <div class="tile-chip" id="tile-${wIdx}" onclick="addTileToDrop('${word.replace(/'/g, "\\'")}', 'tile-${wIdx}')">
              ${word}
            </div>
          `).join('')}
        </div>

        <div id="tile-feedback-box"></div>

        <button class="btn-primary" id="btn-check-tiles" style="width:100%;margin-top:auto" onclick="checkSentenceTiles('${step.targetSentence.replace(/'/g, "\\'")}')">
          Satz überprüfen ✓
        </button>
      </div>
    `;
  }

  if (step.type === 'active_production') {
    return `
      <div class="production-stage">
        <div class="vocab-category-tag" style="background:rgba(245,158,11,0.15);color:#fbbf24">
          ✍️ Aktive Anwendung (Fluency)
        </div>

        <div class="production-prompt-box">
          <div class="production-prompt-title">${step.title}</div>
          <div class="production-prompt-sub">${step.prompt}</div>
          <ul style="margin:10px 0 0 20px;font-size:0.82rem;color:var(--text-secondary)">
            ${step.points.map(p => `<li>${p}</li>`).join('')}
          </ul>
        </div>

        <div class="umlaut-bar">
          <button type="button" class="umlaut-key" onclick="insertRunnerUmlaut('ä')">ä</button>
          <button type="button" class="umlaut-key" onclick="insertRunnerUmlaut('ö')">ö</button>
          <button type="button" class="umlaut-key" onclick="insertRunnerUmlaut('ü')">ü</button>
          <button type="button" class="umlaut-key" onclick="insertRunnerUmlaut('ß')">ß</button>
          <button type="button" class="mic-record-btn" id="btn-runner-mic" onclick="toggleRunnerMic()">
            🎤 Spracheingabe
          </button>
        </div>

        <textarea id="runner-production-text" class="production-textarea" placeholder="Schreibe deinen deutschen Satz hier... (z.B. Ich lerne Deutsch, weil...)"></textarea>

        <div style="display:flex;gap:10px;margin-bottom:14px">
          <button class="btn-secondary" style="flex:1" onclick="gradeRunnerWithProfessor()">
            👨‍🏫 Von Herrn Professor prüfen lassen
          </button>
          <button class="btn-secondary" style="font-size:0.8rem" onclick="toggleRunnerModelAnswer('${step.modelAnswer.replace(/'/g, "\\'")}')">
            💡 Musterlösung
          </button>
        </div>

        <div id="runner-prof-feedback" style="display:none;margin-bottom:16px"></div>

        <button class="btn-primary" style="width:100%;margin-top:auto" onclick="nextRunnerStep()">
          Weiter zum Abschluss →
        </button>
      </div>
    `;
  }

  if (step.type === 'celebration') {
    return `
      <div class="celebration-stage">
        <canvas id="confetti-canvas"></canvas>
        <div class="celebration-trophy">🏆</div>
        <div class="celebration-title">Ausgezeichnet, Guillermo!</div>
        <div class="celebration-sub">Du hast Lektion ${step.lessonId} erfolgreich gemeistert!</div>

        <div class="celebration-stats-grid">
          <div class="celebration-stat-card">
            <div class="celebration-stat-value">+30</div>
            <div class="celebration-stat-label">XP verdient</div>
          </div>
          <div class="celebration-stat-card">
            <div class="celebration-stat-value">⭐⭐⭐</div>
            <div class="celebration-stat-label">3 Sterne</div>
          </div>
          <div class="celebration-stat-card">
            <div class="celebration-stat-value">${state.streak} 🔥</div>
            <div class="celebration-stat-label">Tage-Serie</div>
          </div>
        </div>

        <button class="btn-primary" style="width:100%;max-width:380px" onclick="finishLessonAndGoNext()">
          Nächste Lektion auf dem Lernpfad →
        </button>
      </div>
    `;
  }

  return `<div>Schritt wird geladen...</div>`;
}

function nextRunnerStep() {
  soundEngine.click();
  if (runnerState.currentStepIndex < runnerState.steps.length - 1) {
    runnerState.currentStepIndex++;
    renderRunner();
  }
}

function handleDrillAnswer(chosenIdx, correctIdx, explanation) {
  const isCorrect = chosenIdx === correctIdx;
  const container = document.getElementById('drill-feedback-container');
  const btn = document.getElementById(`drill-opt-${chosenIdx}`);

  // Disable all options
  document.querySelectorAll('.drill-option-btn').forEach(b => b.style.pointerEvents = 'none');

  if (isCorrect) {
    soundEngine.correct();
    btn.classList.add('selected-correct');
    addXp(5);
    container.innerHTML = `
      <div class="runner-feedback-sheet correct">
        <div>
          <div class="feedback-text-title">✓ Ausgezeichnet!</div>
          <div class="feedback-text-desc">${explanation}</div>
        </div>
        <button class="btn-primary" style="padding:10px 22px" onclick="nextRunnerStep()">
          Weiter →
        </button>
      </div>
    `;
  } else {
    soundEngine.wrong();
    btn.classList.add('selected-wrong');
    const correctBtn = document.getElementById(`drill-opt-${correctIdx}`);
    if (correctBtn) correctBtn.classList.add('selected-correct');

    container.innerHTML = `
      <div class="runner-feedback-sheet wrong">
        <div>
          <div class="feedback-text-title">Fast richtig!</div>
          <div class="feedback-text-desc">${explanation}</div>
        </div>
        <button class="btn-secondary" style="padding:10px 22px" onclick="nextRunnerStep()">
          Weiter →
        </button>
      </div>
    `;
  }
}

function addTileToDrop(word, tileId) {
  soundEngine.click();
  const tileEl = document.getElementById(tileId);
  if (!tileEl) return;
  tileEl.classList.add('disabled');

  window.currentDropTokens.push({ word, tileId });
  renderDropTokens();
}

function removeLastTile() {
  if (!window.currentDropTokens || window.currentDropTokens.length === 0) return;
  const last = window.currentDropTokens.pop();
  const tileEl = document.getElementById(last.tileId);
  if (tileEl) tileEl.classList.remove('disabled');
  renderDropTokens();
}

function renderDropTokens() {
  const dropzone = document.getElementById('tiles-dropzone');
  if (!dropzone) return;

  if (window.currentDropTokens.length === 0) {
    dropzone.innerHTML = `<span style="color:var(--text-muted);font-size:0.85rem">Wähle Wörter unten aus...</span>`;
    dropzone.classList.remove('filled');
    return;
  }

  dropzone.classList.add('filled');
  dropzone.innerHTML = window.currentDropTokens.map(item => `
    <div class="tile-chip in-drop">${item.word}</div>
  `).join('');
}

function checkSentenceTiles(expectedSentence) {
  const assembled = window.currentDropTokens.map(t => t.word).join(' ').trim();
  const cleanTarget = expectedSentence.replace(/[.!?]/g, '').trim();
  const box = document.getElementById('tile-feedback-box');
  const btn = document.getElementById('btn-check-tiles');

  if (assembled.toLowerCase() === cleanTarget.toLowerCase()) {
    soundEngine.correct();
    speakGerman(expectedSentence);
    addXp(10);
    box.innerHTML = `
      <div class="runner-feedback-sheet correct" style="margin-bottom:16px">
        <div>
          <div class="feedback-text-title">✓ Perfekt zusammengesetzt!</div>
          <div class="feedback-text-desc">„${expectedSentence}“</div>
        </div>
      </div>
    `;
    btn.innerText = 'Weiter →';
    btn.onclick = nextRunnerStep;
  } else {
    soundEngine.wrong();
    box.innerHTML = `
      <div class="runner-feedback-sheet wrong" style="margin-bottom:16px">
        <div>
          <div class="feedback-text-title">Nicht ganz richtig</div>
          <div class="feedback-text-desc">Richtige Reihenfolge: <strong>${expectedSentence}</strong></div>
        </div>
      </div>
    `;
    btn.innerText = 'Weiter →';
    btn.onclick = nextRunnerStep;
  }
}

function insertRunnerUmlaut(char) {
  const tx = document.getElementById('runner-production-text');
  if (!tx) return;
  const start = tx.selectionStart;
  const end = tx.selectionEnd;
  tx.value = tx.value.substring(0, start) + char + tx.value.substring(end);
  tx.focus();
  tx.selectionStart = tx.selectionEnd = start + 1;
}

let runnerRecognition = null;
function toggleRunnerMic() {
  const btn = document.getElementById('btn-runner-mic');
  const tx = document.getElementById('runner-production-text');
  const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRec) {
    alert('Spracherkennung wird von diesem Browser nicht nativ unterstützt. Bitte verwende Chrome oder Edge!');
    return;
  }

  if (runnerRecognition) {
    runnerRecognition.stop();
    runnerRecognition = null;
    if (btn) btn.classList.remove('recording');
    return;
  }

  runnerRecognition = new SpeechRec();
  runnerRecognition.lang = 'de-DE';
  runnerRecognition.continuous = false;
  runnerRecognition.interimResults = false;

  runnerRecognition.onstart = () => {
    if (btn) btn.classList.add('recording');
    btn.innerText = '🔴 Aufnahme läuft... Sprich jetzt!';
  };

  runnerRecognition.onresult = (e) => {
    const transcript = e.results[0][0].transcript;
    if (tx) tx.value += (tx.value ? ' ' : '') + transcript;
  };

  runnerRecognition.onerror = () => {
    if (btn) {
      btn.classList.remove('recording');
      btn.innerText = '🎤 Spracheingabe';
    }
  };

  runnerRecognition.onend = () => {
    if (btn) {
      btn.classList.remove('recording');
      btn.innerText = '🎤 Spracheingabe';
    }
    runnerRecognition = null;
  };

  runnerRecognition.start();
}

function gradeRunnerWithProfessor() {
  const text = (document.getElementById('runner-production-text')?.value || '').trim();
  const box = document.getElementById('runner-prof-feedback');
  if (!box) return;

  if (!text) {
    alert('Bitte schreibe zuerst einen Satz auf Deutsch oder nutze das Mikrofon!');
    return;
  }

  box.style.display = 'block';
  box.innerHTML = `<div style="color:#fbbf24;padding:12px;text-align:center">👨‍🏫 Herr Professor analysiert deinen Satzbau...</div>`;

  setTimeout(() => {
    let corrections = [];
    if (/weil\s+([a-zäöü]+)\s+(bin|habe|ist|kann|muss|wohne|arbeite)/i.test(text)) {
      corrections.push(`⚠️ <strong>Verbstellung bei „weil“:</strong> Das Verb muss ans Satzende: <em>... weil ich in Berlin <strong>arbeite</strong></em>.`);
    }
    if (/obwohl\s+([a-zäöü]+)\s+(bin|habe|ist|kann|muss)/i.test(text)) {
      corrections.push(`⚠️ <strong>Verbstellung bei „obwohl“:</strong> Auch hier gehört das Verb ans Satzende!`);
    }

    let html = `
      <div class="berlin-example-box" style="border-color:#fbbf24">
        <div style="font-weight:700;color:#fbbf24;margin-bottom:6px">👨‍🏫 Urteil von Herrn Professor:</div>
        <div style="font-size:0.9rem;line-height:1.45;color:var(--text-primary)">
          ${corrections.length > 0 ? corrections.join('<br>') : '✅ <strong>Sehr gut gemacht!</strong> Der Satzbau und die Verbstellung stimmen mit den A2/B1-Regeln überein.'}
        </div>
        <div style="font-size:0.78rem;color:var(--text-secondary);margin-top:8px">
          💡 <em>Tipp:</em> Du kannst diesen Satz auch direkt in den Professor-Chat kopieren für ausführliche Konversation!
        </div>
      </div>
    `;
    box.innerHTML = html;
    addXp(10);
  }, 350);
}

function toggleRunnerModelAnswer(answer) {
  const box = document.getElementById('runner-prof-feedback');
  if (!box) return;
  box.style.display = 'block';
  box.innerHTML = `
    <div class="berlin-example-box">
      <div style="font-weight:700;color:#34d399;margin-bottom:6px">💡 Musterlösung:</div>
      <div style="font-size:0.95rem;color:var(--text-primary);font-style:italic">„${answer}“</div>
      <button class="audio-btn" style="margin-top:8px" onclick="speakGerman('${answer.replace(/'/g, "\\'")}')">🔊 Vorlesen lassen</button>
    </div>
  `;
}

function playAllDialogue() {
  const step = runnerState.steps[runnerState.currentStepIndex];
  if (!step || !step.dialogue) return;

  let delay = 0;
  step.dialogue.forEach(line => {
    setTimeout(() => speakGerman(line.de), delay);
    // Rough estimate of speech duration based on word count
    delay += Math.max(2200, line.de.split(' ').length * 400);
  });
}

function onLessonCompleted(lessonId) {
  soundEngine.fanfare();
  state.completedLessons[lessonId] = {
    stars: 3,
    score: 100,
    completedAt: new Date().toISOString()
  };
  addXp(30);
  updateStreak();
  saveState();

  // Trigger canvas confetti
  setTimeout(() => launchConfetti(), 200);
}

function finishLessonAndGoNext() {
  const nextId = runnerState.lesson.id + 1;
  const nextLesson = LESSONS.find(l => l.id === nextId);

  if (nextLesson && isLessonUnlocked(nextId)) {
    startLessonFlow(nextId);
  } else {
    showDashboard();
  }
}

/* Confetti Particle System */
function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  canvas.width = canvas.parentElement.clientWidth;
  canvas.height = canvas.parentElement.clientHeight;

  const pieces = [];
  const colors = ['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#fbbf24'];

  for (let i = 0; i < 70; i++) {
    pieces.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height - canvas.height,
      size: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      speedY: Math.random() * 4 + 2,
      speedX: (Math.random() - 0.5) * 3,
      rotation: Math.random() * 360,
      rotationSpeed: (Math.random() - 0.5) * 8
    });
  }

  let animationFrame;
  let elapsed = 0;

  function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    pieces.forEach(p => {
      p.y += p.speedY;
      p.x += p.speedX;
      p.rotation += p.rotationSpeed;

      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rotation * Math.PI) / 180);
      ctx.fillStyle = p.color;
      ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
      ctx.restore();
    });

    elapsed++;
    if (elapsed < 140) {
      animationFrame = requestAnimationFrame(update);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

  update();
}

/* Chapter Milestone Checkpoint Launcher */
function openChapterMilestone(moduleId) {
  const mod = MODULES.find(m => m.id === moduleId);
  if (!mod) return;

  const confirmStart = confirm(`Möchtest du den Meilenstein-Abschlusstest für Kapitel ${mod.id} (${mod.title}) starten?`);
  if (!confirmStart) return;

  const firstLessonId = mod.lessons[0];
  startLessonFlow(firstLessonId);
}

/* Helpers to Extract Vocab and Build Recalls */
function extractVocabItems(lesson) {
  const items = [];
  (lesson.lectureContent || []).forEach(sec => {
    if (sec.type === 'vocabulary') {
      const rowMatches = sec.content.matchAll(/<tr>\s*<td>(<strong>)?([^<]+)(<\/strong>)?<\/td>\s*<td>([^<]+)<\/td>\s*<td>([^<]*)<\/td>/gi);
      for (const m of rowMatches) {
        items.push({
          de: m[2].trim(),
          en: m[4].trim(),
          ex: m[5].trim() || 'Ich mag das sehr.'
        });
      }
    }
  });
  return items;
}

function guessGender(deWord) {
  const lower = deWord.toLowerCase();
  if (lower.startsWith('der ') || lower.includes('(der)')) return 'der';
  if (lower.startsWith('die ') || lower.includes('(die)')) return 'die';
  if (lower.startsWith('das ') || lower.includes('(das)')) return 'das';
  return 'other';
}

function buildRecallOptions(correctItem, allItems) {
  const distractors = allItems
    .filter(it => it.en !== correctItem.en)
    .map(it => it.en);
  
  // Fallbacks if not enough distractors
  const fallbacks = ['to arrive', 'friendly', 'happy', 'busy', 'because of', 'together'];
  while (distractors.length < 3) {
    distractors.push(fallbacks.pop());
  }

  // Pick 3 random distractors
  const chosenDistractors = distractors.sort(() => Math.random() - 0.5).slice(0, 3);
  const options = [...chosenDistractors, correctItem.en].sort(() => Math.random() - 0.5);
  const correctIndex = options.indexOf(correctItem.en);

  return { options, correctIndex };
}

/* Reference Mode Renderer (Full Lecture Tables & Exercises) */
function renderReferenceView(lesson) {
  return `
    <div style="background:var(--bg-surface);border:1px solid var(--border-subtle);border-radius:var(--radius-xl);padding:32px;box-shadow:var(--shadow-card)">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
        <div>
          <h2 style="color:var(--text-primary)">${lesson.icon} Lektion ${lesson.id}: ${lesson.titleDe}</h2>
          <div style="color:var(--text-secondary);font-size:0.9rem">${lesson.title}</div>
        </div>
        <button class="btn-primary" onclick="toggleRunnerViewMode()">⚡ Zurück zum Busuu Flow</button>
      </div>

      <div class="reference-content">
        ${(lesson.lectureContent || []).map(sec => `
          <div style="margin-bottom:28px">
            <h3 style="color:#60a5fa;margin-bottom:12px;border-bottom:1px solid var(--border-subtle);padding-bottom:6px">${sec.sectionTitle}</h3>
            <div>${sec.content}</div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

/* ============================================
   ARENAS (SURVIVAL, GOETHE, TRAINER, PROFESSOR)
   ============================================ */
/* Survival Simulator */
function renderSurvivalSimulator() {
  document.getElementById('main-content').innerHTML = `
    <div style="max-width:800px;margin:0 auto">
      <div class="chapter-banner">
        <div class="chapter-badge">Berlin Alltags-Simulator</div>
        <div class="chapter-title">🌆 Reale Lebenssituationen in Berlin</div>
        <div class="chapter-desc">Wähle ein praxisnahes Szenario, um echte Konversationen und typische bürokratische Hürden zu trainieren.</div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-bottom:32px">
        <div class="stone-card-preview" style="max-width:none;text-align:left;padding:20px;cursor:pointer" onclick="startSurvivalScenario('buergeramt')">
          <div style="font-size:2rem;margin-bottom:8px">🏛️</div>
          <div style="font-size:1.1rem;font-weight:800;color:var(--text-primary)">Anmeldung beim Bürgeramt</div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin:6px 0 12px">Wohnungsgeberbestätigung, Reisepass & Meldebescheinigung in Berlin Mitte.</div>
          <button class="btn-primary" style="padding:8px 16px;font-size:0.85rem">Starten →</button>
        </div>

        <div class="stone-card-preview" style="max-width:none;text-align:left;padding:20px;cursor:pointer" onclick="startSurvivalScenario('wg')">
          <div style="font-size:2rem;margin-bottom:8px">🔑</div>
          <div style="font-size:1.1rem;font-weight:800;color:var(--text-primary)">Wohnungsbesichtigung</div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin:6px 0 12px">Gespräch mit dem Vermieter in Neukölln, Kaution & Schufa-Auskunft.</div>
          <button class="btn-primary" style="padding:8px 16px;font-size:0.85rem">Starten →</button>
        </div>

        <div class="stone-card-preview" style="max-width:none;text-align:left;padding:20px;cursor:pointer" onclick="startSurvivalScenario('standup')">
          <div style="font-size:2rem;margin-bottom:8px">💼</div>
          <div style="font-size:1.1rem;font-weight:800;color:var(--text-primary)">Projekt-Meeting & Standup</div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin:6px 0 12px">Status-Updates, Termine verschieben & Fristen mit Kollegen besprechen.</div>
          <button class="btn-primary" style="padding:8px 16px;font-size:0.85rem">Starten →</button>
        </div>
      </div>

      <div id="survival-active-arena"></div>
    </div>
  `;
}

function startSurvivalScenario(key) {
  const arena = document.getElementById('survival-active-arena');
  if (!arena) return;

  const scenarios = {
    buergeramt: {
      title: 'Beim Bürgeramt Berlin',
      prompt: 'Beamter: „Guten Tag! Haben Sie einen Termin und Ihre Wohnungsgeberbestätigung dabei?“',
      options: [
        { text: '„Ja, hier ist meine Bestätigung vom Vermieter und mein Pass.“', correct: true, feedback: 'Perfekt und höflich!' },
        { text: '„Nein, ich will nur Bier trinken.“', correct: false, feedback: 'Das Bürgeramt ist keine Kneipe!' },
        { text: '„Ich weiß nicht, was das ist.“', correct: false, feedback: 'Zu unvorbereitet für eine offizielle Behörde.' }
      ]
    },
    wg: {
      title: 'Wohnungsbesichtigung in Berlin',
      prompt: 'Vermieter: „Ab wann könnten Sie die Wohnung mieten und wie hoch ist Ihr Nettoeinkommen?“',
      options: [
        { text: '„Ich könnte ab dem 1. nächsten Monats einziehen. Mein Nettoeinkommen liegt bei ca. 2.800 Euro.“', correct: true, feedback: 'Ausgezeichnet! Genau die Information, die der Vermieter braucht.' },
        { text: '„Gestern war schön.“', correct: false, feedback: 'Antwort passt nicht zur Frage.' }
      ]
    },
    standup: {
      title: 'Projekt-Standup Meeting',
      prompt: 'Teamleiter: „Guillermo, wie ist der aktuelle Stand bei den Projektfristen?“',
      options: [
        { text: '„Wir liegen gut im Zeitplan, aber wir müssen die Frist für Modul 2 um zwei Tage verschieben.“', correct: true, feedback: 'Professionell und präzise auf B1-Niveau!' },
        { text: '„Ich habe keine Lust mehr.“', correct: false, feedback: 'Nicht professionell im Meeting.' }
      ]
    }
  };

  const sc = scenarios[key];
  if (!sc) return;

  arena.innerHTML = `
    <div class="runner-card" style="min-height:auto;margin-top:20px">
      <h3 style="color:#60a5fa;margin-bottom:12px">${sc.title}</h3>
      <div class="drill-question-box">
        <div class="drill-question-text">${sc.prompt}</div>
        <button class="audio-btn" style="margin-top:8px" onclick="speakGerman('${sc.prompt.replace(/'/g, "\\'")}')">🔊 Anhören</button>
      </div>

      <div class="drill-options-grid">
        ${sc.options.map((opt, i) => `
          <button class="drill-option-btn" onclick="alert('${opt.feedback}'); if(${opt.correct}) addXp(15);">
            ${opt.text}
          </button>
        `).join('')}
      </div>
    </div>
  `;
}

/* Goethe Center */
function renderGoetheCenter() {
  document.getElementById('main-content').innerHTML = `
    <div style="max-width:800px;margin:0 auto">
      <div class="chapter-banner">
        <div class="chapter-badge">Prüfungszentrum</div>
        <div class="chapter-title">🏛️ Offizielles Goethe-Zertifikat Training</div>
        <div class="chapter-desc">Vorbereitung auf die Goethe-Zertifikat A2 und B1 Prüfungen: Lesen, Hören, Schreiben und Sprechen.</div>
      </div>

      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px">
        <div class="stone-card-preview" style="max-width:none;text-align:left;padding:20px">
          <div style="font-size:1.8rem">📖</div>
          <div style="font-weight:800;font-size:1.05rem;color:var(--text-primary);margin:6px 0">Goethe-Schreiben (E-Mail)</div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:12px">Schreibe formelle und informelle Briefe anhand von 3 Leitpunkten mit automatischer Bewertung.</div>
          <button class="btn-primary" style="font-size:0.82rem;padding:8px 16px" onclick="startLessonFlow(1)">Im Flow üben →</button>
        </div>

        <div class="stone-card-preview" style="max-width:none;text-align:left;padding:20px">
          <div style="font-size:1.8rem">🎙️</div>
          <div style="font-weight:800;font-size:1.05rem;color:var(--text-primary);margin:6px 0">Goethe-Sprechen (Dialog)</div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:12px">Gemeinsam etwas planen und Meinung äußern mit Mikrofon-Spracherkennung.</div>
          <button class="btn-primary" style="font-size:0.82rem;padding:8px 16px" onclick="startLessonFlow(1)">Im Flow üben →</button>
        </div>
      </div>
    </div>
  `;
}

/* Drill Trainer */
function renderDrillTrainer() {
  const nouns = [
    { word: 'Tisch', article: 'der' },
    { word: 'Sonne', article: 'die' },
    { word: 'Buch', article: 'das' },
    { word: 'Wohnung', article: 'die' },
    { word: 'Bier', article: 'das' },
    { word: 'Mann', article: 'der' },
    { word: 'Mädchen', article: 'das' },
    { word: 'Freiheit', article: 'die' }
  ];
  const item = nouns[Math.floor(Math.random() * nouns.length)];

  document.getElementById('main-content').innerHTML = `
    <div style="max-width:600px;margin:0 auto">
      <div class="chapter-banner">
        <div class="chapter-badge">Sprint Trainer</div>
        <div class="chapter-title">⚡ Der / Die / Das Schnell-Trainer</div>
        <div class="chapter-desc">Trainiere die Artikel reflexartig und sammle Blitz-XP!</div>
      </div>

      <div class="runner-card" style="text-align:center;align-items:center">
        <div style="font-size:2.8rem;font-weight:800;color:var(--text-primary);margin:24px 0">${item.word}</div>
        
        <div style="display:flex;gap:12px;width:100%;max-width:380px;margin-bottom:24px">
          <button class="btn-primary" style="flex:1;background:var(--busuu-blue)" onclick="checkArticleAnswer('der', '${item.article}')">der</button>
          <button class="btn-primary" style="flex:1;background:#ef4444" onclick="checkArticleAnswer('die', '${item.article}')">die</button>
          <button class="btn-primary" style="flex:1;background:#10b981" onclick="checkArticleAnswer('das', '${item.article}')">das</button>
        </div>

        <div id="trainer-feedback"></div>
      </div>
    </div>
  `;
}

function checkArticleAnswer(chosen, correct) {
  const box = document.getElementById('trainer-feedback');
  if (chosen === correct) {
    soundEngine.correct();
    addXp(5);
    box.innerHTML = `<div style="color:#34d399;font-weight:700">✓ Richtig! ${correct}</div>`;
  } else {
    soundEngine.wrong();
    box.innerHTML = `<div style="color:#f87171;font-weight:700">Falsch! Richtig ist: ${correct}</div>`;
  }
  setTimeout(() => renderDrillTrainer(), 800);
}

/* ============================================
   HERR PROFESSOR HUB (AI & CHAT ASSISTANT)
   ============================================ */
let profState = {
  apiKey: localStorage.getItem('deutschmeister_gemini_key') || '',
  langPref: localStorage.getItem('deutschmeister_lang_pref') || 'de_en'
};

function toggleProfessorHub() {
  document.getElementById('professor-hub')?.classList.toggle('open');
  document.getElementById('professor-backdrop')?.classList.toggle('open');
}

function closeProfessorHub() {
  document.getElementById('professor-hub')?.classList.remove('open');
  document.getElementById('professor-backdrop')?.classList.remove('open');
}

function switchProfTab(tab) {
  document.querySelectorAll('.prof-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.prof-tab-content').forEach(c => c.classList.remove('active'));

  document.getElementById(`prof-tab-btn-${tab}`)?.classList.add('active');
  document.getElementById(`prof-content-${tab}`)?.classList.add('active');
}

function insertUmlautProf(c) {
  const tx = document.getElementById('prof-corrector-text');
  if (!tx) return;
  const start = tx.selectionStart;
  const end = tx.selectionEnd;
  tx.value = tx.value.substring(0, start) + c + tx.value.substring(end);
  tx.focus();
  tx.selectionStart = tx.selectionEnd = start + 1;
}

function saveApiKey() {
  const key = document.getElementById('prof-api-key-input')?.value.trim();
  profState.apiKey = key;
  localStorage.setItem('deutschmeister_gemini_key', key);
  showProfToast('Google Gemini API Key gespeichert! 🔑');
}

function saveProfLangPref() {
  const pref = document.getElementById('prof-lang-pref')?.value;
  profState.langPref = pref;
  localStorage.setItem('deutschmeister_lang_pref', pref);
}

function toggleApiKeyVisibility() {
  const inp = document.getElementById('prof-api-key-input');
  if (inp) inp.type = inp.type === 'password' ? 'text' : 'password';
}

function showProfToast(msg) {
  const t = document.getElementById('prof-toast');
  if (!t) return;
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2400);
}

function askProfSuggestion(q) {
  const inp = document.getElementById('prof-chat-input');
  if (inp) {
    inp.value = q;
    sendProfChatMessage(new Event('submit'));
  }
}

async function sendProfChatMessage(e) {
  if (e) e.preventDefault();
  const inp = document.getElementById('prof-chat-input');
  const text = (inp?.value || '').trim();
  if (!text) return;

  inp.value = '';
  appendProfMsg('user', text);

  // Gemini API call if key present
  if (profState.apiKey) {
    try {
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${profState.apiKey}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{
            role: 'user',
            parts: [{ text: `Du bist Herr Professor, ein freundlicher, hochqualifizierter Deutschlehrer in Berlin. Du unterrichtest Guillermo (Muttersprache Spanisch aus Honduras, lebt in Berlin, Master in International Business Management, arbeitet als Projektmanager).
Antworte präzise auf Deutsch auf A2/B1-Niveau mit kurzen spanischen/englischen Erklärungen für Grammatik:
${text}` }]
          }]
        })
      });
      const data = await response.json();
      const reply = data?.candidates?.[0]?.content?.parts?.[0]?.text;
      if (reply) {
        appendProfMsg('professor', reply);
        return;
      }
    } catch(err) {}
  }

  // Heuristic fallbacks
  setTimeout(() => {
    let reply = `<strong>Sehr gute Frage, Guillermo!</strong><br><br>`;
    if (/weil/i.test(text)) {
      reply += `„Weil“ ist ein subordinierender Konnektor (Kausalsatz). Das finite Verb wandert immer ans <strong>Ende</strong> des Nebensatzes:<br><em>„Ich lerne Deutsch, weil ich in Berlin <strong>arbeite</strong>.“</em>`;
    } else if (/deshalb|deswegen/i.test(text)) {
      reply += `„Deshalb“ ist ein Konjunktionaladverb. Es steht auf Position 1 im Hauptsatz und verlangt <strong>Inversion</strong> (Verb sofort auf Position 2):<br><em>„Ich lebe in Berlin, deshalb <strong>lerne</strong> ich Deutsch.“</em>`;
    } else {
      reply += `Ich habe deine Nachricht erhalten. Im deutschen Alltag in Berlin sind klare Sätze mit der richtigen Verbstellung der Schlüssel zum Erfolg! Frag mich gerne nach Beispielen oder gib mir einen Satz zur Korrektur.`;
    }
    appendProfMsg('professor', reply);
  }, 400);
}

function appendProfMsg(sender, text) {
  const box = document.getElementById('prof-chat-messages');
  if (!box) return;
  const msgEl = document.createElement('div');
  msgEl.className = `prof-msg ${sender}`;
  msgEl.innerHTML = `
    <div class="prof-msg-avatar">${sender === 'professor' ? '👨‍🏫' : '🙋‍♂️'}</div>
    <div class="prof-msg-bubble">${text}</div>
  `;
  box.appendChild(msgEl);
  box.scrollTop = box.scrollHeight;
}

function analyzeTextWithProfessor() {
  const tx = document.getElementById('prof-corrector-text');
  const text = (tx?.value || '').trim();
  const res = document.getElementById('prof-corrector-result');
  if (!res) return;

  if (!text) {
    alert('Bitte gib zuerst einen Satz auf Deutsch ein!');
    return;
  }

  res.style.display = 'block';
  res.innerHTML = `<div style="color:#fbbf24;text-align:center">👨‍🏫 Herr Professor analysiert Satzbau, Verbstellung und Grammatik...</div>`;

  setTimeout(() => {
    let issues = [];
    if (/weil\s+([a-zäöü]+)\s+(bin|habe|ist|kann|muss|wohne|arbeite)/i.test(text)) {
      issues.push(`⚠️ <strong>Verbstellung bei „weil“:</strong> Das Verb muss ans Satzende: <em>... weil ich in Berlin <strong>arbeite</strong></em>.`);
    }
    if (/deshalb\s+([a-zäöü]+)\s+(bin|habe|ist|kann|muss)/i.test(text)) {
      issues.push(`⚠️ <strong>Inversion bei „deshalb“:</strong> Das Verb muss direkt nach <em>deshalb</em> stehen: <em>... deshalb <strong>lerne</strong> ich</em>.`);
    }

    let html = `<div style="font-weight:700;color:#fbbf24;margin-bottom:8px">📋 Analyse von Herrn Professor:</div>`;
    if (issues.length > 0) {
      html += `<div style="background:rgba(239,68,68,0.1);border-left:3px solid var(--danger-red);padding:10px;margin-bottom:12px;border-radius:4px">${issues.join('<br><br>')}</div>`;
    } else {
      html += `<div style="background:rgba(16,185,129,0.1);border-left:3px solid var(--success-green);padding:10px;margin-bottom:12px;border-radius:4px">✅ <strong>Sehr gut!</strong> Keine offensichtlichen Satzbaufehler bei den Konnektoren gefunden.</div>`;
    }
    res.innerHTML = html;
  }, 400);
}

function copyTextForChat() {
  const text = (document.getElementById('prof-corrector-text')?.value || '').trim();
  const exportText = `Hallo Professor! Hier ist meine Aufgabe:

${text}

Kannst du meine Sätze bitte analysieren und korrigieren?`;
  navigator.clipboard.writeText(exportText).then(() => showProfToast('Kopiert! Füge es im Chat ein 📋'));
}

/* Utilities */
function toggleSidebar() {
  document.getElementById('sidebar')?.classList.toggle('open');
}

function resetProgress() {
  if (confirm('Bist du sicher? Aller Fortschritt wird gelöscht!')) {
    localStorage.removeItem(STORAGE_KEY);
    state = getDefaultState();
    showDashboard();
  }
}

/* Initialization */
updateStreak();
showDashboard();
"""
print(f"scripts.py ready. Length: {len(JS_CONTENT)} chars")
