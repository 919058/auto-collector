# 🖱️ Auto Clicker - Setup & Usage Guide

## Python Version (WORKS EVERYWHERE)

This is the **system-wide auto clicker** that works on:
- ✅ Other browser tabs
- ✅ Other applications
- ✅ Games
- ✅ Anywhere on your screen

---

## Installation

### Step 1: Install Python
Download and install Python from: https://www.python.org/downloads/
- **Important:** Check "Add Python to PATH" during installation

### Step 2: Open Command Prompt/Terminal

**Windows:**
- Press `Win + R`
- Type `cmd` and press Enter

**Mac:**
- Press `Cmd + Space`
- Type `terminal` and press Enter

**Linux:**
- Open your terminal application

### Step 3: Install Required Libraries

Copy and paste this command:

```bash
pip install pyautogui keyboard
```

Press Enter and wait for it to finish.

---

## Usage

### Windows:

1. Download `auto_clicker.py` from this repository
2. Open Command Prompt in the folder where the file is
3. Run:
```bash
python auto_clicker.py
```

### Mac:

```bash
python3 auto_clicker.py
```

### Linux:

```bash
python3 auto_clicker.py
```

---

## How to Use

### Main Menu Options:

```
[1] Start Clicking
[2] Stop Clicking
[3] Settings
[4] Test Click (Click once at mouse position)
[5] Exit
```

### Default Settings:
- **Click Interval:** 100ms (0.1 seconds)
- **Total Clicks:** 100
- **Start Delay:** 3 seconds
- **Toggle Key:** F6

### Quick Start:

1. Select `[1] Start Clicking`
2. You'll have 3 seconds to move your mouse (countdown shows)
3. Clicking will start automatically
4. Press `F6` to stop at any time
5. View results (total clicks, CPS, time)

### Customize Settings:

1. Select `[3] Settings`
2. Change:
   - Click interval (milliseconds)
   - Total number of clicks (0 = infinite)
   - Start delay (seconds)
   - **Toggle key** (F6, Q, A, ENTER, etc.)
   - Click button (left/right/middle)

### Test a Single Click:

1. Select `[4] Test Click`
2. You'll have 2 seconds to move mouse to where you want to click
3. It will perform one click

---

## Hotkeys

| Hotkey | Action |
|--------|--------|
| `F6` (or your custom key) | Start/Stop clicking |
| `Ctrl + C` | Force emergency stop |
| Move mouse to **TOP-LEFT corner** | Force quit (FailSafe) |

---

## Examples

### Example 1: Click 500 times with 50ms interval
1. Start program
2. Settings → Change click interval to 50
3. Settings → Change total clicks to 500
4. Select "Start Clicking"
5. Wait for countdown
6. Watches clicks happen automatically

### Example 2: Infinite clicking with custom hotkey
1. Start program
2. Settings → Change toggle key to "Q"
3. Settings → Change total clicks to 0 (infinite)
4. Select "Start Clicking"
5. Press `Q` to start
6. Press `Q` again to stop

### Example 3: Use in a game
1. Configure settings (fast interval like 50-100ms)
2. Start the program
3. Open your game
4. Press your toggle key
5. The clicking will happen in-game

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pyautogui'"
- Run: `pip install pyautogui keyboard`
- Make sure Python is added to PATH

### "Permission denied" on Mac/Linux
- Run: `sudo python3 auto_clicker.py`
- Enter your password

### Clicks not appearing in my game
- Make sure the game window is in focus
- Some games have anti-cheat that blocks automation
- Try increasing the click interval (slower = more reliable)

### How do I stop it if it won't respond?
- Move your mouse to the **TOP-LEFT corner** of the screen
- The program has a failsafe that stops when you do this

### Can I use this on Mac?
- Yes, install pyautogui and keyboard
- Note: You may need to grant permissions in System Preferences → Security & Privacy

---

## Safety Features

✅ **Failsafe Mode:** Move mouse to top-left to force stop  
✅ **Keyboard Interrupt:** Press Ctrl+C to emergency stop  
✅ **Countdown:** 3-second delay before clicking (time to cancel)  
✅ **Custom Hotkeys:** Easy start/stop control  
✅ **Progress Display:** See clicks, speed, and time in real-time  

---

## Performance Stats

The program shows:
- **Clicks:** Total number of clicks performed
- **CPS:** Clicks per second (speed)
- **Time:** How long it took

---

## Important Notes

⚠️ **Use responsibly** - This tool can automate clicking anywhere  
⚠️ **Some games/apps** have anti-cheat that may detect automation  
⚠️ **Repetitive clicking** can cause strain - take breaks  
⚠️ **Always know what you're clicking** - make sure you test first  

---

## Comparison: Web vs Python

| Feature | Web Version | Python Version |
|---------|------------|-----------------|
| Works in browser | ✅ | ❌ |
| Works in other tabs | ❌ | ✅ |
| Works in games | ❌ | ✅ |
| Works in other apps | ❌ | ✅ |
| Requires installation | ❌ | ✅ |
| System-wide | ❌ | ✅ |

**Recommendation:** Use the **Python version** for actual automation!

---

## Need Help?

Check your command prompt for error messages - they tell you what's wrong.

Common issues:
1. Python not installed
2. Libraries not installed (`pip install pyautogui keyboard`)
3. Running old version of the file

---

**Happy Clicking! 🖱️**
