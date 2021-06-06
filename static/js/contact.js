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
