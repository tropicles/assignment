from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        date = data['date']
        time = data['time']
        message = data['message']

        
        conn = sqlite3.connect("logs.db")
        cursor = conn.cursor()

        insert_query = "INSERT INTO logs (date, time, message) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (date, time, message))
        conn.commit()
        conn.close()

        print("Data inserted successfully.")
        return jsonify({"status": "success", "message": "Data inserted successfully"}), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)