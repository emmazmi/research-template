from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv
from codelists import *


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "index_date", "latest": "today"},
        "rate": "uniform",
        "incidence": 1.0,
    },
    index_date="2019-12-01",
    population=patients.satisfying(
        "has_covid AND has_long_covid",
        has_covid=patients.with_these_clinical_events(covid_codes),
        has_long_covid=patients.with_these_clinical_events(long_covid_codes),
    ),

    covid_date=patients.with_these_clinical_events(
        covid_codes,
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 1.0, "date": {"earliest": "index_date"}},
    ),

    long_covid_date=patients.with_these_clinical_events(
        long_covid_codes,
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"incidence": 1.0, "date": {"earliest": "2021-01-01"}},
    ),
)