async function homedata(){
    
const data= { method:'GET',
                
  
 
	 headers:{
	   'Content-Type':'application/json',
        Authorization: 'Bearer ' + sessionStorage.getItem("user_token")
	   
	 },
	   
	 }
   
	const res= await  fetch('http://127.0.0.1:7002/company_register/',data)
	 .then((res)=> {
		  
	   console.log(res.statusText)
	   if(res.statusText=="Forbidden")
	   {
		document.getElementById("message").innerHTML="username or password is wrong"; 
	   }
	   if (!res.ok){
		throw Error(res.statusText)
	  }
	   return res.json()
	   }).then((data)=> {
		   console.log(data);
           document.getElementById('company_name').innerHTML=data.company_name;
	   }).catch((e)=>{
		  {
			 console.log(e) 
			
		  }
	   });


    }
   homedata()
var frame = document.getElementById("frame");

var profilebutton = document.getElementById("companyProfile");
var addproject=document.getElementById("addproject")

profilebutton.addEventListener("click",link1)
addproject.addEventListener("click",link2)

function link1(){
    console.log("run")
  frame.src="companyprofileform.html"
}
function link2(){
  frame.src="addprojectform.html"
}
function link3(){
  frame.src="https://pixabay.com/photo-3114729/"
}