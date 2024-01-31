import os
import multiprocessing

mode = os.environ.get("MODE", "development")
host = os.environ.get("HOST", "localhost")
port = os.environ.get("PORT", "9000")

FUSIONAUTH_BASE_URL = os.environ.get(
    "FUSIONAUTH_BASE_URL", "http://localhost:9011"
)
FUSIONAUTH_CLIENT_ID = os.environ.get(
    "FUSIONAUTH_CLIENT_ID", "6e4e9805-9690-476f-a7d8-2552992c41e1"
)
FUSIONAUTH_CLIENT_SECRET = os.environ.get(
    "FUSIONAUTH_CLIENT_SECRET", "ZyYv1MrS4XjCZKMu0YShVXsGbXoHw57pkXNBcSukY48"
)


def number_of_workers():
    return multiprocessing.cpu_count()


config = {
    "mode": mode,
    "host": host,
    "port": port,
    'bind': '%s:%s' % (host, port),
    'workers': number_of_workers(),
}
