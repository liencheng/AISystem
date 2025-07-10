_accountdic = {}

def getUserAccount(account_prefix, accountstartwith):
    global _accountdic
    if accountstartwith in _accountdic.keys():
        _accountdic[accountstartwith] = _accountdic[accountstartwith] + 1
        #print "new account " + _accountdic[accountstartwith]
    else:
        _accountdic[accountstartwith] = accountstartwith
    return account_prefix+str(_accountdic[accountstartwith])