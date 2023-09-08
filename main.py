from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Request, BackgroundTasks
from datetime import datetime
from utils.email import Email


app = FastAPI()


def send_email(subject, content):
    Email().send(subject, content)

@app.post("/webhook")
async def root(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()


    ## When adding a new webhook, Monday.com sends a challenge parameter
    ## to verify the endpoint. The endpoint must return the challenge
    if data.get("challenge"):
        return data

    item_name = data.get("event", {}).get("pulseName", "No pulse name")
    previous_status = data.get("event", {}).get("previousValue", {}).get("label", {}).get("text", "No label name")
    current_status = data.get("event", {}).get("value", {}).get("label", {}).get("text", "No label name")
    
    ## convert the date time to a human readable format
    timestamp_str = data.get("event", {}).get("triggerTime", None)
    timeline = None
    if timestamp_str:
        timestamp = datetime.fromisoformat(timestamp_str[:-1])
        timeline = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    ## I can not able to get this flat booked value from my webhook
    flat_booked = None

    subject = f"Item Name: {item_name} has changed status"

    content = f"""
    <h1>Item Name: {item_name}</h1>
    <p>Previous Status: {previous_status}</p>
    <p>Current Status: {current_status}</p>
    <p>Timeline: {timeline}</p>
    <p>Flat Booked: {flat_booked}</p>
    """

    background_tasks.add_task(send_email, subject, content)
    return {"message": "Request received"}
