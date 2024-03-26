import pymongo
import pandas as pd

# Set up MongoDB
myclient = pymongo.MongoClient("mongodb+srv://khangwen197:password@cluster0.pqitser.mongodb.net/")
mydb = myclient["CSE4200"]

mycol = mydb["Metrics"]

metrics_data = [data for data in mycol.find()]
df_metrics = pd.DataFrame(metrics_data)
print(df_metrics)