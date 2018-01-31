#print a dictionary in the order by key

d = {"java":9, "javascript":6, "c#":7, "python":3, "html":5, "css":3}

for k,v in sorted(d.items()):
    print(k,v)