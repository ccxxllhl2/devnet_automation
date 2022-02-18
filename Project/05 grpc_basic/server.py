import grpc
import arp_pb2
import arp_pb2_grpc
from concurrent import futures

class do_it(arp_pb2_grpc.get_arpServicer):
    def __init__(self):
        self.username = "yeslab"
        self.password = "yeslab123"
        self.arp_data = "1.1.1.1 aaaa.bbbb.cccc"
        print("服务端已启动！")
        
    def Get_Arp_Info(self, request, context):
        if self.check_user(request.username, request.password):
            return arp_pb2.arpReply(arp_info=self.arp_data)
        else:
            print("认证失败")
            return arp_pb2.arpReply(arp_info="认证失败")
        
    def check_user(self, username, password):
        if (username == self.username) and (password == self.password):
            return True
        else:
            return False
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    arp_pb2_grpc.add_get_arpServicer_to_server(do_it(), server)
    server.add_insecure_port("localhost:10050")
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()