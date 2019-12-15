import base64,lzma,os

header = """import base64,lzma
exec(lzma.decompress(base64.b64decode({data})))"""
filename = input("Input Filename >>>")
data = open(filename)
path,truefilename = os.path.split(filename)
output = header.format(data = base64.b64encode(lzma.compress(bytes(data.read(), 'utf-8'))))
data = open("./compressed/{}".format(truefilename),"w")
data.write(output)
data.close()

