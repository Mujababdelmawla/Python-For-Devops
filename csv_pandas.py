import pandas as pd 
data = pd.read_csv('cpu_stats.csv')
# calculate average cpu usage 
print(f"Average cpu usage: {data['cpu_usage'].mean():.2f}%")
# filter the high cpu usage days and the high memory usage days 
high_cpu_days = data[data['cpu_usage'] > 80]
high_memory_days = data[data['memory_usage'] > 80]
print("high Cpu usage days :")
print(high_cpu_days)
print("high memory usage days :")
print(high_memory_days)