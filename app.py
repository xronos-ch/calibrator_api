from flask import Flask, request, jsonify, Response
import subprocess
import os
from urllib.parse import quote as url_quote

app = Flask(__name__)

@app.route('/run_calibrator', methods=['GET'])
def run_cpp_script():
    try:
        # Get query parameters
        b_param = request.args.get('b')
        s_param = request.args.get('s')

        # Build the command
        command = ['./calibrator']
        if b_param:
            command.extend(['-b', b_param])
        if (s_param):
            command.extend(['-s', s_param])

        # Change to the directory where the script and data are located
        script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bin/'))
        os.chdir(script_dir)

        # Log the command and working directory
        app.logger.info(f"Running command: {' '.join(command)} in {os.getcwd()}")

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Log the output
        app.logger.info(f"Command output: {result.stdout}")
        app.logger.info(f"Command error: {result.stderr}")

        # Return the result as JSON
        return Response(result.stdout, mimetype='application/json')

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()
