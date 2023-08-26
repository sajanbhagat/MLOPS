### I have dockerized the solution into 2 services 
###     a. ServerApp
###     b. UIApp

Steps to setup a demo of the assignment problem 

1. extract the ML Ops Zip file 
2. start a terminal inside the ML Ops Folder
3. make the changes in `UIApp -> static -> server_mapping.js` file to update server_ip to appropriate address
   depending upon where this image is built (for local system update it to localhost)
    server_mapping = {
        "server_ip":"0.0.0.0", #your server ip
        "port": 8650
    }
3. docker build -t mlops_image:latest .
4. docker-compose up
5. once system is up 
    a) UI can be accessed at "<your_ip>:8651"
    b) Server can be accessed at "<your_ip>:8650/docs"
6. follow the word document shared across for greater details 

7. UI -> embedded in FlaskAPP (UIApp -> app.py)
8. ServerAPI -> embedded in FastAPI (Entry Point -> ServerAPP > server.py)

9. for testing the server API 
    * open env.json file at ServerApp/env.json
    * change server_ip =  "127.0.0.1" # to your server ip

10. initiate a terminal inside ServerApp folder and run this command 
    `pytest .\test_stringVectorization.py`
