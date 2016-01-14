# -*- coding: utf-8 -*-

import base64


def b64_to_img(b64_str_pth, dst_pth):
    with open(b64_str_pth, "r") as f:
        MIME_b64_str = f.read()
        # read b64 str from file ("file" to "str")

        MIME_b64_byte = bytes(MIME_b64_str, encoding="utf-8")
        # convert a b64 str into a b64 byte ("str" to "byte")

        raw_byte = base64.decodebytes(MIME_b64_byte)
        # convert a b64 byte into a raw byte ("byte" to "byte), per RFC 2045 / MIME

        with open(dst_pth, "wb") as g:
            g.write(raw_byte)


def img_to_b64(src_pth, b64_str_pth):
    with open(src_pth, "rb") as f:
        raw_byte = f.read()
        # read raw byte from src, "file" to "byte"

        MIME_b64_byte = base64.encodebytes(raw_byte)
        # convert raw byte into b64 byte , "byte" to "byte", per RFC 2045 / MIME

        MIME_b64_str = MIME_b64_byte.decode(encoding="utf-8")
        # decode b64 byte into str, "byte" to "str"

        with open(b64_str_pth, "w") as g:
            g.write(MIME_b64_str)


if __name__ == "__main__":
    img_pth = "2.jpeg"

    b64_str_pth = "new_b65"
    dst_img_pth = "dst_img111.jpeg"

    b64_to_img(b64_str_pth, dst_img_pth)


    src_img_pth = "dst_img.jpeg"
    new_b64_str_pth = "new_b65"

    #img_to_b64(src_img_pth, new_b64_str_pth)