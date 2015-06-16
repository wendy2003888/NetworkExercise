#include <iostream>
#include <string>  
#include <netdb.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <netinet/ip.h> 
#include <arpa/inet.h>
#include <stdlib.h>     
#include <unistd.h>     
#include <sys/types.h>  
#include <sys/ipc.h>    
#include <sys/sem.h>
#include <sys/shm.h>
#include <cstring>
#include <stdio.h>
#include <dirent.h>
#include <errno.h>

#define SERVER_IP "127.0.0.1"
#define SERV_PORT 12345

const int SIZE = 1024;
char data[SIZE];

void client(){  
  
  
    int sockfd, recvbytes;  
    char buffer[SIZE];  
    struct hostent *host;  
    struct sockaddr_in serv_addr;  
  
    if (( sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {  
        perror("socket error!");  
        exit(1);  
    }  
    bzero(&serv_addr,sizeof(serv_addr));  
    serv_addr.sin_family = AF_INET;  
    serv_addr.sin_port  = htons(SERV_PORT);
    // serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_addr.s_addr = inet_addr(SERVER_IP);  //设置ip地址   

    if (connect(sockfd, (struct sockaddr *)&serv_addr,sizeof(struct sockaddr)) == -1) {  
        perror("connect error!");  
        exit(1);  
    }  

    printf("send:");  
    write(sockfd, data, sizeof(data));  
    if ((recvbytes = recv(sockfd, buffer, SIZE ,0)) == -1) {  
        perror("recv error!");  
        exit(1);  
    }  
  
    buffer[recvbytes] = '\0';  
    printf("Received: %s",buffer);  
    close(sockfd);  
}  

int main()  
{  
     
    fgets(data, sizeof(data), stdin);  
    client();
    return 0;  
}  
