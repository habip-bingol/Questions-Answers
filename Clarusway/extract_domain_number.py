# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. For example:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"


# url = "http://github.com/carbonfive/raygun"
# url = "http://www.zombie-bites.com" 
# url = "https://www.cnet.com" 
# url =  "http://google.com"
# url = "http://google.co.jp"
# url = "www.xakep.ru"
# url = "https://youtube.com"
# url = "http://google.co.jp"
# url = "http://www.zombie-bites.com"
url = "http://github.com/carbonfive/raygun"
url.split("//")[-1].split("www.")[-1].split(".")[0]
