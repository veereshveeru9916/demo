from numpy import dtype
df=pd.DataFrame({"study_mode":["online","classroom","online"]})
encoded=pd.get_dummies(df,columns=["study_mode"],dtype=int)
print(encoded)