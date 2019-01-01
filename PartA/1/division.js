function check(){
num=document.getElementById("number").value;
if(num == "")
{
alert("Enter a number");
}
else
{
x=num%3==0;
y=num%7==0;
if (x&&y) 
{
     document.getElementById('result').innerHTML = num + ' is divisible by 3 and 7';
            
}
else if (y)
{
      document.getElementById('result').innerHTML = num + ' is divisible by 7 and not divisible by 3';
}
else if (x)
{
      document.getElementById('result').innerHTML = num + ' is divisible by 3 and not divisible by 7';
}
else
{
     document.getElementById('result').innerHTML = num + ' is neither divisible by 3 and nor by 7';
}
}

}

