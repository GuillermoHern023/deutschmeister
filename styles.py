# Complete CSS Stylesheet Overhaul for DeutschMeister (Busuu & Duolingo High-End Modern Aesthetic)

CSS_CONTENT = """
/* ============================================
   DEUTSCHMEISTER — PREMIUM MODERN DESIGN SYSTEM
   Inspired by Busuu & Linear Dark Mode
   ============================================ */
:root {
  --bg-canvas: #0a0d14;
  --bg-surface: #111827;
  --bg-surface-elevated: #1e293b;
  --bg-surface-card: #182234;
  --bg-card: rgba(30, 41, 59, 0.7);
  --bg-card-hover: rgba(51, 65, 85, 0.85);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-medium: rgba(255, 255, 255, 0.14);
  --border-focus: #3b82f6;
  
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  /* Brand Accents */
  --brand-blue: #3b82f6;
  --brand-blue-hover: #2563eb;
  --brand-blue-dark: #1d4ed8;
  --brand-blue-glow: rgba(59, 130, 246, 0.35);
  
  --brand-green: #10b981;
  --brand-green-hover: #059669;
  --brand-green-glow: rgba(16, 185, 129, 0.35);
  
  --brand-amber: #f59e0b;
  --brand-amber-light: #fbbf24;
  --brand-amber-glow: rgba(245, 158, 11, 0.35);
  
  --brand-red: #ef4444;
  --brand-red-glow: rgba(239, 68, 68, 0.3);
  
  --brand-purple: #8b5cf6;
  --brand-purple-glow: rgba(139, 92, 246, 0.3);
  
  /* Typography */
  --font-main: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  /* Radii */
  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-full: 9999px;
  
  /* Shadows & Depth */
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.2);
  --shadow-md: 0 6px 18px rgba(0,0,0,0.35);
  --shadow-lg: 0 12px 35px -5px rgba(0,0,0,0.5), 0 0 1px 1px rgba(255,255,255,0.06);
  --shadow-glow-blue: 0 0 25px var(--brand-blue-glow);
  --shadow-glow-green: 0 0 25px var(--brand-green-glow);
  --shadow-glow-amber: 0 0 25px var(--brand-amber-glow);
  
  --transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
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
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

/* App Shell */
#app { display: flex; width: 100%; min-height: 100vh; }

/* ============================================
   SIDEBAR
   ============================================ */
.sidebar {
  width: 280px;
  background-color: var(--bg-surface);
  border-right: 1px solid var(--border-subtle);
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
}
.sidebar::-webkit-scrollbar { width: 5px; }
.sidebar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }

.sidebar-header {
  padding: 24px 20px 18px;
  border-bottom: 1px solid var(--border-subtle);
}
.sidebar-header h1 {
  font-size: 1.3rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 10px;
}
.sidebar-header h1 span {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.sidebar-header .subtitle {
  font-size: 0.76rem;
  color: var(--text-secondary);
  margin-top: 4px;
}

/* Nav Modes */
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
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-secondary);
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  text-align: left;
  width: 100%;
}
.nav-mode-btn:hover {
  background: var(--bg-surface-elevated);
  color: var(--text-primary);
}
.nav-mode-btn.active {
  background: linear-gradient(135deg, rgba(59,130,246,0.18), rgba(59,130,246,0.06));
  color: #60a5fa;
  border-color: rgba(59,130,246,0.35);
  font-weight: 700;
}
.nav-mode-badge {
  margin-left: auto;
  font-size: 0.65rem;
  padding: 2px 7px;
  border-radius: var(--radius-full);
  background: rgba(59,130,246,0.25);
  color: #93c5fd;
  font-weight: 700;
}

/* User Progress Bar in Sidebar */
.xp-bar-container {
  padding: 14px 16px;
  margin: 6px 14px;
  background: var(--bg-surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}
.xp-label {
  display: flex;
  justify-content: space-between;
  font-size: 0.74rem;
  color: var(--text-secondary);
  font-weight: 600;
  margin-bottom: 8px;
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
  font-size: 0.76rem;
  font-weight: 700;
  color: #fbbf24;
}
.streak-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.76rem;
  font-weight: 700;
  color: #f97316;
}

/* Level Tabs */
.level-tabs {
  display: flex;
  gap: 4px;
  padding: 4px;
  background: rgba(0,0,0,0.3);
  margin: 6px 14px;
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
  background: var(--brand-blue);
  color: #fff;
  box-shadow: 0 2px 8px rgba(59,130,246,0.45);
}

/* Sidebar Options */
.sidebar-options {
  padding: 6px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.76rem;
  color: var(--text-muted);
}
.toggle-pill {
  padding: 5px 12px;
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
  background: rgba(255,255,255,0.12);
  color: var(--text-primary);
  border-color: var(--border-medium);
}

/* ============================================
   MAIN CONTENT AREA
   ============================================ */
.main-content {
  margin-left: 280px;
  flex: 1;
  min-height: 100vh;
  padding: 24px 36px 120px;
  max-width: 1100px;
}

/* Top Sticky Navigation Pill */
.timeline-top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 14px;
  background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(17, 24, 39, 0.8));
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 14px 22px;
  margin-bottom: 36px;
  box-shadow: var(--shadow-lg);
}
.course-identity {
  display: flex;
  align-items: center;
  gap: 14px;
}
.flag-avatar {
  font-size: 2rem;
  line-height: 1;
  filter: drop-shadow(0 2px 8px rgba(0,0,0,0.3));
}
.course-name {
  font-weight: 800;
  font-size: 1.15rem;
  letter-spacing: -0.01em;
  color: #fff;
}
.course-sub {
  font-size: 0.78rem;
  color: var(--text-secondary);
}

.top-stats-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
.stat-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  font-size: 0.82rem;
  font-weight: 700;
  box-shadow: var(--shadow-sm);
}
.stat-pill.streak { color: #f97316; border-color: rgba(249,115,22,0.25); }
.stat-pill.xp { color: #fbbf24; border-color: rgba(251,191,36,0.25); }
.stat-pill.level { color: #60a5fa; border-color: rgba(96,165,250,0.25); }

.sound-toggle-btn {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 7px 12px;
  cursor: pointer;
  color: var(--text-secondary);
  font-size: 0.9rem;
  transition: var(--transition);
}
.sound-toggle-btn:hover {
  color: var(--text-primary);
  border-color: var(--border-medium);
  transform: scale(1.05);
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
  background: linear-gradient(145deg, #182234, #0f172a);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-lg);
  padding: 24px 28px;
  margin-bottom: 40px;
  box-shadow: var(--shadow-lg);
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
  background: linear-gradient(180deg, var(--brand-blue), var(--brand-purple));
  border-radius: 6px 0 0 6px;
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
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: #fff;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.chapter-desc {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 16px;
}
.chapter-progress-box {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 0.8rem;
  color: var(--text-muted);
}
.chapter-progress-bar {
  flex: 1;
  height: 8px;
  background: rgba(255,255,255,0.08);
  border-radius: var(--radius-full);
  overflow: hidden;
}
.chapter-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #34d399);
  border-radius: var(--radius-full);
  transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Stepping-Stone Track */
.path-track {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 36px;
  position: relative;
  padding: 10px 0;
}

/* Vertical Continuous Connecting Trail */
.path-track::before {
  content: '';
  position: absolute;
  top: 10px;
  bottom: 20px;
  width: 6px;
  background: repeating-linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.12),
    rgba(255, 255, 255, 0.12) 10px,
    transparent 10px,
    transparent 20px
  );
  border-radius: var(--radius-full);
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
.stone-row.stagger-left { transform: translateX(-65px); }
.stone-row.stagger-center { transform: translateX(0); }
.stone-row.stagger-right { transform: translateX(65px); }

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
  transform: translateY(-4px);
}

/* Tactile 3D Circular Stone Button */
.stone-circle {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.85rem;
  position: relative;
  transition: var(--transition);
  user-select: none;
}

/* States with Tactile 3D Depths (Busuu & Duolingo style) */
.stone-circle.completed {
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border: 3px solid #34d399;
  box-shadow: 0 8px 0 #047857, 0 12px 24px var(--brand-green-glow);
  color: #fff;
}
.stone-circle.completed:active {
  transform: translateY(6px);
  box-shadow: 0 2px 0 #047857, 0 6px 14px var(--brand-green-glow);
}

.stone-circle.active {
  width: 88px;
  height: 88px;
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  border: 3px solid #93c5fd;
  box-shadow: 0 9px 0 #1e40af, 0 15px 30px var(--brand-blue-glow);
  color: #fff;
}
.stone-circle.active:active {
  transform: translateY(7px);
  box-shadow: 0 2px 0 #1e40af, 0 6px 16px var(--brand-blue-glow);
}

.stone-circle.locked {
  background: #1e293b;
  border: 2px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 6px 0 #0f172a;
  color: #64748b;
  opacity: 0.7;
}

/* Pulsing Halo on Active Stone */
@keyframes pulse-ring {
  0% { transform: scale(0.96); opacity: 0.85; }
  50% { transform: scale(1.22); opacity: 0; }
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
  border: 3px solid #60a5fa;
  animation: pulse-ring 2.2s infinite cubic-bezier(0.4, 0, 0.6, 1);
  pointer-events: none;
}

/* "START HIER" Floating Badge */
.start-here-beacon {
  position: absolute;
  top: -36px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 5px 14px;
  border-radius: var(--radius-full);
  box-shadow: 0 4px 14px var(--brand-amber-glow);
  white-space: nowrap;
  animation: bounce-gentle 1.8s infinite;
  display: flex;
  align-items: center;
  gap: 5px;
  z-index: 5;
}
.start-here-beacon::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  border-width: 6px 6px 0;
  border-style: solid;
  border-color: #d97706 transparent transparent;
}
@keyframes bounce-gentle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}

/* Stone Star Rating Display */
.stone-stars {
  margin-top: 10px;
  font-size: 0.76rem;
  letter-spacing: 2px;
}

/* Stone Preview Card Underneath */
.stone-card-preview {
  margin-top: 10px;
  background: var(--bg-surface-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px 16px;
  text-align: center;
  max-width: 220px;
  box-shadow: var(--shadow-md);
  transition: var(--transition);
}
.stone-container:hover .stone-card-preview {
  border-color: rgba(96, 165, 250, 0.4);
  box-shadow: 0 8px 20px rgba(0,0,0,0.4);
}
.stone-card-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.stone-card-sub {
  font-size: 0.74rem;
  color: var(--text-secondary);
  margin-top: 2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.stone-card-meta {
  font-size: 0.7rem;
  color: #60a5fa;
  margin-top: 4px;
  font-weight: 600;
}

/* Chapter Milestone Stone */
.milestone-stone-circle {
  width: 96px;
  height: 96px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.4rem;
  background: linear-gradient(135deg, #f59e0b 0%, #b45309 100%);
  border: 4px solid #fde68a;
  box-shadow: 0 9px 0 #78350f, 0 16px 30px var(--brand-amber-glow);
  color: #fff;
  position: relative;
  cursor: pointer;
  transition: var(--transition);
}
.milestone-stone-circle:hover {
  transform: translateY(-4px);
  box-shadow: 0 13px 0 #78350f, 0 20px 40px var(--brand-amber-glow);
}
.milestone-stone-circle:active {
  transform: translateY(7px);
  box-shadow: 0 2px 0 #78350f, 0 8px 16px var(--brand-amber-glow);
}
.milestone-beacon {
  position: absolute;
  top: -32px;
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  white-space: nowrap;
  box-shadow: 0 4px 12px var(--brand-green-glow);
}

/* ============================================
   BUSUU MICRO-LESSON RUNNER (FULL-SCREEN FLOW)
   ============================================ */
.busuu-runner {
  max-width: 720px;
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
  padding: 4px 0;
}
.btn-runner-close {
  width: 42px;
  height: 42px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  font-size: 1.15rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  flex-shrink: 0;
}
.btn-runner-close:hover {
  background: var(--bg-card-hover);
  color: #fff;
  border-color: var(--border-medium);
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
  background: linear-gradient(90deg, #3b82f6, #60a5fa, #34d399);
  border-radius: var(--radius-full);
  transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.runner-step-badge {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-muted);
  white-space: nowrap;
}
.runner-mode-toggle {
  font-size: 0.76rem;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  border: 1px solid var(--border-subtle);
  background: var(--bg-surface-elevated);
  color: var(--text-secondary);
  cursor: pointer;
  transition: var(--transition);
  font-weight: 600;
}
.runner-mode-toggle:hover {
  color: #fff;
  border-color: #60a5fa;
}

/* Runner Card Body */
.runner-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-lg);
  padding: 38px 34px;
  box-shadow: var(--shadow-lg);
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
  font-size: 0.74rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 5px 14px;
  border-radius: var(--radius-full);
  background: rgba(59,130,246,0.15);
  color: #60a5fa;
  margin-bottom: 22px;
}
.vocab-word-hero {
  font-size: 2.6rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
  line-height: 1.2;
}
.vocab-gender-pill {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: var(--radius-full);
  margin-bottom: 18px;
}
.gender-der { background: rgba(59,130,246,0.22); color: #60a5fa; border: 1px solid rgba(59,130,246,0.35); }
.gender-die { background: rgba(239,68,68,0.22); color: #f87171; border: 1px solid rgba(239,68,68,0.35); }
.gender-das { background: rgba(16,185,129,0.22); color: #34d399; border: 1px solid rgba(16,185,129,0.35); }
.gender-other { background: rgba(139,92,246,0.22); color: #c4b5fd; border: 1px solid rgba(139,92,246,0.35); }

.audio-hero-btn {
  width: 68px;
  height: 68px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  border: none;
  color: #fff;
  font-size: 1.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 8px 0 #1e40af, 0 14px 28px var(--brand-blue-glow);
  transition: var(--transition);
  margin: 10px 0 24px;
}
.audio-hero-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 0 #1e40af, 0 16px 32px var(--brand-blue-glow);
}
.audio-hero-btn:active {
  transform: translateY(6px);
  box-shadow: 0 2px 0 #1e40af, 0 6px 16px var(--brand-blue-glow);
}

.vocab-meaning {
  font-size: 1.35rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
  font-weight: 500;
}

/* Spanish Helper Callout Box (For Guillermo) */
.spanish-helper-box {
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  margin-bottom: 24px;
  text-align: left;
  width: 100%;
}
.spanish-helper-header {
  font-size: 0.8rem;
  font-weight: 800;
  color: #fbbf24;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.spanish-helper-text {
  font-size: 0.88rem;
  color: #f1f5f9;
  line-height: 1.5;
}

/* Real-world Berlin Example Box */
.berlin-example-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  text-align: left;
  width: 100%;
  margin-bottom: 28px;
}
.berlin-example-label {
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #34d399;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.berlin-example-de {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.berlin-example-en {
  font-size: 0.86rem;
  color: var(--text-secondary);
}

/* Step 2: Instant Recall Drill */
.micro-drill-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.drill-instruction {
  font-size: 0.82rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #60a5fa;
  margin-bottom: 12px;
}
.drill-question-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 24px;
  text-align: center;
  margin-bottom: 24px;
}
.drill-question-text {
  font-size: 1.4rem;
  font-weight: 800;
  color: #fff;
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
  padding: 16px 22px;
  font-size: 1.02rem;
  font-weight: 600;
  color: var(--text-primary);
  cursor: pointer;
  transition: var(--transition);
  text-align: left;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 4px 0 #0f172a;
}
.drill-option-btn:hover {
  background: var(--bg-card-hover);
  border-color: #60a5fa;
  transform: translateY(-2px);
  box-shadow: 0 6px 0 #0f172a;
}
.drill-option-btn:active {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #0f172a;
}
.drill-option-btn.selected-correct {
  background: rgba(16,185,129,0.2);
  border-color: #10b981;
  color: #34d399;
}
.drill-option-btn.selected-wrong {
  background: rgba(239,68,68,0.2);
  border-color: #ef4444;
  color: #f87171;
}

/* Bottom Sheet Feedback for Micro-Drill */
.runner-feedback-sheet {
  border-radius: var(--radius-md);
  padding: 18px 24px;
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: slideInUp 0.25s ease;
}
.runner-feedback-sheet.correct {
  background: rgba(16,185,129,0.18);
  border: 1px solid #10b981;
}
.runner-feedback-sheet.wrong {
  background: rgba(239,68,68,0.18);
  border: 1px solid #ef4444;
}
.feedback-text-title {
  font-size: 1.1rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
}
.runner-feedback-sheet.correct .feedback-text-title { color: #34d399; }
.runner-feedback-sheet.wrong .feedback-text-title { color: #f87171; }
.feedback-text-desc {
  font-size: 0.85rem;
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
  border: 1px solid var(--border-subtle);
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
  border-radius: 18px;
  position: relative;
  box-shadow: var(--shadow-sm);
}
.chat-msg-row.left .chat-bubble {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-top-left-radius: 4px;
}
.chat-msg-row.right .chat-bubble {
  background: linear-gradient(135deg, rgba(59,130,246,0.25), rgba(59,130,246,0.12));
  border: 1px solid rgba(59,130,246,0.4);
  border-top-right-radius: 4px;
}
.chat-speaker {
  font-size: 0.72rem;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 4px;
}
.chat-text-de {
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
  line-height: 1.45;
}
.chat-text-en {
  font-size: 0.82rem;
  color: var(--text-muted);
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
.play-chat-audio-btn:hover { color: #60a5fa; }

/* Step 5: Sentence Builder (Word Tiles) */
.tiles-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.tiles-drop-area {
  min-height: 84px;
  background: var(--bg-surface-elevated);
  border: 2px dashed var(--border-subtle);
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
  border-color: #60a5fa;
  background: rgba(59,130,246,0.08);
}
.tile-chip {
  padding: 10px 18px;
  background: var(--bg-surface-card);
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-sm);
  font-size: 1.02rem;
  font-weight: 700;
  color: #fff;
  cursor: pointer;
  user-select: none;
  box-shadow: 0 4px 0 #0f172a;
  transition: var(--transition);
}
.tile-chip:hover {
  transform: translateY(-2px);
  border-color: #60a5fa;
  box-shadow: 0 6px 0 #0f172a;
}
.tile-chip.in-drop {
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border-color: #93c5fd;
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
  border-radius: var(--radius-md);
  padding: 20px;
  margin-bottom: 20px;
}
.production-prompt-title {
  font-size: 1.2rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 8px;
}
.production-prompt-sub {
  font-size: 0.88rem;
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
  color: #fff;
  resize: vertical;
  min-height: 110px;
  margin-bottom: 8px;
  box-shadow: var(--shadow-sm);
}
.production-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: var(--shadow-glow-blue);
}
.umlaut-bar {
  display: flex;
  gap: 6px;
  margin-bottom: 16px;
}
.umlaut-key {
  padding: 6px 14px;
  border-radius: var(--radius-xs);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: #fff;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
}
.umlaut-key:hover {
  background: var(--brand-blue);
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
  color: #fff;
  font-weight: 600;
  font-size: 0.86rem;
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
  color: #fff;
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
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 18px 14px;
  text-align: center;
  box-shadow: var(--shadow-sm);
}
.celebration-stat-value {
  font-size: 1.5rem;
  font-weight: 800;
  color: #fbbf24;
}
.celebration-stat-label {
  font-size: 0.74rem;
  color: var(--text-muted);
  margin-top: 4px;
  font-weight: 600;
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

/* Primary & Secondary Buttons */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 28px;
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  border: none;
  color: #fff;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 16px var(--brand-blue-glow);
  transition: var(--transition);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 22px var(--brand-blue-glow);
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
  color: #fff;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}
.btn-secondary:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-medium);
}

/* Audio Button Standard */
.audio-btn {
  background: rgba(59,130,246,0.18);
  border: 1px solid rgba(59,130,246,0.3);
  border-radius: var(--radius-full);
  padding: 4px 10px;
  font-size: 0.85rem;
  cursor: pointer;
  color: #60a5fa;
  transition: var(--transition);
}
.audio-btn:hover {
  background: var(--brand-blue);
  color: #fff;
  transform: scale(1.05);
}

/* Step 2b: Fill-in-the-Blank (Lückentext) */
.fill-blank-stage {
  display: flex;
  flex-direction: column;
  flex: 1;
}
.fill-blank-sentence-card {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 26px 22px;
  text-align: center;
  margin-bottom: 22px;
  font-size: 1.3rem;
  font-weight: 600;
  color: #fff;
  line-height: 1.6;
}
.blank-placeholder {
  display: inline-block;
  min-width: 90px;
  border-bottom: 3px solid #60a5fa;
  color: #60a5fa;
  font-weight: 800;
  padding: 0 8px;
}
.fill-blank-hint {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: #fbbf24;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid rgba(245, 158, 11, 0.25);
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
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 14px 18px;
  font-size: 1.15rem;
  font-weight: 600;
  color: #fff;
  transition: var(--transition);
}
.fill-blank-input:focus {
  outline: none;
  border-color: #60a5fa;
  box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
}
.fill-blank-input.correct {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.12);
  color: #34d399;
}
.fill-blank-input.wrong {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.12);
  color: #f87171;
}

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
  background: var(--bg-surface-elevated);
  border: 2px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px 14px;
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--text-primary);
  text-align: center;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 4px 0 #0f172a;
  min-height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
}
.matching-card:hover {
  background: var(--bg-card-hover);
  border-color: #60a5fa;
  transform: translateY(-2px);
  box-shadow: 0 6px 0 #0f172a;
}
.matching-card:active {
  transform: translateY(2px);
  box-shadow: 0 2px 0 #0f172a;
}
.matching-card.selected {
  border-color: #3b82f6;
  background: rgba(59, 130, 246, 0.22);
  color: #93c5fd;
  box-shadow: 0 4px 0 #1e40af, 0 0 12px rgba(59, 130, 246, 0.4);
  transform: translateY(-2px);
}
.matching-card.matched {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.2);
  color: #34d399;
  cursor: default;
  pointer-events: none;
  box-shadow: none;
  opacity: 0.88;
}
.matching-card.wrong {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.25);
  color: #f87171;
  animation: matchShake 0.4s ease;
}
@keyframes matchShake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}

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
  border-radius: var(--radius-xs);
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
"""
