from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def route_main():
    add_new_request("POST")
    return 'Request counter'


def read_file():
    requests = {}
    with open('request_counts.txt') as file:
        for line in file:
            separators_index = line.find(":")
            requests[line[:separators_index]] = int(line[separators_index + 2:])
    return requests


def write_file(requests):
    with open('request_counts.txt', 'w') as file:
        for key, value in requests.items():
            file.write(key + ": " + str(value) + "\n")


def add_new_request(method):
    requests = read_file()
    requests[method] += 1
    write_file(requests)


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_request_counter():
    add_new_request(request.method)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
