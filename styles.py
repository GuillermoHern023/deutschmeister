CSS_CONTENT = """/* ============================================
   DEUTSCHMEISTER • FRIENDLY PASTEL DESIGN SYSTEM
   Warm, Cheerful, Tactile & Accessible
   ============================================ */

:root {
  /* Warm, Friendly Pastel Canvas & Card Surfaces (Default Light) */
  --bg-canvas: #faf8f5;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #f4f6fa;
  --bg-surface-card: #ffffff;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f5f9;
  
  --border-subtle: #e8ecf4;
  --border-medium: #cbd5e1;
  --border-focus: #38bdf8;
  
  /* Highly Readable, Warm Slate Typography (WCAG AAA/AA 4.5:1+) */
  --text-primary: #1e293b;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  
  /* Friendly Pastel Accent Tokens */
  /* 1. Pastel Sky (Der / Primary Action / Runner Focus) */
  --pastel-sky: #38bdf8;
  --pastel-sky-hover: #0ea5e9;
  --pastel-sky-bg: #e0f2fe;
  --pastel-sky-border: #bae6fd;
  --pastel-sky-shadow: #0284c7;
  --pastel-sky-text: #0369a1;
  --pastel-sky-dark: #0369a1;

  /* 2. Pastel Mint (Das / Success / Level Progression) */
  --pastel-mint: #34d399;
  --pastel-mint-hover: #10b981;
  --pastel-mint-bg: #dcfce7;
  --pastel-mint-border: #86efac;
  --pastel-mint-shadow: #059669;
  --pastel-mint-text: #15803d;

  /* 3. Pastel Butter / Amber (Streak / XP / Golden Stars) */
  --pastel-amber: #fbbf24;
  --pastel-amber-hover: #f59e0b;
  --pastel-amber-bg: #fef3c7;
  --pastel-amber-border: #fde68a;
  --pastel-amber-shadow: #d97706;
  --pastel-amber-text: #b45309;

  /* 4. Pastel Strawberry / Coral (Die / Spanish Tips / Alerts) */
  --pastel-coral: #fb7185;
  --pastel-coral-hover: #f43f5e;
  --pastel-coral-bg: #ffe4e6;
  --pastel-coral-border: #fecdd3;
  --pastel-coral-shadow: #e11d48;
  --pastel-coral-text: #be123c;

  /* 5. Pastel Lilac / Lavender (Sentence Builder / Milestones) */
  --pastel-lavender: #c084fc;
  --pastel-lavender-hover: #a855f7;
  --pastel-lavender-bg: #f3e8ff;
  --pastel-lavender-border: #e9d5ff;
  --pastel-lavender-shadow: #9333ea;
  --pastel-lavender-text: #7e22ce;

  /* Legacy Brand Variables mapped to pastel tokens for 100% compatibility */
  --brand-blue: var(--pastel-sky);
  --brand-blue-hover: var(--pastel-sky-hover);
  --brand-blue-dark: var(--pastel-sky-shadow);
  --brand-blue-glow: rgba(56, 189, 248, 0.35);

  --brand-green: var(--pastel-mint);
  --brand-green-hover: var(--pastel-mint-hover);
  --brand-green-glow: rgba(52, 211, 153, 0.35);

  --brand-amber: var(--pastel-amber);
  --brand-amber-light: var(--pastel-amber-border);
  --brand-amber-glow: rgba(251, 191, 36, 0.35);

  --brand-red: var(--pastel-coral);
  --brand-red-glow: rgba(251, 113, 133, 0.35);

  --brand-purple: var(--pastel-lavender);
  --brand-purple-glow: rgba(192, 132, 252, 0.35);

  /* Typography */
  --font-main: 'Plus Jakarta Sans', 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  /* Friendly Rounded Radii */
  --radius-xs: 8px;
  --radius-sm: 12px;
  --radius-md: 18px;
  --radius-lg: 26px;
  --radius-full: 9999px;
  
  /* Soft Ambient Lighting & Depth */
  --shadow-sm: 0 2px 6px rgba(100, 116, 139, 0.08);
  --shadow-md: 0 8px 24px rgba(100, 116, 139, 0.12);
  --shadow-lg: 0 16px 36px rgba(100, 116, 139, 0.14);
  --shadow-glow-blue: 0 0 20px var(--brand-blue-glow);
  --shadow-glow-green: 0 0 20px var(--brand-green-glow);
  --shadow-glow-amber: 0 0 20px var(--brand-amber-glow);
  
  /* Cheerful Bouncy Transitions */
  --transition: all 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
  --transition-smooth: all 0.25s ease;
}

/* Pastel Night Theme Option */
[data-theme="dark"] {
  --bg-canvas: #0f172a;
  --bg-surface: #1e293b;
  --bg-surface-elevated: #28354f;
  --bg-surface-card: #1e293b;
  --bg-card: #1e293b;
  --bg-card-hover: #334155;

  --border-subtle: rgba(255, 255, 255, 0.1);
  --border-medium: rgba(255, 255, 255, 0.18);
  --border-focus: #38bdf8;

  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;

  --pastel-sky-bg: rgba(56, 189, 248, 0.18);
  --pastel-sky-border: rgba(56, 189, 248, 0.35);
  --pastel-sky-text: #7dd3fc;
  --pastel-sky-dark: #7dd3fc;

  --pastel-mint-bg: rgba(52, 211, 153, 0.18);
  --pastel-mint-border: rgba(52, 211, 153, 0.35);
  --pastel-mint-text: #6ee7b7;

  --pastel-amber-bg: rgba(251, 191, 36, 0.18);
  --pastel-amber-border: rgba(251, 191, 36, 0.35);
  --pastel-amber-text: #fde047;

  --pastel-coral-bg: rgba(251, 113, 133, 0.18);
  --pastel-coral-border: rgba(251, 113, 133, 0.35);
  --pastel-coral-text: #fda4af;

  --pastel-lavender-bg: rgba(192, 132, 252, 0.18);
  --pastel-lavender-border: rgba(192, 132, 252, 0.35);
  --pastel-lavender-text: #d8b4fe;

  --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 16px 36px rgba(0, 0, 0, 0.5);
}

/* Global Reset & Base Typography */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font-main);
  background-color: var(--bg-canvas);
  color: var(--text-primary);
  font-size: 15px;
  scroll-behavior: smooth;
  transition: background-color 0.3s ease, color 0.3s ease;
}

body {
  min-height: 100vh;
  display: flex;
  overflow-x: hidden;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

/* App Shell */
#app {
  display: flex;
  width: 100%;
  min-height: 100vh;
}

/* ============================================
   SIDEBAR
   ============================================ */
.sidebar {
  width: 290px;
  background-color: var(--bg-surface);
  border-right: 2px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
  box-shadow: 2px 0 16px rgba(100, 116, 139, 0.05);
}
.sidebar::-webkit-scrollbar { width: 5px; }
.sidebar::-webkit-scrollbar-thumb { background: var(--border-medium); border-radius: 4px; }

.sidebar-header {
  padding: 24px 22px 18px;
  border-bottom: 2px solid var(--border-subtle);
}
.sidebar-header h1 {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 10px;
}
.sidebar-header h1 span {
  background: linear-gradient(135deg, #0ea5e9, #6366f1);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.sidebar-header .subtitle {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-secondary);
  margin-top: 4px;
}

/* XP Bar & Daily Stats */
.xp-bar-container {
  padding: 16px 20px;
  border-bottom: 2px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  margin: 12px 14px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-subtle);
}
.xp-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  font-weight: 800;
  color: var(--text-secondary);
  margin-bottom: 8px;
}
.xp-bar {
  height: 10px;
  background: var(--border-medium);
  border-radius: var(--radius-full);
  overflow: hidden;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.06);
}
.xp-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--pastel-amber), #fbbf24);
  border-radius: var(--radius-full);
  transition: width 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);
}
.level-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--pastel-amber-text);
  background: var(--pastel-amber-bg);
  padding: 4px 10px;
  border-radius: var(--radius-full);
  border: 1px solid var(--pastel-amber-border);
}
.streak-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.78rem;
  font-weight: 800;
  color: #ea580c;
  background: #fff7ed;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  border: 1px solid #fed7aa;
}

/* 15-Minute Study Timer Card in Sidebar */
.sidebar-timer-card {
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  cursor: pointer;
  transition: var(--transition);
  width: 100%;
  margin-top: 12px;
  box-shadow: 0 3px 0 var(--border-medium);
}
.sidebar-timer-card:hover {
  border-color: var(--pastel-sky);
  transform: translateY(-2px);
  box-shadow: 0 5px 0 var(--pastel-sky-border);
}
.sidebar-timer-card:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--border-medium);
}
.sidebar-timer-card.running {
  border-color: var(--pastel-mint);
  background: var(--pastel-mint-bg);
  box-shadow: 0 3px 0 var(--pastel-mint-border);
}
.timer-status-badge {
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  border: 1px solid var(--border-medium);
  transition: var(--transition);
}
.sidebar-timer-card.running .timer-status-badge {
  background: var(--pastel-mint-border);
  color: var(--pastel-mint-text);
  border-color: var(--pastel-mint);
}

/* Level Tabs */
.level-tabs {
  display: flex;
  gap: 4px;
  padding: 4px;
  background: var(--bg-surface-elevated);
  margin: 6px 14px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
}
.level-tab-btn {
  flex: 1;
  padding: 8px 4px;
  border-radius: var(--radius-xs);
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
}
.level-tab-btn:hover { color: var(--text-primary); }
.level-tab-btn.active {
  background: var(--pastel-sky);
  color: #fff;
  font-weight: 800;
  box-shadow: 0 3px 0 var(--pastel-sky-shadow), 0 4px 10px rgba(14, 165, 233, 0.25);
}

/* Sidebar Options & Controls */
.sidebar-options {
  padding: 4px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-secondary);
}
.toggle-pill {
  padding: 6px 14px;
  border-radius: var(--radius-full);
  border: 1.5px solid var(--border-medium);
  background: var(--bg-surface);
  color: var(--text-primary);
  font-size: 0.74rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 2px 0 var(--border-medium);
}
.toggle-pill:hover {
  background: var(--bg-surface-elevated);
  border-color: var(--pastel-sky);
  transform: translateY(-1px);
  box-shadow: 0 3px 0 var(--border-medium);
}
.toggle-pill:active {
  transform: translateY(1px);
  box-shadow: 0 1px 0 var(--border-medium);
}

/* Chapter Navigation Items in Sidebar */
.chapter-nav-item {
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  transition: var(--transition);
  margin-bottom: 4px;
  border: 1px solid transparent;
}
.chapter-nav-item:hover {
  background: var(--bg-surface-elevated);
  color: var(--text-primary);
  border-color: var(--border-subtle);
  transform: translateX(3px);
}
.chapter-nav-item.active {
  background: var(--pastel-sky-bg);
  color: var(--pastel-sky-text);
  font-weight: 700;
  border-color: var(--pastel-sky-border);
}

/* ============================================
   MAIN CONTENT AREA
   ============================================ */
.main-content {
  margin-left: 290px;
  flex: 1;
  padding: 40px 36px 120px;
  min-height: 100vh;
  position: relative;
  max-width: 960px;
  margin-right: auto;
}

/* Top Sticky Navigation Pill on Main Content */
.timeline-top-nav {
  position: sticky;
  top: 16px;
  z-index: 80;
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 18px 24px;
  margin-bottom: 30px;
  box-shadow: 0 8px 24px rgba(100, 116, 139, 0.08);
  backdrop-filter: blur(12px);
}
.course-identity {
  display: flex;
  align-items: center;
  gap: 14px;
}
.flag-avatar {
  font-size: 2.2rem;
  line-height: 1;
}
.course-name {
  font-size: 1.18rem;
  font-weight: 800;
  color: var(--text-primary);
}
.course-sub {
  font-size: 0.82rem;
  color: var(--text-secondary);
}

.top-stats-row {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.stat-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  font-size: 0.82rem;
  font-weight: 800;
  border: 1.5px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  box-shadow: 0 2px 0 var(--border-medium);
}
.stat-pill.streak {
  background: #fff7ed;
  border-color: #fed7aa;
  color: #ea580c;
  box-shadow: 0 2px 0 #fdba74;
}
.stat-pill.xp {
  background: var(--pastel-amber-bg);
  border-color: var(--pastel-amber-border);
  color: var(--pastel-amber-text);
  box-shadow: 0 2px 0 #fcd34d;
}
.stat-pill.level {
  background: var(--pastel-mint-bg);
  border-color: var(--pastel-mint-border);
  color: var(--pastel-mint-text);
  box-shadow: 0 2px 0 #86efac;
}

/* 15-Minute Timer Pill */
.stat-pill.timer-pill {
  background: var(--pastel-amber-bg);
  border-color: var(--pastel-amber-border);
  color: var(--pastel-amber-text);
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 3px 0 #fcd34d;
}
.stat-pill.timer-pill:hover {
  background: #fef08a;
  transform: translateY(-2px);
  box-shadow: 0 4px 0 #fcd34d;
}
.stat-pill.timer-pill:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 #fcd34d;
}
.stat-pill.timer-pill.running {
  background: var(--pastel-mint-bg);
  border-color: var(--pastel-mint);
  color: var(--pastel-mint-text);
  box-shadow: 0 3px 0 var(--pastel-mint-shadow);
  animation: timerPulse 2s infinite ease-in-out;
}
@keyframes timerPulse {
  0%, 100% { box-shadow: 0 3px 0 var(--pastel-mint-shadow), 0 0 6px rgba(52, 211, 153, 0.25); }
  50% { box-shadow: 0 3px 0 var(--pastel-mint-shadow), 0 0 16px rgba(52, 211, 153, 0.45); }
}

.sound-toggle-btn {
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-full);
  padding: 6px 12px;
  cursor: pointer;
  font-size: 0.95rem;
  transition: var(--transition);
  box-shadow: 0 2px 0 var(--border-medium);
}
.sound-toggle-btn:hover {
  transform: scale(1.05);
}

/* Hero Next Lesson Card */
.hero-next-card {
  background: linear-gradient(135deg, #e0f2fe 0%, #ecfdf5 100%);
  border: 2px solid #bae6fd;
  border-radius: var(--radius-lg);
  padding: 26px 30px;
  margin-bottom: 38px;
  box-shadow: 0 10px 24px rgba(56, 189, 248, 0.12);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  color: #0284c7;
  border: 1.5px solid #bae6fd;
  font-size: 0.74rem;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: var(--radius-full);
  margin-bottom: 10px;
  letter-spacing: 0.05em;
  box-shadow: 0 2px 6px rgba(14, 165, 233, 0.12);
}
.hero-title {
  font-size: 1.45rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 4px;
}
.hero-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
}

/* ============================================
   BUSUU TIMELINE (STEPPING-STONE LEARNING PATH)
   ============================================ */
.busuu-timeline {
  max-width: 680px;
  margin: 0 auto;
  position: relative;
}

/* Chapter Card Banner */
.timeline-chapter {
  margin-bottom: 70px;
  position: relative;
}
.chapter-banner {
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 26px 30px;
  margin-bottom: 40px;
  box-shadow: 0 10px 28px rgba(100, 116, 139, 0.08);
  position: relative;
  overflow: hidden;
}
.chapter-banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 6px;
  height: 100%;
  background: linear-gradient(180deg, var(--pastel-sky), var(--pastel-mint));
  border-radius: 6px 0 0 6px;
}
.chapter-badge {
  display: inline-block;
  font-size: 0.74rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--pastel-sky-dark);
  background: var(--pastel-sky-bg);
  padding: 3px 10px;
  border-radius: var(--radius-full);
  margin-bottom: 8px;
}
.chapter-title {
  font-size: 1.45rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: var(--text-primary);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.chapter-desc {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 16px;
}
.chapter-progress-box {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-secondary);
}
.chapter-progress-bar {
  flex: 1;
  height: 10px;
  background: var(--border-subtle);
  border-radius: var(--radius-full);
  overflow: hidden;
}
.chapter-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--pastel-sky), var(--pastel-mint));
  border-radius: var(--radius-full);
  transition: width 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Stepping-Stone Track */
.path-track {
  position: relative;
  padding: 20px 0 40px;
}
.path-track::before {
  content: '';
  position: absolute;
  top: 40px;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  border-left: 3px dashed var(--border-medium);
  z-index: 1;
}

/* Stepping Stone Row */
.stone-row {
  display: flex;
  justify-content: center;
  margin-bottom: 48px;
  position: relative;
  z-index: 2;
  transition: transform 0.3s ease;
}
.stone-row.stagger-center { transform: translateX(0); }
.stone-row.stagger-left   { transform: translateX(-80px); }
.stone-row.stagger-right  { transform: translateX(80px); }

.stone-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  position: relative;
  transition: var(--transition);
}
.stone-container:hover {
  transform: translateY(-4px);
}

/* Tactile 3D Circular Stone Button */
.stone-circle {
  width: 82px;
  height: 82px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.9rem;
  position: relative;
  transition: var(--transition);
  user-select: none;
}

/* States with Tactile 3D Depths (Busuu & Duolingo style) */
.stone-circle.completed {
  background: linear-gradient(145deg, #4ade80 0%, #22c55e 100%);
  border: 3px solid #bbf7d0;
  box-shadow: 0 8px 0 #15803d, 0 12px 24px rgba(34, 197, 94, 0.25);
  color: #fff;
}
.stone-circle.completed:active {
  transform: translateY(6px);
  box-shadow: 0 2px 0 #15803d, 0 4px 10px rgba(34, 197, 94, 0.2);
}

.stone-circle.active {
  width: 90px;
  height: 90px;
  background: linear-gradient(145deg, #38bdf8 0%, #0ea5e9 100%);
  border: 3.5px solid #bae6fd;
  box-shadow: 0 9px 0 #0284c7, 0 15px 30px rgba(14, 165, 233, 0.3);
  color: #fff;
}
.stone-circle.active:active {
  transform: translateY(7px);
  box-shadow: 0 2px 0 #0284c7, 0 6px 14px rgba(14, 165, 233, 0.2);
}

.stone-circle.unlocked {
  background: var(--bg-surface);
  border: 3px solid var(--border-medium);
  box-shadow: 0 6px 0 var(--border-medium);
  color: var(--text-primary);
}
.stone-circle.unlocked:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 var(--border-medium);
}

.stone-circle.locked {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  box-shadow: 0 6px 0 var(--border-medium);
  color: var(--text-muted);
  opacity: 0.75;
}

/* Milestone Checkpoint Crown */
.stone-circle.checkpoint.completed {
  background: linear-gradient(145deg, #fbbf24 0%, #f59e0b 100%);
  border: 3.5px solid #fde68a;
  box-shadow: 0 9px 0 #b45309, 0 14px 28px rgba(245, 158, 11, 0.3);
}

/* Pulsing Halo on Active Stone */
@keyframes pulse-ring {
  0% { transform: scale(0.96); opacity: 0.85; }
  50% { transform: scale(1.25); opacity: 0; }
  100% { transform: scale(0.96); opacity: 0; }
}
.stone-circle.active::before {
  content: '';
  position: absolute;
  top: -12px;
  left: -12px;
  right: -12px;
  bottom: -12px;
  border-radius: var(--radius-full);
  border: 3px solid var(--pastel-sky);
  animation: pulse-ring 2.2s infinite cubic-bezier(0.4, 0, 0.6, 1);
  pointer-events: none;
}

/* "START HIER" Floating Badge */
.start-here-beacon {
  position: absolute;
  top: -38px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
  font-size: 0.74rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
  white-space: nowrap;
  animation: bounce-gentle 1.8s infinite ease-in-out;
  pointer-events: none;
  z-index: 10;
}
.start-here-beacon::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  border-width: 5px 5px 0;
  border-style: solid;
  border-color: #d97706 transparent transparent;
}
@keyframes bounce-gentle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}

/* Stone Sub-Labels & Stars */
.stone-title-label {
  margin-top: 10px;
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-secondary);
  max-width: 140px;
  text-align: center;
  line-height: 1.3;
}
.stone-stars {
  display: flex;
  gap: 2px;
  margin-top: 4px;
  font-size: 0.78rem;
}

/* Hover Preview Card on Stepping Stones */
.stone-card-preview {
  position: absolute;
  bottom: 105px;
  left: 50%;
  transform: translateX(-50%) translateY(8px);
  width: 250px;
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  box-shadow: 0 14px 30px rgba(100, 116, 139, 0.16);
  opacity: 0;
  pointer-events: none;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 100;
  text-align: center;
}
.stone-container:hover .stone-card-preview {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* ============================================
   LESSON RUNNER (BUSUU FULL-SCREEN FOCUS FLOW)
   ============================================ */
.busuu-runner {
  max-width: 720px;
  margin: 0 auto;
  animation: fadeIn 0.25s ease;
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Runner Top Bar */
.runner-topbar {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 0 28px;
}
.btn-runner-close {
  width: 42px;
  height: 42px;
  border-radius: var(--radius-full);
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  color: var(--text-secondary);
  font-size: 1.15rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 2px 0 var(--border-medium);
}
.btn-runner-close:hover {
  background: #fee2e2;
  color: #ef4444;
  border-color: #fca5a5;
  transform: scale(1.05);
}

.runner-progress-container {
  flex: 1;
  height: 14px;
  background: var(--border-subtle);
  border-radius: var(--radius-full);
  overflow: hidden;
  position: relative;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.06);
}
.runner-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #38bdf8, #34d399);
  border-radius: var(--radius-full);
  transition: width 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 0 10px rgba(52, 211, 153, 0.4);
}

.runner-timer-pill {
  background: var(--pastel-amber-bg);
  border: 1.5px solid var(--pastel-amber-border);
  color: var(--pastel-amber-text);
  border-radius: var(--radius-full);
  padding: 6px 14px;
  font-size: 0.82rem;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
  box-shadow: 0 2px 0 var(--pastel-amber-border);
}
.runner-timer-pill:hover {
  background: #fef08a;
}
.runner-timer-pill.running {
  background: var(--pastel-mint-bg);
  border-color: var(--pastel-mint);
  color: var(--pastel-mint-text);
  box-shadow: 0 2px 0 var(--pastel-mint-border);
}

.runner-step-badge {
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--text-secondary);
  white-space: nowrap;
}

.runner-mode-toggle {
  font-size: 0.78rem;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  border: 1.5px solid var(--border-medium);
  background: var(--bg-surface);
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition);
  font-weight: 700;
  box-shadow: 0 2px 0 var(--border-medium);
}
.runner-mode-toggle:hover {
  color: var(--text-primary);
  border-color: var(--pastel-sky);
}

/* Runner Card Body */
.runner-card {
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 38px 34px;
  box-shadow: 0 16px 36px rgba(100, 116, 139, 0.1);
  min-height: 480px;
  display: flex;
  flex-direction: column;
  position: relative;
  animation: slideInUp 0.3s ease;
}
@keyframes slideInUp {
  from { opacity: 0; transform: translateY(14px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Step 1: Vocab Discovery Card */
.vocab-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 1;
}
.vocab-category-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 5px 14px;
  border-radius: var(--radius-full);
  background: var(--pastel-sky-bg);
  color: var(--pastel-sky-dark);
  border: 1px solid var(--pastel-sky-border);
  margin-bottom: 22px;
}
.vocab-word-hero {
  font-size: 2.7rem;
  font-weight: 800;
  color: var(--text-primary);
  letter-spacing: -0.02em;
  margin-bottom: 12px;
  line-height: 1.2;
}
.vocab-gender-pill {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: var(--radius-full);
  margin-bottom: 18px;
}
.gender-der { background: #e0f2fe; color: #0284c7; border: 1.5px solid #bae6fd; }
.gender-die { background: #ffe4e6; color: #e11d48; border: 1.5px solid #fecdd3; }
.gender-das { background: #dcfce7; color: #15803d; border: 1.5px solid #86efac; }
.gender-other { background: #f3e8ff; color: #7e22ce; border: 1.5px solid #e9d5ff; }

.audio-hero-btn {
  width: 72px;
  height: 72px;
  border-radius: var(--radius-full);
  background: linear-gradient(145deg, #38bdf8 0%, #0ea5e9 100%);
  border: none;
  color: #fff;
  font-size: 1.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 8px 0 #0284c7, 0 14px 28px rgba(14, 165, 233, 0.35);
  transition: var(--transition);
  margin: 10px 0 24px;
}
.audio-hero-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 0 #0284c7, 0 16px 32px rgba(14, 165, 233, 0.4);
}
.audio-hero-btn:active {
  transform: translateY(6px);
  box-shadow: 0 2px 0 #0284c7, 0 6px 14px rgba(14, 165, 233, 0.25);
}

.vocab-meaning {
  font-size: 1.4rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
  font-weight: 600;
}

/* Spanish Helper Callout Box (For Guillermo) */
.spanish-helper-box {
  background: #fffbeb;
  border: 1.5px solid #fde68a;
  border-radius: var(--radius-md);
  padding: 16px 20px;
  margin-bottom: 24px;
  text-align: left;
  width: 100%;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.08);
}
.spanish-helper-header {
  font-size: 0.82rem;
  font-weight: 800;
  color: #b45309;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.spanish-helper-text {
  font-size: 0.9rem;
  color: #78350f;
  line-height: 1.5;
}

/* Real-world Berlin Example Box */
.berlin-example-box {
  background: #f0fdf4;
  border: 1.5px solid #bbf7d0;
  border-radius: var(--radius-md);
  padding: 16px 20px;
  text-align: left;
  width: 100%;
  margin-bottom: 28px;
  box-shadow: 0 2px 8px rgba(34, 197, 94, 0.06);
}
.berlin-example-label {
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #15803d;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.berlin-example-de {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.berlin-example-en {
  font-size: 0.88rem;
  color: var(--text-secondary);
}

/* Step 2: Instant Recall Drill */
.micro-drill-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.drill-instruction {
  font-size: 0.84rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--pastel-sky-dark);
  margin-bottom: 12px;
}
.drill-question-box {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 24px;
  text-align: center;
  margin-bottom: 24px;
}
.drill-question-text {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text-primary);
}
.drill-options-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  margin-bottom: 24px;
}
.drill-option-btn {
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 22px;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  cursor: pointer;
  transition: var(--transition);
  text-align: left;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 4px 0 var(--border-medium);
}
.drill-option-btn:hover {
  background: #f8fafc;
  border-color: var(--pastel-sky);
  transform: translateY(-2px);
  box-shadow: 0 6px 0 var(--pastel-sky-border);
}
.drill-option-btn:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--border-medium);
}
.drill-option-btn.selected-correct {
  background: #dcfce7;
  border-color: #4ade80;
  color: #15803d;
  box-shadow: 0 4px 0 #22c55e;
}
.drill-option-btn.selected-wrong {
  background: #ffe4e6;
  border-color: #fb7185;
  color: #be123c;
  box-shadow: 0 4px 0 #f43f5e;
}

/* Bottom Sheet Feedback for Drills */
.runner-feedback-sheet {
  border-radius: var(--radius-md);
  padding: 18px 24px;
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: slideInUp 0.25s ease;
  box-shadow: 0 4px 14px rgba(100, 116, 139, 0.08);
}
.runner-feedback-sheet.correct {
  background: #dcfce7;
  border: 2px solid #86efac;
}
.runner-feedback-sheet.wrong {
  background: #ffe4e6;
  border: 2px solid #fecdd3;
}
.feedback-text-title {
  font-size: 1.15rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
}
.runner-feedback-sheet.correct .feedback-text-title { color: #15803d; }
.runner-feedback-sheet.wrong .feedback-text-title { color: #be123c; }
.feedback-text-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  margin-top: 4px;
  font-weight: 500;
}

/* Step 2b: Fill-in-the-Blank (Lückentext) */
.fill-blank-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.fill-blank-sentence-card {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 26px 22px;
  text-align: center;
  margin-bottom: 22px;
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.6;
}
.blank-placeholder {
  display: inline-block;
  min-width: 90px;
  border-bottom: 3.5px solid var(--pastel-sky);
  color: var(--pastel-sky-dark);
  font-weight: 800;
  padding: 0 8px;
}
.fill-blank-hint {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--pastel-amber-text);
  background: var(--pastel-amber-bg);
  border: 1px solid var(--pastel-amber-border);
  border-radius: var(--radius-full);
  padding: 4px 14px;
  margin-top: 14px;
}
.fill-blank-input-group {
  display: flex;
  gap: 10px;
  margin-bottom: 18px;
}
.fill-blank-input {
  flex: 1;
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  transition: var(--transition);
}
.fill-blank-input:focus {
  outline: none;
  border-color: var(--pastel-sky);
  box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.2);
}
.fill-blank-input.correct {
  border-color: var(--pastel-mint);
  background: var(--pastel-mint-bg);
  color: var(--pastel-mint-text);
}
.fill-blank-input.wrong {
  border-color: var(--pastel-coral);
  background: var(--pastel-coral-bg);
  color: var(--pastel-coral-text);
}

/* Step 3: Busuu Grammar Snapshot */
.grammar-snapshot-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.grammar-hero-card {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 20px;
}
.grammar-rule-summary {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 16px;
  line-height: 1.5;
}

/* Step 4: Dialogue in Action (WhatsApp / iMessage Style) */
.dialogue-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.dialogue-chat-box {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}
.chat-msg-row {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.chat-msg-row.right {
  flex-direction: row-reverse;
}
.chat-avatar {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1.5px solid var(--border-medium);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  flex-shrink: 0;
  box-shadow: var(--shadow-sm);
}
.chat-bubble {
  max-width: 75%;
  padding: 14px 18px;
  border-radius: 20px;
  position: relative;
  box-shadow: 0 2px 8px rgba(100, 116, 139, 0.08);
}
.chat-msg-row.left .chat-bubble {
  background: #f8fafc;
  border: 1.5px solid #e2e8f0;
  border-top-left-radius: 4px;
  color: var(--text-primary);
}
.chat-msg-row.right .chat-bubble {
  background: #e0f2fe;
  border: 1.5px solid #bae6fd;
  border-top-right-radius: 4px;
  color: #0c4a6e;
}
.chat-speaker {
  font-size: 0.74rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}
.chat-msg-row.left .chat-speaker { color: #64748b; }
.chat-msg-row.right .chat-speaker { color: #0284c7; }
.chat-text-de {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.45;
}
.chat-text-en {
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-top: 4px;
}
.play-chat-audio-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 1.05rem;
  margin-left: 6px;
  transition: var(--transition);
}
.play-chat-audio-btn:hover { color: var(--pastel-sky); }

/* Step 4b: Word Matching Pairs (Wortpaare verbinden) */
.matching-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.matching-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-bottom: 24px;
}
.matching-card {
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-md);
  padding: 16px 14px;
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--text-primary);
  text-align: center;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 4px 0 var(--border-medium);
  min-height: 58px;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
}
.matching-card:hover {
  background: #f8fafc;
  border-color: var(--pastel-sky);
  transform: translateY(-2px);
  box-shadow: 0 6px 0 var(--pastel-sky-border);
}
.matching-card:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--border-medium);
}
.matching-card.selected {
  border-color: var(--pastel-sky);
  background: var(--pastel-sky-bg);
  color: var(--pastel-sky-dark);
  box-shadow: 0 4px 0 var(--pastel-sky-shadow), 0 0 14px rgba(56, 189, 248, 0.35);
  transform: translateY(-2px);
}
.matching-card.matched {
  border-color: var(--pastel-mint);
  background: var(--pastel-mint-bg);
  color: var(--pastel-mint-text);
  cursor: default;
  pointer-events: none;
  box-shadow: none;
  opacity: 0.95;
}
.matching-card.wrong {
  border-color: var(--pastel-coral);
  background: var(--pastel-coral-bg);
  color: var(--pastel-coral-text);
  animation: matchShake 0.4s ease;
}
@keyframes matchShake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}

/* Step 5: Sentence Builder (Word Tiles) */
.tiles-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.tiles-drop-area {
  min-height: 84px;
  background: var(--bg-surface-elevated);
  border: 2.5px dashed var(--border-medium);
  border-radius: var(--radius-md);
  padding: 16px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-bottom: 24px;
  transition: var(--transition);
}
.tiles-drop-area.filled {
  border-color: var(--pastel-lavender);
  background: var(--pastel-lavender-bg);
}
.tile-chip {
  padding: 10px 18px;
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  border-radius: 14px;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  cursor: pointer;
  user-select: none;
  box-shadow: 0 4px 0 var(--border-medium);
  transition: var(--transition);
}
.tile-chip:hover {
  transform: translateY(-2px);
  border-color: var(--pastel-lavender);
  box-shadow: 0 6px 0 var(--pastel-lavender-border);
}
.tile-chip:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--border-medium);
}
.tile-chip.in-drop {
  background: var(--pastel-lavender-bg);
  border-color: var(--pastel-lavender);
  color: var(--pastel-lavender-text);
  box-shadow: 0 3px 0 var(--pastel-lavender-shadow);
}
.tile-chip.disabled {
  opacity: 0.25;
  pointer-events: none;
}
.tiles-bank {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 28px;
}

/* Step 6: Active Production (Speaking / Writing) */
.production-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.production-prompt-box {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 22px;
  margin-bottom: 20px;
}
.production-prompt-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 6px;
}
.production-prompt-sub {
  font-size: 0.88rem;
  color: var(--text-secondary);
}
.umlaut-bar {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-bottom: 12px;
}
.umlaut-key {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  color: var(--text-primary);
  font-weight: 800;
  font-size: 1.1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
  box-shadow: 0 3px 0 var(--border-medium);
}
.umlaut-key:hover {
  background: var(--bg-surface-elevated);
  border-color: var(--pastel-sky);
  transform: translateY(-1px);
}
.umlaut-key:active {
  transform: translateY(2px);
  box-shadow: 0 1px 0 var(--border-medium);
}
.mic-record-btn {
  padding: 0 16px;
  height: 40px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  color: var(--text-primary);
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-left: auto;
  transition: var(--transition);
  box-shadow: 0 3px 0 var(--border-medium);
}
.mic-record-btn:hover {
  border-color: var(--pastel-coral);
}
.mic-record-btn.recording {
  background: #fee2e2;
  border-color: #ef4444;
  color: #b91c1c;
  animation: pulse 1.5s infinite;
}
.production-textarea {
  width: 100%;
  min-height: 110px;
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-md);
  padding: 16px;
  font-size: 1.05rem;
  color: var(--text-primary);
  font-family: inherit;
  resize: vertical;
  margin-bottom: 16px;
  transition: var(--transition);
}
.production-textarea:focus {
  outline: none;
  border-color: var(--pastel-sky);
  box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.2);
}

/* Step 7: Celebration Screen */
.celebration-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 1;
  padding: 24px 0;
}
.celebration-trophy {
  font-size: 5rem;
  animation: bounce-gentle 2s infinite;
  margin-bottom: 14px;
}
.celebration-title {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.celebration-sub {
  font-size: 1.05rem;
  color: var(--text-secondary);
  margin-bottom: 30px;
}
.celebration-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  width: 100%;
  max-width: 460px;
  margin-bottom: 34px;
}
.celebration-stat-card {
  background: var(--bg-surface);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 18px 14px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(100, 116, 139, 0.08);
}
.celebration-stat-value {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--pastel-amber-text);
}
.celebration-stat-label {
  font-size: 0.74rem;
  color: var(--text-secondary);
  margin-top: 4px;
  font-weight: 700;
}
#confetti-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 50;
}

/* Primary & Secondary Buttons (Tactile 3D) */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: var(--radius-full);
  background: linear-gradient(180deg, #38bdf8 0%, #0ea5e9 100%);
  border: none;
  color: #fff;
  font-size: 1rem;
  font-weight: 800;
  cursor: pointer;
  box-shadow: 0 5px 0 #0284c7, 0 10px 20px rgba(14, 165, 233, 0.25);
  transition: var(--transition);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 7px 0 #0284c7, 0 14px 24px rgba(14, 165, 233, 0.35);
}
.btn-primary:active {
  transform: translateY(4px);
  box-shadow: 0 1px 0 #0284c7, 0 4px 8px rgba(14, 165, 233, 0.2);
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 22px;
  border-radius: var(--radius-full);
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  color: var(--text-primary);
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 0 var(--border-medium);
  transition: var(--transition);
}
.btn-secondary:hover {
  background: var(--bg-surface-elevated);
  border-color: var(--text-muted);
  transform: translateY(-2px);
  box-shadow: 0 6px 0 var(--border-medium);
}
.btn-secondary:active {
  transform: translateY(3px);
  box-shadow: 0 1px 0 var(--border-medium);
}

/* 15-Minute Study Timer Finish Overlay */
.timer-finish-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  animation: fadeIn 0.25s ease;
}
.timer-finish-card {
  background: var(--bg-surface);
  border: 3px solid var(--pastel-mint);
  border-radius: var(--radius-lg);
  max-width: 440px;
  width: 100%;
  padding: 36px 30px;
  text-align: center;
  box-shadow: 0 20px 50px rgba(100, 116, 139, 0.25), 0 0 30px rgba(52, 211, 153, 0.3);
  animation: slideInUp 0.3s ease;
}

/* Audio Player Helpers */
.audio-btn {
  background: var(--bg-surface-elevated);
  border: 1.5px solid var(--border-medium);
  border-radius: var(--radius-full);
  padding: 4px 10px;
  cursor: pointer;
  font-size: 0.85rem;
  color: var(--text-secondary);
  transition: var(--transition);
}
.audio-btn:hover {
  color: var(--pastel-sky-dark);
  border-color: var(--pastel-sky);
  background: var(--pastel-sky-bg);
}

/* Mobile Hamburger Toggle */
.mobile-toggle {
  display: none;
  position: fixed;
  top: 14px;
  left: 14px;
  z-index: 101;
  background: var(--bg-surface);
  border: 2px solid var(--border-medium);
  color: var(--text-primary);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 1.2rem;
  cursor: pointer;
  box-shadow: 0 3px 0 var(--border-medium);
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .mobile-toggle { display: block; }
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .main-content { margin-left: 0; padding: 60px 16px 120px; }
  .stone-row.stagger-left, .stone-row.stagger-right { transform: translateX(0); }
}

/* Stone Preview Card Inner Typography & Milestone Stones */
.stone-card-title {
  font-size: 0.92rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 4px;
}
.stone-card-sub {
  font-size: 0.78rem;
  color: var(--text-secondary);
  margin-bottom: 8px;
}
.stone-card-meta {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--pastel-sky-text);
  background: var(--pastel-sky-bg);
  border-radius: var(--radius-full);
  padding: 4px 10px;
}
.milestone-stone-circle {
  width: 92px;
  height: 92px;
  background: linear-gradient(145deg, #fbbf24 0%, #f59e0b 100%) !important;
  border: 3.5px solid #fde68a !important;
  box-shadow: 0 9px 0 #b45309, 0 14px 28px rgba(245, 158, 11, 0.3) !important;
  color: #fff !important;
}
.milestone-beacon {
  background: linear-gradient(135deg, #a855f7, #7e22ce) !important;
  box-shadow: 0 4px 12px rgba(168, 85, 247, 0.35) !important;
}
.milestone-beacon::after {
  border-color: #7e22ce transparent transparent !important;
}

/* Multi-Word Vocabulary Deck Switcher */
.vocab-deck-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  width: 100%;
  margin-bottom: 20px;
}
.vocab-deck-pill {
  padding: 6px 13px;
  border-radius: var(--radius-full);
  border: 1.5px solid var(--border-medium);
  background: var(--bg-surface);
  color: var(--text-secondary);
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 2px 0 var(--border-medium);
}
.vocab-deck-pill:hover {
  border-color: var(--pastel-sky);
  color: var(--text-primary);
  transform: translateY(-1px);
}
.vocab-deck-pill.active {
  background: var(--pastel-sky);
  border-color: var(--pastel-sky-shadow);
  color: #ffffff;
  box-shadow: 0 3px 0 var(--pastel-sky-shadow);
}
.vocab-deck-pill.seen:not(.active) {
  background: var(--pastel-mint-bg);
  border-color: var(--pastel-mint-border);
  color: var(--pastel-mint-text);
}
.vocab-deck-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 12px;
  margin-top: auto;
  padding-top: 10px;
}

/* Step: Reading Comprehension (Lesetext & Verstehen) */
.reading-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.reading-article-card {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-left: 6px solid var(--pastel-lavender);
  border-radius: var(--radius-md);
  padding: 22px 24px;
  margin-bottom: 18px;
  box-shadow: var(--shadow-sm);
}
.reading-article-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 12px;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--border-subtle);
}
.reading-article-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text-primary);
}
.reading-article-body {
  font-size: 1.06rem;
  line-height: 1.75;
  color: var(--text-primary);
  font-weight: 500;
}
.reading-glossary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(195px, 1fr));
  gap: 8px;
  margin-bottom: 20px;
}
.reading-glossary-item {
  background: var(--pastel-lavender-bg);
  border: 1px solid var(--pastel-lavender-border);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 0.82rem;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.reading-glossary-de {
  font-weight: 800;
  color: var(--pastel-lavender-text);
}
.reading-glossary-en {
  color: var(--text-secondary);
  font-size: 0.78rem;
}

/* Dark Mode Overrides for Callout Boxes & Chat Bubbles */
[data-theme="dark"] .hero-next-card {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.16) 0%, rgba(52, 211, 153, 0.14) 100%);
  border-color: rgba(56, 189, 248, 0.35);
}
[data-theme="dark"] .hero-badge {
  background: #0f172a;
  color: #7dd3fc;
  border-color: rgba(56, 189, 248, 0.4);
}
[data-theme="dark"] .spanish-helper-box {
  background: rgba(251, 191, 36, 0.12);
  border-color: rgba(251, 191, 36, 0.35);
}
[data-theme="dark"] .spanish-helper-header { color: #fde047; }
[data-theme="dark"] .spanish-helper-text { color: #fef3c7; }
[data-theme="dark"] .berlin-example-box {
  background: rgba(52, 211, 153, 0.12);
  border-color: rgba(52, 211, 153, 0.35);
}
[data-theme="dark"] .berlin-example-label { color: #6ee7b7; }
[data-theme="dark"] .chat-msg-row.left .chat-bubble {
  background: #28354f;
  border-color: rgba(255,255,255,0.12);
  color: #f8fafc;
}
[data-theme="dark"] .chat-msg-row.right .chat-bubble {
  background: rgba(56, 189, 248, 0.2);
  border-color: rgba(56, 189, 248, 0.4);
  color: #f0f9ff;
}
[data-theme="dark"] .chat-msg-row.right .chat-speaker { color: #7dd3fc; }
[data-theme="dark"] .runner-feedback-sheet.correct {
  background: rgba(52, 211, 153, 0.18);
  border-color: rgba(52, 211, 153, 0.45);
}
[data-theme="dark"] .runner-feedback-sheet.correct .feedback-text-title { color: #6ee7b7; }
[data-theme="dark"] .runner-feedback-sheet.wrong {
  background: rgba(251, 113, 133, 0.18);
  border-color: rgba(251, 113, 133, 0.45);
}
[data-theme="dark"] .runner-feedback-sheet.wrong .feedback-text-title { color: #fda4af; }
[data-theme="dark"] .drill-option-btn.selected-correct {
  background: rgba(52, 211, 153, 0.22);
  border-color: #34d399;
  color: #6ee7b7;
}
[data-theme="dark"] .drill-option-btn.selected-wrong {
  background: rgba(251, 113, 133, 0.22);
  border-color: #fb7185;
  color: #fda4af;
}

/* Friendly Pastel Toast Notification */
.app-toast {
  position: fixed;
  bottom: 28px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: var(--bg-surface);
  color: var(--text-primary);
  border: 2px solid var(--pastel-sky);
  border-radius: var(--radius-full);
  padding: 12px 24px;
  font-size: 0.92rem;
  font-weight: 700;
  box-shadow: 0 10px 28px rgba(15, 23, 42, 0.18), 0 4px 0 var(--pastel-sky-shadow);
  opacity: 0;
  pointer-events: none;
  transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 9999;
}
.app-toast.show {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Reference Mode Tables */
.reference-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1px solid var(--border-subtle);
}
.reference-content th {
  background: var(--pastel-sky-bg);
  color: var(--pastel-sky-text);
  text-align: left;
  padding: 10px 14px;
  font-size: 0.84rem;
  font-weight: 800;
}
.reference-content td {
  padding: 10px 14px;
  border-top: 1px solid var(--border-subtle);
  font-size: 0.9rem;
  color: var(--text-primary);
}
.reference-content tr:nth-child(even) td {
  background: var(--bg-surface-elevated);
}
"""
