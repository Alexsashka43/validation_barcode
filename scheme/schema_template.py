schema = {
    "type": "object",
    "properties": {
        "PN": {"type": "string"},
        "DESCRIPTION": {"type": "string"},
        "LOCATION": {"type": "integer"},
        "RECEIVER": {"type": "integer"},
        "EXP_DATE": {"type": "string", "format": "date"},
        "CERT_SOURCE": {"type": "string"},
        "SN": {"type": "integer"},
        "CONDITION": {"type": "string"},
        "UOM": {"type": "string"},
        "PO": {"type": "string"},
        "REC_DATE": {"type": "string", "format": "date"},
        "MFG": {"type": "string"},
        "BATCH": {"type": "integer"},
        "DOM": {"type": "string", "format": "date"},
        "REMARK": {"type": "string"},
        "LOT": {"type": "integer"},
        "TAGGED_BY": {"type": "string"},
        "Qty": {"type": "integer"},
        "NOTES": {"type": "string"},
    },
    "required": [
        "PN", "DESCRIPTION", "LOCATION", "RECEIVER", "EXP_DATE", "CERT_SOURCE",
        "SN", "CONDITION", "UOM", "PO", "REC_DATE", "MFG", "BATCH", "DOM", "LOT", "Qty", "NOTES"
    ]
}


