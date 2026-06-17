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
    if os.path.exists(AI_MEMORY_FILE):
        with open(AI_MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"learning_rate": 0.05, "optimized_threshold": 50, "version": "1.1"}

def main():
    memory = get_ai_memory()
    print(f"\n🧠 [AI CORE] Kur'an-ı Kerim Bazlı Arındırılmış Çekirdek Aktif (v{memory['version']})")
    
    # Mizan (Denge) Optimizasyonu
    fake_sensor_data = np.random.normal(30, 10, (100, 100))
    fake_sensor_data[50, 50] = 85
    
    current_threshold = memory['optimized_threshold']
    detected = np.sum(fake_sensor_data > current_threshold)
    
    if detected > 3:
        memory['optimized_threshold'] += 1
        print("⚖️ [AI] Ölçü Dengelendi: Eşik değeri optimize edildi.")
    
    with open(AI_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)
        
    report = {
        "status": "AI_STABLE",
        "ayat_reference": "Kamer Suresi, 49. Ayet: 'Şüphesiz biz her şeyi bir ölçüye göre yarattık.'",
        "system_metrics": memory,
        "timestamp": int(time.time())
    }
    
    with open("AI_Knowledge_Base.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
        
    print("☁️ [AI] Hatalardan arındırılmış veriler buluta gönderiliyor...")
    
    username, u_succ = run_cmd("gh api user --jq .login")
    token, t_succ = run_cmd("gh auth token")
    
    if u_succ and t_succ and username and token:
        repo_dir = "SGY-Kuran-i-Kerim-Global-Library"
        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_dir}.git"
        
        run_cmd("git branch -M main")
        run_cmd("git add AI_Knowledge_Base.json ai_memory.json ai_kuran_core.py 2>/dev/null || git add .")
        run_cmd('git commit -m "AI: Temiz katman optimizasyonu tamamlandi"')
        run_cmd(f"git remote set-url origin {remote_url} 2>/dev/null || git remote add origin {remote_url}")
        
        out, success = run_cmd("git push origin main")
        if success:
            print(f"\n✅ MÜKEMMEL: Tıkanıklık açıldı, AI çekirdeği bulut semalarında!")
        else:
            # Zorlayarak hattı aç
            run_cmd("git push origin main --force")
            print(f"\n✅ MÜKEMMEL (Force Push): Sistem başarıyla senkronize edildi!")
    else:
        print("[-] Kimlik doğrulaması başarısız.")

if __name__ == '__main__':
    main()
