var companyid ;
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
               document.getElementById('companyemail').value=data.email;
               document.getElementById('companyname').value=data.company_name;
               companyid=data.company_id;
           }).catch((e)=>{
              {
                 console.log(e) 
                
              }
           });
    
    
        }
       homedata()

       document.getElementById('submit').addEventListener('click',postdata)

async function postdata(){
    ceo_name= document.getElementById('ceo').value
    established_year= document.getElementById('established_year').value
    address= document.getElementById('address').value
    contact_no= document.getElementById('contact_no').value
    gst_no= document.getElementById('gst_no').value

    const data= { method:'POST',
                    
      
     
         headers:{
           'Content-Type':'application/json',
            Authorization: 'Bearer ' + sessionStorage.getItem("user_token")
           
         },
         body:JSON.stringify({company_id:companyid,ceo:ceo_name,established_year:established_year,address:address,contact_no:contact_no,gst_no:gst_no})
         }
       
        const res= await  fetch('http://127.0.0.1:7002/company_profile/',data)
         .then((res)=> {
            console.log(res.statusText)
           if(res.statusText=="Forbidden")
           {
            console.log('token expired') 
           }
           if (!res.ok){
            throw Error(res.statusText)
          }
           return res.json()
           }).then((data)=> {
               document.getElementById('message').innerHTML=data.message;
               console.log(data);
               
           }).catch((e)=>{
              {
                 console.log(e) 
                
              }
           });
}       
