job_data = [
    {
        "job_title": "Data Scientist",
        "job_skills": ["Python", "Machine Learning", "SQL", "Statistics"],
        "remote": True
    },
    {
        "job_title": "Data Analyst",
        "job_skills": ["Excel", "Power BI", "SQL", "Data Visualization"],
        "remote": False
    },
    {
        "job_title": "Machine Learning Engineer",
        "job_skills": ["Python", "TensorFlow", "Deep Learning", "NLP"],
        "remote": True
    },
    {
        "job_title": "Business Intelligence Analyst",
        "job_skills": ["Tableau", "SQL", "Data Warehousing", "ETL"],
        "remote": False
    },
    {
        "job_title": "Data Engineer",
        "job_skills": ["Python", "Spark", "AWS", "Data Pipelines"],
        "remote": True
    }
]


# print(list(filter(lambda job: job["remote"], job_data)))

print(list(filter(lambda job: job["remote"] and "Python" in job['job_skills'], job_data)))


