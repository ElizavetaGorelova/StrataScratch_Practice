# You have been asked to find the job titles of the highest-paid employees.

# Your output should include the highest-paid title or multiple titles with the same salary.


import pandas as pd

worker[worker.salary == worker.salary.max()].merge(title, how = 'inner', left_on = 'worker_id', right_on = 'worker_ref_id')[['worker_title']]
