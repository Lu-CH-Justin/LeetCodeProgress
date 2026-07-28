import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df1 = students.merge(subjects, how = 'cross')
    df2 = examinations.groupby(['student_id','subject_name']).size().reset_index(name = 'attended_exams')
    df = df1.merge(df2, on = ['student_id','subject_name'], how = 'left')
    df['attended_exams'] = df['attended_exams'].fillna(0)
    return df.sort_values(['student_id','subject_name'])