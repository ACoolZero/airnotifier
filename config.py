# https = True
# httpscertfile = "/path/to/ssl/certificate.cert"
# httpskeyfile = "/path/to/ssl/server.key"

port = 8801

# mongouri = 'mongodb://root:pass@localhost:27017/'
mongouri = "mongodb://mongodb:27018/" # This is for quick use inside my Docker

passwordsalt = 'd2o0n1g2s0h3e1n1g'
cookiesecret = 'airnotifiercookiesecret'
debug = True

masterdb = "airnotifier"
collectionprefix = "obj_"
dbprefix = ""
appprefix = "app_"
# sentrydsn = "https://xxxxxxx@sentry.io/xxxxxxx"
