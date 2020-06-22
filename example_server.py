import socketserver
import json
import base64

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        self.data = json.loads(self.data)

        if 'PlateDetectedEvent' in self.data:
            if 'VehicleImage' in self.data['PlateDetectedEvent']:
                with open(f"images/{self.data['PlateDetectedEvent']['Date']}{self.data['PlateDetectedEvent']['Time']}-{self.data['PlateDetectedEvent']['PlateNumber']}-vehicle.jpg", "wb") as fh:
                    fh.write(base64.decodebytes(str.encode(self.data['PlateDetectedEvent']['VehicleImage'])))
            if 'PlateImage' in self.data['PlateDetectedEvent']:
                with open(f"images/{self.data['PlateDetectedEvent']['Date']}{self.data['PlateDetectedEvent']['Time']}-{self.data['PlateDetectedEvent']['PlateNumber']}-plate.jpg", "wb") as fh:
                    fh.write(base64.decodebytes(str.encode(self.data['PlateDetectedEvent']['PlateImage'])))




if __name__ == "__main__":
    HOST, PORT = "157.230.222.187", 5999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
