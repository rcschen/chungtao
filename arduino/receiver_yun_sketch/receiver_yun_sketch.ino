#include <Wire.h>
#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
//#include <iostream>
//#include <vector>

//using namespace std;
YunServer restServer;
int wireAddress = 4;
const int fullFactorValue = 100;

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
     //Serial.println("----");
}

void process(YunClient restClient) {
  
     String command = restClient.readStringUntil('/');
     Serial.println(">>>>>>>>>>"+command);
     if (command == "fullfw") {  
      Serial.println("fffffff"); 
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

void sendControl(int control[]) {
    Wire.beginTransmission(wireAddress);
    Serial.print(control[0]);
    Serial.print(control[1]);
    Serial.print(control[2]);
    Serial.println(control[3]);
    Serial.println("-------------");
    Wire.write(control[0]);
    Wire.write(",");
    Wire.write(control[1]);
    Wire.write(",");
    Wire.write(control[2]);
    Wire.write(",");
    Wire.write(control[3]);
   Wire.endTransmission();
}

void fullfw(YunClient client) {
    String para = client.readStringUntil('\n');
    float factor = para.toFloat();
    int control[4];
    control[0] = 1;
    control[1] = fullFactorValue*factor ;
    control[2] = 0;
    control[3] = fullFactorValue*factor;
    sendControl(control);
}

void back(YunClient client) {
    String para = client.readStringUntil('\n');
    float factor = para.toFloat();
    int control[4];
    control[0] = 0;
    control[1] = fullFactorValue*factor ;
    control[2] = 1;
    control[3] = fullFactorValue*factor;
    sendControl(control);
}

void turnRight(YunClient client){
    String para = client.readStringUntil('\n');
    float factor = para.toFloat();
    int control[4];
    control[0] = 1;
    control[1] = fullFactorValue*factor ;
    control[2] = 0;
    control[3] = fullFactorValue;
    sendControl(control);
}

void turnLeft(YunClient client) {
    String para = client.readStringUntil('\n');
    float factor = para.toFloat();
    int control[4];
    control[0] = 1;
    control[1] = fullFactorValue;
    control[2] = 0;
    control[3] = fullFactorValue*factor;
    sendControl(control);
}

void getStop (YunClient client) {
     String para = client.readStringUntil('\n');
    float factor = para.toFloat();
    int control[4];
    control[0] = 0;
    control[1] = 0;
    control[2] = 0;
    control[3] = 0;
    sendControl(control);
}







