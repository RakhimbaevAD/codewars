def hex_string_to_RGB(hex_string): 
    convert_result = dict()
    _, hex_string = hex_string.split('#')
    convert_result['r'] = int(hex_string[:2], 16)
    convert_result['g'] = int(hex_string[2:4], 16)
    convert_result['b'] = int(hex_string[4:], 16)
    return convert_result