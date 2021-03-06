import json
import pymongo
import sys
import hashlib
import os
import errno
from article import article
from bson.objectid import ObjectId

class PrintWriter(object):
    """Class for writing JSON data to the screen."""
    def __init__(self):
        pass

    def write(self, json_data):
        """Write a JSON serializable object to the screen.

        Arguments:
        json_data -- A JSON serializable object.
        """
        print json.dumps(json_data, indent=4, ensure_ascii=False)

class FileWriter(object):
    """Class for writing JSON data to a file."""

    def __init__(self):
        check_and_make_dir("./test_files/")



    def write(self, json_data):
        """Write a JSON serializable object to a file.

        Arguments:
        json_data -- A JSON serializable object.
        """
        filepath = "./test_files/" + hashlib.md5(json_data["title"]).hexdigest() + ".json"
        pretty_string = json.dumps(json_data, indent=4)
        with open(filepath, 'w') as output_file:
            output_file.write(pretty_string)

def check_and_make_dir(path):
    '''Makes dir with given path, unless if it already exists.'''
    try:
        os.mkdir(path)
    except OSError as e:
        pass

class MongoWriter():
    def __init__(self, host, port):
      self.m = pymongo.MongoClient(host, port)
      self.db = self.m.big_data

    def write(self, article, htmldata):
        try:
            htmlDict = {}
            articleDict = article.__dict__
            original_id = ObjectId()
            htmlDict[_id] = original_id
            htmlDict[data] = htmldata
            articleDict[htmlKey] = original_id

            self.db.articles.insert(articleDict)
            self.db.html.insert(htmlDict)
        except:
            print("Unexpected error:", sys.exc_info()[0])
