# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with your data)
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
}

# Creating a DataFrame from the sample data
df = pd.DataFrame(data)

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Category'], df['Value'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
