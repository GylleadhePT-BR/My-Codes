
//Configurações de Portas do Arduino

//Sensor
const int TRIG = 13;
const int ECHO = 12;

//Demais componentes
const int ledRed = 3;
const int ledBlue = 4;
const int ledGreen = 5;
const int ledYellow = 6;
const int ledBrown = 7;

void setup() {
  Serial.begin(9600);
  
  // Configurações do Sensor
  pinMode(TRIG,OUTPUT);
  pinMode(ECHO,INPUT);
  
  // Configurações do LED
  pinMode(ledGreen, OUTPUT);
  pinMode(ledRed, OUTPUT);
  pinMode(ledBlue, OUTPUT);
  pinMode(ledBrown, OUTPUT);
  pinMode(ledYellow, OUTPUT);

}

void loop() {
  int distancia = sensor(TRIG,ECHO);

    if(distancia <= 50){
      digitalWrite(ledRed, HIGH);
    }
    if(distancia <=40){
      digitalWrite(ledBlue , HIGH);  
    }
    if(distancia <= 30){
      digitalWrite(ledGreen , HIGH);
    }
    if(distancia <= 20){
      digitalWrite(ledYellow , HIGH);
    }
    if(distancia <= 10){
      digitalWrite(ledBrown , HIGH);
    }
  delay(100);
}

int sensor(int pinotrig,int pinoecho){
  digitalWrite(pinotrig,LOW);
  delayMicroseconds(2);
  digitalWrite(pinotrig,HIGH);
  delayMicroseconds(10);
  digitalWrite(pinotrig,LOW);

  return pulseIn(pinoecho,HIGH)/58;
}
