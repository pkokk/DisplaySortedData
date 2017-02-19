from bottle import route, run
import pandas as pd


def sort_by(df, col_name):
    df_sorted = df.sort(col_name).to_html(classes='table',index=False,escape=False)
    return df_sorted
 
if __name__ == '__main__':
    
    full_path = "data.csv" 
    df = pd.read_csv(full_path, delimiter = ';', header = 0)
    
    @route('/name/')
    def name_disp():
        return sort_by(df, 'Name')
    
    @route('/age/')
    def age_disp():
        return sort_by(df, 'Age')
    
    @route('/salary/')
    def salary_disp():
        return sort_by(df, 'Salary')
    
    
    run(host='localhost', port=8080, debug=True)

