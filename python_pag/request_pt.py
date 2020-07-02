import requests


# form-data post发送excel文件
reqUrl = "https://demo.meix.com/iamanage/conferenceCall/importHcBillListenList.do"
queryData = {
    "clientstr": (None,
                  "{'token':'D5535A2A59F3C5FA37151A688773E6EBB64CF2BA5C7070D317EA5C83C67EC365AABB2080143EA2B1FE81FC3206B8C4CF86D8CB655676368A3B4C96F003AF54EC46BDDA3B363A48C55636181A5EB4DD406DC3955541BECBF5D6ECAFC4CF0E53E967B9FAD07043FA6D0CBA5DA6D1511F4EC2C9307694425A6AA39299980571060411B5E10D8732DFE39234210A5AD2170576E9BFB85B9F23B6'}"),
    "file": ("file", open("abc.xlsx", "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
}
heades = {
    "Accept": "*/*",
    "Cache-Control": "no-cache",
}
req = requests.post(reqUrl, headers=heades, files=queryData)

# 请求头 Accept-Language 必须传正确，不然出现乱码