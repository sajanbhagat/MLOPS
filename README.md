## I have dockerized the solution into 2 services 
   * ServerApp
   * UIApp

### Steps to set a demo of the assignment problem 

1. Extract the ML Ops Zip file 
2. Start a terminal inside the ML Ops Folder
3. Make changes in the `UIApp -> static -> server_mapping.js` file to update `server_ip` to the appropriate IP address
   depending upon where this image is to be built (for the local system update it to localhost)
   ```
   server_mapping = {
        "server_ip":"0.0.0.0", #your server IP
        "port": 8650
    }
3. docker build -t mlops_image:latest .
4. docker-compose up
5. Once the system is up 
    a) UI can be accessed at "<your_ip>:8651"
    b) Server can be accessed at "<your_ip>:8650/docs"
6. Follow the Word document shared across for greater details 

7. UI -> embedded in FlaskAPP (UIApp -> app.py)
8. ServerAPI -> embedded in FastAPI (Entry Point -> ServerAPP > server.py)

9. For running test cases on server API 
    * open the `env.json` file at `ServerApp/env.json`
    * change server_ip =  "127.0.0.1" # to your server IP

10. initiate a terminal inside the ServerApp folder and run this command 
    `pytest .\test_stringVectorization.py`
