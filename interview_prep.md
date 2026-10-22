# Junior Data Analyst Interview Preparation



## 1. Technical Questions



### Q1. What is the difference between SQL WHERE and HAVING?

`WHERE` filters individual rows before grouping. `HAVING` filters grouped results after `GROUP BY`. For example, `WHERE` can select transactions from 2026, while `HAVING` can select branches whose total sales exceed KES 100,000.



### Q2. What is the difference between INNER JOIN and LEFT JOIN?

`INNER JOIN` returns rows with matching records in both tables. `LEFT JOIN` returns every row from the left table and matching rows from the right table, including unmatched left-side rows.



### Q3. How do you handle missing values in pandas?

First, I use `df.isnull().sum()` to identify missing values. I then investigate why values are missing and choose an appropriate treatment, such as filling numerical values with a suitable statistic or removing records when justified. I document the decision to protect data quality.



### Q4. What is exploratory data analysis (EDA)?

EDA is the process of understanding a dataset before drawing conclusions. I inspect data types, missing values, duplicates, distributions, outliers, and relationships using pandas, summary statistics, and visualizations.



### Q5. What is an A/B test?

An A/B test compares two versions of a product or experience to determine whether a change affects an outcome, such as conversion. I define a metric, assign users to groups, collect enough data, compare results statistically, and report uncertainty before recommending a change.



## 2. Behavioural Questions - STAR Method



Use real examples from your experience. Adapt the drafts below so they accurately reflect what you did.



### Q6. Tell me about a time you solved a problem.



**Situation:** During a data analytics assignment, I needed to prepare a dataset for analysis.



**Task:** I had to identify data quality issues and make the dataset suitable for reliable analysis.



**Action:** I used Python and pandas to inspect missing values, check duplicates, validate records, and document cleaning decisions.



**Result:** I produced a cleaner dataset that could be used for analysis and reporting. I would explain the exact measurable result from my project if asked.



### Q7. Tell me about a time you learned a new skill.



**Situation:** My data analytics training required me to work with tools such as Python, SQL, and data visualization.



**Task:** I needed to apply these tools to practical analytical problems.



**Action:** I practised through weekly projects, wrote SQL queries, explored data with pandas, and documented my work in GitHub repositories.



**Result:** I developed practical project experience and evidence of my learning that I can share with employers.



## 3. Questions to Ask the Interviewer



- What would success look like in the first three months?

- Which tools and data sources does the team use most?

- How does the team communicate findings to non-technical stakeholders?



## 4. Final Preparation Checklist



- [ ] Practise explaining each project without reading notes.

- [ ] Be ready to demonstrate one SQL query and one pandas analysis.

- [ ] Review project results and explain their limitations.

- [ ] Replace generic STAR examples with accurate personal experiences.

- [ ] Practise answering aloud in clear, concise language.





