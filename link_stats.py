import tweepy
from coinmarketcap import Market

# simple twitter bot to show basic stats for a coin
# used chainlink as an example to check out coinmarketcap lib and api
# will come back to this and try to make it input based at some point

coinmarketcap = Market()
link = coinmarketcap.ticker(1975)
total_market = coinmarketcap.stats()

total_mcap = total_market['data']['quotes']['USD']['total_market_cap']
chainlink_mcap = link['data']['quotes']['USD']['market_cap']
link_price = link['data']['quotes']['USD']['price']
link_volume = link['data']['quotes']['USD']['volume_24h']
link_percent24h = link['data']['quotes']['USD']['percent_change_24h']
link_rank = link['data']['rank']
link_dominance = chainlink_mcap / total_mcap * 100

stats = f'''Chainlink $LINK stats:

CMC Rank: {link_rank}
Price: ${link_price:.3}
%Change (24h): {link_percent24h}%
Volume (24h): ${link_volume:,.0f} USD
Market Share: {link_dominance:.2}%
Market Cap: ${chainlink_mcap:,.0f} USD
Total Market Cap: ${total_mcap:,.0f} USD'''

#add your own oauth
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

api.update_status(stats)
