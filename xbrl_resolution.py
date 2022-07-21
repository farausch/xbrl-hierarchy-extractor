from bs4 import BeautifulSoup
from Levenshtein import distance as levenshtein_distance

class XBRLResolution:

    def __init__(self):
        pass

    def get_all_xbrl_entities(self, label_file):
        entity_dict = {}
        with open(label_file) as f:
            soup = BeautifulSoup(f, "lxml")
        for tag in soup.find_all(name="label"):
            if not "documentation" in tag["xlink:role"]:
                entity_dict[tag["id"].split("label_de-gaap-ci_")[1]] = tag.text
        return entity_dict

    def get_xbrl_entity(self, label_text, xbrl_entities):
        closest_match = ""
        closest_distance = 1000
        for xbrl_id, xbrl_entity in xbrl_entities.items():
            distance = levenshtein_distance(label_text, xbrl_entity)
            if distance < closest_distance:
                closest_match = xbrl_id
                closest_distance = distance
        return closest_match