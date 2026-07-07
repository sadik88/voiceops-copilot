def detect_alert(text):

    alerts = {

        "DBReplicationFailure": "DBReplicationFailure",

        "CertificateExpiry": "CertificateExpiry",

        "CpuPegging": "CpuPegging",

        "CallManagerDown": "CallManagerDown",

        "RISDataCollector": "RISDataCollector",

        "DRFBackupFailure": "DRFBackupFailure"

    }

    for alert in alerts:

        if alert.lower() in text.lower():

            return alerts[alert]

    return None