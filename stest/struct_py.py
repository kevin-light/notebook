

list = [{'orgName': "安信基金管理有限责任公司", 'certCode': "F06900001000011", 'certName': "投资经理", 'obtainDate': "2019-10-10"},
        {'orgName': "安信基金管理有限责任公司", 'certCode': "F06900001000011", 'certName': "投资经理", 'obtainDate': "2019-10-10"}]

for kv in list:
    if "orgName" or "aa" in kv:
        print(11)
    print(tuple(kv.values()))