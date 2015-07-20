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
}

void process(YunClient restClient) {
  
     String command = restClient.readStringUntil('\');
     Serial.println(">>>>>>>>>>"+command);
     if (command == "fullfw") {   
         fullfw(restClient);
     }
     else if (command == "back") {
         back(restClient);
     }
     else if (command == "turnright") {
         turnRight(restClient);
     }
     else if (command == "turnleft") {
         turnLeft(restClient);
     }
     else if(command == "stop") {
         getStop(restClient);
     }
     else {
         Serial.println("Command Not Found:" + command);
     }
}

void fullfw(YunClient client) {
}

void back(YunClient client) {
}

void turnRight(YunClient client){
}

void turnLeft(YunClient client) {
}

void getStop (YunClient client) {
}

