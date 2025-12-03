def get_enhanced_ui_html():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhisperLiveKit - Real-time Speech Recognition</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f5f5f5;
            --text-primary: #333333;
            --text-secondary: #666666;
            --accent: #4CAF50;
            --border: #e0e0e0;
            --shadow: rgba(0,0,0,0.1);
            --github-star: #ffd700;
        }
        
        [data-theme="dark"] {
            --bg-primary: #1a1a1a;
            --bg-secondary: #2d2d2d;
            --text-primary: #e0e0e0;
            --text-secondary: #a0a0a0;
            --accent: #66BB6A;
            --border: #404040;
            --shadow: rgba(0,0,0,0.3);
            --github-star: #ffd700;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            transition: all 0.3s ease;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 2px solid var(--border);
            margin-bottom: 20px;
        }
        
        h1 { font-size: 28px; color: var(--accent); }
        
        .controls {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        
        /* GitHub 按钮组样式 */
        .github-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            padding: 15px;
            background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
            border-radius: 12px;
            box-shadow: 0 2px 8px var(--shadow);
            flex-wrap: wrap;
            align-items: center;
        }
        
        .github-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 500;
            font-size: 14px;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .github-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px var(--shadow);
        }
        
        .btn-star {
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            color: #000;
            border-color: #ffd700;
            font-size: 16px;
            font-weight: 600;
            animation: pulse 2s infinite;
        }
        
        .btn-star:hover {
            background: linear-gradient(135deg, #ffed4e 0%, #ffd700 100%);
            box-shadow: 0 4px 20px rgba(255, 215, 0, 0.4);
        }
        
        .btn-bug {
            background: #f44336;
            color: white;
        }
        
        .btn-bug:hover {
            background: #d32f2f;
        }
        
        .btn-feature {
            background: #2196F3;
            color: white;
        }
        
        .btn-feature:hover {
            background: #1976D2;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
            background: var(--accent);
            color: white;
        }
        
        button:hover { opacity: 0.9; transform: translateY(-1px); }
        button:disabled { opacity: 0.5; cursor: not-allowed; }
        
        .btn-secondary {
            background: var(--bg-secondary);
            color: var(--text-primary);
            border: 1px solid var(--border);
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 300px;
            gap: 20px;
        }
        
        @media (max-width: 768px) {
            .main-content { grid-template-columns: 1fr; }
            .github-buttons { justify-content: center; }
        }
        
        .transcription-area {
            background: var(--bg-secondary);
            border-radius: 12px;
            padding: 20px;
            min-height: 400px;
            box-shadow: 0 2px 8px var(--shadow);
        }
        
        .settings-panel {
            background: var(--bg-secondary);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 2px 8px var(--shadow);
        }
        
        .setting-group {
            margin-bottom: 20px;
        }
        
        .setting-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--text-secondary);
        }
        
        select, input {
            width: 100%;
            padding: 8px;
            border: 1px solid var(--border);
            border-radius: 6px;
            background: var(--bg-primary);
            color: var(--text-primary);
        }
        
        .status {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        
        .status.connected { background: #4CAF50; color: white; }
        .status.disconnected { background: #f44336; color: white; }
        .status.recording { background: #FF9800; color: white; }
        
        .transcript-item {
            padding: 12px;
            margin-bottom: 10px;
            background: var(--bg-primary);
            border-radius: 8px;
            border-left: 3px solid var(--accent);
        }
        
        .speaker-label {
            font-weight: 600;
            color: var(--accent);
            margin-bottom: 4px;
        }
        
        .timestamp {
            font-size: 11px;
            color: var(--text-secondary);
            margin-left: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎙️ WhisperLiveKit</h1>
            <div class="controls">
                <select id="langSelect" onchange="updateLanguage()">
                    <option value="en">English</option>
                    <option value="zh">中文</option>
                    <option value="zh-TW">中文繁體</option>
                    <option value="ja">日本語</option>
                </select>
                <button class="btn-secondary" onclick="toggleTheme()">🌓</button>
                <button class="btn-secondary" onclick="toggleSettings()">⚙️</button>
            </div>
        </header>
        
        <!-- GitHub 按钮组 -->
        <div class="github-buttons">
            <a href="https://github.com/neosun100/whisperlivekit-enhanced" target="_blank" class="github-btn btn-star">
                ⭐ Star on GitHub
            </a>
            <a href="https://github.com/neosun100/whisperlivekit-enhanced/issues/new?labels=bug&template=bug_report.md" target="_blank" class="github-btn btn-bug">
                🐛 Report Bug
            </a>
            <a href="https://github.com/neosun100/whisperlivekit-enhanced/issues/new?labels=enhancement&template=feature_request.md" target="_blank" class="github-btn btn-feature">
                💡 Request Feature
            </a>
        </div>
        
        <div class="main-content">
            <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <div>
                        <span class="status disconnected" id="status">Disconnected</span>
                    </div>
                    <div>
                        <button id="startBtn" onclick="startRecording()">Start Recording</button>
                        <button id="stopBtn" onclick="stopRecording()" disabled>Stop</button>
                        <button class="btn-secondary" onclick="clearTranscript()">Clear</button>
                    </div>
                </div>
                
                <div class="transcription-area" id="transcriptArea">
                    <p style="color: var(--text-secondary); text-align: center; padding: 40px;">
                        Click "Start Recording" to begin transcription
                    </p>
                </div>
            </div>
            
            <div class="settings-panel" id="settingsPanel" style="display: none;">
                <h3 style="margin-bottom: 20px;">Settings</h3>
                
                <div class="setting-group">
                    <label>Model</label>
                    <select id="modelSelect">
                        <option value="tiny">Tiny (fastest)</option>
                        <option value="base">Base</option>
                        <option value="small">Small</option>
                        <option value="medium" selected>Medium</option>
                        <option value="large">Large (best quality)</option>
                    </select>
                </div>
                
                <div class="setting-group">
                    <label>Source Language</label>
                    <select id="sourceLanguage">
                        <option value="auto">Auto Detect</option>
                        <option value="en">English</option>
                        <option value="zh">Chinese</option>
                        <option value="ja">Japanese</option>
                        <option value="es">Spanish</option>
                        <option value="fr">French</option>
                    </select>
                </div>
                
                <div class="setting-group">
                    <label>
                        <input type="checkbox" id="diarizationCheck"> Enable Speaker Diarization
                    </label>
                </div>
                
                <div class="setting-group">
                    <label>Idle Timeout (minutes)</label>
                    <input type="number" id="idleTimeout" value="10" min="1" max="60">
                </div>
            </div>
        </div>
    </div>
    
    <script>
        const translations = {
            en: {
                title: "WhisperLiveKit",
                start: "Start Recording",
                stop: "Stop",
                clear: "Clear",
                connected: "Connected",
                disconnected: "Disconnected",
                recording: "Recording",
                settings: "Settings"
            },
            zh: {
                title: "实时语音识别",
                start: "开始录音",
                stop: "停止",
                clear: "清空",
                connected: "已连接",
                disconnected: "未连接",
                recording: "录音中",
                settings: "设置"
            },
            "zh-TW": {
                title: "即時語音辨識",
                start: "開始錄音",
                stop: "停止",
                clear: "清空",
                connected: "已連接",
                disconnected: "未連接",
                recording: "錄音中",
                settings: "設定"
            },
            ja: {
                title: "リアルタイム音声認識",
                start: "録音開始",
                stop: "停止",
                clear: "クリア",
                connected: "接続済み",
                disconnected: "未接続",
                recording: "録音中",
                settings: "設定"
            }
        };
        
        let ws = null;
        let mediaRecorder = null;
        let currentLang = 'en';
        
        function toggleTheme() {
            const theme = document.documentElement.getAttribute('data-theme');
            document.documentElement.setAttribute('data-theme', theme === 'dark' ? 'light' : 'dark');
        }
        
        function toggleSettings() {
            const panel = document.getElementById('settingsPanel');
            panel.style.display = panel.style.display === 'none' ? 'block' : 'none';
        }
        
        function updateLanguage() {
            currentLang = document.getElementById('langSelect').value;
            const t = translations[currentLang];
            document.getElementById('startBtn').textContent = t.start;
            document.getElementById('stopBtn').textContent = t.stop;
        }
        
        function clearTranscript() {
            document.getElementById('transcriptArea').innerHTML = '';
        }
        
        async function startRecording() {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            ws = new WebSocket(`${protocol}//${window.location.host}/asr`);
            
            ws.onopen = () => {
                document.getElementById('status').textContent = translations[currentLang].connected;
                document.getElementById('status').className = 'status connected';
                document.getElementById('startBtn').disabled = true;
                document.getElementById('stopBtn').disabled = false;
            };
            
            ws.onmessage = (event) => {
                const data = JSON.parse(event.data);
                if (data.type === 'transcript') {
                    addTranscript(data);
                }
            };
            
            ws.onerror = () => {
                document.getElementById('status').textContent = 'Error';
                document.getElementById('status').className = 'status disconnected';
            };
            
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(stream);
            
            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0 && ws.readyState === WebSocket.OPEN) {
                    ws.send(event.data);
                }
            };
            
            mediaRecorder.start(100);
            document.getElementById('status').textContent = translations[currentLang].recording;
            document.getElementById('status').className = 'status recording';
        }
        
        function stopRecording() {
            if (mediaRecorder) {
                mediaRecorder.stop();
                mediaRecorder.stream.getTracks().forEach(track => track.stop());
            }
            if (ws) {
                ws.close();
            }
            document.getElementById('status').textContent = translations[currentLang].disconnected;
            document.getElementById('status').className = 'status disconnected';
            document.getElementById('startBtn').disabled = false;
            document.getElementById('stopBtn').disabled = true;
        }
        
        function addTranscript(data) {
            const area = document.getElementById('transcriptArea');
            const item = document.createElement('div');
            item.className = 'transcript-item';
            
            let html = '';
            if (data.speaker) {
                html += `<div class="speaker-label">Speaker ${data.speaker}</div>`;
            }
            html += `<div>${data.text}<span class="timestamp">${new Date().toLocaleTimeString()}</span></div>`;
            
            item.innerHTML = html;
            area.appendChild(item);
            area.scrollTop = area.scrollHeight;
        }
    </script>
</body>
</html>"""
