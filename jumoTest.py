import pandas as pd
import dateutil.parser

from loan_parameter import LoanParameter


def read_from_csv():

    file = r'Loans.csv'
    df = pd.read_csv(file)

    loanDataLists = []

    for column in df.loc[0:, 'Network':'Amount']:

        loanDataLists.append(df[column])

    return loanDataLists



def get_totals_and_count(column_data, data_type):
    count = 0
    loadDataInterimList = []

    for dataItem in column_data:

        if data_type == 'Month':
            dataItem = dateutil.parser.parse(dataItem).strftime('%B')

        if LoanParameter.create_item(dataItem) not in loadDataInterimList:
            nt = LoanParameter.create_item(dataItem)
            nt.loan_amount(loanDataLists[3][count])
            nt.set_loan_type(data_type)
            loadDataInterimList.append(nt)
        else:
            bt = LoanParameter.create_item(dataItem)
            bt.loan_amount(loanDataLists[3][count])
            bt.set_number_of_loans()

        count = count + 1

    return pd.DataFrame.from_records([s.to_tuple() for s in loadDataInterimList],columns = ['Parameter','Total Amount of loans','Count of loans'])


def build_dataframes_and_write_csv():

    loanParameters = ['Network', 'Month', 'Product']
    dataframes = []

    for param in loanParameters:

        if param == 'Month':
            df = get_totals_and_count(loanDataLists[1], param)
        else:
            df = get_totals_and_count(loanDataLists[loanParameters.index(param)], param)

        dataframes.append(df)

    pdoutput = pd.concat(dataframes, join='outer')
    pdoutput.to_csv('Output.csv')


if __name__ == '__main__':
    loanDataLists = read_from_csv()
    build_dataframes_and_write_csv()


