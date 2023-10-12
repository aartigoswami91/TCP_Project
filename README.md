# TCP Server Client Connection


# Functinality
Application contains following steps

1. Read and Parse the SIP Registrations File:
2. Set Up the TCP Server:
3. Handle Client Connections and Lookup Requests:
4. Run the Server:

# Running the Application locally
1. Clone the reponsitory
git clone url
2. run the server
   python server.py
   <img width="969" alt="image" src="https://github.com/aartigoswami91/goto/assets/101053581/e42790ee-3225-4ede-85dd-864d65f081c2">

4. run client
   python client.py
4.it will show the confirmation message server has connected

<img width="969" alt="image" src="https://github.com/aartigoswami91/goto/assets/101053581/5bf44388-0f60-4e7b-86a7-a05148c42d17">
5. Next step ask user to enter AOR
6. If record matches with the given AOR, it will return the record related to the AOR otherwise server will return empty line.
7. server will close the connection if server does not recieve any request within 10 sec.

   
