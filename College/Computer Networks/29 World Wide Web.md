Links: [[27 Application Layer]], [[28 Domain Name System]]
___
# The World Wide Web (WWW)
The World Wide Web is an architectural framework for accessing linked documents spread across thousands of servers over the internet.

### Web Architecture
The WWW operates strictly on a Client-Server architecture, relying on specific components to function.

#### The Client
The client is the user's local machine (e.g., a smartphone or laptop) that initiates communication. It relies on a specific piece of software to interact with the web:

##### User Agent
The actual software application running on the client that makes the network requests. While a **Web Browser** (Chrome, Firefox, Safari) is the most common User Agent, it is not the only one. 

Automated bots (like the Google Search crawler), command-line tools (like `curl` or `wget`), and mobile apps fetching API data are all considered User Agents. 

The User Agent is responsible for parsing the server's response and rendering it into a format the user can understand.

#### The Server
A Web Server is a highly powerful, always-on machine with a fixed IP address.

- It constantly listens on specific ports: **Port 80** for unencrypted HTTP traffic and **Port 443** for encrypted HTTPS traffic.
- When a request arrives, the server software (like Apache or Nginx) locates the requested resource on its hard drive (or dynamically generates it via a database) and returns it to the client.

#### URI (Uniform Resource Identifier)
A URI is the standard global mechanism used to uniquely identify any resource (an image, an HTML page, a video) on the web. 
The most common form of a URI is a **URL (Uniform Resource Locator)**, which not only identifies the resource but also explicitly states *how* to locate it on the network.

A standard URL consists of several distinct parts. Here is a breakdown of a complex example URL:
`https://www.youtube.com/watch?v=TpYhbMIr4ZA&list=RDWPD-U0hlIy0&index=8`

[Click Here](https://www.youtube.com/watch?v=TpYhbMIr4ZA&list=RDWPD-U0hlIy0&index=8)

1. **Protocol (Scheme):** `https://`
   - Tells the browser to use HTTP securely encrypted with TLS.
2. **Host (Domain Name):** `www.youtube.com`
   - The human-readable name of the server being contacted.
3. **Port:** *(Implicit)* `:443`
   - Usually hidden by the browser, but defaults to 443 because the protocol is HTTPS.
4. **Path:** `/watch`
   - The specific resource or endpoint on the server being accessed.
5. **Query Parameters:** `?v=TpYhbMIr4ZA&list=RDWPD-U0hlIy0&index=8`
   - Extra variables passed to the server, starting with a `?`.
   - Multiple variables are strung together using the `&` symbol.
   - In this example, it passes the video ID (`v`), the playlist ID (`list`), and the track number (`index`).

## HTTP (HyperText Transfer Protocol)
HTTP is the foundational protocol used to fetch resources on the WWW. It is a **Client-Server**, **Stateless** protocol.
- **Stateless:** The server does not remember anything about previous requests. Every single request is treated as brand new. (This is exactly why "Cookies" were invented—to force the browser to send saved state data alongside every request).

### HTTP Messages
HTTP uses two primary types of messages: Requests and Responses.

#### HTTP Request
Sent by the client to request an action.
- **Request Line:** Contains the Method (`GET`, `POST`, `PUT`, `DELETE`), the URI (`/index.html`), and the HTTP Version (`HTTP/1.1`).
- **Headers:** Additional metadata (e.g., `Host: www.google.com`, `User-Agent: Mozilla/5.0`).
- **Body:** (Optional) Data being sent to the server (e.g., submitting a login form via `POST`).

#### HTTP Response
Sent by the server back to the client.
- **Status Line:** Contains the HTTP Version (`HTTP/1.1`), the Status Code (`200`, `404`, `500`), and a Status Message (`OK`, `Not Found`).
- **Headers:** Metadata about the response (e.g., `Content-Type: text/html`).
- **Body:** The actual requested resource (e.g., the raw HTML code of the webpage).

> [!NOTE] TCP Connections in WWW
> Modern HTTP/1.1 uses **Persistent Connections** by default. Instead of opening a new TCP 3-way handshake for every single image and CSS file on a webpage, the browser keeps a single TCP connection open and funnels multiple HTTP requests through the same pipe.
