
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

int num1,num2;

void loop() {
 while (!Serial.available());
 num1, num2 = Serial.readString().toInt();
 if ((num1 >= 20)||(num2 >= 20)){
  Serial.println(num1 + num2);
 } else {
  Serial.println(num1 - num2);
 }
}
