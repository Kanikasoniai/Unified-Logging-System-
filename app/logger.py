
from datetime import datetime
from schema import LogSchema
from storage import save_log

def log_event(module, event, data):

    log = LogSchema(
        module=module,
        event=event,
        timestamp=datetime.utcnow().isoformat(),
        data=data
    )

    save_log(log.model_dump())
    print("Log Saved:", log.model_dump())