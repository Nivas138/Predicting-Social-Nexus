def main():

    global api, cmax, locords

    # Geo-coordinates of five metropolitan areas
    # London, NYC (lower, middle, upper), Wash DC, San Francisco, New Brunswick (NJ)
    locords =  {'lo': '0, 51.503, 20km',
                'nyl': '-74, 40.73, 2mi',
                'nym': '-74, 40.74, 2mi',
                'nyu': '-73.96, 40.78, 2mi',
                'dc': '-77.04, 38.91, 2mi',
                'sf': '-122.45, 37.74, 5km',
                'nb': '-74.45, 40.49, 2mi'}
    # Maximum allowed tweet count (note: Twitter sets this to ~180 per 15 minutes)
    cmax = 50
    # OAuth key file
    authfile = './auth.k'

    tw_parser()
    api = tw_oauth(authfile)
    tw_search(api)

if __name__ == "__main__":
    main()
