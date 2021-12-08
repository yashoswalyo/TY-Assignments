#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 7777
#define WINDOW 2
int main(int argc, char const *argv[])
{
	int server_fd, new_socket, valread;
	struct sockaddr_in address;
	socklen_t add_len = sizeof(address);
	char buffer[128] = "123456";
	char response[2] = {0};
	int counter = 0;
	// Creating socket file descriptor
	server_fd = socket(AF_INET, SOCK_STREAM, 0);
	// Setting up the configuration
	address.sin_family = AF_INET;
	address.sin_addr.s_addr = INADDR_ANY;
	address.sin_port = htons(PORT);
	// Forcefully attaching socket to the port 8080
	bind(server_fd, (struct sockaddr *)&address, add_len);
	listen(server_fd, 1);
	new_socket = accept(server_fd, (struct sockaddr *)&address, &add_len);
	if (new_socket == -1)
	{
		perror("Error connecting to client");
		exit(EXIT_FAILURE);
	}
	while (counter < strlen(buffer))
	{
		printf("Sending %c%c\n", buffer[counter], buffer[counter + 1]);
		send(new_socket, buffer + counter, WINDOW, 0);
		read(new_socket, response, 1);
		if (response[0] == '0')
		{
			printf("Received negative acknowledgedment\n");
		}
		else
		{
			printf("Received Positive acknowledgement %c\n", response[0]);
			counter += 2;
		}
	}
	return 0;
}
