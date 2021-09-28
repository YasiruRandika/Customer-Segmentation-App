from summery import get_summary
from botocore.utils import parse_timestamp
from back_end import read_csv_file
import pandas as pd
import numpy as np
import boto3;

clustered_customers_df = read_csv_file()
#Min and Max
max_balance = max(clustered_customers_df['balance'])
min_balance = min(clustered_customers_df['balance'])

bin_labels = np.linspace(min_balance, max_balance, num=6) #Contains the range Values

#data about cluster0
cluster0_data = clustered_customers_df.loc[clustered_customers_df['cluster'] == 0]
cluster1_data = clustered_customers_df.loc[clustered_customers_df['cluster'] == 1]
cluster2_data = clustered_customers_df.loc[clustered_customers_df['cluster'] == 4]



qs0 = pd.cut(cluster0_data['balance'], bins=bin_labels)
y_values_c0 = np.array(qs0.value_counts())

qs1= pd.cut(cluster1_data['balance'], bins=bin_labels)
y_values_c1 = np.array(qs1.value_counts())

qs2= pd.cut(cluster2_data['balance'], bins=bin_labels)
y_values_c2 = np.array(qs2.value_counts())

#Generating x labels
x_labels  = []

for i in range(1,len(bin_labels)):
   label=""
   label=str(round(bin_labels[i-1]))+" - "+str(round(bin_labels[i]))
   x_labels.append(label)

#print('X_labels',x_labels)
balancedf_c0 = pd.DataFrame({'x_values':x_labels,'y_values':y_values_c0})
balancedf_c1 = pd.DataFrame({'x_values':x_labels,'y_values':y_values_c1})
balancedf_c2 = pd.DataFrame({'x_values':x_labels,'y_values':y_values_c2})


def cluster0_summery(): 
   return get_summary(0,'balance')

def cluster1_summery(): 
   return balancedf_c1

def cluster2_summery(): 
   return balancedf_c2