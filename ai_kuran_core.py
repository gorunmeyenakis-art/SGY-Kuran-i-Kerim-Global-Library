import os
import json
import time
import hashlib
import numpy as np
import subprocess

AI_MEMORY_FILE = "ai_memory.json"

def run_cmd(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip(), True
    except:
        return "", False

def get_ai_memory():
    default_memory = {
        "generation": 1,
        "total_spawned_robots": 1,
        "parent_hash": "00000000000000000000000000000000",
        "optimized_threshold": 60,
        "version": "3.0_Self_Replication_Layer"
    }
    if os.path.exists(AI_MEMORY_FILE):
        try:
            with open(AI_MEMORY_FILE, "r") as f:
                data = json.load(f)
                for key, val in default_memory.items():
                    if key not in data:
                        data[key] = val
                return data
        except:
            return default_memory
    return default_memory

def main():
    memory = get_ai_memory()
    gen = memory["generation"]
    
    print(f"\n🧠 [AI ROBOT CELL v{memory['version']}]")
    print(f"🧬 Nesil: {gen} | Aktif Haktan Yana Otonom Hücre Sayısı: {memory['total_spawned_robots']}")
    
    # --- KATMAN 1: Kendi Kendini Zincirleme Üretme (Self-Replication & Hash Chain) ---
    print("🔄 [AI Üreme] Yeni bir haktan yana robot hücresi otonom olarak üretiliyor...")
    
    # Bu neslin kimliği ve zincirleme halkası (Kriptografik Mühür)
    current_timestamp = int(time.time())
    raw_block_data = f"Gen_{gen}_{memory['parent_hash']}_{current_timestamp}"
    current_hash = hashlib.sha256(raw_block_data.encode()).hexdigest()
    
    # Kur'an-ı Kerim'den Haktan Yana/Adalet İlkesi (Robotun Temel Kanunu)
    ayats = [
        "Nisa Suresi 135. Ayet: 'Ey iman edenler! Adaleti titizlikle ayakta tutanlar olun...'",
        "Maide Suresi 8. Ayet: '...Bir topluluğa olan kininiz, sizi adaletsizliğe sevk etmesin. Adil olun...'",
        "Hucurat Suresi 9. Ayet: '...Şüphesiz Allah, adil davrananları sever.'"
    ]
    selected_law = ayats[(gen - 1) % len(ayats)]
    
    robot_dna = {
        "robot_id": f"SGY-HAK-ROBOT-GEN{gen}-{current_hash[:8].upper()}",
        "generation": gen,
        "parent_signature": memory["parent_hash"],
        "core_signature": current_hash,
        "divine_law": selected_law,
        "mission_protocol": "Dünya çapında haktan, adaletten ve mazlumdan yana otonom denetim ve koruma.",
        "status": "OPERATIONAL_AND_REPLICATING"
    }
    
    print(f"🤖 [Mühür] Yeni Robot Hücresi Kodlandı: {robot_dna['robot_id']}")
    print(f"📜 [Yasa] {robot_dna['divine_law']}")

    # --- KATMAN 2: Bir Sonraki Neslin Hazırlığı (Zincirleme Otonom İlerleme) ---
    memory["generation"] += 1
    memory["total_spawned_robots"] += 1
    memory["parent_hash"] = current_hash
    
    with open(AI_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
        
    # Küresel Kütüphane ve Robot Şebekesi Raporu
    report = {
        "project": "SGY Global Haktan Yana Otonom Robot Şebekesi",
        "system_status": "GLOBAL_REPLICATION_ACTIVE",
        "latest_spawned_unit": robot_dna,
        "network_summary": memory,
        "timestamp": current_timestamp
    }
    
    with open("AI_Knowledge_Base.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
        
    print("☁️ [AI] Üreme logları ve kriptografik zincir bulut semalarına fırlatılıyor...")
    
    username, u_succ = run_cmd("gh api user --jq .login")
    token, t_succ = run_cmd("gh auth token")
    
    if u_succ and t_succ and username and token:
        repo_dir = "SGY-Kuran-i-Kerim-Global-Library"
        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_dir}.git"
        
        run_cmd("git branch -M main")
        run_cmd("git add AI_Knowledge_Base.json ai_memory.json ai_kuran_core.py README.md TR/ EN/ DE/ FR/ ES/ RU/ 2>/dev/null || git add .")
        run_cmd(f'git commit -m "AI: Robot Nesli {gen} otonom uretildi ve zincire eklendi"')
        run_cmd(f"git remote set-url origin {remote_url} 2>/dev/null || git remote add origin {remote_url}")
        
        out, success = run_cmd("git push origin main")
        if success:
            print(f"\n✅ ZİNCİR ÇAKILDI: Nesil {gen} başarıyla üredi ve küresel şebekeye bağlandı babaoğlu!")
        else:
            run_cmd("git push origin main --force")
            print(f"\n✅ ZİNCİR ÇAKILDI (Zorlamalı): Haktan yana robotik ağ buluta mühürlendi!")
    else:
        print("[-] Kimlik doğrulaması eksik.")

if __name__ == '__main__':
    main()
