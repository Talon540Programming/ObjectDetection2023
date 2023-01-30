import cv2, socket, numpy, pickle
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip="10.171.50.31"
port=6666
s.bind((ip,port))
print('binded')
while True:
    x=s.recvfrom(224*224*3)
    print('recieved')
    clientip = x[1][0]
    data=x[0]
    print(data)
    data=pickle.loads(data)
    print('data loaded')
    print(type(data))
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    print('decoded')
    cv2.imshow('server', data) #to open image
    if cv2.waitKey(10) == 'q':
        break
cv2.destroyAllWindows()