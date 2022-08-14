import http.client as hc
import json as js
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
conn = hc.HTTPSConnection("api.collectapi.com")
headers = {'content-type': "application/json",
           'authorization': "apikey your Token" }
conn.request("GET", "/corona/countriesData", headers=headers)
res = conn.getresponse()
data = res.read()
data_json = data.decode("utf-8")
data_dict = js.loads(data_json)
data_result = data_dict["result"]
mydata = {}
for say in range(len(data_result)-1):
    result_dict = data_result[say]
    new_totalDeaths = result_dict["totalDeaths"]
    if new_totalDeaths=='': new_totalDeaths='0'
    new_totalDeaths = new_totalDeaths.replace(",","")
    new_totalDeaths = int(new_totalDeaths)
    mydata[result_dict["country"]] = new_totalDeaths
df = pd.DataFrame(mydata.values(), index=mydata.keys(), columns=['TotalDeaths'])
df = df["TotalDeaths"].sort_values(ascending=False)
dnum = 20
sns.set(rc={'figure.figsize':(12,5)})
ax = sns.barplot(x=(df.head(dnum).values), y=df.head(dnum).index)
ax.set_title('Covid19 Total Deaths Base On Countries') 
ax.set_xlabel('Values')
ax.set_ylabel('Countries')
plt.show()


# =============================================================================
# {
#   "success": true,
#   "result": [
#     {
#       "country": "China",
#       "totalcases": "80,881",
#       "newCases": "+21",
#       "totaldeaths": "3,226",
#       "newDeaths": "+13",
#       "totalRecovered": "68,709",
#       "activeCases": "8,946"
#     },
#     {
#       "country": "Italy",
#       "totalcases": "27,980",
#       "newCases": "",
#       "totaldeaths": "2,158",
#       "newDeaths": "",
#       "totalRecovered": "2,749",
#       "activeCases": "23,073"
#     },
#     "..."
#   ]
# }
# =============================================================================


