import matplotlib.pyplot as plt
import pandas as pd

# Function to do some comparison between professionals and students
def plot_stud_prof(prof_stack="", stud_stack="", prof="", stud="", column="", title=""):
    if column!="":
        prof=prof_stack[column]
        stud=stud_stack[column]
    p = prof.value_counts(normalize=True)[:10]
    v_stud = stud.value_counts(normalize=True)
    s = v_stud.loc[p.index]
    df = pd.DataFrame([p, s])
    df = df.T
    df.columns = ["Professional", "Student"]
    df.plot.bar(figsize=(7,7))
    plt.title(title + ' distribution for Professionals/Students')
    plt.ylabel("Ratio")
    plt.show()
    
    
# We filter out the devs upon some criteria
def row_filter(stack, row):
    if row.Professional not in ["Student", 
                                "Professional developer"]:
        return False
    if row.Professional == "Professional developer":
        if row.EmploymentStatus not in ['Employed part-time',
                                        'Employed full-time',
                                        'Independent contractor, freelancer, or self-employed']:
            return False
        # After checking salary values, we decided to remove the first 5%
        # quantile as they were mostly outliers (values inbetween 0 and 100)
        if row.isnull().Salary or row.Salary < stack.Salary.quantile(0.05):
            return False
        if row.isnull().JobSatisfaction and row.isnull().CareerSatisfaction:
            return False
    else:
        if row.isnull().ExpectedSalary or row.ExpectedSalary < stack.ExpectedSalary.quantile(0.05):
            return False
    return True