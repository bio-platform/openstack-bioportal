from requests import get, post, put
from pprint import pprint
pprint(put("http://localhost:5000/").json())
pprint(post("http://localhost:5000/", json={"keyname": "abc",
                                            "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8/gLmsGBgpxqGUy1a4G+sXNRhSCbQgJXpOc1M6Zy/3EH0VsE+mGsFsb2dD4j/FRaSzw9oaKkCsSJn9caTVaPODSq9vV6qhMZyZxiCxB+qmcpsIOqg0XpoeXP/zzymYVATPtBMHFVkfcXaohEetzxUtxAtacYJdlIo9EyPRSfxpA+l3tpCEfWlqFWOIEdxjafagN4IUj//7SeCXo++QgnCngpiF0E6BLoVaOzLHJC+HLvzZmH8d3LiJm7RWHiKqf14VHtaNkbDxi7A+ckobW4jRPzVEUzn3kORfFN96dbovyziJmIOW8i+WzOGGYX/lPVL6FZ890oTExhuTWURefVZ"}).json())