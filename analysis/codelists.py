from cohortextractor import codelist, codelist_from_csv

covid_codes = codelist_from_csv(
    "codelists/opensafely-covid-identification-in-primary-care-probable-covid-positive-test.csv", system="ctv3", column="CTV3ID"
)

long_covid_codes = codelist_from_csv(
    "codelists/opensafely-nice-managing-the-long-term-effects-of-covid-19-64f1ae69.csv", system="snomed", column="code"
)