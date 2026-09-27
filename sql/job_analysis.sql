-- 1. Total number of jobs
SELECT COUNT(*) AS total_jobs
FROM jobs;


-- 2. Jobs by employment type
SELECT employmentType, COUNT(*) AS job_count
FROM jobs
GROUP BY employmentType
ORDER BY job_count DESC;


-- 3. Jobs by seniority
SELECT seniority, COUNT(*) AS job_count
FROM jobs
GROUP BY seniority
ORDER BY job_count DESC;


-- 4. Jobs with salary information
SELECT
    title,
    companyName,
    minSalary,
    maxSalary,
    currency,
    salaryPeriod
FROM jobs
WHERE minSalary IS NOT NULL
   OR maxSalary IS NOT NULL
ORDER BY maxSalary DESC;


-- 5. Companies with multiple job postings
SELECT companyName, COUNT(*) AS job_count
FROM jobs
GROUP BY companyName
HAVING COUNT(*) > 1
ORDER BY job_count DESC;