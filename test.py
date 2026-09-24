from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


# res = tavily_search("Best hotels in Nagpur")
# print(res)

# res = search_flights("Plan a 7 days Rajasthan trip from Delhi")
# print(res)

res = run_travel_agent('Plan a 2 days trip from india to japan', 'test_user')
print(res)