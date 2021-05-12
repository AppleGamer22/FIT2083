from pandas import read_csv

cve_raw = read_csv("./CVE_raw.csv")
cve_filtered = cve_raw[cve_raw["Description"].str.contains("linux|windows", case = False)]
print(cve_filtered)