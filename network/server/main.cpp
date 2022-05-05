#include<iostream>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

using namespace std;


#pragma comment(lib, "Ws2_32.lib")
#define DEFAULT_PORT "27015"


int main() {

	WSADATA wsaData;
	int iResult;
	iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
	if (iResult != 0) {
		cout << "WSAStartup failed:" << iResult <<endl;
		return 1;
	}


	typedef struct addrinfo
	{
		int                 ai_flags;       // AI_PASSIVE, AI_CANONNAME, AI_NUMERICHOST
		int                 ai_family;      // PF_xxx
		int                 ai_socktype;    // SOCK_xxx
		int                 ai_protocol;    // 0 or IPPROTO_xxx for IPv4 and IPv6
		size_t              ai_addrlen;     // Length of ai_addr
		char* ai_canonname;   // Canonical name for nodename
		_Field_size_bytes_(ai_addrlen) struct sockaddr* ai_addr;        // Binary address
		struct addrinfo* ai_next;        // Next structure in linked list
	}

	struct addrinfo* result = NULL, * ptr = NULL, hints;

	ZeroMemory(&hints, sizeof(hints));
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_protocol = IPPROTO_TCP;
	hints.ai_flags = AI_PASSIVE;

	// Resolve the local address and port to be used by the server
	iResult = getaddrinfo(NULL, DEFAULT_PORT, &hints, &result);
	if (iResult != 0) {
		std::cout << "getaddrinfo failed: " << iResult << std::endl;
		WSACleanup();
		return 1;
	}


	SOCKET ListenSocket = INVALID_SOCKET;
	// Create a SOCKET for the server to listen for client connections

	ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
	if (ListenSocket == INVALID_SOCKET) {
		std::cout << "Error at socket(): " << WSAGetLastError() << std::endl;
		freeaddrinfo(result);
		WSACleanup();
		return 1;
	}
	return 0;
}