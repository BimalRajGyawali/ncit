let inputs = document.getElementById(`fieldset${event.target.id}`).getElementsByTagName('input');

let len = inputs.length - event.target.id;   //removing buttons from length

 for(let i=0; i<len; i++){
    if(!inputs[i].value){
            inputs[i].focus();
            inputs[i].style.outline = '1px solid red';
            inputs[i].classList.add('error');
            inputs[i].addEventListener('keydown', ()=>{
                  inputs[i].style.outline = 0;
                  inputs[i].style.color = 'black';

                  inputs[i].classList.remove('error');

            });
         return false;
     }
  }
 if(event.target.id == 1){
        /* Confirm roll is a number */
let roll = inputs[0].value;
let rollPattern = /^\d+$/;
 if(!rollPattern.test(roll)){

      inputs[0].value = '';
      inputs[0].placeholder = `${roll} is not a valid roll number`;
      inputs[0].focus();
      inputs[0].style.outline = '1px solid red';
      inputs[0].classList.add('error');
      inputs[0].addEventListener('keydown', ()=>{
        inputs[0].style.outline = 0;
        inputs[0].style.color = 'black';
        inputs[0].classList.remove('error');
        inputs[0].placeholder = 'Enter your roll number eg: 181522';
    })
     return false;
 }


    fetch('/accounts/roll/',{
       method : 'POST',
       headers: {'Content-Type': 'application/json'},
       body: JSON.stringify({
         roll: parseInt(roll)
       })

    })
    .then(response => response.json())
    .then(data => {

          document.getElementById('roll-error').textContent = data.msg;


    })

 }
return false;




/* on submit */

let inputs = document.getElementById(`fieldset${event.target.id}`).getElementsByTagName('input');
let len = inputs.length - 2;   //removing buttons from length

 for(let i=0; i<len; i++){
     if(!inputs[i].value){
            inputs[i].focus();
            inputs[i].style.outline = '1px solid red';
            inputs[i].classList.add('error');
               inputs[i].addEventListener('keydown', ()=>{
              inputs[i].style.outline = 0;
              inputs[i].style.color = 'black';
              inputs[i].classList.remove('error');

            });

            return false;

     }
  }


  let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  let email = inputs[0].value;

  if(!emailPattern.test(email)){
      inputs[0].value = '';
      inputs[0].placeholder = `${email} is not valid email`;
      inputs[0].focus();
      inputs[0].style.outline = '1px solid red';
      inputs[0].classList.add('error');
      inputs[0].addEventListener('keydown', ()=>{
       inputs[0].style.outline = 0;
       inputs[0].style.color = 'black';
       inputs[0].classList.remove('error');
       inputs[0].placeholder = 'Enter your email';
      })
     return false;
  }


  let password = inputs[1].value;
  let password1 = inputs[2].value;
  let pswdError = document.getElementById('pswd-error');
  let confirmPswdError = document.getElementById('confirm-pswd-error');


  if(password.length < 5 || password.indexOf(' ')>=0){
     pswdError.textContent = 'Password must be at least 5 characters long with no spaces';
     inputs[1].focus();
     inputs[1].style.outline = '1px solid red';

  inputs[1].addEventListener('keydown', ()=>{
    pswdError.textContent = '';
    inputs[1].style.outline = '';
    confirmPswdError.textContent = '';
    inputs[2].style.outline = '';
  })

     return false;

  }

  /* check whether two pswds are same or not */
  if(password !== password1){
        confirmPswdError.textContent = "Passwords didn't match";
        inputs[2].focus();
        inputs[2].style.outline = '1px solid red';

        inputs[2].addEventListener('keydown', ()=>{
              confirmPswdError.textContent = '';
              inputs[2].style.outline = '';
        })

    return false;
  }




})
