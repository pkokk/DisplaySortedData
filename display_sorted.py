from bottle import route, run
import pandas as pd

#function to sort dataframe by column name AND transform sorted dataframe into html table
def sort_by(df, col_name):
    df_sorted = df.sort(col_name).to_html(classes='table',index=False,escape=False)
    return df_sorted
 
if __name__ == '__main__':
    
    full_path = "data.csv" 
    df = pd.read_csv(full_path, delimiter = ';', header = 0)
    
    #create 3 different routes, each with one sorting
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

