# CSS Styles for DeutschMeister (Busuu-Inspired Architecture)

CSS_CONTENT = """
/* ============================================
   DEUTSCHMEISTER - BUSUU MODERN DESIGN SYSTEM
   ============================================ */
:root {
  --bg-canvas: #0b0f19;
  --bg-surface: #111827;
  --bg-surface-elevated: #1f2937;
  --bg-card: rgba(31, 41, 55, 0.7);
  --bg-card-hover: rgba(55, 65, 81, 0.85);
  --bg-glass: rgba(255, 255, 255, 0.04);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-focus: #3b82f6;
  --text-primary: #f9fafb;
  --text-secondary: #9ca3af;
  --text-muted: #6b7280;
  
  --busuu-blue: #2563eb;
  --busuu-blue-hover: #1d4ed8;
  --busuu-blue-glow: rgba(37, 99, 235, 0.35);
  --success-green: #10b981;
  --success-green-hover: #059669;
  --success-green-glow: rgba(16, 185, 129, 0.35);
  --gold-star: #f59e0b;
  --gold-light: #fbbf24;
  --gold-glow: rgba(245, 158, 11, 0.35);
  --danger-red: #ef4444;
  --danger-glow: rgba(239, 68, 68, 0.3);
  --purple-accent: #8b5cf6;
  
  --font-main: 'Inter', system-ui, -apple-system, sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
  
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 28px;
  --radius-full: 9999px;
  
  --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
  --shadow-stone: 0 8px 24px rgba(0, 0, 0, 0.45);
  --shadow-active: 0 0 25px var(--busuu-blue-glow);
  --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-main);
  background-color: var(--bg-canvas);
  color: var(--text-primary);
  min-height: 100vh;
  display: flex;
  overflow-x: hidden;
  line-height: 1.5;
}

/* App Shell */
#app { display: flex; width: 100%; min-height: 100vh; }

/* Sidebar */
.sidebar {
  width: 290px;
  background-color: var(--bg-surface);
  border-right: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  transition: transform 0.3s ease;
  overflow-y: auto;
}
.sidebar-header {
  padding: 24px 20px 16px;
  border-bottom: 1px solid var(--border-subtle);
}
.sidebar-header h1 {
  font-size: 1.35rem;
  font-weight: 800;
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: flex;
  align-items: center;
  gap: 8px;
}
.sidebar-header .subtitle {
  font-size: 0.78rem;
  color: var(--text-secondary);
  margin-top: 4px;
}

/* Navigation Modes */
.nav-modes {
  padding: 16px 14px 8px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.nav-mode-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-secondary);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  text-align: left;
  width: 100%;
}
.nav-mode-btn:hover {
  background: var(--bg-card);
  color: var(--text-primary);
}
.nav-mode-btn.active {
  background: linear-gradient(135deg, rgba(37,99,235,0.2), rgba(37,99,235,0.08));
  color: #60a5fa;
  border-color: rgba(37,99,235,0.4);
}
.nav-mode-badge {
  margin-left: auto;
  font-size: 0.68rem;
  padding: 2px 7px;
  border-radius: var(--radius-full);
  background: rgba(37,99,235,0.25);
  color: #93c5fd;
  font-weight: 700;
}

/* User Progress Bar in Sidebar */
.xp-bar-container {
  padding: 14px 18px;
  margin: 8px 14px;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
}
.xp-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--text-secondary);
  margin-bottom: 6px;
}
.xp-bar {
  height: 8px;
  background: rgba(255,255,255,0.08);
  border-radius: var(--radius-full);
  overflow: hidden;
}
.xp-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #f59e0b, #fbbf24);
  border-radius: var(--radius-full);
  transition: width 0.4s ease;
}
.level-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fbbf24;
}
.streak-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.75rem;
  font-weight: 700;
  color: #f97316;
}

/* Level Tabs */
.level-tabs {
  display: flex;
  gap: 4px;
  padding: 10px 14px;
  background: rgba(0,0,0,0.2);
  margin: 6px 14px;
  border-radius: var(--radius-md);
}
.level-tab-btn {
  flex: 1;
  padding: 7px 4px;
  border-radius: var(--radius-sm);
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
}
.level-tab-btn.active {
  background: var(--busuu-blue);
  color: #fff;
  box-shadow: 0 2px 8px rgba(37,99,235,0.4);
}

/* Sidebar Options */
.sidebar-options {
  padding: 8px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.78rem;
  color: var(--text-muted);
}
.toggle-pill {
  padding: 4px 10px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  font-size: 0.72rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}
.toggle-pill:hover {
  background: rgba(255,255,255,0.1);
  color: var(--text-primary);
}

/* Main Content Area */
.main-content {
  margin-left: 290px;
  flex: 1;
  min-height: 100vh;
  padding: 24px 32px 100px;
  max-width: 1200px;
}

/* Top Sticky Navigation Pill on Main Content */
.timeline-top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 12px 20px;
  margin-bottom: 28px;
  box-shadow: var(--shadow-card);
}
.course-identity {
  display: flex;
  align-items: center;
  gap: 12px;
}
.flag-avatar {
  font-size: 1.8rem;
  line-height: 1;
}
.course-name {
  font-weight: 800;
  font-size: 1.05rem;
  color: var(--text-primary);
}
.course-sub {
  font-size: 0.76rem;
  color: var(--text-secondary);
}

.top-stats-row {
  display: flex;
  align-items: center;
  gap: 16px;
}
.stat-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  font-size: 0.82rem;
  font-weight: 700;
}
.stat-pill.streak { color: #f97316; }
.stat-pill.xp { color: #fbbf24; }
.stat-pill.level { color: #60a5fa; }
.sound-toggle-btn {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 6px 10px;
  cursor: pointer;
  color: var(--text-secondary);
  font-size: 0.85rem;
  transition: var(--transition);
}
.sound-toggle-btn:hover { color: var(--text-primary); }

/* ============================================
   BUSUU TIMELINE (STEPPING-STONE LEARNING PATH)
   ============================================ */
.busuu-timeline {
  max-width: 760px;
  margin: 0 auto;
  position: relative;
}

/* Chapter Card Banner */
.timeline-chapter {
  margin-bottom: 60px;
  position: relative;
}
.chapter-banner {
  background: linear-gradient(135deg, rgba(31, 41, 55, 0.85), rgba(17, 24, 39, 0.95));
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 20px 24px;
  margin-bottom: 32px;
  box-shadow: var(--shadow-card);
  position: relative;
  overflow: hidden;
}
.chapter-banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 5px;
  height: 100%;
  background: linear-gradient(180deg, var(--busuu-blue), var(--purple-accent));
}
.chapter-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #60a5fa;
  margin-bottom: 6px;
}
.chapter-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.chapter-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 12px;
}
.chapter-progress-box {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.78rem;
  color: var(--text-muted);
}
.chapter-progress-bar {
  flex: 1;
  height: 6px;
  background: rgba(255,255,255,0.08);
  border-radius: var(--radius-full);
  overflow: hidden;
}
.chapter-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #34d399);
  border-radius: var(--radius-full);
  transition: width 0.4s ease;
}

/* Stepping-Stone Track & Flow */
.path-track {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 28px;
  position: relative;
  padding: 10px 0;
}

/* Vertical Winding SVG Path */
.path-track::before {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 4px;
  background: repeating-linear-gradient(
    180deg,
    rgba(255,255,255,0.12),
    rgba(255,255,255,0.12) 8px,
    transparent 8px,
    transparent 16px
  );
  z-index: 1;
}

/* Stepping Stone Row */
.stone-row {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 2;
  width: 100%;
}
.stone-row.stagger-left { transform: translateX(-55px); }
.stone-row.stagger-center { transform: translateX(0); }
.stone-row.stagger-right { transform: translateX(55px); }

/* The Stone Container */
.stone-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  position: relative;
  transition: var(--transition);
}
.stone-container:hover {
  transform: translateY(-3px) scale(1.02);
}

/* Circular Stone Button */
.stone-circle {
  width: 74px;
  height: 74px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.7rem;
  box-shadow: var(--shadow-stone);
  position: relative;
  transition: var(--transition);
  border: 4px solid transparent;
  user-select: none;
}

/* States */
.stone-circle.completed {
  background: linear-gradient(135deg, #10b981, #059669);
  border-color: #34d399;
  color: #fff;
  box-shadow: 0 0 20px var(--success-green-glow);
}
.stone-circle.active {
  width: 82px;
  height: 82px;
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border-color: #60a5fa;
  color: #fff;
  box-shadow: 0 0 25px var(--busuu-blue-glow);
}
.stone-circle.locked {
  background: #1e293b;
  border-color: rgba(255,255,255,0.08);
  color: var(--text-muted);
  opacity: 0.65;
}

/* Active Stone Pulsing Halo */
@keyframes pulse-ring {
  0% { transform: scale(0.95); opacity: 0.8; }
  50% { transform: scale(1.2); opacity: 0; }
  100% { transform: scale(0.95); opacity: 0; }
}
.stone-circle.active::before {
  content: '';
  position: absolute;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  border-radius: var(--radius-full);
  border: 3px solid #3b82f6;
  animation: pulse-ring 2s infinite cubic-bezier(0.4, 0, 0.6, 1);
  pointer-events: none;
}

/* "START HIER" Floating Callout Badge */
.start-here-beacon {
  position: absolute;
  top: -34px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 12px var(--gold-glow);
  white-space: nowrap;
  animation: bounce-gentle 1.8s infinite;
  display: flex;
  align-items: center;
  gap: 4px;
  z-index: 5;
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
  50% { transform: translateY(-4px); }
}

/* Stone Star Rating Display */
.stone-stars {
  margin-top: 6px;
  font-size: 0.7rem;
  letter-spacing: 2px;
}

/* Stone Title Card Under/Beside */
.stone-card-preview {
  margin-top: 8px;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 8px 14px;
  text-align: center;
  max-width: 210px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
.stone-card-title {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.stone-card-sub {
  font-size: 0.72rem;
  color: var(--text-secondary);
  font-style: italic;
  margin-top: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.stone-card-meta {
  font-size: 0.68rem;
  color: #60a5fa;
  margin-top: 4px;
  font-weight: 600;
}

/* Chapter Milestone Stone */
.milestone-stone-circle {
  width: 90px;
  height: 90px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  background: linear-gradient(135deg, #f59e0b, #b45309);
  border: 4px solid #fde68a;
  box-shadow: 0 0 25px var(--gold-glow);
  color: #fff;
  position: relative;
  cursor: pointer;
  transition: var(--transition);
}
.milestone-stone-circle:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: 0 0 35px var(--gold-glow);
}
.milestone-beacon {
  position: absolute;
  top: -30px;
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  white-space: nowrap;
}

/* ============================================
   BUSUU MICRO-LESSON RUNNER (FULL-SCREEN FLOW)
   ============================================ */
.busuu-runner {
  max-width: 740px;
  margin: 0 auto;
  min-height: 80vh;
  display: flex;
  flex-direction: column;
}

/* Runner Top Bar */
.runner-topbar {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding: 8px 0;
}
.btn-runner-close {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  flex-shrink: 0;
}
.btn-runner-close:hover {
  background: var(--bg-card-hover);
  color: var(--text-primary);
}
.runner-progress-container {
  flex: 1;
  height: 12px;
  background: rgba(255,255,255,0.08);
  border-radius: var(--radius-full);
  overflow: hidden;
  position: relative;
}
.runner-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #2563eb, #60a5fa);
  border-radius: var(--radius-full);
  transition: width 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.runner-step-badge {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-muted);
  white-space: nowrap;
}
.runner-mode-toggle {
  font-size: 0.75rem;
  padding: 6px 12px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition);
}
.runner-mode-toggle:hover {
  color: #fff;
  border-color: #60a5fa;
}

/* Runner Card Body */
.runner-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-xl);
  padding: 36px 32px;
  box-shadow: var(--shadow-card);
  min-height: 460px;
  display: flex;
  flex-direction: column;
  position: relative;
  animation: slideInUp 0.3s ease;
}
@keyframes slideInUp {
  from { opacity: 0; transform: translateY(12px); }
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
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  background: rgba(37,99,235,0.15);
  color: #60a5fa;
  margin-bottom: 20px;
}
.vocab-word-hero {
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 12px;
  line-height: 1.2;
}
.vocab-gender-pill {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: var(--radius-full);
  margin-bottom: 16px;
}
.gender-der { background: rgba(59,130,246,0.2); color: #60a5fa; border: 1px solid rgba(59,130,246,0.3); }
.gender-die { background: rgba(239,68,68,0.2); color: #f87171; border: 1px solid rgba(239,68,68,0.3); }
.gender-das { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(16,185,129,0.3); }
.gender-other { background: rgba(139,92,246,0.2); color: #c4b5fd; border: 1px solid rgba(139,92,246,0.3); }

.audio-hero-btn {
  width: 64px;
  height: 64px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border: none;
  color: #fff;
  font-size: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 6px 20px var(--busuu-blue-glow);
  transition: var(--transition);
  margin: 10px 0 24px;
}
.audio-hero-btn:hover {
  transform: scale(1.08);
  box-shadow: 0 8px 25px var(--busuu-blue-glow);
}
.audio-hero-btn:active { transform: scale(0.96); }

.vocab-meaning {
  font-size: 1.25rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
  font-style: italic;
}

/* Spanish Helper Callout Box (For Guillermo) */
.spanish-helper-box {
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  margin-bottom: 24px;
  text-align: left;
  width: 100%;
}
.spanish-helper-header {
  font-size: 0.78rem;
  font-weight: 800;
  color: #fbbf24;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.spanish-helper-text {
  font-size: 0.85rem;
  color: var(--text-primary);
  line-height: 1.45;
}

/* Real-world Berlin Example Box */
.berlin-example-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  text-align: left;
  width: 100%;
  margin-bottom: 24px;
}
.berlin-example-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #34d399;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.berlin-example-de {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.berlin-example-en {
  font-size: 0.85rem;
  color: var(--text-secondary);
}

/* Step 2: Instant Recall Drill */
.micro-drill-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.drill-instruction {
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #60a5fa;
  margin-bottom: 12px;
}
.drill-question-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px;
  text-align: center;
  margin-bottom: 24px;
}
.drill-question-text {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-primary);
}
.drill-options-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  margin-bottom: 24px;
}
.drill-option-btn {
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  cursor: pointer;
  transition: var(--transition);
  text-align: left;
  display: flex;
  align-items: center;
  gap: 12px;
}
.drill-option-btn:hover {
  background: var(--bg-card-hover);
  border-color: #60a5fa;
  transform: translateX(4px);
}
.drill-option-btn.selected-correct {
  background: rgba(16,185,129,0.18);
  border-color: #10b981;
  color: #34d399;
}
.drill-option-btn.selected-wrong {
  background: rgba(239,68,68,0.18);
  border-color: #ef4444;
  color: #f87171;
}

/* Bottom Sheet Feedback for Micro-Drill */
.runner-feedback-sheet {
  border-radius: var(--radius-lg);
  padding: 18px 24px;
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: slideInUp 0.25s ease;
}
.runner-feedback-sheet.correct {
  background: rgba(16,185,129,0.15);
  border: 1px solid #10b981;
}
.runner-feedback-sheet.wrong {
  background: rgba(239,68,68,0.15);
  border: 1px solid #ef4444;
}
.feedback-text-title {
  font-size: 1.05rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
}
.runner-feedback-sheet.correct .feedback-text-title { color: #34d399; }
.runner-feedback-sheet.wrong .feedback-text-title { color: #f87171; }
.feedback-text-desc {
  font-size: 0.82rem;
  color: var(--text-secondary);
  margin-top: 4px;
}

/* Step 3: Busuu Grammar Snapshot */
.grammar-snapshot-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.grammar-hero-card {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 20px;
}
.grammar-rule-summary {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 16px;
  line-height: 1.5;
}
.syntax-visual-blocks {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 16px 0;
}
.syntax-chip {
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  font-weight: 700;
}
.syntax-chip.connector { background: #f59e0b; color: #000; }
.syntax-chip.subject { background: #3b82f6; color: #fff; }
.syntax-chip.verb-end { background: #ef4444; color: #fff; border: 2px dashed #fca5a5; }
.syntax-chip.neutral { background: rgba(255,255,255,0.1); color: #fff; }

.contrast-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 16px;
}
@media (max-width: 600px) {
  .contrast-row { grid-template-columns: 1fr; }
}
.contrast-box {
  padding: 12px 14px;
  border-radius: var(--radius-md);
  font-size: 0.85rem;
}
.contrast-box.wrong {
  background: rgba(239,68,68,0.1);
  border: 1px solid rgba(239,68,68,0.3);
  color: #fca5a5;
}
.contrast-box.correct {
  background: rgba(16,185,129,0.1);
  border: 1px solid rgba(16,185,129,0.3);
  color: #6ee7b7;
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
  width: 42px;
  height: 42px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  flex-shrink: 0;
}
.chat-bubble {
  max-width: 75%;
  padding: 14px 18px;
  border-radius: 18px;
  position: relative;
}
.chat-msg-row.left .chat-bubble {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-top-left-radius: 4px;
}
.chat-msg-row.right .chat-bubble {
  background: linear-gradient(135deg, rgba(37,99,235,0.25), rgba(37,99,235,0.15));
  border: 1px solid rgba(37,99,235,0.4);
  border-top-right-radius: 4px;
}
.chat-speaker {
  font-size: 0.72rem;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 4px;
}
.chat-text-de {
  font-size: 1.02rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.45;
}
.chat-text-en {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-top: 4px;
}
.play-chat-audio-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 1rem;
  margin-left: 6px;
  transition: var(--transition);
}
.play-chat-audio-btn:hover { color: #60a5fa; }

/* Step 5: Sentence Builder (Word Tiles) */
.tiles-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.tiles-drop-area {
  min-height: 80px;
  background: var(--bg-surface-elevated);
  border: 2px dashed var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 16px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-bottom: 24px;
  transition: var(--transition);
}
.tiles-drop-area.filled {
  border-color: #60a5fa;
  background: rgba(37,99,235,0.08);
}
.tile-chip {
  padding: 10px 16px;
  background: var(--bg-card);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
  cursor: pointer;
  user-select: none;
  box-shadow: 0 4px 10px rgba(0,0,0,0.25);
  transition: var(--transition);
}
.tile-chip:hover {
  transform: translateY(-2px);
  background: var(--bg-card-hover);
  border-color: #60a5fa;
}
.tile-chip.in-drop {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border-color: #60a5fa;
  color: #fff;
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
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 20px;
  margin-bottom: 20px;
}
.production-prompt-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.production-prompt-sub {
  font-size: 0.85rem;
  color: var(--text-secondary);
}
.production-textarea {
  width: 100%;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  font-size: 1.05rem;
  font-family: var(--font-main);
  color: var(--text-primary);
  resize: vertical;
  min-height: 110px;
  margin-bottom: 8px;
}
.production-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 15px var(--busuu-blue-glow);
}
.umlaut-bar {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
}
.umlaut-key {
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
}
.umlaut-key:hover {
  background: var(--busuu-blue);
  color: #fff;
}
.mic-record-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  transition: var(--transition);
}
.mic-record-btn.recording {
  background: #ef4444;
  color: #fff;
  border-color: #f87171;
  animation: pulse-ring 1.5s infinite;
}

/* Step 7: Celebration Screen */
.celebration-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 1;
  padding: 20px 0;
}
.celebration-trophy {
  font-size: 4.5rem;
  animation: bounce-gentle 2s infinite;
  margin-bottom: 12px;
}
.celebration-title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.celebration-sub {
  font-size: 1rem;
  color: var(--text-secondary);
  margin-bottom: 28px;
}
.celebration-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  width: 100%;
  max-width: 440px;
  margin-bottom: 32px;
}
.celebration-stat-card {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 16px 12px;
  text-align: center;
}
.celebration-stat-value {
  font-size: 1.4rem;
  font-weight: 800;
  color: #fbbf24;
}
.celebration-stat-label {
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-top: 4px;
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

/* Common Primary & Secondary Action Buttons */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  border: none;
  color: #fff;
  font-size: 1.02rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 16px var(--busuu-blue-glow);
  transition: var(--transition);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px var(--busuu-blue-glow);
}
.btn-primary:active { transform: translateY(0); }

.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 22px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}
.btn-secondary:hover {
  background: var(--bg-card-hover);
  border-color: rgba(255,255,255,0.2);
}

/* Audio Button Standard */
.audio-btn {
  background: rgba(37,99,235,0.2);
  border: 1px solid rgba(37,99,235,0.3);
  border-radius: var(--radius-full);
  padding: 4px 8px;
  font-size: 0.85rem;
  cursor: pointer;
  color: #60a5fa;
  transition: var(--transition);
}
.audio-btn:hover {
  background: var(--busuu-blue);
  color: #fff;
}
.audio-btn.turtle {
  background: rgba(245,158,11,0.2);
  border-color: rgba(245,158,11,0.3);
  color: #fbbf24;
}

/* ============================================
   ARENAS & FLOATING ASSISTANT
   ============================================ */
/* Professor FAB Button */
.professor-fab {
  position: fixed;
  bottom: 24px;
  right: 28px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 20px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #1e293b, #0f172a);
  border: 2px solid #f59e0b;
  color: #fde68a;
  font-weight: 700;
  font-size: 0.92rem;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(0,0,0,0.5), 0 0 20px var(--gold-glow);
  z-index: 999;
  transition: var(--transition);
}
.professor-fab:hover {
  transform: translateY(-3px) scale(1.03);
}

/* Professor Hub Drawer */
.professor-hub {
  position: fixed;
  top: 0;
  right: 0;
  width: 440px;
  max-width: 95vw;
  height: 100vh;
  background: var(--bg-surface);
  border-left: 1px solid var(--border-subtle);
  box-shadow: -10px 0 35px rgba(0,0,0,0.6);
  z-index: 1000;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
}
.professor-hub.open { transform: translateX(0); }
.professor-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(4px);
  z-index: 998;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}
.professor-backdrop.open { opacity: 1; pointer-events: auto; }

.prof-header {
  padding: 20px;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.prof-title-box { display: flex; align-items: center; gap: 12px; }
.prof-avatar-large { font-size: 2rem; }
.prof-header h3 { font-size: 1.1rem; color: #fbbf24; }
.prof-status { font-size: 0.75rem; color: var(--text-secondary); display: flex; align-items: center; gap: 6px; }
.status-dot { width: 8px; height: 8px; border-radius: var(--radius-full); background: #10b981; }
.prof-close-btn { background: transparent; border: none; font-size: 1.2rem; color: var(--text-muted); cursor: pointer; }

.prof-nav-tabs {
  display: flex;
  border-bottom: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
}
.prof-tab {
  flex: 1;
  padding: 12px 8px;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
}
.prof-tab.active {
  color: #fbbf24;
  border-bottom: 2px solid #fbbf24;
  background: var(--bg-surface);
}

.prof-tab-content {
  flex: 1;
  overflow-y: auto;
  padding: 18px;
  display: none;
}
.prof-tab-content.active { display: flex; flex-direction: column; }

/* Professor Chat Messages */
.prof-chat-messages {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 14px;
}
.prof-msg { display: flex; gap: 10px; }
.prof-msg.user { flex-direction: row-reverse; }
.prof-msg-avatar { font-size: 1.5rem; }
.prof-msg-bubble {
  max-width: 80%;
  padding: 12px 16px;
  border-radius: 16px;
  font-size: 0.9rem;
  line-height: 1.45;
}
.prof-msg.professor .prof-msg-bubble {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-top-left-radius: 4px;
  color: var(--text-primary);
}
.prof-msg.user .prof-msg-bubble {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: #fff;
  border-top-right-radius: 4px;
}
.prof-suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 12px;
}
.prof-chip {
  padding: 5px 10px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  font-size: 0.72rem;
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition);
}
.prof-chip:hover {
  border-color: #fbbf24;
  color: #fbbf24;
}
.prof-chat-input-bar {
  display: flex;
  gap: 8px;
}
.prof-chat-input-bar input {
  flex: 1;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 10px 16px;
  color: var(--text-primary);
  font-size: 0.88rem;
}
.prof-chat-input-bar input:focus {
  outline: none;
  border-color: #3b82f6;
}
.prof-send-btn {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  background: var(--busuu-blue);
  border: none;
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}
.prof-toast {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #10b981;
  color: #fff;
  padding: 10px 20px;
  border-radius: var(--radius-full);
  font-weight: 700;
  font-size: 0.85rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.3);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 2000;
  pointer-events: none;
}
.prof-toast.show { transform: translateX(-50%) translateY(0); }

/* Mobile Hamburger Toggle */
.mobile-toggle {
  display: none;
  position: fixed;
  top: 14px;
  left: 14px;
  z-index: 101;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-primary);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 1.2rem;
  cursor: pointer;
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .mobile-toggle { display: block; }
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .main-content { margin-left: 0; padding: 60px 16px 120px; }
  .stone-row.stagger-left, .stone-row.stagger-right { transform: translateX(0); }
}

/* Reference Lecture Mode Tables */
.reference-lecture-table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  background: var(--bg-surface-elevated);
  border-radius: var(--radius-md);
  overflow: hidden;
}
.reference-lecture-table th {
  background: rgba(255,255,255,0.05);
  padding: 12px 14px;
  text-align: left;
  font-size: 0.82rem;
  color: #60a5fa;
  border-bottom: 1px solid var(--border-subtle);
}
.reference-lecture-table td {
  padding: 12px 14px;
  border-bottom: 1px solid var(--border-subtle);
  font-size: 0.9rem;
}
"""
print(f"styles.py ready. Length: {len(CSS_CONTENT)} chars")
