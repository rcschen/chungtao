#include <Wire.h>
#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>

YunServer restServer;

void setup() {
     Wire.begin();
     Bridge.begin();
     Serial.begin(9600);
     restServer.listenOnLocalhost();
     restServer.begin();
}

void loop() {
     YunClient restClient = restServer.accept();
     if (restClient) {
          process(restClient);
          restClient.stop();
     }
     delay(50); 
     Serial.println("----------");
}

void process(YunClient restClient) {
  
     String command = restClient.readStringUntil('/');
     Serial.println(">>>>>>>>>>"+command);
     if (command == "robot") {   
        //robotCommand(client);
     }
}


