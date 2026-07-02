# You’re building an API for a simple event management system. The API should:

# Allow users to add a new event with a POST request to /events.
# Let users update an existing event title via PATCH to /events/<id>.
# Enable users to remove an event by sending a DELETE to /events/<id>.
# The API should respond with structured JSON and appropriate HTTP status codes.

# Use @app.route() decorators with the appropriate methods argument.
# Accept and handle JSON data in the request body using request.get_json().
# Simulate data persistence using an in-memory list of Event objects.
# Format all output with jsonify() and include helpful error messages.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated date
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

@app.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    event = next((e for e in events if e.id == id), None)
    return jsonify(event.to_dict()) if event else ("Event not found", 404)


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())


@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    global events
    event = next((e for e in events if e.id == id), None)
    

if __name__ == "__main__":
    app.run(debug=True)
