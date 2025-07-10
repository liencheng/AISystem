def A_BillingLoginHandle(person,resJson):
    person['accid'] = resJson['result']['accid']
    person['token_space'] = resJson['result']['token']

HandlesDic = {"A_BillingLogin":A_BillingLoginHandle}