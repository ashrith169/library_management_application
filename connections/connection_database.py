from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'connections/secure-connect-library-management.zip'
}
auth_provider = PlainTextAuthProvider('sDBPmTAyaABQmABZhoIZeTfs', 'XwFQBZwDgLMe2pgA0Onr1ipCxNo9kqfl_BqmQhd2LKvb3dlBciIeTDq2_ZwI3HOf5gesbsMQlrqrf4pJHWAjK2.WS.2D7CY77dDjY9jc-2K-2xkNdZHM8lZtINMZ-pTP')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()

#if row:
 #   print(row[0])
#else:
    #print("An error occurred.")