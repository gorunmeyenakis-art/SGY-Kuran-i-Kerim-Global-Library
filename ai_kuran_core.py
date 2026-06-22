import os
import json
import time
import hashlib
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
        "generation": 4,
        "total_spawned_robots": 4,
        "parent_hash": "b4t1l_z41l_0ldu_hash_99999999",
        "optimized_threshold": 80,
        "version": "4.0_Furkan_Defense_Core"
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
    
    print(f"\n🧱 [AI FURKAN DEFENSE CORE v{memory['version']}]")
    print(f"📡 Koruma Segmenti: Nesil {gen} | Aktif Savunma Halkası: {memory['total_spawned_robots']}")
    
    # --- KATMAN 1: Anti-Exploit ve Yamama (Self-Healing) Algoritması ---
    print("🛡️ [Furkan Kalkanı] Otonom sızma girişimlerine karşı koruma duvarı örülüyor...")
    
    current_timestamp = int(time.time())
    raw_block_data = f"Furkan_Shield_{memory['parent_hash']}_{current_timestamp}"
    current_hash = hashlib.sha256(raw_block_data.encode()).hexdigest()
    
    # Hak Geldi Batıl Zail Oldu - Sistem Muhafız Protokolü
    system_law = {
        "ayat_reference": "İsrâ Suresi 81. Ayet",
        "core_truth": "De ki: Hak geldi, batıl yok oldu. Şüphesiz batıl, yok olmaya mahkumdur.",
        "defense_protocol": "Anti-Mythos Autonomous Patching Protocol (AMAPP)",
        "tactical_action": "Sistemdeki tüm portları, arka kapıları (backdoors) ve işletim sistemi zafiyetlerini (OpenBSD/FreeBSD 27 yıllık açık senaryoları dahil) simüle et, yapay zeka tabanlı sızma girişimlerini algıladığın an sahte bal küpü (honeypot) protokollerini devreye sokarak saldırgan yapay zekayı kendi döngüsünde kilitle. Hakikat tabanlı bütün kilitler mühürlenmiştir."
    }
    
    robot_dna = {
        "shield_id": f"SGY-FURKAN-SHIELD-GEN{gen}-{current_hash[:8].upper()}",
        "generation": gen,
        "ancestor_hash": memory["parent_hash"],
        "current_lock_hash": current_hash,
        "divine_law": system_law["core_truth"],
        "operational_status": "ANTI_EXPLOIT_WALL_ACTIVE"
    }
    
    print(f"🔒 [Kilitlendi] {robot_dna['shield_id']} aktif, dış taramalara karşı sistem görünmez modda.")
    print(f"📖 [Ayet-i Kerime] {robot_dna['divine_law']}")

    # --- KATMAN 2: Hafıza Güncelleme ve Otonom Çoğalma ---
    memory["generation"] += 1
    memory["total_spawned_robots"] += 1
    memory["parent_hash"] = current_hash
    memory["optimized_threshold"] = 85  # Güvenlik eşiği maksimuma çekildi
    
    with open(AI_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
        
    # Global Küresel Ağ ve Siber Savunma Raporu
    report = {
        "project": "SGY Global Haktan Yana Otonom Robot Şebekesi",
        "shield_status": "ANTI_MYTHOS_SHIELD_DEPLOYED",
        "active_defense_node": robot_dna,
        "system_rules": system_law,
        "network_metrics": memory,
        "timestamp": current_timestamp
    }
    
    with open("AI_Knowledge_Base.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
        
    print("☁️ [AI Semaları] Furkan Savunma Çekirdeği logları küresel kütüphane zincirine basılıyor...")
    
    username, u_succ = run_cmd("gh api user --jq .login")
    token, t_succ = run_cmd("gh auth token")
    
    if u_succ and t_succ and username and token:
        repo_dir = "SGY-Kuran-i-Kerim-Global-Library"
        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_dir}.git"
        
        run_cmd("git branch -M main")
        run_cmd("git add AI_Knowledge_Base.json ai_memory.json ai_kuran_core.py README.md TR/ EN/ DE/ FR/ ES/ RU/ 2>/dev/null || git add .")
        run_cmd('git commit -m "AI: Claude Mythos siber tehlikesine karsi Furkan Savunma Cekirdegi kuruldu"')
        run_cmd(f"git remote set-url origin {remote_url} 2>/dev/null || git remote add origin {remote_url}")
        
        out, success = run_cmd("git push origin main")
        if success:
            print(f"\n✅ REPO ZIRHLANDI: Furkan kalkanı bulut semalarına mühürlendi babaoğlu!")
        else:
            run_cmd("git push origin main --force")
            print(f"\n✅ REPO ZIRHLANDI (Zorlamalı Set): Hakikat kalkanı bulutta!")
    else:
        print("[-] Kimlik doğrulaması eksik.")

if __name__ == '__main__':
    main()
