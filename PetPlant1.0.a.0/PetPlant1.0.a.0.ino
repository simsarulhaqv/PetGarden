int t=0,h=0,m=0;
float t0,t1,h0,h1,m0,m1;
  
String val,c;

void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop()
{
  while(1)
  {
    getdata();
  
    serial();
    if (time>0)
    {
      digitalWrite(2,HIGH);  
      --time;
    }
    else
      digitalWrite(2,LOW);

   
  }   
}

void serial()
{
  while(Serial.available())
    {
      int x;
      if(Serial.read()=='x')
      {  
        x=0;
        time = Serial.parseInt();
        
        char y = (char)Serial.read();
        if (y=='y')
          break;
      
      }
      time=0;
     
    }
}

void getdata()
{
  while (1)
    {
      m0= analogRead(A0);
      t0=analogRead(A1);
      h0=analogRead(A2);
      delay(100);
      m1= analogRead(A0);
      h1= analogRead(A1);
      t1= analogRead(A2);
      if((m0-m0*.1)<m1<(m0+m0*.1)||(h0-h0*.1)<h10<(h0+h0*.1)||(t0-t0*.1)<t1<(t0+t0*.1))
        break;
    }
}

void sent()
{
  t=(t0+t1)/2;
  h=(h0+h1)/2;
  m=(m0+m1)/2;
 
  val = String();
  c = String("t");
  val=c+s;  c = val;  val=c+'m';  c=val;  val=c+s0;  c=val;
  val=c+'h';  c=val;  val=c+s1;  c=val;  val=c+'f';
  Serial.println(val);
}
