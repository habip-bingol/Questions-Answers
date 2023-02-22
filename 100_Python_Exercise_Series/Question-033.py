# Create a dictionary with Dict Comprehensions from the lists below which is appropriate, such as: {"TR": "Turkey"}.
# countries ;    
# country_code_list = ["TR", "US", "CN", "SE", "FR", "NL"]
# country_list = ["Netherlands", "France", "Sweden", "United States", "China", "Turkey"]


country_code_list = ["TR", "US", "CN", "SE", "FR", "NL"]
country_list = ["Netherlands", "France", "Sweden", "United States", "China", "Turkey"]

country_dict = {i:j for i in country_code_list for j in country_list if i[0] == j[0]}
print(country_dict)