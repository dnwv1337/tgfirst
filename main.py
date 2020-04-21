import requests

r = requests.post('https://www.kfc.ru/api/account/verify', data = {"phone":"+79877084109",
	"g-recaptcha-response":"03AHaCkAbuiIvY7Zl5PwQpN3bb6OZnavy-SezLqBYnbBBq0NXHELBZfaBBzUPWQSrlwCJKDm2oGMyY9agjS_Mu1Wn-epNB-KiziZymjenJrjpyzAxWrCcDznMf59KXZ5Jj8gQR3hWxfQifnGJjARbXZxmMIpShwBISx_5SlH0kwLI6i7OKaN4-sil1jFf3JkrMlxobvrHCzWOGTYyi2oYlXdLy9Y6-reqsJS8LDm8JkTePEwFsfAxgKIItCqLALgP1g58tnXDJWKbNkiMMLMmZVFLJZcFrq6OLPGXu5HqRKhwCbk0i847LVS7MnlYyOy4xVIJLCVAbj0NTx23Du4Mjf8j1fvDcExXy_-FH05znLjhXeVLiZ07kbqwkuqWQG39Rh0Lp4oNqPnnq"},
headers ={
	'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	'Connection' : 'keep-alive',
	'Host' : 'www.kfc.ru',
	'Origin' : 'https://www.kfc.ru',
	'Referer' : 'https://www.kfc.ru/login'
	})
print(r)
print(r.text)

