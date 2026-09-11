// Auto Clicker Logic
class AutoClicker {
    constructor() {
        this.isRunning = false;
        this.clickCount = 0;
        this.startTime = null;
        this.intervalId = null;
        this.timerIntervalId = null;
        this.mouseX = 0;
        this.mouseY = 0;

        this.initializeElements();
        this.setupEventListeners();
        this.trackMousePosition();
    }

    initializeElements() {
        this.clickIntervalInput = document.getElementById('clickInterval');
        this.totalClicksInput = document.getElementById('totalClicks');
        this.toggleKeyInput = document.getElementById('toggleKey');
        this.startDelayInput = document.getElementById('startDelay');
        this.mouseFollowCheckbox = document.getElementById('mouseFollow');
        this.clickButtonSelect = document.getElementById('clickButton');
        this.startBtn = document.getElementById('startBtn');
        this.stopBtn = document.getElementById('stopBtn');
        this.resetBtn = document.getElementById('resetBtn');
        this.clicksPerformed = document.getElementById('clicksPerformed');
        this.statusDisplay = document.getElementById('status');
        this.elapsedTime = document.getElementById('elapsedTime');
        this.cpsDisplay = document.getElementById('cps');
    }

    setupEventListeners() {
        this.startBtn.addEventListener('click', () => this.start());
        this.stopBtn.addEventListener('click', () => this.stop());
        this.resetBtn.addEventListener('click', () => this.reset());

        // Keyboard event listener for hotkeys
        document.addEventListener('keydown', (e) => this.handleKeypress(e));
    }

    trackMousePosition() {
        document.addEventListener('mousemove', (e) => {
            this.mouseX = e.clientX;
            this.mouseY = e.clientY;
        });
    }

    handleKeypress(event) {
        // Get hotkey combinations
        const toggleKey = this.toggleKeyInput.value.toLowerCase();
        const keyPressed = event.key.toLowerCase();
        
        // Support for Ctrl+Q, Ctrl+A, Ctrl+S, etc.
        const isCtrlCombo = event.ctrlKey && keyPressed === toggleKey;
        const isAltCombo = event.altKey && keyPressed === toggleKey;
        const isShiftCombo = event.shiftKey && keyPressed === toggleKey;
        const isSingleKey = !event.ctrlKey && !event.altKey && !event.shiftKey && keyPressed === toggleKey;

        // Check if any combination matches
        if (isCtrlCombo || isAltCombo || isShiftCombo || isSingleKey) {
            event.preventDefault();
            this.toggleClicker();
        }

        // Special hotkeys
        if (event.ctrlKey && keyPressed === 'q') {
            event.preventDefault();
            this.stop();
        }

        if (event.ctrlKey && keyPressed === 's') {
            event.preventDefault();
            this.start();
        }

        if (event.ctrlKey && keyPressed === 'r') {
            event.preventDefault();
            this.reset();
        }
    }

    toggleClicker() {
        if (this.isRunning) {
            this.stop();
        } else {
            this.start();
        }
    }

    start() {
        if (this.isRunning) return;

        const startDelay = parseInt(this.startDelayInput.value) * 1000;
        const clickInterval = parseInt(this.clickIntervalInput.value);
        const totalClicks = parseInt(this.totalClicksInput.value);

        this.statusDisplay.textContent = 'Countdown...';
        this.statusDisplay.style.color = '#ff9800';

        setTimeout(() => {
            if (!this.isRunning) {
                this.isRunning = true;
                this.startTime = Date.now();
                this.clickCount = 0;

                this.statusDisplay.textContent = 'Active';
                this.statusDisplay.style.color = '#4caf50';
                this.startBtn.disabled = true;

                // Start timer display
                this.timerIntervalId = setInterval(() => this.updateTimer(), 100);

                // Start clicking
                this.intervalId = setInterval(() => {
                    this.performClick();

                    if (totalClicks > 0 && this.clickCount >= totalClicks) {
                        this.stop();
                    }
                }, clickInterval);
            }
        }, startDelay);
    }

    stop() {
        if (!this.isRunning) return;

        this.isRunning = false;
        clearInterval(this.intervalId);
        clearInterval(this.timerIntervalId);

        this.statusDisplay.textContent = 'Stopped';
        this.statusDisplay.style.color = '#f44336';
        this.startBtn.disabled = false;
    }

    reset() {
        this.stop();
        this.clickCount = 0;
        this.startTime = null;
        this.clicksPerformed.textContent = '0';
        this.elapsedTime.textContent = '0s';
        this.cpsDisplay.textContent = '0';
        this.statusDisplay.textContent = 'Inactive';
        this.statusDisplay.style.color = '#999';
    }

    performClick() {
        this.clickCount++;
        this.clicksPerformed.textContent = this.clickCount;

        // Perform actual mouse click
        try {
            const button = this.clickButtonSelect.value;
            const options = {
                bubbles: true,
                cancelable: true,
                view: window
            };

            let eventType = 'click';
            if (button === 'right') {
                eventType = 'contextmenu';
                options.button = 2;
            } else if (button === 'middle') {
                eventType = 'click';
                options.button = 1;
            } else {
                options.button = 0;
            }

            // Create and dispatch mouse event at current position
            const mouseEvent = new MouseEvent(eventType, options);
            const element = document.elementFromPoint(this.mouseX, this.mouseY);
            if (element) {
                element.dispatchEvent(mouseEvent);
            }

            // Alternative: Use click at mouse position if checkbox is enabled
            if (this.mouseFollowCheckbox.checked) {
                // This simulates clicking at the mouse position
                console.log(`Clicked at position: ${this.mouseX}, ${this.mouseY}`);
            }
        } catch (error) {
            console.error('Click error:', error);
        }
    }

    updateTimer() {
        if (!this.isRunning || !this.startTime) return;

        const elapsed = Math.floor((Date.now() - this.startTime) / 1000);
        this.elapsedTime.textContent = elapsed + 's';

        if (elapsed > 0) {
            const cps = (this.clickCount / elapsed).toFixed(2);
            this.cpsDisplay.textContent = cps;
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const clicker = new AutoClicker();

    // Show instructions for hotkeys
    const toggleKeyInput = document.getElementById('toggleKey');
    const updateHotkeyDisplay = () => {
        const key = toggleKeyInput.value || 'F6';
        console.log(`Hotkey set to: ${key}`);
        console.log(`Also supports: Ctrl+${key}, Alt+${key}, Shift+${key}`);
        console.log(`Special hotkeys: Ctrl+S (Start), Ctrl+Q (Stop), Ctrl+R (Reset)`);
    };

    toggleKeyInput.addEventListener('change', updateHotkeyDisplay);
    toggleKeyInput.addEventListener('blur', updateHotkeyDisplay);
    updateHotkeyDisplay();
});
