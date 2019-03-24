/*
  Arduino BLE Shield (HM-10) Testing Sketch
  by JP Liew http://jpliew.com
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <SoftwareSerial.h>

#define BUFFER_LENGTH 100

SoftwareSerial ble(2,3);  // For Uno, HM10 TX pin to Arduino Uno pin D2, HM10 RX pin to Arduino Uno pin D3
//SoftwareSerial ble(10,11);  // For Mega 2560, HM10 TX pin to Arduino Mega 2650 pin D10, HM10 RX pin to Arduino Mega 2560 pin D11

char buffer[BUFFER_LENGTH]; // Buffer to store response
int timeout=800;    // Wait 800ms each time for BLE to response, depending on your application, adjust this value accordingly
long bauds[] = {9600,57600,115200,38400,2400,4800,19200}; // common baud rates, when using HM-10 module with SoftwareSerial, try not to go over 57600

long BLEAutoBaud() {
  int baudcount=sizeof(bauds)/sizeof(long);
  for(int i=0; i<baudcount; i++) {
    for(int x=0; x<3; x++) {  // test at least 3 times for each baud
      Serial.print("Testing baud ");
      Serial.println(bauds[i]);
      ble.begin(bauds[i]);
      if (BLEIsReady()) {
        return bauds[i];
      }
    }
  }
  return -1;
}
      
boolean BLEIsReady() {
  BLECmd(timeout, "AT" ,buffer);    // Send AT and store response to buffer 
  if (strcmp(buffer,"OK")==0){    
    return true;
  } else {
    return false;
  }  
}

boolean BLECmd(long timeout, char* command, char* temp) {
  long endtime;
  boolean found=false;
  endtime=millis()+timeout;   // 
  memset(temp,0,BUFFER_LENGTH);   // clear buffer
  found=true;
  Serial.print("Arduino send = ");
  Serial.println(command);
  ble.print(command);
  
  // The loop below wait till either a response is received or timeout
  // The problem with this BLE Shield is the HM-10 module does not response with CR LF at the end of the response,
  // so a timeout is required to detect end of response and also prevent the loop locking up.

  while(!ble.available()){
    if(millis()>endtime) {      // timeout, break
      found=false;
      break;
    }
  }  

  if (found) {          // response is available
    int i=0;
    while(ble.available()) {    // loop and read the data
      char a=ble.read();
      // Serial.print((char)a); // Uncomment this to see raw data from BLE
      temp[i]=a;      // save data to buffer
      i++;
      if (i>=BUFFER_LENGTH) break;  // prevent buffer overflow, need to break
      delay(1);     // give it a 2ms delay before reading next character
    }
    Serial.print("BLE reply    = ");
    Serial.println(temp);
    return true;
  } else {
    Serial.println("BLE timeout!");
    return false;
  }
}

void setup() {
  Serial.begin(9600); 

  pinMode(13, OUTPUT);
  digitalWrite(13,LOW);

  // If you see lots of BLE timeout on Serial Monitor after BLEAutoBaud completed, most likely your have a bad shield
  // Check if the shield JUMPER is correctly set to 
  // HM10 TX to D2
  // HM10 RX to D3
  long baudrate = BLEAutoBaud();

  if (baudrate>0) {
    Serial.print("Found BLE baud rate ");
    Serial.println(baudrate);
  } else {
    Serial.println("No BLE detected.");
    while(1){};     // No BLE found, just going to stop here
  }

  // The following commands are just to demonstrate the shield is working properly,
  // in actual application, only call those that are needed by your application.
  // Check HM-10 datasheet for the description of the commands.
  //BLECmd(timeout,"AT+RENEW",buffer);
  BLECmd(timeout,"AT+NAME?",buffer);
  BLECmd(timeout,"AT+BAUD?",buffer);
  BLECmd(timeout,"AT+MODE?",buffer);
  BLECmd(timeout,"AT+PASS?",buffer);
  BLECmd(timeout,"AT+VERS?",buffer);
  BLECmd(timeout,"AT+RADD?",buffer);
  BLECmd(timeout,"AT+ADDR?",buffer);
  BLECmd(timeout,"AT+TYPE?",buffer);
  BLECmd(timeout,"AT+POWE?",buffer);
  BLECmd(timeout,"AT+SHOW1",buffer);
  BLECmd(timeout,"AT+NOTI1",buffer);
  //BLECmd(timeout,"AT+FILT?",buffer);
  //BLECmd(timeout,"AT+ROLE1",buffer);
  //BLECmd(timeout,"AT+IMME1",buffer);
  //BLECmd(timeout,"AT+DISC?",buffer);
  Serial.println("----------------------");
  Serial.println("Waiting for remote connection...");
}

void loop() {
  if (ble.available()) {
    char c =(char)ble.read();
    Serial.print(c);
    if (c=='1') digitalWrite(13,HIGH);    // if received character 1 from BLE, set PIN 13 high
    if (c=='0') digitalWrite(13,LOW);   // if received character 0 from BLE, set PIN 13 low
  }  
}
