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

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome to the Event Management API!"}), 200


@app.route("/events", methods=["GET", "POST"])
def handle_events():
    if request.method == "GET":
        return jsonify([event.to_dict() for event in events]), 200

    if request.method == "POST":

        data = request.get_json()
        
        if not data or "title" not in data:
            return jsonify({"error": "Missing 'title' in request body"}), 400

        
        
        new_id = events[-1].id + 1 if events else 1
        new_event = Event(id=new_id, title=data["title"])
        events.append(new_event)
        return jsonify(new_event.to_dict()), 201



@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    
    data = request.get_json()
    
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            
            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

if __name__ == "__main__":
    app.run(debug=True)
