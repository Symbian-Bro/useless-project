int ldrpin = A3; //Code fails to compile when I remove this line. I have no idea why.
// Only A3 used inside the main code snippets
void setup(){
  pinMode(A3,INPUT);
  Serial.begin(9600);
}
void loop(){
  int x = analogRead(A3);
  Serial.println(x);
}
