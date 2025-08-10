int ldrpin = A3;
void setup(){
  pinMode(A3,INPUT);
  Serial.begin(9600);
}
void loop(){
  int x = analogRead(A3);
  Serial.println(x);
}
