from mycroft import FallbackSkill
import grpc
from . import sanjeev_pb2, sanjeev_pb2_grpc
#from . import sanjeev_pb2_grpc

class Retriever(object):

    def __init__(self):

        self.host = 'localhost'
        self.server_port = 46001

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.stub = sanjeev_pb2_grpc.SanjeevStub(self.channel)

    def get_response(self, prompt):
        request = sanjeev_pb2.Prompt(body=prompt)
        return self.stub.GetResponse(request).body
    

class Sanjeev(FallbackSkill):

    def __init__(self):
        super(Sanjeev, self).__init__(name='Sanjeev Fallback')
        self.retriever = Retriever()

    def initialize(self):
        self.register_fallback(self.handle_fallback, 90)

    def handle_fallback(self, message):
        utterance = message.data.get("utterance")
        response = self.retriever.get_response(utterance)
        self.speak(response)
        return True

    def shutdown(self):
        self.remove_fallback(self.handle_fallback)
        super(Sanjeev, self).shutdown()

def create_skill():
    return Sanjeev()

