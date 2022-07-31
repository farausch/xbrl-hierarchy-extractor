# xbrl-hierarchy-extractor

The XBRL hierarchy extractor receives a set of XBRL entities as nodes and returns their hierarchy in form of edges.

## Setup

This repository contains a Dockerfile for deploying the service. A ready-to-use deployment is also available (see example usage)

## Example Usage
`curl -X POST "https://xbrl-hierarchy-extractor-mtvfo2xgia-ey.a.run.app/hierarchy?" -H "Content-Type: application/json" -d '[{"id": 0, "label": "Summe Aktiva"}, {"id": 1, "label": "Anlagevermögen"}, {"id": 2, "label": "Umlaufvermögen"}, {"id": 3, "label": "Guthaben bei Kreditinstituten"}]'`
