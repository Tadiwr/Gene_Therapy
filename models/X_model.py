
import pandas as pd

# XModel is a class containing the different variables in a gene therapy trial!

class XModel:
    
    drug_id = "" #
    status = "" #
    points = 0 #
    vector = "" #
    safety_met = "" #
    route = "" #
    area = "" #
    phase = "" #
    completion = 0 #

    # factory method that returns a 
    # dataframe that can be predicted

    