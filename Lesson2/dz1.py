str_variable = "Str"
int_variable = 42
flot_variable = 42.42
bool_variable = True
none_variable = None
list_variable = [42, 42.42]
set_variable = {32, 42}
tuple_variable = (32, 42)
dict_variable = {32: "fist", 42: "second"}

list_variables = [str_variable, int_variable, flot_variable, bool_variable,
                  none_variable, list_variable, set_variable, tuple_variable, dict_variable]
list_type = [str, int, float, bool, type(None), list, set, tuple, dict]

for idx, value in enumerate(list_variables):
    print(idx, f"value - {value} type is type(value)")
    if type(value) == list_type[idx]:
        print("Да, это верный тип")
