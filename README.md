# TCP Server Client Connection


# Functinality

Application contains following steps
<li>Server read the AOR record file</li>
<li>server can connect multiple file</li>
<li>client can request with AOR number and if number matches with the given AOR number then server return matched AOR data one at a time</li>
<li>If server does not receive any record within 10 sec then connect will get close.</li>

# Running the Application locally
1. Clone the reponsitory
   ```
   git clone https://github.com/aartigoswami91/goto
   ```

3. run the server
   ```
   python server.py
   ```
   
   <img width="969" alt="image" src="https://github.com/aartigoswami91/goto/assets/101053581/e42790ee-3225-4ede-85dd-864d65f081c2">

5. run client
   ```
      python client.py
   ```
   
4.it will show the confirmation message server has connected

<img width="969" alt="image" src="https://github.com/aartigoswami91/goto/assets/101053581/5bf44388-0f60-4e7b-86a7-a05148c42d17">

5. Next step ask user to enter AOR
   
7. If record matches with the given AOR, it will return the record related to the AOR otherwise server will return empty line.
   
8. server will close the connection if server does not recieve any request within 10 sec.

   
