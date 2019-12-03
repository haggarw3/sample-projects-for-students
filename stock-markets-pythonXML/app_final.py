import requests
import json
import main_functions

#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=PCJ0V6DYSEYQS4SD
API_KEY = "PCJ0V6DYSEYQS4SD"

#had to copy and paste these. API only offers stock Ticker info, but not name.
all_stocks = {
"stocks" : [
#{"ticker":"AAPL","name":"Apple Inc.", "img_src":"https://pbs.twimg.com/profile_images/1110319067280269312/iEqpsbUA_400x400.png"},
{"ticker":"ABBV","name":"AbbVie Inc.", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fabbvie_416x416.jpg"},
{"ticker":"ABT","name":"Abbott Labs", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fabbott-laboratories_416x416.jpg"},
{"ticker":"ACN","name":"Accenture", "img_src": "https://katrinaosleja.lv/wp-content/uploads/2017/07/accenture-logo.png"},
{"ticker":"ADBE","name":"Adobe Inc.", "img_src": "https://cdn.freebiesupply.com/logos/large/2x/adobe-01-logo-png-transparent.png"},
{"ticker":"AGN","name":"Allergan", "img_src": "https://media.licdn.com/dms/image/C4E0BAQH-aGLnQS9XRw/company-logo_200_200/0?e=2159024400&v=beta&t=OMS2rFEvv55JzX8uWMeN2KbhTaTJ_9on7cTgJhi4A8s"},
{"ticker":"AIG","name":"American Inter.", "img_src": "https://www.insurancejournal.com/app/uploads/2011/01/aig-1024x1024.png"},
{"ticker":"ALL","name":"Allstate", "img_src": "https://assets.reviews.com/uploads/2015/09/25003340/allstate-corp.jpg"},
{"ticker":"AMGN","name":"Amgen Inc.", "img_src": "https://yt3.ggpht.com/a/AGF-l7_7DyRBPaBB6rR9Irc-h1vfr_d-cFo9bfdYQQ=s900-mo-c-c0xffffffff-rj-k-no"},
{"ticker":"AMZN","name":"Amazon.", "img_src": "http://g-ec2.images-amazon.com/images/G/01/social/api-share/amazon_logo_500500._V323939215_.png"},
{"ticker":"AXP","name":"AmericanExpress", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/American_Express_logo_%282018%29.svg/1200px-American_Express_logo_%282018%29.svg.png"},
{"ticker":"BA","name":"Boeing Co.", "img_src": "http://www.riter-induction.com/wp-content/uploads/2015/03/co-logo-boeing.png"},
{"ticker":"BAC","name":"Bank of America", "img_src": "https://awardwallet.com/blog/wp-content/uploads/2017/10/Bank-of-America-Logo-Featured.png"},
{"ticker":"BIIB","name":"Biogen", "img_src": "http://www.johnpendleton.com/jpportfolio/wp-content/uploads/2015/06/biogenLogo1-465x346.jpg"},
{"ticker":"BK","name":"Bank of NY Mellon", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fbank-of-ny-mellon_416x416.jpg"},
{"ticker":"BKNG","name":"Booking", "img_src": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Logo_of_Booking_Holdings_Inc%2C%28lock_up%2C_stacked_with_Brands%2C_full_color%29.PNG"},
{"ticker":"BLK","name":"BlackRock Inc", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fblackrock_416x416.jpg"},
{"ticker":"BMY","name":"Bristol-Myers Squibb", "img_src": "https://3blaws.s3.amazonaws.com/BMSF-blue-logo.png"},
{"ticker":"BRK.B","name":"Berkshire Hathaway", "img_src": "https://bostonagentmagazine.com/wp-content/uploads/2018/09/bhhs-lockup-logoquality-seal-2jpg-611a8cdb34f3c397-1024x878.jpg"},
{"ticker":"C","name":"Citigroup Inc", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Citi.svg/1200px-Citi.svg.png"},
{"ticker":"CAT","name":"Caterpillar Inc.", "img_src": "https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/28/2019/02/19072842/Caterpillar.png"},
{"ticker":"CELG","name":"Celgene Corp", "img_src": "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Celgene_logo.svg/1200px-Celgene_logo.svg.png"},
{"ticker":"CHTR","name":"Charter Comm.", "img_src": "https://www.rbr.com/wp-content/uploads/charter-1-e1562097150553.jpg"},
{"ticker":"CL","name":"Colgate-Palmolive", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5c13d340a7ea4370591a5bc7%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D0%26cropX2%3D416%26cropY1%3D0%26cropY2%3D416"},
{"ticker":"COF","name":"Capital One", "img_src": "https://awardwallet.com/blog/wp-content/uploads/2017/04/Capital-One-Logo-Featured.jpg"},
{"ticker":"COP","name":"ConocoPhillips", "img_src": "https://stocknews.com/wp-content/uploads/2019/04/download-13.png"},
{"ticker":"COST","name":"Costco", "img_src": "https://media.licdn.com/dms/image/C4D0BAQFgmh2pajt3jQ/company-logo_200_200/0?e=2159024400&v=beta&t=PvgNnkl06fFOyEuieerGDaPk9Gk7xZLaXit4ePzszhs"},
{"ticker":"CSCO","name":"Cisco Systems", "img_src": "https://hypertecdirect.com/wp-content/uploads/2015/10/cisco-logo.png"},
{"ticker":"CVS","name":"CVS Health", "img_src": "https://www.hnmagazine.com/wp-content/uploads/2018/04/cvs-health-logo.jpg"},
{"ticker":"CVX","name":"Chevron", "img_src": "https://media.licdn.com/dms/image/C560BAQFIzPIYfEdWdw/company-logo_200_200/0?e=2159024400&v=beta&t=xQCC50_cEjc1B5H_9yooZdFmMujR3wRRoUUp0NrM804"},
{"ticker":"DD","name":"DuPont de Nemours", "img_src": "https://media.licdn.com/dms/image/C4D0BAQH4yb7AdtEA0g/company-logo_200_200/0?e=2159024400&v=beta&t=K7DHQOp5C_tTkJgIh1NxSTteP7XpuqjQxRADmuUnO-Y"},
{"ticker":"DHR","name":"Danaher Corp.", "img_src": "https://botw-pd.s3.amazonaws.com/styles/logo-thumbnail/s3/0018/3523/brand.gif?itok=JLUSfgkR"},
{"ticker":"DIS","name":"Disney", "img_src": "https://i.pinimg.com/originals/d7/18/3f/d7183f72078df410f83279c1b7bbc191.jpg"},
{"ticker":"DOW","name":"Dow Inc.", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Dow_Chemical_Company_logo.svg/1200px-Dow_Chemical_Company_logo.svg.png"},
{"ticker":"DUK","name":"Duke Energy", "img_src": "https://www.fortwright.com/DesktopModules/DnnForge%20-%20NewsArticles/ImageHandler.ashx?Width=350&Height=350&HomeDirectory=%2FPortals%2Ffortwright%2F&FileName=Images%2FNews%2Fdukeenergylogo.png&PortalID=1&q=1&s=1"},
{"ticker":"EMR","name":"Emerson Electric", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Femerson-electric_416x416.jpg"},
{"ticker":"EXC","name":"Exelon", "img_src": "https://g.foolcdn.com/art/companylogos/square/exc.png"},
{"ticker":"F","name":"Ford Motors", "img_src": "https://media.licdn.com/dms/image/C4D0BAQGUxHv2MadZ9w/company-logo_200_200/0?e=2159024400&v=beta&t=_k4HaL9mXJUQzQ40_nAywfnJEH_2c6FWwBiqGJRd_HM"},
{"ticker":"FB","name":"Facebook", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/F_icon.svg/1024px-F_icon.svg.png"},
{"ticker":"FDX","name":"FedEx", "img_src": "https://yt3.ggpht.com/a/AGF-l79rwk83D8OjC8bg9uD-Yx2TuCDU2kQopsE_ig=s900-mo-c-c0xffffffff-rj-k-no"},
{"ticker":"GD","name":"General Dynamics", "img_src": "https://g.foolcdn.com/art/companylogos/square/gd.png"},
{"ticker":"GE","name":"General Electric", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/General_Electric_logo.svg/1024px-General_Electric_logo.svg.png"},
{"ticker":"GILD","name":"Gilead Sciences", "img_src": "https://g.foolcdn.com/art/companylogos/square/gild.png"},
{"ticker":"GM","name":"General Motors", "img_src": "https://cdn.freebiesupply.com/logos/large/2x/general-motors-logo-png-transparent.png"},
{"ticker":"GOOG","name":"Alphabet Inc. C", "img_src": "https://seeklogo.net/wp-content/uploads/2016/02/alphabet-inc-logo-preview-400x400.png"},
{"ticker":"GOOGL","name":"Alphabet Inc. A", "img_src": "https://images.theconversation.com/files/93616/original/image-20150902-6700-t2axrz.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1000&fit=clip"},
{"ticker":"GS","name":"Goldman Sachs", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Goldman_Sachs.svg/1200px-Goldman_Sachs.svg.png"},
{"ticker":"HD","name":"Home Depot", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/TheHomeDepot.svg/1200px-TheHomeDepot.svg.png"},
{"ticker":"HON","name":"Honeywell", "img_src": "http://seekvectorlogo.com/wp-content/uploads/2018/02/honeywell-vector-logo-small.png"},
{"ticker":"IBM","name":"IBM", "img_src": "https://design-language-api.eu-de.mybluemix.net/images/core-blue40-blue90.svg"},
{"ticker":"INTC","name":"Intel Corp.", "img_src": "https://media.licdn.com/dms/image/C4D0BAQEQxLTTAA1tTA/company-logo_200_200/0?e=2159024400&v=beta&t=j4UVG4ef3PpUYHytoDWtYHhoqcJbwYzNDNCz9-ldsn8"},
{"ticker":"JNJ","name":"Johnson & Johnson", "img_src": "https://yt3.ggpht.com/a/AGF-l7_sHkNtnCAHfJq1gQLIz1lwahbT3Y7FvvxC0Q=s900-mo-c-c0xffffffff-rj-k-no"},
{"ticker":"JPM","name":"JPMorgan Chase", "img_src": "https://g.foolcdn.com/art/companylogos/square/jpm.png"},
{"ticker":"KHC","name":"Kraft Heinz", "img_src": "https://media.licdn.com/dms/image/C4E0BAQFfNExxO-UJZw/company-logo_200_200/0?e=2159024400&v=beta&t=C3NeNWF1JsJ_gemiLTPXjnwPE_G6_IQ0btHx7df8o8w"},
{"ticker":"KMI","name":"Kinder Morgan", "img_src": "https://cdn.worldvectorlogo.com/logos/kinder-morgan-1.svg"},
{"ticker":"KO","name":"The Coca-Cola Company", "img_src": "https://botw-pd.s3.amazonaws.com/styles/logo-thumbnail/s3/0016/9323/brand.gif?itok=usCNyorW"},
{"ticker":"LLY","name":"Eli Lilly", "img_src": "https://media.licdn.com/dms/image/C4E0BAQHI_1SzFANyBw/company-logo_200_200/0?e=2159024400&v=beta&t=C_hSrGkGzlTb4RCeRyLHZGIDzGw2KJVQ9e7MNLb-vhM"},
{"ticker":"LMT","name":"Lockheed Martin", "img_src": "http://seekvectorlogo.com/wp-content/uploads/2017/12/lockheed-martin-vector-logo-small.png"},
{"ticker":"LOW","name":"Lowe's", "img_src": "https://pbs.twimg.com/profile_images/729776009231380480/Dozl6Ihw_400x400.jpg"},
{"ticker":"MA","name":"MasterCard Inc", "img_src": "https://brand.mastercard.com/content/dam/mccom/brandcenter/thumbnails/mastercard_vrt_pos_92px_2x.png"},
{"ticker":"MCD","name":"McDonald's Corp", "img_src": "https://i.pinimg.com/originals/f4/4e/ec/f44eecf0fa921427f4a4669fb8f69115.png"},
{"ticker":"MDLZ","name":"Mondelēz Int.", "img_src": "https://www.mondelezinternational.com/~/media/mondelezcorporate/uploads/newsroom/visual-library/mdlz_rgb_w_hires.jpg?la=en"},
{"ticker":"MDT","name":"Medtronic plc", "img_src": "https://cdn.freebiesupply.com/logos/large/2x/medtronic-logo-png-transparent.png"},
{"ticker":"MET","name":"MetLife Inc.", "img_src": "http://www.metlife.com/content/dam/metlifecom/us/social-share/metlife-logo-share.jpg"},
{"ticker":"MMM","name":"3M Company", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2F3m_416x416.jpg"},
{"ticker":"MO","name":"Altria Group", "img_src": "https://pbs.twimg.com/profile_images/1282715496/AG_pos_fullws_nor_a_400x400.jpg"},
{"ticker":"MRK","name":"Merck & Co.", "img_src": "https://g.foolcdn.com/art/companylogos/square/mrk.png"},
{"ticker":"MS","name":"Morgan Stanley", "img_src": "https://g.foolcdn.com/art/companylogos/square/ms.png"},
{"ticker":"MSFT","name":"Microsoft", "img_src": "https://yt3.ggpht.com/a/AGF-l78f8ES-9_eZieHn8YSzA5IloOiJ0Bb6OwlJ=s900-mo-c-c0xffffffff-rj-k-no"},
{"ticker":"NEE","name":"NextEra Energy", "img_src": "http://www.investor.nexteraenergy.com/~/media/Images/N/NEE-IR/logo/og-logo.png"},
{"ticker":"NFLX","name":"Netflix", "img_src": "https://images-na.ssl-images-amazon.com/images/I/41Ix1vMUK7L._SY355_.png"},
{"ticker":"NKE","name":"Nike, Inc.", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Old_Nike_logo.jpg/220px-Old_Nike_logo.jpg"},
{"ticker":"NVDA","name":"NVIDIA Corp.", "img_src": "https://yt3.ggpht.com/a/AGF-l79_Wt7ESATI74kJxTR_Vb4O7suwKHieH_ka9g=s900-mo-c-c0xffffffff-rj-k-no"},
{"ticker":"ORCL","name":"Oracle", "img_src": "https://pbs.twimg.com/profile_images/1142449815030079488/hsR5mWV7_400x400.jpg"},
{"ticker":"OXY","name":"Occidental Petrol", "img_src": "https://media.licdn.com/dms/image/C4E0BAQFwd3YoRnbaUg/company-logo_200_200/0?e=2159024400&v=beta&t=IUSjBi6Nh1fdyZe24dCgSswcR761adoe1wEWMpUKvao"},
{"ticker":"PEP","name":"PepsiCo", "img_src": "https://www.pepsico.com/images/album/brand-logos/pepsi-logo.jpg?sfvrsn=5f47a137_2"},
{"ticker":"PFE","name":"Pfizer Inc", "img_src": "http://seekvectorlogo.com/wp-content/uploads/2018/03/pfizer-vector-logo-small.png"},
{"ticker":"PG","name":"Procter & Gamble", "img_src": "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Procter_%26_Gamble_logo.svg/1200px-Procter_%26_Gamble_logo.svg.png"},
{"ticker":"PM","name":"Philip Morris", "img_src": "https://cdn.worldvectorlogo.com/logos/philip-morris-international.svg"},
{"ticker":"PYPL","name":"PayPal Holdings", "img_src": "https://seeklogo.net/wp-content/uploads/2015/11/paypal-logo-preview.png"},
{"ticker":"QCOM","name":"Qualcomm Inc.", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5bc4a70d31358e59f57aaab7%2F0x0.jpg%3Fbackground%3D000000%26cropX1%3D0%26cropX2%3D416%26cropY1%3D0%26cropY2%3D416"},
{"ticker":"RTN","name":"Raytheon Co.", "img_src": "https://dwglogo.com/wp-content/uploads/2016/03/Raytheon_logo_02.png"},
{"ticker":"SBUX","name":"Starbucks Corp.", "img_src": "https://www.corpgov.net/wp-content/uploads/2016/03/Starbucks-Corporation.png"},
{"ticker":"SLB","name":"Schlumberger", "img_src": "https://media.licdn.com/dms/image/C4D0BAQHsiK38EEDiMg/company-logo_200_200/0?e=2159024400&v=beta&t=nSRCuiWpJOw_DG8TF6WZ93pUqvWbu_sv5LIB5Wn4LTU"},
{"ticker":"SO","name":"Southern Company", "img_src": "https://www.southerncompany.com/content/dam/southern-company/Logos/Vertical_Logos/620x465-southern_power_v_cmyk.jpg.img.320.low.jpg/1503949194404.jpg"},
{"ticker":"SPG","name":"Simon Property", "img_src": "https://media.licdn.com/dms/image/C4E0BAQHxQ4wCVGBrjQ/company-logo_200_200/0?e=2159024400&v=beta&t=VwqSyT2-A-cAmoEXGx_WQ5qn_-Q0RXqjKxIh134VdTM"},
{"ticker":"T","name":"AT&T Inc", "img_src": "https://www.att.com/ecms/dam/att/consumer/global/logos/att_globe_500x500.jpg"},
{"ticker":"TGT","name":"Target", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Target_logo.svg/1200px-Target_logo.svg.png"},
{"ticker":"TXN","name":"Texas Instruments", "img_src": "https://cdn.freebiesupply.com/logos/large/2x/texas-instruments-1-logo-png-transparent.png"},
{"ticker":"UNH","name":"UnitedHealth Group", "img_src": "https://bloximages.newyork1.vip.townnews.com/ifallsjournal.com/content/tncms/assets/v3/editorial/5/5e/55e357b2-9d07-5bd5-93d7-277a889b124d/5c2f9d0696e38.image.jpg"},
{"ticker":"UNP","name":"Union Pacific Corp.", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Union_pacific_railroad_logo.svg/1200px-Union_pacific_railroad_logo.svg.png"},
{"ticker":"UPS","name":"United Parcel Service", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/UPS_Logo_Shield_2017.svg/1200px-UPS_Logo_Shield_2017.svg.png"},
{"ticker":"USB","name":"U.S. Bancorp", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fus-bancorp_416x416.jpg"},
{"ticker":"UTX","name":"United Tech", "img_src": "https://usa.visa.com/dam/VCOM/global/pay-with-visa/images/vco-cards-linear-icon-450x450.png"},
{"ticker":"V","name":"Visa Inc.", "img_src": "https://www.logolynx.com/images/logolynx/82/826264bdb2e7a4f132886cb1d6729509.jpeg"},
{"ticker":"VZ","name":"Verizon", "img_src": "https://cdn.freebiesupply.com/logos/large/2x/verizon-4-logo-png-transparent.png"},
{"ticker":"WBA","name":"Walgreens Boots Alliance", "img_src": "https://media.licdn.com/dms/image/C4E0BAQFROcP05We0pQ/company-logo_200_200/0?e=2159024400&v=beta&t=ufOJM6_gU9qc2q9sLb1IE9VfGinUA2OHpJyv4CyRvwQ"},
{"ticker":"WFC","name":"Wells Fargo", "img_src": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Wells_Fargo_Bank.svg/1200px-Wells_Fargo_Bank.svg.png"},
{"ticker":"WMT","name":"Walmart", "img_src": "http://www.braindw.com/wp-content/uploads/2018/05/logo-walmart.jpg"},
{"ticker":"XOM","name":"Exxon Mobil", "img_src": "https://thumbor.forbes.com/thumbor/416x416/filters%3Aformat%28jpg%29/https%3A%2F%2Fi.forbesimg.com%2Fmedia%2Flists%2Fcompanies%2Fexxon-mobil_416x416.jpg"}
]
}


full_stock_info = all_stocks.copy() 
x = 0

def get_datetoday():
	import datetime
	currentDT = datetime.datetime.now()

	month = currentDT.month
	day = currentDT.day

	if month <10:
		month = "0"+str(month)

	if day <10:
		day = "0"+str(day)

	day = str(day)
	month = str(month)
	datetoday = str(currentDT.year)+"-"+month+"-"+day
	return datetoday

datetoday = get_datetoday()
#one api call = info for only one stock for current date

stock_count =1 
for i in full_stock_info["stocks"]:
	try:
		r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+i["ticker"]+'&apikey=' + API_KEY).json()

		#Referencing a weekend date causes an error. Market is closed.
		stock_info = r['Time Series (Daily)']["2019-10-03"]
	


		stock_info["open"] = stock_info.pop("1. open")
		stock_info["high"] = stock_info.pop("2. high")
		stock_info["low"] = stock_info.pop("3. low")
		stock_info["close"] = stock_info.pop("4. close")
		stock_info["volume"] = stock_info.pop("5. volume")


	#inserts formatted stock info into dict
		stock_info["open"] = round(float(stock_info["open"]),2)
		stock_info["high"] = round(float(stock_info["high"]),2)
		stock_info["low"] = round(float(stock_info["low"]),2)
		stock_info["close"] = round(float(stock_info["close"]),2)
		stock_info["volume"] = round(float(stock_info["volume"]),2)

		full_stock_info["stocks"][x]["info"] = stock_info
		print(full_stock_info["stocks"][x]["info"])
	
	#inserts stock buy/sell link in dict 
		full_stock_info["stocks"][x]["link"] = "https://robinhood.com/stocks/"+i["ticker"]


	#calculates percent change over day from open to close and inserts to dict
		percent_change = "{:.2f}".format((((float(full_stock_info["stocks"][x]["info"]["close"]) / float(full_stock_info["stocks"][x]["info"]["open"]))-1)*100),2)
		full_stock_info["stocks"][x]["change"] = percent_change
		x += 1
	except KeyError:
		print("something happened with ",i["ticker"],"'s get request. Continuing.....")

def get_top5(stocks):
	counter = 0
	top_5 = []
	while counter < len(stocks["stocks"]):
		changes = []
		if len(top_5) == 5:
			current_stock = float(stocks["stocks"][counter]["change"])
			for element in top_5:
				changes.append(element["change"])

			for element in top_5:
				if element["change"] == min(changes) and current_stock > element["change"]:
					element["change"] = current_stock
					element["name"] = stocks["stocks"][counter]["name"]
					break
		else:
			top_5.append({"name":stocks["stocks"][counter]["name"], "change":float(stocks["stocks"][counter]["change"])})
		counter += 1
	return top_5
 
def get_bottom5(stocks):
	counter = 0
	bottom_5 = []
	while counter < len(stocks["stocks"]):
		changes = []
		if len(bottom_5) == 5:
			current_stock = float(stocks["stocks"][counter]["change"])
			for element in bottom_5:
				changes.append(element["change"])

			for element in bottom_5:
				if element["change"] == max(changes) and current_stock < element["change"]:
					element["change"] = current_stock
					element["name"] = stocks["stocks"][counter]["name"]
					break
		else:
			bottom_5.append({"name":stocks["stocks"][counter]["name"], "change":float(stocks["stocks"][counter]["change"])})
		counter += 1
	return bottom_5

top = get_top5(full_stock_info)
bottom = get_bottom5(full_stock_info)
print("Top stocks: ",top)
print("Bottom stocks: ", bottom)

full_stock_info["top"] = top
full_stock_info["bottom"] = bottom


main_functions.save_to_file(full_stock_info, "stock_data.json")




