import model_math
import mylog
import transform_num
import view


def button_click():
    value1, value2, do = view.input_data()
    value1, value2 = transform_num.transform_numbers(num_type, value1, value2)
    result = model_math.calc(value1, do, value2)
    view.view_data('Ответ: ', result)
    log.write_log(value1, do, value2, result)


# button_click()
