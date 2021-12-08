#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#define PORT 7777
#define WINDOW 2
void main()
{
	int sock = socket(AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in address;
	char buffer[WINDOW + 1] = {0};
	char counter = 1;
	char response[5] = {0};
	address.sin_family = AF_INET;
	address.sin_port = htons(PORT);
	if (inet_pton(AF_INET, "127.0.0.1", &address.sin_addr) == -1)
	{
		perror("Invalid IP value");
		exit(EXIT_FAILURE);
	}
	if (connect(sock, (struct sockaddr *)&address, sizeof(address)))
	{
		perror("Error connecting to client");
		exit(EXIT_FAILURE);
	}
	while (counter < 7)
	{
		read(sock, buffer, WINDOW);
		printf("\nReceived %s\n", buffer);
		response[0] = 'y';
		if (response[0] == 'y')
		{
			counter += 2;
			printf("Sending acknowledgement %d\n", counter);
			sprintf(response, "%d", counter);
		}
		else
		{
			printf("Sending negative acknowledgement\n");
			sprintf(response, "%d", 0);
		}
		send(sock, response, 1, 0);
		getchar(); // to skip the \n
	}
}
