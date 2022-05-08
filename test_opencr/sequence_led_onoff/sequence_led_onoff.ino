//led가 한번에 켜졌다, 순차적으로 꺼지는 것을 무한 반복하는 코드
void setup() {
  // put your setup code here, to run once:
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // LED ON
  digitalWrite(22, HIGH);
  digitalWrite(23, HIGH);
  digitalWrite(24, HIGH);
  digitalWrite(25, HIGH);
  delay(1000);
  
  // LED OFF
  digitalWrite(22, 0);
  delay(1000);
  digitalWrite(23, 0);
  delay(1000);
  digitalWrite(24, 0);
  delay(1000);
  digitalWrite(25, 0);
  delay(1000);
}
