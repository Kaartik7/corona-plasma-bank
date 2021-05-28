import csv

#################################################################################

#The following is the table for patient-donor blood group compatibility.

#    ___________________________
#   | Patient    |  CCP Donor   |
#    ___________________________
#   |    A       |     A,AB     |
#    ___________________________
#   |    B       |    B,AB      |
#    ___________________________
#   |    AB      |    AB        |
#    ___________________________
#   |    O       |   O,A,B,AB   |
#    ___________________________

donor_comp = {'A':['A','B'],'B':['B','AB'], 'AB': ['AB'], 'O':['O','A','B','AB'] }


def find_donor(blood_group: str) -> list:
    """
    Takes the blood group as input and gives a list of donors along with contact
    details as output.
    """
    potential_donors = []
    potential_blood_groups = donor_comp[blood_group]
    with open('donors.csv') as CSV_FILE1:
        donor_data = csv.reader(CSV_FILE1)
        next(donor_data)  # to skip the first row
        for row in donor_data:
            if row[1] in potential_blood_groups:
                potential_donors.append((row[0], row[4]))
    return potential_donors



