import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.1.1")
# And you would get your results in json
print(results)