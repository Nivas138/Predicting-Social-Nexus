relaton=df[1:20][['created','texts','retweet','hashtags','followers','friends']]

relaton.sort_values(['followers'],ascending=[False])

relaton.sort_values(['retweet'],ascending=[False])