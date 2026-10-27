"""
body.py - Clean, focused HTML structure for DeutschMeister
Focuses 100% on a distraction-free, progressive course journey from A1 to B1.
"""

BODY_CONTENT = """
<button class="mobile-toggle" onclick="toggleSidebar()" aria-label="Menu">☰</button>

<div id="app">
  <!-- Modern Sleek Sidebar -->
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h1>🇩🇪 DeutschMeister</h1>
      <div class="subtitle">Lernpfad • A1 bis B1</div>
    </div>

    <!-- XP Bar & Daily Stats -->
    <div class="xp-bar-container">
      <div class="xp-label">
        <span id="xp-current">0 XP</span>
        <span id="xp-next">100 XP</span>
      </div>
      <div class="xp-bar"><div class="xp-bar-fill" id="xp-bar-fill" style="width:0%"></div></div>
      <div style="display:flex;justify-content:center;gap:12px;margin-top:10px">
        <span class="level-badge" id="level-badge">⭐ Level 1</span>
        <span class="streak-badge" id="streak-badge">🔥 0 Tage</span>
      </div>

      <!-- 15-Minute Daily Study Timer Card -->
      <button class="sidebar-timer-card" id="sidebar-timer-card" onclick="toggleDailyTimer()" title="15 Minuten täglicher Fokus: Klicke zum Starten/Pausieren">
        <div style="display:flex;align-items:center;gap:10px">
          <span style="font-size:1.25rem">⏱️</span>
          <div style="text-align:left">
            <div style="font-size:0.68rem;text-transform:uppercase;color:var(--text-muted);font-weight:700;letter-spacing:0.04em">15-Min. Tagesziel</div>
            <div style="font-size:1rem;font-weight:800;color:var(--text-primary)" class="timer-display-text" id="sidebar-timer-display">15:00</div>
          </div>
        </div>
        <span class="timer-status-badge" id="sidebar-timer-badge">Start</span>
      </button>
    </div>

    <!-- Level Selector Tabs -->
    <div style="padding:10px 14px 4px;font-size:0.75rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.05em">Stufe wählen:</div>
    <div class="level-tabs" id="level-tabs-container">
      <button class="level-tab-btn active" id="btn-level-a1" onclick="changeLevel('A1')">A1</button>
      <button class="level-tab-btn" id="btn-level-a21" onclick="changeLevel('A2.1')">A2.1</button>
      <button class="level-tab-btn" id="btn-level-a22" onclick="changeLevel('A2.2')">A2.2</button>
      <button class="level-tab-btn" id="btn-level-b1" onclick="changeLevel('B1')">B1</button>
    </div>

    <!-- Quick Navigation to Chapter on Timeline -->
    <div id="sidebar-chapters" style="flex:1;overflow-y:auto;padding:8px 14px"></div>

    <!-- Sidebar Bottom Controls -->
    <div style="padding:14px 18px;border-top:1px solid var(--border-subtle);display:flex;flex-direction:column;gap:10px">
      <div class="sidebar-options">
        <span>Thema:</span>
        <button class="toggle-pill" id="btn-theme-toggle" onclick="toggleTheme()" title="Zwischen Pastel Tag und Pastel Nacht wechseln">🌸 Pastel Tag</button>
      </div>

      <div class="sidebar-options" style="padding-top:2px">
        <span>Fortschritt:</span>
        <button class="toggle-pill" id="btn-unlock-toggle" onclick="toggleFreeMode()" title="Lerne der Reihe nach oder schalte alle Lektionen frei">🔒 Schritt für Schritt</button>
      </div>

      <div class="sidebar-options" style="padding-top:2px">
        <span>Soundeffekte:</span>
        <button class="toggle-pill" id="btn-sound-toggle" onclick="toggleSound()" title="Audio-Feedback an/aus">🔊 Ton: An</button>
      </div>

      <button class="btn-secondary" style="width:100%;font-size:0.78rem;padding:8px;margin-top:4px" onclick="resetProgress()">
        ⚙️ Fortschritt zurücksetzen
      </button>
    </div>
  </nav>

  <!-- Main Content Container -->
  <main class="main-content" id="main-content">
    <!-- Rendered dynamically -->
  </main>
</div>
"""
print(f"body.py ready. Length: {len(BODY_CONTENT)} chars")
