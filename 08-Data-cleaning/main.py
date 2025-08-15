from datetime import datetime
import ast

# print(datetime.now())


data_science_job = [
    {
        'job_title': 'Data Scientist',
        'job_skills': "['Python', 'SQL', 'Machine Learning']",
        'job_date': '14-08-2025'
    },
    {
        'job_title': 'Data Analyst',
        'job_skills': "['Excel', 'Power BI', 'SQL', 'Data Visualization']",
        'job_date': '15-08-2025'
    },
    {
        'job_title': 'Machine Learning Engineer',
        'job_skills': "['Python', 'TensorFlow', 'Deep Learning', 'NLP']",
        'job_date': '16-08-2025'
    },
    {
        'job_title': 'Business Intelligence Analyst',
        'job_skills': "['Tableau', 'SQL', 'Data Warehousing', 'ETL']",
        'job_date': '17-08-2025'
    },
    {
        'job_title': 'Data Engineer',
        'job_skills': "['Python', 'Spark', 'AWS', 'Data Pipelines']",
        'job_date': '18-08-2025'
    },
    {
        'job_title': 'AI Researcher',
        'job_skills': "['Python', 'PyTorch', 'Reinforcement Learning', 'Computer Vision']",
        'job_date': '19-08-2025'
    }
]


# print(data_science_job[0]['job_date'])

test_date = data_science_job[0]['job_date']
# print(datetime.strptime(test_date, '%d-%m-%Y'))


for job in data_science_job:
  job['job_date'] = datetime.strptime(job['job_date'], '%d-%m-%Y')
  job['job_skills'] = ast.literal_eval(job['job_skills'])
print(data_science_job)