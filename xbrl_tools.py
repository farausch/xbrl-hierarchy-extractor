from flask import jsonify
from xbrl_resolution import XBRLResolution

class XBRLTools:

    def __init__(self):
        pass

    def extract_hierarchy(self, nodes, xbrl_entity_dict):
        xbrl_resolution = XBRLResolution()
        node_id2xbrl_id = {}
        edges = []
        for node in nodes:
            if not node["label"].replace(".", "").replace(",", "").isnumeric():
                xbrl_id = xbrl_resolution.get_xbrl_entity(node["label"], xbrl_entity_dict)
                for i in range(10):
                    xbrl_id = xbrl_id.replace("_" + str(i), "")
                node_id2xbrl_id[node["id"]] = xbrl_id
        for node_id_a, xbrl_id_a in node_id2xbrl_id.items():
            for node_id_b, xbrl_id_b in node_id2xbrl_id.items():
                has_intermediate_child = False
                for node_id_c, xbrl_id_c in node_id2xbrl_id.items():
                    # No item in between the two candidates which is also a child
                    if len(xbrl_id_c.split(".")) > len(xbrl_id_b.split(".")) and len(xbrl_id_c.split(".")) < len(xbrl_id_a.split(".")) and xbrl_id_c.startswith(xbrl_id_b):
                        has_intermediate_child = True
                if not has_intermediate_child:
                    if xbrl_id_a.startswith(xbrl_id_b) and len(xbrl_id_a.split(".")) > len(xbrl_id_b.split(".")):
                        edges.append({"from": node_id_b, "to": node_id_a, "label": "has_child"})
        print(edges)
        return jsonify(edges)