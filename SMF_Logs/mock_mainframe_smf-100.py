import json
import random
import csv
from datetime import datetime, timedelta
from pathlib import Path

# ================== CONFIGURATION ==================
NUM_RECORDS = 50
ATTACK_INJECTION_RATE = 0.18  # ~18% of records will be suspicious

# Data pools
USERS = ['SYSADM', 'IBMUSER', 'TESTUSR1', 'GUEST', 'ADMIN', 'HACKER01', 'BRUTEFORCE', 'UNKNOWN']
RESOURCES = ['SYS1.PARMLIB', 'SYS1.LINKLIB', 'SYS1.PROCLIB', 'USER.DATASET', 'RACF.PROFILE', 
             'DB2.TABLESPACE', 'CICS.TRAN', 'TSO.LOGON', 'APF.LIBRARY']
SYSTEMS = ['MVSA', 'MVSProd1', 'SYSB']

EVENT_DESCRIPTIONS = {
    80: {  # RACF focused
        1: "Successful Logon",
        2: "Logon Failure - Invalid Password",
        13: "Access Violation",
        14: "Unauthorized Access Attempt",
        15: "Password Change",
        18: "Privilege Escalation Attempt"
    }
}

def generate_synthetic_smf(num_records=50, attack_injection=True):
    records = []
    base_time = datetime.now() - timedelta(days=2)
    
    for _ in range(num_records):
        record_type = 80  # Focus heavily on RACF for your project
        
        timestamp = (base_time + timedelta(minutes=random.randint(0, 2880))).isoformat()
        user_id = random.choice(USERS)
        resource = random.choice(RESOURCES)
        return_code = random.choice([0, 4, 8, 12])
        
        # === ATTACK INJECTION LOGIC ===
        is_attack = attack_injection and random.random() < ATTACK_INJECTION_RATE
        
        if is_attack:
            user_id = random.choice(['HACKER01', 'BRUTEFORCE'])
            return_code = random.choice([8, 12])  # Failure codes
            event_code = random.choice([2, 13, 14])
            description = EVENT_DESCRIPTIONS[80].get(event_code, "Suspicious Activity")
            
            # Brute-force simulation (multiple rapid failures)
            if random.random() < 0.45:
                for i in range(random.randint(4, 12)):
                    fail_time = (base_time + timedelta(minutes=random.randint(0, 30))).isoformat()
                    records.append({
                        "timestamp": fail_time,
                        "record_type": 80,
                        "user_id": user_id,
                        "event_code": 2,
                        "event_description": "RACF Logon Failure - Invalid Password",
                        "resource_name": "TSO.LOGON",
                        "return_code": 8,
                        "ip_address": f"192.168.{random.randint(10,99)}.{random.randint(1,254)}",
                        "system_id": random.choice(SYSTEMS),
                        "job_name": "TSO"
                    })
        else:
            event_code = random.choice(list(EVENT_DESCRIPTIONS[80].keys()))
            description = EVENT_DESCRIPTIONS[80][event_code]
        
        record = {
            "timestamp": timestamp,
            "record_type": record_type,
            "user_id": user_id,
            "event_code": event_code,
            "event_description": description,
            "resource_name": resource,
            "return_code": return_code,
            "ip_address": f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            "system_id": random.choice(SYSTEMS),
            "job_name": random.choice(["TSO", "RACF", "JES2", "IKJEFT"]),
            "success": return_code == 0
        }
        records.append(record)
    
    return records


# ================== GENERATE & SAVE ==================
if __name__ == "__main__":
    print("Generating synthetic SMF/RACF data...")
    data = generate_synthetic_smf(NUM_RECORDS, attack_injection=True)
    
    # Save as JSON
    with open("synthetic_smf_logs.json", "w") as f:
        json.dump(data, f, indent=2)
    
    # Save as CSV (SIEM-friendly)
    with open("synthetic_smf_logs.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Generated {len(data)} records")
    print("   • synthetic_smf_logs.json")
    print("   • synthetic_smf_logs.csv")
    
    # Show sample attack
    attacks = [r for r in data if r["user_id"] in ["HACKER01", "BRUTEFORCE"]]
    print(f"\nSample brute-force attempts generated: {len(attacks)}")
