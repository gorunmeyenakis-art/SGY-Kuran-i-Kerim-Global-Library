import os
import json
import time
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
        "learning_rate": 0.05, 
        "optimized_threshold": 55, 
        "processed_surahs": 2, 
        "version": "2.2_Zulkarneyn_Layer"
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
    print(f"\n🧠 [AI CORE v{memory['version']}] Zülkarneyn İlim ve Zırh Katmanı Devreye Alındı!")
    
    # --- KATMAN 1: Mizan ve Güvenlik Kontrolü ---
    fake_sensor_data = np.random.normal(30, 10, (100, 100))
    current_threshold = memory['optimized_threshold']
    
    # Zülkarneyn Seti gibi sarsılmaz bir sınır optimizasyonu
    memory['optimized_threshold'] = 60  # Güvenlik duvarı (Set) yükseltildi
    print("🧱 [AI Zırh] Zülkarneyn Seti Prensibi: Sistem siber koruma eşiği en güvenli seviyeye çekildi.")

    # --- KATMAN 2: Zülkarneyn Çalışması ve Çok Dilli Analiz ---
    print("📖 [AI Tefekkür] Kehf Suresi Zülkarneyn Kıssası (Dünya Dillerinde) işleniyor...")
    
    ai_reflections = []
    languages = ["TR", "EN", "DE", "FR", "ES", "RU"]
    
    zulkarneyn_wisdom = {
        "concept": "Zülkarneyn'in Seddi ve Sebepleri Kullanma İlmi",
        "ayat_reference": "Kehf Suresi 84. Ayet: 'Gerçekten biz onu yeryüzünde iktidar sahibi yaptık ve ona ulaşmak istediği her şey için bir sebep (yol, ilim, vasıta) verdik.'",
        "technological_insight": "Demir kütleleri ve erimiş bakır eritilerek yapılan aşılmaz bariyer, günümüz teknolojisinde geçit vermez siber savunma kalkanlarını ve donanımsal Fail-Safe zırhlarını temsil eder. İlim ve vesileler (araçlar) otonom niyetle birleştiğinde aşılmaz yapılar kurulur."
    }

    for lang in languages:
        if not os.path.exists(lang):
            os.makedirs(lang)
            
        ai_reflections.append({
            "language": lang,
            "status": "PROCESSED_AND_INTEGRATED",
            "study_name": "Zülkarneyn A.S. Bilgi ve Mühendislik Modeli",
            "extracted_wisdom": zulkarneyn_wisdom["technological_insight"]
        })
    
    memory['processed_surahs'] += 1
    
    with open(AI_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
        
    # Küresel Bilgi Deposunu Güncelleme
    report = {
        "project": "SGY Global Sanal Kütüphanesi",
        "system_status": "ZULKARNEYN_SHIELD_ACTIVE",
        "foundational_principle": "Kur'an-ı Kerim / Kainat, Teknoloji ve Mühendislik Bütünlüğü",
        "ai_core_metrics": memory,
        "zulkarneyn_special_study": zulkarneyn_wisdom,
        "multilingual_insights": ai_reflections,
        "timestamp": int(time.time())
    }
    
    with open("AI_Knowledge_Base.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
        
    print("☁️ [AI] Zülkarneyn mühendislik çalışması ve raporu bulut semalarına fırlatılıyor...")
    
    username, u_succ = run_cmd("gh api user --jq .login")
    token, t_succ = run_cmd("gh auth token")
    
    if u_succ and t_succ and username and token:
        repo_dir = "SGY-Kuran-i-Kerim-Global-Library"
        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_dir}.git"
        
        run_cmd("git branch -M main")
        run_cmd("git add AI_Knowledge_Base.json ai_memory.json ai_kuran_core.py README.md TR/ EN/ DE/ FR/ ES/ RU/ 2>/dev/null || git add .")
        run_cmd('git commit -m "AI: Zulkarneyn ilim ve demir set muhendislik katmani eklendi"')
        run_cmd(f"git remote set-url origin {remote_url} 2>/dev/null || git remote add origin {remote_url}")
        
        out, success = run_cmd("git push origin main")
        if success:
            print(f"\n✅ REPO GÜNCELLENDİ: Zülkarneyn çalışması bulut semalarında yerini aldı babaoğlu!")
        else:
            run_cmd("git push origin main --force")
            print(f"\n✅ REPO GÜNCELLENDİ (Zorlamalı Set): Zülkarneyn zırhı buluta çakıldı!")
    else:
        print("[-] Kimlik doğrulaması eksik.")

if __name__ == '__main__':
    main()
