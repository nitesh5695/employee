console.log("javascript run");
document.getElementById('submit').addEventListener('click',check2);
//  function register() {
//   let email=document.getElementById('email').value
//   let name=document.getElementById('name').value
//   let password=document.getElementById('password').value
 
//   const data= {
//     email:email,
//    company_name:name,
//     password:password
// } 
//   const Header= {
//     headers:{
//       Authorization: 'Bearer ' + "uyguyguy"
//                 }
//  }            
              
//   axios.post('http://127.0.0.1:7002/company_register/',data,Header)
//     .then((res)=>{
//       console.log(res)
//       document.getElementById("message").innerHTML=res.data.email;
//       if (!res.ok){
//           throw Error(res.statusText)
//       }
//     }).then((data)=>{
//          console.log(data)
//       }) .catch((error)=>console.log(error))

// }

// function check() {
// data={

// 	password:"nit123",
// 	company_name:"infosys",
// 	email:"prince.singh@gmail.com"
// }

  
//   axios.get('http://127.0.0.1:7002/company_profile/')
//     .then(function (response) {
//       console.log(response);
//     })
//     .catch(function (error) {
//       console.log(error);
//     });   
// }
function check2(){
  let email=document.getElementById('email').value
  let name=document.getElementById('name').value
  let password=document.getElementById('password').value
  const testURL = 'http://127.0.0.1:7002/company_register/';
  const data= { method:'POST',
                
  
 
  headers:{
    'Content-Type':'application/json',
    
  },
    body:JSON.stringify({email:email,company_name:name,password:password})
  }

	fetch('http://127.0.0.1:7002/company_register/',data)
  .then((response)=> {
		if (!response.ok){
      throw Error(res.statusText)
    }
    return response.json()
	}).then((data)=> {
    document.getElementById("message").innerHTML=data.email;
		console.log(data);
	}).catch((e)=>{
		console.log(e);
	});
}