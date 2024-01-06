import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


row_values = np.arange(5,115,5)
column_values = np.arange(500,1175,25)

modified_column_names= [str(col) +'(m/s)' for col in column_values]
modified_row_names =[str(row) +'(m)' for row in row_values]
    
data = []

for row in row_values:
    row_data =[]
    
    for col in column_values:
        row_data.append(row / col)
        
    data.append(row_data)
    
df = pd.DataFrame(data, index = modified_row_names, columns = modified_column_names)


Bullet_Travel_Time = df.round(3)


plt.subplots(dpi=100, figsize=(20, 15))
sns.heatmap(Bullet_Travel_Time , annot=True, cbar=True,  xticklabels=column_values, yticklabels=row_values)

plt.title('Bullet Time to Target (seconds)')
plt.xlabel('Velocity (meters/second)')
plt.ylabel('Distance To Target (meters)')
# Placing the column names on top of the heatmap
plt.tick_params(axis='x', which='both', bottom=True, top=True, labeltop=True, labelbottom=True)

Tac_Sprint_Speed = 7.5
Player_width = 0.6

df2 = pd.DataFrame(Bullet_Travel_Time.values*Tac_Sprint_Speed, index=Bullet_Travel_Time.index, columns=Bullet_Travel_Time.columns)

Distance_Player_Traveled_Post_Shot = df2.round(4)



Ploting_single_row= Bullet_Travel_Time.loc['110(m)'].values
# Get the column values as a list for the x-axis
