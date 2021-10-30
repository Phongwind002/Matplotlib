
import numpy as np
import pandas as pd
my_column_names = ['Môt', 'hai', 'ba', 'bon']

my_data = np.random.randint(low=0, high=101, size=(3, 4))

df = pd.DataFrame(data=my_data, columns=my_column_names)

print(df)

print("\nCột thứ 2 : %d\n" % df['Môt'][1])

df['Hulk'] = df['ba'] + df['bon']

print(df)