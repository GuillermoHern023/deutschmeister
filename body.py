# HTML Body for DeutschMeister

BODY_CONTENT = """
<button class="mobile-toggle" onclick="toggleSidebar()" aria-label="Menu">☰</button>

<div id="app">
  <!-- Modern Sleek Sidebar -->
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <h1>🇩🇪 DeutschMeister</h1>
      <div class="subtitle">Busuu-Lernpfad • A2.1 bis B1 & Goethe</div>
    </div>

    <!-- Main Navigation Arenas -->
    <div class="nav-modes">
      <button class="nav-mode-btn active" id="nav-mode-course" onclick="switchNavMode('course')">
        <span>🗺️</span>
        <span>Busuu-Lernpfad</span>
      </button>
      <button class="nav-mode-btn" id="nav-mode-survival" onclick="switchNavMode('survival')">
        <span>🌆</span>
        <span>Berlin Alltags-Simulator</span>
      </button>
      <button class="nav-mode-btn" id="nav-mode-goethe" onclick="switchNavMode('goethe')">
        <span>🏛️</span>
        <span>Goethe-Prüfungszentrum</span>
        <span class="nav-mode-badge">A2 / B1</span>
      </button>
      <button class="nav-mode-btn" id="nav-mode-trainer" onclick="switchNavMode('trainer')">
        <span>⚡</span>
        <span>Grammatik & Artikel Sprint</span>
      </button>
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
    </div>

    <!-- Learning Mode Options -->
    <div class="sidebar-options">
      <span>Fortschritt:</span>
      <button class="toggle-pill" id="btn-unlock-toggle" onclick="toggleFreeMode()" title="Lerne der Reihe nach oder schalte alle Lektionen frei">🔒 Schritt für Schritt</button>
    </div>

    <div class="sidebar-options" style="padding-top:2px">
      <span>Soundeffekte:</span>
      <button class="toggle-pill" id="btn-sound-toggle" onclick="toggleSound()" title="Audio-Feedback an/aus">🔊 Ton: An</button>
    </div>

    <!-- Level Selector Tabs -->
    <div style="padding:4px 14px 2px;font-size:0.75rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.05em">Stufe wählen:</div>
    <div class="level-tabs" id="level-tabs-container">
      <button class="level-tab-btn active" id="btn-level-a21" onclick="changeLevel('A2.1')">A2.1</button>
      <button class="level-tab-btn" id="btn-level-a22" onclick="changeLevel('A2.2')">A2.2</button>
      <button class="level-tab-btn" id="btn-level-b1" onclick="changeLevel('B1')">B1</button>
    </div>

    <!-- Quick Navigation to Chapter -->
    <div id="sidebar-chapters" style="flex:1;overflow-y:auto;padding:8px 14px"></div>

    <!-- Bottom Actions -->
    <div style="padding:14px 18px;border-top:1px solid var(--border-subtle)">
      <button class="btn-secondary" style="width:100%;font-size:0.78rem;padding:8px" onclick="resetProgress()">
        ⚙️ Fortschritt zurücksetzen
      </button>
    </div>
  </nav>

  <!-- Main Content Container -->
  <main class="main-content" id="main-content">
    <!-- Rendered dynamically -->
  </main>
</div>

<!-- Floating Professor FAB Button -->
<button class="professor-fab" onclick="toggleProfessorHub()" title="Dein persönlicher Deutschlehrer & Korrektor">
  <span style="font-size:1.35rem">👨‍🏫</span>
  <span>Herr Professor</span>
</button>

<!-- Backdrop -->
<div class="professor-backdrop" id="professor-backdrop" onclick="closeProfessorHub()"></div>

<!-- Sliding Professor Hub Drawer -->
<aside class="professor-hub" id="professor-hub" aria-label="Professor Assistant">
  <div class="prof-header">
    <div class="prof-title-box">
      <div class="prof-avatar-large">👨‍🏫</div>
      <div>
        <h3>Herr Professor</h3>
        <div class="prof-status"><span class="status-dot"></span> Bereit für Feedback & Dialog</div>
      </div>
    </div>
    <button class="prof-close-btn" onclick="closeProfessorHub()">✕</button>
  </div>

  <div class="prof-nav-tabs">
    <button class="prof-tab active" id="prof-tab-btn-chat" onclick="switchProfTab('chat')">💬 Live-Chat</button>
    <button class="prof-tab" id="prof-tab-btn-corrector" onclick="switchProfTab('corrector')">✍️ Korrektor</button>
    <button class="prof-tab" id="prof-tab-btn-settings" onclick="switchProfTab('settings')">⚙️ Einstellungen</button>
  </div>

  <!-- Tab 1: Live Chat -->
  <div class="prof-tab-content active" id="prof-content-chat">
    <div class="prof-chat-messages" id="prof-chat-messages">
      <div class="prof-msg professor">
        <div class="prof-msg-avatar">👨‍🏫</div>
        <div class="prof-msg-bubble">
          <strong>Hallo Guillermo! Willkommen im Unterricht!</strong><br>
          Ich bin dein persönlicher Deutschlehrer. Frag mich alles zur Grammatik, übe Konversation auf Deutsch oder bitte mich um Beispielsätze für deinen Berliner Alltag!
        </div>
      </div>
    </div>
    
    <div class="prof-suggestions" id="prof-suggestions">
      <button class="prof-chip" onclick="askProfSuggestion('Erklär mir kurz den Unterschied zwischen weil und deshalb!')">💡 weil vs. deshalb</button>
      <button class="prof-chip" onclick="askProfSuggestion('Wie schreibe ich eine perfekte E-Mail für das Goethe-Zertifikat?')">✉️ Goethe-Schreibtipps</button>
      <button class="prof-chip" onclick="askProfSuggestion('Lass uns ein kurzes Alltagsgespräch über Berlin führen!')">☕ Smalltalk auf Deutsch</button>
    </div>

    <form class="prof-chat-input-bar" onsubmit="sendProfChatMessage(event)">
      <input type="text" id="prof-chat-input" placeholder="Schreib deinem Professor auf Deutsch..." autocomplete="off">
      <button type="submit" class="prof-send-btn" id="prof-send-btn">➤</button>
    </form>
  </div>

  <!-- Tab 2: Corrector -->
  <div class="prof-tab-content" id="prof-content-corrector">
    <p style="font-size:0.86rem;color:var(--text-secondary);margin-bottom:12px">
      Schreib hier deine deutschen Sätze oder Hausaufgaben. Ich analysiere Satzbau, Verbstellung bei <em>weil/obwohl/deshalb</em> und Fälle:
    </p>

    <div class="umlaut-bar">
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('ä')">ä</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('ö')">ö</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('ü')">ü</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('ß')">ß</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('Ä')">Ä</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('Ö')">Ö</button>
      <button type="button" class="umlaut-key" onclick="insertUmlautProf('Ü')">Ü</button>
    </div>

    <textarea id="prof-corrector-text" class="production-textarea" rows="6" placeholder="Schreib hier deine Sätze auf Deutsch..."></textarea>
    <div style="text-align:right;font-size:0.75rem;color:var(--text-muted);margin:4px 0 12px"><span id="prof-char-count">0</span> Zeichen</div>

    <div style="display:flex;gap:10px;margin-bottom:14px">
      <button class="btn-primary" style="flex:1" onclick="analyzeTextWithProfessor()">⚡ Im Browser analysieren</button>
      <button class="btn-secondary" style="flex:1" onclick="copyTextForChat()">📋 Für Chat kopieren</button>
    </div>

    <div id="prof-corrector-result" class="berlin-example-box" style="display:none;padding:16px;border-color:var(--gold-star);"></div>
  </div>

  <!-- Tab 3: Settings -->
  <div class="prof-tab-content" id="prof-content-settings">
    <div style="background:var(--bg-surface-elevated);border:1px solid var(--border-subtle);border-radius:var(--radius-lg);padding:18px">
      <h4 style="color:var(--gold-light);margin-bottom:8px">🤖 Google Gemini KI-Anbindung</h4>
      <p style="font-size:0.83rem;color:var(--text-secondary);margin-bottom:12px;line-height:1.5">
        Trage deinen kostenlosen <strong>Google Gemini API Key</strong> ein für unbegrenzte, intelligente Live-Korrekturen und freie Konversation direkt im Browser. Der Key wird sicher ausschließlich lokal in deinem Browser (localStorage) gespeichert.
      </p>
      <div style="display:flex;gap:8px;margin-bottom:10px">
        <input type="password" id="prof-api-key-input" class="production-textarea" style="min-height:auto;padding:8px 12px;flex:1" placeholder="AIzaSy...">
        <button class="btn-secondary" style="padding:0 12px" onclick="toggleApiKeyVisibility()">👁️</button>
      </div>
      <button class="btn-primary" style="width:100%;margin-bottom:12px" onclick="saveApiKey()">Key speichern</button>
      <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noopener" style="color:var(--busuu-blue);font-size:0.8rem;text-decoration:none;display:inline-block">
        🔗 Kostenlosen Gemini Key auf Google AI Studio holen (30 Sek.) →
      </a>

      <hr style="border:0;border-top:1px solid var(--border-subtle);margin:18px 0">

      <h4 style="color:var(--gold-light);margin-bottom:8px">🗣️ Erklär-Sprache (Feedback)</h4>
      <select id="prof-lang-pref" class="production-textarea" style="min-height:auto;padding:8px 12px" onchange="saveProfLangPref()">
        <option value="de_en">Deutsch mit englischen Erklärungen (Empfohlen)</option>
        <option value="de_es">Deutsch mit spanischen Erklärungen (Para Guillermo)</option>
        <option value="de_only">100% Deutsch (Immersion)</option>
      </select>
    </div>
  </div>
</aside>

<div id="prof-toast" class="prof-toast">In die Zwischenablage kopiert! 📋</div>
"""
print(f"body.py ready. Length: {len(BODY_CONTENT)} chars")
