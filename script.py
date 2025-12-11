import time
import random
import datetime

# --- RAY TACHYON SYSTEM RADAR ---
# Script dummy untuk simulasi monitoring server otomatis

def init_radar():
    print(f"[{datetime.datetime.now()}] INITIALIZING RADAR PROTOCOL...")
    print("Connecting to secure nodes...")
    time.sleep(1)
    print("Access granted.\n")

def scan_network():
    nodes = ["Node-Alpha", "Server-Bravo", "Database-X", "Gateway-09"]
    
    while True:
        target = random.choice(nodes)
        load = random.randint(5, 99)
        
        status = "STABLE"
        alert = ""
        
        if load > 85:
            status = "CRITICAL"
            alert = " >> AUTOMATION TRIGGERED: COOLING DOWN SYSTEM..."
        elif load > 50:
            status = "WARNING"
            
        print(f"[RADAR SCAN] Target: {target} | CPU Load: {load}% | [{status}]{alert}")
        
        # Simulasi delay biar kayak real-time monitoring
        time.sleep(2)

if __name__ == "__main__":
    init_radar()
    try:
        scan_network()
    except KeyboardInterrupt:
        print("\n[SYSTEM] Radar Shutting Down...")
