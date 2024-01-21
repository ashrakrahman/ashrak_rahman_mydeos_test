# server.py

from flask import Flask, request, jsonify
from threading import Thread
from lru_cache import LRUCache  # Import the LRUCache class library

app = Flask(__name__)


class GeoDistributedLRUCacheServer:
    def __init__(self, capacity, expiration_time_seconds, region):
        self.lru_cache = LRUCache(capacity, expiration_time_seconds)
        self.region = region

    def process_request(self, key, value):
        # Process the request and interact with the Geo Distributed LRU Cache
        if self.region == "us-east":
            # Additional logic for us-east region
            self.lru_cache.insert_to_us_east_database(key, value)
        elif self.region == "us-west":
            # Additional logic for us-west region
            self.lru_cache.insert_to_us_west_database(key, value)
        else:
            # Default logic for other regions
            self.lru_cache.insert(key, value)


# Cache capacity=2, Cache exiration time = 60 sec, current region = northamerica-northeast1-a
geo_cache_server = GeoDistributedLRUCacheServer(2, 60, "northamerica-northeast1-a")


@app.route("/insert", methods=["POST"])
def insert():
    data = request.get_json()
    key = data["key"]
    value = data["value"]

    # Process the request asynchronously to avoid blocking
    Thread(target=geo_cache_server.process_request, args=(key, value)).start()

    return jsonify(
        {
            "message": "Request received for key:"
            + str(key)
            + " and being processed asynchronously."
        }
    )


@app.route("/get", methods=["GET"])
def get():
    key = int(request.args.get("key"))
    result = geo_cache_server.lru_cache.get(key)
    return jsonify({"result": result})


@app.route("/get_list", methods=["GET"])
def get_list():
    result = geo_cache_server.lru_cache.get_list()
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=5000)
