import xmltodict
import json
def read_from_file(file_name):
	with open(file_name, 'r') as read_from_file:
		file = json.load(read_from_file)
		print('You succesfully read from {0}.'.format(file_name))
		return file

sd_json = read_from_file("stock_data.json")
print(sd_json)
sd_json2 = {"all":sd_json}
sd_json2 = xmltodict.unparse(sd_json2, pretty=True)
sd_json_final = sd_json2[:38] + '\n<?xml-stylesheet type = "text/xsl" href = "stock_app.xsl"?>\n' + sd_json2[38:]

with open("stock_data.xml" , "w") as f:
	f.write(sd_json_final)

