function preventEmptyInput(inputs){
  for(let i=0; i<inputs.length; i++){
     if(!inputs[i].value.trim()){
         inputs[i].value = 'Required field';
         alert('hello');
     }
  }
}


let nextbtns = document.getElementsByClassName('next');

for(let i=0 ;i<nextbtns.length; i++){
   nextbtns[i].addEventListener('click', ()=>{
   console.log(`fieldset${i+1}`);
       preventEmptyInput(document.getElementById(`fieldset${i+1}`).getElementsByTagName('input'));


   })
}