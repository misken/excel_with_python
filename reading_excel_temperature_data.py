import xlrd
import csv
import openpyxl


def consolidate_logger_xlsheets_xlrd(fn_xlsx, fn_csv, verbose=True):
    """
    Combine xlsx sheets and output as csv using xlrd.

    Args:
        fn_xlsx: filename of Excel file to process
        fn_csv:  filename of output CSV file
        verbose: If true (default), writes status messages
    Returns:
        nothing, just writes CSV file

    """

    # Open the workbook
    wb_sites = xlrd.open_workbook(fn_xlsx)

    # Accumulate the rows (lists) into another list. We'll up with a list of lists.
    data = []
    for sheet in wb_sites.sheets():
        if verbose:
            print("xlrd:", sheet.name, sheet.nrows)

        site = sheet.name

        # Get the rows for the current sheet
        for rownum in range(1,sheet.nrows): # Think carefully about the sheet.nrows
            datarow = sheet.row_values(rownum)
            datarow.append(site)
            data.append(datarow)
    if verbose:
        print("xlrd:", "Total number of rows: ", len(data), "\n")

    # Write out CSV file
    with open(fn_csv, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def consolidate_logger_xlsheets_openpyxl(fn_xlsx, fn_csv, verbose=True):
    """
    Combine xlsx sheets and output as csv using openpyxl

    Args:
        fn_xlsx: filename of Excel file to process
        fn_csv:  filename of output CSV file
        verbose: If true (default), writes status messages
    Returns:
        nothing, just writes CSV file

    """
    # Open the workbook
    wb_sites = openpyxl.load_workbook(fn_xlsx)

    # Accumulate the rows (lists) into another list. We'll up with a list of lists.
    data = []
    for ws in wb_sites:
        if verbose:
            print("openpyxl:", ws.title)

        site = ws.title

        # Get the rows for the current sheet
        #for row in ws.rows[1:]:
        for row in ws.iter_rows():
            ws_data = [cell.value for cell in row]
            ws_data.append(site)
            data.append(ws_data)

    if verbose:
        print("openpyxl:", "Total number of rows: ", len(data), "\n")


    # Write CSV file
    with open(fn_csv, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)

# The lines below are NOT part of the function above, they are just part of
# this Python script file. They represent a common "pattern" in creating
# Python scripts. Essentially, the if is checking to see if this
# script was run as a 'main' program (either run
# from the command line or run by pushing the Run button in the IDE). If it
# was, it executes the lines after the if statement. If instead,
# this file was imported by another script and then the function called from
# that program, the input and output filenames to process would be passed in as part of the
# function call. Of course, instead of supplying a default filename here,
# we could instead allow for the filename to be passed in as a command line
# argument. See p389 in DWwP for basic info on dealing with command line
# arguments. See the accepted answer in the following StackOverflow question
# for more details: http://stackoverflow.com/questions/419163/what-does-if-name-main-do

if __name__ == '__main__':

    xlsxfile = 'data/sites_1_6.xlsx'

    csvfile1 = 'data/sites_1_6_xlrd.csv'
    csvfile2 = 'data/sites_1_6_openpyxl.csv'

    consolidate_logger_xlsheets_xlrd(xlsxfile, csvfile1)
    consolidate_logger_xlsheets_openpyxl(xlsxfile, csvfile2)