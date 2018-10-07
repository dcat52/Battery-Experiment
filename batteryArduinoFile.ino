float aref_voltage;

void setup()
{
  Serial.begin(9600);
  analogReference(EXTERNAL);
  aref_voltage = 2.000;
}

void loop()
{
  for(int index=0; index <= 5; index++) {
    
    int sensorValue = analogRead(index);
    
       double sensorValue2 = (sensorValue / 1024.0) * aref_voltage;
       
       Serial.print(index);
       Serial.print(", ");
       Serial.println(sensorValue2,5);
       
       delay(500);
    
  }
}
