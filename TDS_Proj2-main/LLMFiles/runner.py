
import pandas as pd

df = pd.read_csv("demo-audio-data.csv", header=None)

# The column will be named 0 by default
df.columns = ['numbers']

cutoff = 43910

# Filter numbers greater than the cutoff
filtered_df = df[df['numbers'] > cutoff]

# Sum the filtered numbers
answer = filtered_df['numbers'].sum()

print(int(answer))
