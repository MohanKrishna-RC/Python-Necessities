import pingouin as pg

df = pd.read_csv("2.csv")

pg.corr(x= df["height"],y=df["weight"])

df.corr().round(2)