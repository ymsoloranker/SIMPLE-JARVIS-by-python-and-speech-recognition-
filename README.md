# Jarvis 🎙️

A personal voice-controlled AI assistant built in Python. Talks back, opens your apps, hits your browser, and keeps you locked in when you need it.

Built solo by **Hamza**.

## Features

- 🗣️ **Voice input/output** — listens via mic (Google Speech Recognition) and replies out loud (pyttsx3, tuned to a deeper "Jarvis" voice if available)
- 🕐 **Time & date** — just ask
- 🌐 **Browser control** — opens YouTube, GitHub, Fiverr, or searches Google for anything you say
- 💻 **System commands** — launches VS Code, Notepad, or grabs a screenshot
- 🔥 **Hamza mode** — built-in motivation, Solo Leveling, and David Goggins lines for when you need to lock back in
- 🛑 **Clean shutdown** — say "goodbye" / "shutdown" and it exits

## Commands it understands

| Say this | It does this |
|---|---|
| "hello" / "hey jarvis" | Wakes up and responds |
| "who are you" | Introduces itself |
| "what's the time" | Tells you the time |
| "what's the date" | Tells you the date |
| "open youtube" | Opens YouTube |
| "open github" | Opens GitHub |
| "open fiverr" | Opens Fiverr |
| "search [anything]" | Googles it |
| "open vs code" | Launches VS Code |
| "open notepad" | Opens Notepad |
| "screenshot" | Takes a screenshot |
| "motivate me" | Gets you back on grind |
| "solo leveling" | Shadow monarch mode |
| "goggins" | Stay hard |
| "shutdown" / "goodbye" | Shuts Jarvis down |

## Setup

**1. Clone it**
```bash
git clone https://github.com/Shirosaki/jarvis.git
cd jarvis
```

**2. Install dependencies**
```bash
pip install speechrecognition pyttsx3 pyaudio
```

> On Windows, if `pyaudio` fails to install with pip, grab the matching wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) or install via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

**3. Run it**
```bash
python jarvis.py
```

Then just talk. Jarvis is listening.

## Requirements

- Python 3.8+
- A working microphone
- Internet connection (speech recognition uses Google's API)

## Roadmap

- [ ] Wake word detection (no more manual start)
- [ ] Local speech recognition (offline mode)
- [ ] Custom command plugin system
- [ ] Ollama integration for actual conversation, not just command matching

## License

MIT — do whatever you want with it, just don't sell it back to me.

---

Built with zero plan B. 🖤
