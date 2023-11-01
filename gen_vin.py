def cheker(var_1):
    if type(var_1) != str:
        raise TypeError (f"Вибачте, але ми не можемо працювати з {type(var_1)},"
                         f"ми працюємо з типом str")
    else:
        return  var_1

first_var = "Hello"
cheker(first_var)