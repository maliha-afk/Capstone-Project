import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

emp_data={
    "name":["atiya","zaheen",np.nan,np.nan],
    "age":["29","28","31","27"],
    "salary":[2000,"6000",1000,np.nan]
}

emp_df=pd.DataFrame(emp_data)

emp_df["name"]=emp_df["name"].fillna("unknown")
emp_df["age"]=emp_df["age"].astype(int)

#emp_df["salary"]=emp_df["salary"].astype(int)

emp_df["salary"]=pd.to_numeric(emp_df["salary"])
avg_salary=emp_df["salary"].mean()
emp_df["salary"]=emp_df["salary"].fillna(avg_salary)
print(emp_df)