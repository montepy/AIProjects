import sys
import io
import binascii
import fileinput

compressee = open(sys.argv[1], "r", encoding="utf-8")
compressed = file("output.txt", "w", encoding="utf-8")

bio = io.BytesIO(compressee)

view = bio.
