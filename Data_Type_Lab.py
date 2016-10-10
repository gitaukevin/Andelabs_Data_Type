def data_type(sample_data):#Defining function data_type that takes sample_data as argument.
    Data_type = type(sample_data)
    if Data_type == list:
        if len(sample_data) < 3:#returns the third element in the list if it does exist and none if ain't existing.
            return None
        else:
            return sample_data[2]
    elif Data_type == int:#Showing how integers compare to 100.
        if sample_data < 100:
            return 'less than 100'
        elif sample_data == 100:
            return 'equal to 100'
        else:
            return 'more than 100'
    elif Data_type == str: #returns the lenght of the string
        return len(sample_data)
    elif Data_type == bool:#returns the boolean
        return sample_data
    else:
        return "no value"
