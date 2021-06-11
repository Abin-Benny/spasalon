function submitmessage()
    {
        if(document.contact.fname.value=="")
        {
            document.getElementById("lfname").innerHTML="Enter Your First Name";
            return false;
        }
        else
            document.getElementById("lfname").innerHTML="";

         if(document.contact.lname.value=="")
        {
            document.getElementById("llname").innerHTML="Enter Your Last Name";
            return false;
        }
        else
            document.getElementById("llname").innerHTML="";


        if(document.contact.email.value=="")
        {
            document.getElementById("lemail").innerHTML="Enter Email ID";
            return false;
        }
        else
        {
            document.getElementById("lemail").innerHTML="";
            var mailformat = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
            if(document.contact.email.value.match(mailformat))
                document.getElementById("lemail").innerHTML="";
            else
            {
                document.getElementById("lemail").innerHTML="Invalid Email";
                return false;
            }
        }


        if(document.contact.subject.value=="")
        {
            document.getElementById("lsubject").innerHTML="Enter Subject";
            return false;
        }
        else
            document.getElementById("lsubject").innerHTML="";
        if(document.contact.message.value=="")
        {
            document.getElementById("lmessage").innerHTML="Enter Message";
            return false;
        }
        else
            document.getElementById("lmessage").innerHTML="";
    }


/*User Registration Validation*/

function register()
    {
        if(document.contact.fname.value=="")
        {
            document.getElementById("lfname").innerHTML="Enter Your First Name";
            return false;
        }
        else
        {
            var regName = /^[a-zA-Z]+$/;
            if(document.contact.fname.value.match(regName))
                 document.getElementById("lfname").innerHTML="";
            else
            {
                document.getElementById("lfname").innerHTML="Inavalid Name";
                return false;
            }
        }
        if(document.contact.lname.value=="")
        {
            document.getElementById("llname").innerHTML="Enter Your Last Name";
            return false;
        }
        else
           {
            var regName = /^[a-zA-Z]+$/;
            if(document.contact.lname.value.match(regName))
                 document.getElementById("llname").innerHTML="";
            else
            {
                document.getElementById("llname").innerHTML="Inavalid Name";
                return false;
            }
        }
        if(document.contact.email.value=="")
        {
            document.getElementById("lemail").innerHTML="Enter Email ID";
            return false;
        }
        else
        {
            document.getElementById("lemail").innerHTML="";
            var mailformat = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
            if(document.contact.email.value.match(mailformat))
                document.getElementById("lemail").innerHTML="";
            else
            {
                document.getElementById("lemail").innerHTML="Invalid Email";
                return false;
            }
        }
        if(document.contact.pass.value=="")
        {
            document.getElementById("lpass").innerHTML="Enter Password";
            return false;
        }
        else
        {
            var pregexp=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
            if(document.contact.pass.value.match(pregexp))
                   document.getElementById("lpass").innerHTML="";
            else
            {
                   document.getElementById("lpass").innerHTML="Contains eight characters,upper&lowercase letter,digit&special characters";
                   return false;
            }
        }
        if(document.contact.cpass.value=="")
        {
            document.getElementById("lcpass").innerHTML="Enter Password";
            return false;
        }
        else
        {
            document.getElementById("lcpass").innerHTML="";
            if(document.contact.pass.value!=document.contact.cpass.value)
           {
                document.getElementById("lcpass").innerHTML="Password Mismatch";
                return false;
           }
           else
                document.getElementById("lcpass").innerHTML="";
        }
        if(document.contact.mobile.value=="")
        {
            document.getElementById("lmob").innerHTML="Enter Your Mobile Number";
            return false;
        }
        else
        {
            var phoneno = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
            if(document.contact.mobile.value.match(phoneno))
                document.getElementById("lmob").innerHTML="";
            else
            {
                document.getElementById("lmob").innerHTML="Invalid Mobile Number";
                return false;
            }
        }
        if(document.contact.address.value=="")
        {
            document.getElementById("laddress").innerHTML="Enter Your Address";
            return false;
        }
        else
            document.getElementById("laddress").innerHTML="";
    }

