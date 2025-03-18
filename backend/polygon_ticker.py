from polygon import RESTClient

client = RESTClient("EtJGViuG3xNXZXWOZMnQOoaMxKzuuZ4N")

tickers = []
for t in client.list_tickers(market="fx", active="true", order="asc", limit="3", sort="ticker"):
    tickers.append(t)
    break


print(tickers)