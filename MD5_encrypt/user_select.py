import MD5, MD5_1, MD5_1_4, MD5_1_2_4, MD5_1_2_3_4, MD5_1_2, MD5_1_2_3, MD5_2, MD5_3, MD5_4, MD5_2_3, MD5_2_4, MD5_3_4, \
    MD5_2_3_4, MD5_1_3, MD5_1_3_4


def MD5_select(text, selected_options):
    # 将字符串转换为十六进制字符串
    text = text.replace('\n', '')
    hex_string = text.encode().hex()
    # hex_string = ''.join(hex(ord(c))[2:] for c in text)
    if "Option 1" in selected_options:
        if "Option 2" in selected_options:
            if "Option 3" in selected_options:
                if "Option 4" in selected_options:
                    hashes = MD5_1_2_3_4.md5(hex_string)
                else:
                    hashes = MD5_1_2_3.md5(hex_string)
            elif "Option 4" in selected_options:
                hashes = MD5_1_2_4.md5(hex_string)
            else:
                hashes = MD5_1_2.md5(hex_string)
        elif "Option 3" in selected_options:
            if "Option 4" in selected_options:
                hashes = MD5_1_3_4.md5(hex_string)
            else:
                hashes = MD5_1_3.md5(hex_string)
        elif "Option 4" in selected_options:
            hashes = MD5_1_4.md5(hex_string)
        else:
            hashes = MD5_1.md5(hex_string)
    elif "Option 2" in selected_options:
        if "Option 3" in selected_options:
            if "Option 4" in selected_options:
                hashes = MD5_2_3_4.md5(hex_string)
            else:
                hashes = MD5_2_3.md5(hex_string)
        elif "Option 4" in selected_options:
            hashes = MD5_2_4.md5(hex_string)
        else:
            hashes = MD5_2.md5(hex_string)
    elif "Option 3" in selected_options:
        if "Option 4" in selected_options:
            hashes = MD5_3_4.md5(hex_string)
        else:
            hashes = MD5_3.md5(hex_string)
    elif "Option 4" in selected_options:
        hashes = MD5_4.md5(hex_string)
    else:
        hashes = MD5.md5(hex_string)
    return hashes
