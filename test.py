# from tools.tavily_tool import tavily_search
# from tools.flight_tool import search_flights
# from backend import run_travel_agent
#from mcp_client_test import get_all_tools, tavily_mcp_search
import asyncio
from mcp_client import get_all_tools 

# res = tavily_search("Best hotels in Nagpur")
# print(res)

# res = search_flights("Plan a 7 days Rajasthan trip from Delhi")
# print(res)

# res = run_travel_agent('Plan a 2 days trip from india to japan', 'test_user')
# print(res)



# if __name__ == "__main__":
#     asyncio.run(get_all_tools())



# if __name__ == "__main__":
#     # Run the asynchronous function in the event loop
#     asyncio.run(tavily_mcp_search('Who won the 2023 FIFA World Cup?'))


if __name__ == "__main__":
    # Run the asynchronous function in the event loop
    asyncio.run(get_all_tools())