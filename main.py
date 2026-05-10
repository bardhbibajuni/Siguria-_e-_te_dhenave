BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(text):

    data = text.encode("utf-8")

    result = ""

    for i in range(0, len(data), 3):

        block = data[i:i + 3]

        byte1 = block[0]
        byte2 = block[1] if len(block) > 1 else 0
        byte3 = block[2] if len(block) > 2 else 0

        combined = (byte1 << 16) | (byte2 << 8) | byte3

        index1 = (combined >> 18) & 63
        index2 = (combined >> 12) & 63
        index3 = (combined >> 6) & 63
        index4 = combined & 63

        result += BASE64_TABLE[index1]
        result += BASE64_TABLE[index2]

        if len(block) > 1:
            result += BASE64_TABLE[index3]
        else:
            result += "="

        if len(block) > 2:
            result += BASE64_TABLE[index4]
        else:
            result += "="

    return result


def decode(base64_text):

    result_bytes = bytearray()

    for i in range(0, len(base64_text), 4):

        block = base64_text[i:i + 4]

        padding = block.count("=")

        block = block.replace("=", "A")

        index1 = BASE64_TABLE.index(block[0])
        index2 = BASE64_TABLE.index(block[1])
        index3 = BASE64_TABLE.index(block[2])
        index4 = BASE64_TABLE.index(block[3])

        combined = (index1 << 18) | (index2 << 12) | (index3 << 6) | index4

        byte1 = (combined >> 16) & 255
        byte2 = (combined >> 8) & 255
        byte3 = combined & 255

        result_bytes.append(byte1)

        if padding < 2:
            result_bytes.append(byte2)

        if padding < 1:
            result_bytes.append(byte3)

    return result_bytes.decode("utf-8")

#Jakup

