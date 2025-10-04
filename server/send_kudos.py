from database import Kudos, db
import time
from main import app


@app.post("/kudos")
async def send_kudos(kudos: dict):
    try:
        k = Kudos(
            len(db),
            kudos["author"],
            kudos["message"],
            time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            0,
        )
        db.append(k)
    except Exception as e:
        print(f"Error saving kudos: {e}")
    return {"status": "201 Created", "kudos": k}
