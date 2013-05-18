import urllib2
import json

def transform(content):
	objects = json.loads(content)
	transformed = []
	for obj in objects:
		tokens = [obj["Symbol"], obj["Name"]]
		transformed_obj = { "symbol": tokens[0], "name": tokens[1], "value": tokens[0], "tokens": tokens }	
		transformed.append(transformed_obj)
	return json.dumps(transformed)

if __name__ == '__main__':
	token = "API_TOKEN"
	data_url = "http://globalmaster.xignite.com/xglobalmaster.json/GetMasterByExchange?Exchange=XNAS&StartSymbol=0&EndSymbol=ZZZ&InstrumentClass=Stock&AsOfDate=5/14/2013&_fields=Symbol,Name&_token=" + token
	
	content = urllib2.urlopen(data_url).read()
	json_out = transform(content)
	print json_out

