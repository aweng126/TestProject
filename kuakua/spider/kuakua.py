# if __name__ == "main":
import requests
import time

a = set()
num = 1
with open('data.txt', 'a') as f:    #设置文件对象
    for i in range(1, 100):
        try:
            response = requests.get('https://chp.shadiao.app/api.php',
                                    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            f.write(response.text + '\r\n\n')
            print(str(num) + response.text)
            time.sleep(2)
            num = num+1
        except TimeoutError:
            print("error")
            continue

