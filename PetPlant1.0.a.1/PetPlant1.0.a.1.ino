
unsigned int t=00,m=00,h=00,l=00,w=0;
float t0,t1,m0,m1,h0,h1,l0,l1,w0,w1;
long i=0; // variable for seconds count
long time=0,minu=60;
String val,c;

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  for(i=0;i<2;i++)// i increments corresponds to each cycle ie for each econd
  {
    delay(990); //to get one second delay (approximately)
    getdata(); //taking reading

    if (time>0)
    {
      if(minu==0)
      {
        --time;
        minu=60;//60 sec for a minute
      }

      digitalWrite(13,HIGH);  
      --minu;
    }
    else
    {
      serial();  //checking data from pi
      minu=60;
      digitalWrite(13,LOW);
    }
  }
  sent(); // send data to pi for every five minutes approx.

}

void serial()
{
  while(Serial.available()) //reading a data sent b/w 'x' and 'y' from pi
  {
    if(Serial.read()=='x')  //checking starting ie 'x'
    {                 
      time = Serial.parseInt();  // reading integer in data in 
      // data sent is time to watering the plant in minutes
      char y = (char)Serial.read(); //checking ending ie 'y'
      Serial.println(time);
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
 m0= analogRead(A0);     //first samples
 t0=analogRead(A1);
 h0=analogRead(A2);
 l0=analogRead(A3);
 w0=analogRead(A4);
 delay(100);
 m1= analogRead(A0);    //second samples
 h1= analogRead(A1);
 t1= analogRead(A2);
 l1=analogRead(A3);
 w1=analogRead(A4);
 
 // checking for error in samples , ie sample1 may have only maximum of +/-5%
 if((m0-m0*.05)<m1<(m0+m0*.05)||(h0-h0*.05)<h1<(h0+h0*.05)||(t0-t0*.05)<t1<(t0+t0*.05)||(l0-l0*.05)<l1<(l0+l0*.05)||(w0-w0*.05)<w1<(w0+w0*.05))
 break;
 }
 
 t=(t0+t1)/2;  //taking average of samples
 h=(h0+h1)/2;
 m=(m0+m1)/2;
 l=(l0+l1)/2;
 w=(w0+w1)/2;
 
 // converting to rewuire scales
 //temp
 t=(t*500)/1024;
 //moisture
 m=m;
 //humidity
 h=h;
 //light 
 l=(l*100)/1024;
 //water requirement , ie leaf humidity.
 w=w;
 
 }
 
 void sent()
 {
 val = String();

 if(t<10)       //prefixing zero if variable is of single digit
   val+='0';
 while(t>99)   //if variable is of morethan 2 digit then scaling
   t/=10;
 val+=t;       //concatinating strings and variables
 Serial.println(val.length());

 if(m<10)
   val+='0';  
 while(m>99)
   m/=10;
 val+=m;
 Serial.println(val.length());

 if(h<10)
   val+='0';  
 while(h>99)
   h/=10;
 val+=h;
 Serial.println(val.length());

 if(l<10)
   val+='0';                     // concatinating aal datas to a string
 while(l>99)
   l/=10;
 val+=l;
 Serial.println(val.length());

 if(w<10)
   val+='0';    
 while(w>99)
   w/=10;
 val+=w;
 Serial.println(val.length());

 Serial.println(val);  // sent data to pi
 }
 
