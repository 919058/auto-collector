"""
Auto Clicker - System-wide mouse automation tool
Works on Windows, Mac, and Linux
Requires: pip install pyautogui keyboard
"""

import pyautogui
import keyboard
import time
import threading
from datetime import datetime

class AutoClickerApp:
    def __init__(self):
        self.is_running = False
        self.is_paused = False
        self.click_count = 0
        self.start_time = None
        
        # Default settings
        self.click_interval = 0.1  # seconds
        self.total_clicks = 100
        self.start_delay = 3
        self.toggle_key = 'f6'
        self.click_button = 'left'  # left, right, middle
        self.click_at_mouse = True
        
        # Prevent accidental automation
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.01
        
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("     🖱️  AUTO CLICKER - System Wide Edition")
        print("="*50)
        print("\n[1] Start Clicking")
        print("[2] Stop Clicking")
        print("[3] Settings")
        print("[4] Test Click (Click once at mouse position)")
        print("[5] Exit\n")
        
    def display_settings(self):
        """Display current settings"""
        print("\n" + "-"*50)
        print("Current Settings:")
        print("-"*50)
        print(f"Click Interval: {self.click_interval}s")
        print(f"Total Clicks: {self.total_clicks} (0 = infinite)")
        print(f"Start Delay: {self.start_delay}s")
        print(f"Toggle Key: {self.toggle_key}")
        print(f"Click Button: {self.click_button}")
        print(f"Click at Mouse Position: {self.click_at_mouse}")
        print("-"*50 + "\n")
        
    def change_settings(self):
        """Change settings"""
        while True:
            print("\nSettings Menu:")
            print("[1] Click Interval (ms)")
            print("[2] Total Clicks")
            print("[3] Start Delay (seconds)")
            print("[4] Toggle Key")
            print("[5] Click Button (left/right/middle)")
            print("[6] Click at Mouse Position (True/False)")
            print("[7] Back to Main Menu\n")
            
            choice = input("Select option: ").strip()
            
            if choice == '1':
                try:
                    interval = int(input("Enter click interval in milliseconds (10-10000): "))
                    if 10 <= interval <= 10000:
                        self.click_interval = interval / 1000
                        print(f"✓ Interval set to {self.click_interval}s")
                    else:
                        print("❌ Value must be between 10-10000")
                except ValueError:
                    print("❌ Invalid input")
                    
            elif choice == '2':
                try:
                    clicks = int(input("Enter total clicks (0 for infinite): "))
                    if clicks >= 0:
                        self.total_clicks = clicks
                        print(f"✓ Total clicks set to {self.total_clicks}")
                    else:
                        print("❌ Value must be 0 or higher")
                except ValueError:
                    print("❌ Invalid input")
                    
            elif choice == '3':
                try:
                    delay = int(input("Enter start delay in seconds (0-60): "))
                    if 0 <= delay <= 60:
                        self.start_delay = delay
                        print(f"✓ Start delay set to {self.start_delay}s")
                    else:
                        print("❌ Value must be between 0-60")
                except ValueError:
                    print("❌ Invalid input")
                    
            elif choice == '4':
                key = input("Enter toggle key (e.g., f6, q, a, enter): ").strip().lower()
                if key:
                    self.toggle_key = key
                    print(f"✓ Toggle key set to {self.toggle_key}")
                    
            elif choice == '5':
                button = input("Enter button (left/right/middle): ").strip().lower()
                if button in ['left', 'right', 'middle']:
                    self.click_button = button
                    print(f"✓ Click button set to {self.click_button}")
                else:
                    print("❌ Invalid button")
                    
            elif choice == '6':
                value = input("Click at mouse position? (True/False): ").strip().lower()
                if value in ['true', '1', 'yes']:
                    self.click_at_mouse = True
                    print("✓ Will click at mouse position")
                elif value in ['false', '0', 'no']:
                    self.click_at_mouse = False
                    print("✓ Will click at current position")
                else:
                    print("❌ Invalid input")
                    
            elif choice == '7':
                break
            else:
                print("❌ Invalid option")
                
    def countdown(self, seconds):
        """Display countdown before clicking starts"""
        for i in range(seconds, 0, -1):
            print(f"\r⏳ Starting in {i} seconds... (Press {self.toggle_key.upper()} to cancel)", end='', flush=True)
            time.sleep(1)
            if not self.is_running:
                print("\n❌ Cancelled")
                return False
        print("\n✓ Clicking started! Press {} to stop".format(self.toggle_key.upper()))
        return True
        
    def perform_click(self):
        """Perform a single mouse click"""
        try:
            x, y = pyautogui.position()
            
            if self.click_button == 'left':
                pyautogui.click(button='left')
            elif self.click_button == 'right':
                pyautogui.click(button='right')
            elif self.click_button == 'middle':
                pyautogui.click(button='middle')
                
            self.click_count += 1
            return True
        except Exception as e:
            print(f"\n❌ Click error: {e}")
            return False
            
    def clicking_thread(self):
        """Thread that performs the clicking"""
        if not self.countdown(self.start_delay):
            self.is_running = False
            return
            
        self.start_time = datetime.now()
        self.click_count = 0
        
        while self.is_running:
            if not self.is_paused:
                self.perform_click()
                
                # Display progress every 10 clicks
                if self.click_count % 10 == 0:
                    elapsed = (datetime.now() - self.start_time).total_seconds()
                    cps = self.click_count / elapsed if elapsed > 0 else 0
                    print(f"\r📊 Clicks: {self.click_count} | CPS: {cps:.2f} | Time: {elapsed:.1f}s", end='', flush=True)
                
                # Check if we've reached the click limit
                if self.total_clicks > 0 and self.click_count >= self.total_clicks:
                    self.is_running = False
                    break
                    
            time.sleep(self.click_interval)
            
        elapsed = (datetime.now() - self.start_time).total_seconds() if self.start_time else 0
        cps = self.click_count / elapsed if elapsed > 0 else 0
        print(f"\n\n✓ Clicking finished!")
        print(f"Total Clicks: {self.click_count}")
        print(f"Time Elapsed: {elapsed:.2f}s")
        print(f"Clicks/Second: {cps:.2f}\n")
        
    def start(self):
        """Start the auto clicker"""
        if self.is_running:
            print("❌ Already running!")
            return
            
        print("\n" + "="*50)
        print("Starting Auto Clicker...")
        print(f"Press {self.toggle_key.upper()} at any time to stop")
        print(f"Settings: {self.click_interval*1000:.0f}ms interval | {self.total_clicks if self.total_clicks > 0 else 'infinite'} clicks")
        print("="*50)
        
        self.is_running = True
        
        # Start clicking in separate thread
        click_thread = threading.Thread(target=self.clicking_thread, daemon=True)
        click_thread.start()
        
        # Wait for toggle key or termination
        try:
            while self.is_running:
                if keyboard.is_pressed(self.toggle_key):
                    time.sleep(0.2)  # Debounce
                    self.stop()
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.stop()
            
        click_thread.join(timeout=2)
        
    def stop(self):
        """Stop the auto clicker"""
        if self.is_running:
            self.is_running = False
            print("\n\n⏹️  Stopped")
        else:
            print("❌ Not running")
            
    def test_click(self):
        """Perform a single test click"""
        print("\n⏳ Click will happen in 2 seconds... Move your mouse to test location")
        time.sleep(2)
        
        x, y = pyautogui.position()
        print(f"🖱️  Clicking at position ({x}, {y})")
        self.perform_click()
        print("✓ Click performed!\n")
        
    def run(self):
        """Main application loop"""
        print("\n" + "="*50)
        print("🖱️  AUTO CLICKER - System Wide Edition")
        print("="*50)
        print("\n⚠️  IMPORTANT:")
        print("  • Move mouse to TOP-LEFT corner to force stop")
        print("  • This tool can click anywhere on your screen")
        print("  • Use responsibly!")
        print("  • Press Ctrl+C to emergency stop\n")
        
        input("Press ENTER to continue...")
        
        while True:
            self.display_menu()
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.start()
            elif choice == '2':
                self.stop()
            elif choice == '3':
                self.display_settings()
                self.change_settings()
            elif choice == '4':
                self.test_click()
            elif choice == '5':
                print("\n✓ Goodbye!")
                break
            else:
                print("❌ Invalid option")
                

def main():
    try:
        app = AutoClickerApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n❌ Program interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
