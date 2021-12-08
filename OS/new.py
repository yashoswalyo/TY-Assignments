from yt_dlp import extractor

url = "safdsa"
res = extractor.list_extractors(18)
for i in range(len(res)):
	print( res[i])
