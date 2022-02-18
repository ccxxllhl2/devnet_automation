import grpc
import arp_pb2
import arp_pb2_grpc

def run():
    connect = grpc.insecure_channel("localhost:10050")
    stub = arp_pb2_grpc.get_arpStub(channel=connect)
    response = stub.Get_Arp_Info(arp_pb2.arpRequest(username="yeslab", password="yeslab1234"))
    print("-------客户端接收到消息-------")
    print(response.arp_info)
    
if __name__ == "__main__":
    run()